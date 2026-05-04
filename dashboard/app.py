import os

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import snowflake.connector
import streamlit as st

st.set_page_config(
    page_title="MLB Analytics: Traditional vs. Advanced Metrics",
    page_icon="⚾",
    layout="wide",
)


@st.cache_resource
def get_connection():
    try:
        creds = st.secrets["snowflake"]
        return snowflake.connector.connect(
            account=creds["account"],
            user=creds["user"],
            password=creds["password"],
            database=creds["database"],
            warehouse=creds["warehouse"],
        )
    except (FileNotFoundError, KeyError):
        from dotenv import load_dotenv

        load_dotenv()
        return snowflake.connector.connect(
            account=os.environ["SNOWFLAKE_ACCOUNT"],
            user=os.environ["SNOWFLAKE_USER"],
            password=os.environ["SNOWFLAKE_PASSWORD"],
            database=os.environ.get("SNOWFLAKE_DATABASE", "BASEBALL_ANALYTICS"),
            warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE", "BASEBALL_WH"),
        )


@st.cache_data(ttl=3600)
def load_season_batters():
    conn = get_connection()
    return pd.read_sql(
        """
        SELECT
            s.player_id,
            p.full_name,
            t.name AS team_name,
            t.abbreviation AS team_abbr,
            s.season,
            s.plate_appearances,
            s.at_bats,
            s.hits,
            s.batting_avg,
            s.on_base_pct,
            s.slugging_pct,
            s.ops,
            s.babip,
            s.home_runs,
            s.strikeouts,
            s.walks,
            s.xwoba,
            s.barrel_pct,
            s.avg_exit_velocity,
            s.avg_launch_angle,
            s.xwoba - s.batting_avg AS gap_score
        FROM MART.FCT_PLAYER_SEASON_STATS s
        JOIN MART.DIM_PLAYERS p ON s.player_id = p.player_id
        JOIN MART.DIM_TEAMS t ON s.team_id = t.team_id
        WHERE s.player_type = 'batter'
          AND s.xwoba IS NOT NULL
          AND s.plate_appearances > 0
        """,
        conn,
    )


@st.cache_data(ttl=3600)
def load_game_stats(player_id, season):
    conn = get_connection()
    return pd.read_sql(
        """
        SELECT
            g.game_date,
            g.at_bats,
            g.hits,
            g.home_runs,
            g.walks,
            g.strikeouts,
            g.plate_appearances,
            g.avg_xwoba,
            g.barrel_count,
            g.avg_exit_velocity,
            g.batted_ball_events
        FROM MART.FCT_PLAYER_GAME_STATS g
        WHERE g.player_id = %s
          AND g.season = %s
        ORDER BY g.game_date
        """,
        conn,
        params=(int(player_id), int(season)),
    )


# -- Sidebar --
st.sidebar.title("⚾ MLB Analytics")
st.sidebar.caption("Traditional vs. Advanced Metrics")

df_all = load_season_batters()

seasons = sorted(df_all["SEASON"].unique(), reverse=True)
season = st.sidebar.selectbox("Season", seasons)

min_pa = st.sidebar.slider("Minimum Plate Appearances", 0, 500, 100, 25)

teams = sorted(df_all[df_all["SEASON"] == season]["TEAM_NAME"].unique())
selected_teams = st.sidebar.multiselect("Filter by Team", teams, default=teams)

df = df_all[
    (df_all["SEASON"] == season)
    & (df_all["PLATE_APPEARANCES"] >= min_pa)
    & (df_all["TEAM_NAME"].isin(selected_teams))
].copy()

# -- Tabs --
tab1, tab2, tab3 = st.tabs(
    ["📊 League Overview", "🔍 Player Deep Dive", "⚔️ Team Comparison"]
)

with tab1:
    st.info("League Overview — coming next")

with tab2:
    st.info("Player Deep Dive — coming next")

with tab3:
    st.info("Team Comparison — coming next")
