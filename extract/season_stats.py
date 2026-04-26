import sys

import pandas as pd
import statsapi

from extract.utils import load_to_snowflake

DEFAULT_SEASONS = [2024, 2025]


def fetch_stats(season, group):
    all_splits = []
    offset = 0
    limit = 1000
    while True:
        data = statsapi.get(
            "stats",
            {
                "stats": "season",
                "group": group,
                "season": season,
                "sportId": 1,
                "limit": limit,
                "offset": offset,
            },
        )
        splits = data["stats"][0]["splits"]
        all_splits.extend(splits)
        if len(splits) < limit:
            break
        offset += limit
    return all_splits


def parse_hitting(splits, season):
    rows = []
    for s in splits:
        stat = s["stat"]
        rows.append(
            {
                "player_id": s["player"]["id"],
                "player_name": s["player"]["fullName"],
                "season": int(s["season"]),
                "team_id": s["team"]["id"],
                "player_type": "batter",
                "games_played": stat.get("gamesPlayed"),
                "plate_appearances": stat.get("plateAppearances"),
                "at_bats": stat.get("atBats"),
                "hits": stat.get("hits"),
                "doubles": stat.get("doubles"),
                "triples": stat.get("triples"),
                "home_runs": stat.get("homeRuns"),
                "rbi": stat.get("rbi"),
                "walks": stat.get("baseOnBalls"),
                "strikeouts": stat.get("strikeOuts"),
                "stolen_bases": stat.get("stolenBases"),
                "hit_by_pitches": stat.get("hitByPitch"),
                "avg": stat.get("avg"),
                "obp": stat.get("obp"),
                "slg": stat.get("slg"),
                "ops": stat.get("ops"),
                "babip": stat.get("babip"),
                "games_started": None,
                "wins": None,
                "losses": None,
                "era": None,
                "innings_pitched": None,
                "earned_runs": None,
                "whip": None,
                "strikeouts_per_9": None,
                "walks_per_9": None,
                "saves": None,
                "holds": None,
            }
        )
    return rows


def parse_pitching(splits, season):
    rows = []
    for s in splits:
        stat = s["stat"]
        rows.append(
            {
                "player_id": s["player"]["id"],
                "player_name": s["player"]["fullName"],
                "season": int(s["season"]),
                "team_id": s["team"]["id"],
                "player_type": "pitcher",
                "games_played": stat.get("gamesPlayed"),
                "plate_appearances": None,
                "at_bats": None,
                "hits": stat.get("hits"),
                "doubles": None,
                "triples": None,
                "home_runs": stat.get("homeRuns"),
                "rbi": None,
                "walks": stat.get("baseOnBalls"),
                "strikeouts": stat.get("strikeOuts"),
                "stolen_bases": None,
                "hit_by_pitches": stat.get("hitBatsmen"),
                "avg": None,
                "obp": None,
                "slg": None,
                "ops": None,
                "babip": None,
                "games_started": stat.get("gamesStarted"),
                "wins": stat.get("wins"),
                "losses": stat.get("losses"),
                "era": stat.get("era"),
                "innings_pitched": stat.get("inningsPitched"),
                "earned_runs": stat.get("earnedRuns"),
                "whip": stat.get("whip"),
                "strikeouts_per_9": stat.get("strikeoutsPer9Inn"),
                "walks_per_9": stat.get("walksPer9Inn"),
                "saves": stat.get("saves"),
                "holds": stat.get("holds"),
            }
        )
    return rows


def extract_season_stats(seasons=None):
    seasons = seasons or DEFAULT_SEASONS
    all_rows = []
    for season in seasons:
        hitting = fetch_stats(season, "hitting")
        pitching = fetch_stats(season, "pitching")
        all_rows.extend(parse_hitting(hitting, season))
        all_rows.extend(parse_pitching(pitching, season))
        print(f"  {season}: {len(hitting)} batters, {len(pitching)} pitchers")

    df = pd.DataFrame(all_rows)
    print(f"Extracted {len(df)} total season stat records")
    load_to_snowflake(df, "SEASON_STATS")


if __name__ == "__main__":
    seasons = [int(s) for s in sys.argv[1].split(",")] if len(sys.argv) > 1 else None
    extract_season_stats(seasons)
