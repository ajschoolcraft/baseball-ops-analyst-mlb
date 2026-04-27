import pandas as pd
import statsapi

from extract.utils import load_to_snowflake


def extract_teams():
    data = statsapi.get("teams", {"sportId": 1})
    teams = []
    for t in data["teams"]:
        teams.append(
            {
                "team_id": t["id"],
                "name": t["name"],
                "abbreviation": t["abbreviation"],
                "league": t["league"]["name"],
                "division": t["division"]["name"],
            }
        )
    df = pd.DataFrame(teams)
    print(f"Extracted {len(df)} teams")
    load_to_snowflake(df, "TEAMS")


if __name__ == "__main__":
    extract_teams()
