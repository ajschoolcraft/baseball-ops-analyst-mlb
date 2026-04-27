import calendar
import sys

import pandas as pd
from pybaseball import statcast

from extract.utils import load_to_snowflake

DEFAULT_SEASONS = [2024, 2025]

COLUMNS = [
    "game_pk",
    "game_date",
    "game_year",
    "batter",
    "pitcher",
    "player_name",
    "events",
    "description",
    "bb_type",
    "stand",
    "p_throws",
    "home_team",
    "away_team",
    "pitch_type",
    "pitch_name",
    "release_speed",
    "release_spin_rate",
    "effective_speed",
    "launch_speed",
    "launch_angle",
    "launch_speed_angle",
    "hit_distance_sc",
    "estimated_ba_using_speedangle",
    "estimated_woba_using_speedangle",
    "woba_value",
    "woba_denom",
    "babip_value",
    "iso_value",
    "bat_speed",
    "swing_length",
    "at_bat_number",
    "pitch_number",
]


def extract_statcast(seasons=None):
    seasons = seasons or DEFAULT_SEASONS
    all_chunks = []

    for season in seasons:
        for month in range(3, 12):
            last_day = calendar.monthrange(season, month)[1]
            start = f"{season}-{month:02d}-01"
            end = f"{season}-{month:02d}-{last_day}"
            print(f"  Fetching {start} to {end}...")
            try:
                df = statcast(start_dt=start, end_dt=end)
                if df is not None and len(df) > 0:
                    available = [c for c in COLUMNS if c in df.columns]
                    chunk = df[available].copy()
                    all_chunks.append(chunk)
                    print(f"    {len(chunk)} pitches")
                else:
                    print(f"    0 pitches")
            except Exception as e:
                print(f"    Warning: failed for {start}: {e}")

    if not all_chunks:
        print("No Statcast data extracted")
        return

    df = pd.concat(all_chunks, ignore_index=True)

    for col in df.select_dtypes(include=["Int64"]).columns:
        df[col] = df[col].astype("float64")
    for col in df.select_dtypes(include=["Float64"]).columns:
        df[col] = df[col].astype("float64")

    print(f"Extracted {len(df)} total Statcast pitches")
    load_to_snowflake(df, "STATCAST")


if __name__ == "__main__":
    seasons = [int(s) for s in sys.argv[1].split(",")] if len(sys.argv) > 1 else None
    extract_statcast(seasons)
