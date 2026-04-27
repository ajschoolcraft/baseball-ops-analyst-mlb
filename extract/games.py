import sys

import pandas as pd
import statsapi

from extract.utils import load_to_snowflake

DEFAULT_SEASONS = [2024, 2025]


def extract_games(seasons=None):
    seasons = seasons or DEFAULT_SEASONS
    all_games = []
    for season in seasons:
        schedule = statsapi.schedule(
            start_date=f"03/01/{season}",
            end_date=f"11/30/{season}",
            sportId=1,
        )
        for g in schedule:
            if g["game_type"] != "R":
                continue
            if g["status"] != "Final":
                continue
            all_games.append(
                {
                    "game_id": g["game_id"],
                    "game_date": g["game_date"],
                    "game_type": g["game_type"],
                    "home_team_id": g["home_id"],
                    "away_team_id": g["away_id"],
                    "home_score": g["home_score"],
                    "away_score": g["away_score"],
                    "venue_name": g["venue_name"],
                    "status": g["status"],
                    "season": season,
                }
            )
        print(f"  {season}: {len([g for g in all_games if g['season'] == season])} games")

    df = pd.DataFrame(all_games)
    print(f"Extracted {len(df)} total games")
    load_to_snowflake(df, "GAMES")


if __name__ == "__main__":
    seasons = [int(s) for s in sys.argv[1].split(",")] if len(sys.argv) > 1 else None
    extract_games(seasons)
