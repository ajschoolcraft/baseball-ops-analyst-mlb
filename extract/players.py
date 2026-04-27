import sys

import pandas as pd
import statsapi

from extract.utils import load_to_snowflake

DEFAULT_SEASONS = [2024, 2025]


def extract_players(seasons=None):
    seasons = seasons or DEFAULT_SEASONS
    all_players = []
    for season in seasons:
        data = statsapi.get("sports_players", {"sportId": 1, "season": season})
        for p in data["people"]:
            all_players.append(
                {
                    "player_id": p["id"],
                    "full_name": p["fullName"],
                    "position": p["primaryPosition"]["abbreviation"],
                    "bats": p.get("batSide", {}).get("code"),
                    "throws": p.get("pitchHand", {}).get("code"),
                    "birth_date": p.get("birthDate"),
                    "debut_date": p.get("mlbDebutDate"),
                    "active": p.get("active", False),
                    "team_id": p.get("currentTeam", {}).get("id"),
                    "season": season,
                }
            )
        print(f"  {season}: {len(data['people'])} players")

    df = pd.DataFrame(all_players)
    df = df.drop_duplicates(subset=["player_id", "season"])
    print(f"Extracted {len(df)} total player-season records")
    load_to_snowflake(df, "PLAYERS")


if __name__ == "__main__":
    seasons = [int(s) for s in sys.argv[1].split(",")] if len(sys.argv) > 1 else None
    extract_players(seasons)
