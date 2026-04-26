import sys
import time

import pandas as pd
import statsapi

from extract.utils import load_to_snowflake

DEFAULT_SEASONS = [2024, 2025]


def get_player_ids_with_positions(season):
    data = statsapi.get("sports_players", {"sportId": 1, "season": season})
    return [(p["id"], p["primaryPosition"]["abbreviation"]) for p in data["people"]]


def fetch_game_logs(player_id, season, group):
    try:
        data = statsapi.get(
            "people",
            {
                "personIds": player_id,
                "hydrate": f"stats(group=[{group}],type=[gameLog],season={season})",
            },
        )
        person = data["people"][0]
        stats_list = person.get("stats", [])
        if not stats_list:
            return []
        return stats_list[0].get("splits", [])
    except Exception as e:
        print(f"    Warning: failed for player {player_id} ({group}): {e}")
        return []


def parse_hitting_log(split, player_id):
    stat = split["stat"]
    return {
        "player_id": player_id,
        "player_name": split["player"]["fullName"],
        "game_id": split["game"]["gamePk"],
        "game_date": split["date"],
        "season": int(split["season"]),
        "team_id": split["team"]["id"],
        "player_type": "batter",
        "at_bats": stat.get("atBats"),
        "hits": stat.get("hits"),
        "doubles": stat.get("doubles"),
        "triples": stat.get("triples"),
        "home_runs": stat.get("homeRuns"),
        "rbi": stat.get("rbi"),
        "runs": stat.get("runs"),
        "walks": stat.get("baseOnBalls"),
        "strikeouts": stat.get("strikeOuts"),
        "stolen_bases": stat.get("stolenBases"),
        "plate_appearances": stat.get("plateAppearances"),
        "innings_pitched": None,
        "earned_runs": None,
        "pitching_strikeouts": None,
        "pitching_walks": None,
        "pitching_hits": None,
        "pitching_home_runs": None,
        "pitches": None,
        "wins": None,
        "losses": None,
    }


def parse_pitching_log(split, player_id):
    stat = split["stat"]
    return {
        "player_id": player_id,
        "player_name": split["player"]["fullName"],
        "game_id": split["game"]["gamePk"],
        "game_date": split["date"],
        "season": int(split["season"]),
        "team_id": split["team"]["id"],
        "player_type": "pitcher",
        "at_bats": None,
        "hits": None,
        "doubles": None,
        "triples": None,
        "home_runs": None,
        "rbi": None,
        "runs": None,
        "walks": None,
        "strikeouts": None,
        "stolen_bases": None,
        "plate_appearances": None,
        "innings_pitched": stat.get("inningsPitched"),
        "earned_runs": stat.get("earnedRuns"),
        "pitching_strikeouts": stat.get("strikeOuts"),
        "pitching_walks": stat.get("baseOnBalls"),
        "pitching_hits": stat.get("hits"),
        "pitching_home_runs": stat.get("homeRuns"),
        "pitches": stat.get("numberOfPitches"),
        "wins": stat.get("wins"),
        "losses": stat.get("losses"),
    }


def extract_game_logs(seasons=None):
    seasons = seasons or DEFAULT_SEASONS
    all_rows = []

    for season in seasons:
        players = get_player_ids_with_positions(season)
        print(f"  {season}: processing {len(players)} players...")

        for i, (pid, pos) in enumerate(players):
            if pos == "TWP":
                for split in fetch_game_logs(pid, season, "hitting"):
                    all_rows.append(parse_hitting_log(split, pid))
                for split in fetch_game_logs(pid, season, "pitching"):
                    all_rows.append(parse_pitching_log(split, pid))
            elif pos == "P":
                for split in fetch_game_logs(pid, season, "pitching"):
                    all_rows.append(parse_pitching_log(split, pid))
            else:
                for split in fetch_game_logs(pid, season, "hitting"):
                    all_rows.append(parse_hitting_log(split, pid))

            if (i + 1) % 100 == 0:
                print(f"    {i + 1}/{len(players)} players processed")
            time.sleep(0.1)

        print(f"  {season}: {len([r for r in all_rows if r['season'] == season])} game log rows")

    df = pd.DataFrame(all_rows)
    print(f"Extracted {len(df)} total game log records")
    load_to_snowflake(df, "GAME_LOGS")


if __name__ == "__main__":
    seasons = [int(s) for s in sys.argv[1].split(",")] if len(sys.argv) > 1 else None
    extract_game_logs(seasons)
