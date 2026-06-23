"""Generate static CSV data for the dashboard.

Pulls from MLB Stats API and Baseball Savant leaderboards so the dashboard
works without a live Snowflake connection.

Usage:
    python -m dashboard.generate_data                  # 2025 + 2026
    python -m dashboard.generate_data --seasons 2025   # specific seasons
    python -m dashboard.generate_data --season-only     # skip slow game stats
"""

import calendar
import os
import sys

import pandas as pd
import statsapi
from pybaseball import (
    statcast,
    statcast_batter_expected_stats,
    statcast_batter_exitvelo_barrels,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def generate_season_batters(seasons):
    os.makedirs(DATA_DIR, exist_ok=True)

    teams_data = statsapi.get("teams", {"sportId": 1})
    teams = {
        t["id"]: {"name": t["name"], "abbreviation": t["abbreviation"]}
        for t in teams_data["teams"]
    }

    def safe_float(val):
        if isinstance(val, str):
            return None if val in (".---", "-.--") else float(val)
        return float(val) if val is not None else None

    all_rows = []
    for season in seasons:
        print(f"Fetching {season} batting stats from MLB API...")
        data = statsapi.get(
            "stats",
            {
                "stats": "season",
                "group": "hitting",
                "sportIds": 1,
                "season": season,
                "playerPool": "ALL",
                "limit": 5000,
            },
        )
        for split in data["stats"][0]["splits"]:
            stat = split["stat"]
            if stat["plateAppearances"] == 0:
                continue
            team_id = split["team"]["id"]
            team_info = teams.get(team_id, {"name": "Unknown", "abbreviation": "UNK"})
            all_rows.append(
                {
                    "PLAYER_ID": split["player"]["id"],
                    "FULL_NAME": split["player"]["fullName"],
                    "TEAM_NAME": team_info["name"],
                    "TEAM_ABBR": team_info["abbreviation"],
                    "SEASON": int(split["season"]),
                    "PLATE_APPEARANCES": stat["plateAppearances"],
                    "AT_BATS": stat["atBats"],
                    "HITS": stat["hits"],
                    "BATTING_AVG": safe_float(stat.get("avg")),
                    "ON_BASE_PCT": safe_float(stat.get("obp")),
                    "SLUGGING_PCT": safe_float(stat.get("slg")),
                    "OPS": safe_float(stat.get("ops")),
                    "BABIP": safe_float(stat.get("babip")),
                    "HOME_RUNS": stat["homeRuns"],
                    "STRIKEOUTS": stat["strikeOuts"],
                    "WALKS": stat["baseOnBalls"],
                }
            )

    df = pd.DataFrame(all_rows)

    for season in seasons:
        print(f"Fetching {season} Statcast leaderboards...")
        mask = df["SEASON"] == season
        try:
            xstats = statcast_batter_expected_stats(season, minPA=1)
            xwoba_map = xstats.set_index("player_id")["est_woba"]
            df.loc[mask, "XWOBA"] = df.loc[mask, "PLAYER_ID"].map(xwoba_map)
        except Exception as e:
            print(f"  Warning: expected stats failed for {season}: {e}")

        try:
            barrels = statcast_batter_exitvelo_barrels(season, minBBE=1)
            b_map = barrels.set_index("player_id")
            df.loc[mask, "BARREL_PCT"] = df.loc[mask, "PLAYER_ID"].map(
                b_map["brl_percent"]
            )
            df.loc[mask, "AVG_EXIT_VELOCITY"] = df.loc[mask, "PLAYER_ID"].map(
                b_map["avg_hit_speed"]
            )
            df.loc[mask, "AVG_LAUNCH_ANGLE"] = df.loc[mask, "PLAYER_ID"].map(
                b_map["avg_hit_angle"]
            )
        except Exception as e:
            print(f"  Warning: barrel data failed for {season}: {e}")

    df["GAP_SCORE"] = df["XWOBA"] - df["BATTING_AVG"]

    path = os.path.join(DATA_DIR, "season_batters.csv")
    df.to_csv(path, index=False)
    print(f"Saved {len(df)} rows to {path}")
    return df


def generate_game_stats(seasons):
    os.makedirs(DATA_DIR, exist_ok=True)

    all_chunks = []
    for season in seasons:
        for month in range(3, 12):
            last_day = calendar.monthrange(season, month)[1]
            start = f"{season}-{month:02d}-01"
            end = f"{season}-{month:02d}-{last_day}"
            print(f"  Fetching Statcast {start} to {end}...")
            try:
                df = statcast(start_dt=start, end_dt=end)
                if df is not None and len(df) > 0:
                    all_chunks.append(df)
                    print(f"    {len(df)} pitches")
                else:
                    print(f"    0 pitches")
            except Exception as e:
                print(f"    Warning: {e}")

    if not all_chunks:
        print("No Statcast data retrieved")
        return

    raw = pd.concat(all_chunks, ignore_index=True)

    hit_events = {"single", "double", "triple", "home_run"}
    walk_events = {"walk"}
    so_events = {"strikeout", "strikeout_double_play"}
    hr_events = {"home_run"}
    non_ab_events = {
        "walk",
        "hit_by_pitch",
        "sac_fly",
        "sac_bunt",
        "sac_fly_double_play",
        "catcher_interf",
    }

    pa_rows = raw[raw["events"].notna()].copy()
    batting = (
        pa_rows.groupby(["batter", "game_pk", "game_date"])
        .agg(
            plate_appearances=("events", "count"),
            hits=("events", lambda x: x.isin(hit_events).sum()),
            home_runs=("events", lambda x: x.isin(hr_events).sum()),
            walks=("events", lambda x: x.isin(walk_events).sum()),
            strikeouts=("events", lambda x: x.isin(so_events).sum()),
            non_ab=("events", lambda x: x.isin(non_ab_events).sum()),
        )
        .reset_index()
    )
    batting["at_bats"] = batting["plate_appearances"] - batting["non_ab"]
    batting.drop(columns=["non_ab"], inplace=True)

    batted = raw[raw["launch_speed"].notna()].copy()
    sc_game = (
        batted.groupby(["batter", "game_pk"])
        .agg(
            avg_xwoba=("estimated_woba_using_speedangle", "mean"),
            barrel_count=("launch_speed_angle", lambda x: (x == 6).sum()),
            avg_exit_velocity=("launch_speed", "mean"),
            batted_ball_events=("launch_speed", "count"),
        )
        .reset_index()
    )

    game_df = batting.merge(sc_game, on=["batter", "game_pk"], how="inner")
    game_df["game_date"] = pd.to_datetime(game_df["game_date"])
    game_df["season"] = game_df["game_date"].dt.year

    game_df = game_df.rename(
        columns={
            "batter": "PLAYER_ID",
            "game_date": "GAME_DATE",
            "at_bats": "AT_BATS",
            "hits": "HITS",
            "home_runs": "HOME_RUNS",
            "walks": "WALKS",
            "strikeouts": "STRIKEOUTS",
            "plate_appearances": "PLATE_APPEARANCES",
            "avg_xwoba": "AVG_XWOBA",
            "barrel_count": "BARREL_COUNT",
            "avg_exit_velocity": "AVG_EXIT_VELOCITY",
            "batted_ball_events": "BATTED_BALL_EVENTS",
            "season": "SEASON",
        }
    )

    keep_cols = [
        "PLAYER_ID",
        "GAME_DATE",
        "SEASON",
        "AT_BATS",
        "HITS",
        "HOME_RUNS",
        "WALKS",
        "STRIKEOUTS",
        "PLATE_APPEARANCES",
        "AVG_XWOBA",
        "BARREL_COUNT",
        "AVG_EXIT_VELOCITY",
        "BATTED_BALL_EVENTS",
    ]
    game_df = game_df[keep_cols]

    path = os.path.join(DATA_DIR, "game_stats.csv")
    game_df.to_csv(path, index=False)
    print(f"Saved {len(game_df)} rows to {path}")
    return game_df


if __name__ == "__main__":
    seasons = [2025, 2026]
    season_only = False

    for arg in sys.argv[1:]:
        if arg.startswith("--seasons"):
            val = arg.split("=")[1] if "=" in arg else sys.argv[sys.argv.index(arg) + 1]
            seasons = [int(s) for s in val.split(",")]
        elif arg == "--season-only":
            season_only = True

    print("=== Phase 1: Season Batters ===")
    generate_season_batters(seasons)

    if not season_only:
        print("\n=== Phase 2: Game Stats (pulling raw Statcast — this takes ~10 min) ===")
        generate_game_stats(seasons)

    print("\nDone!")
