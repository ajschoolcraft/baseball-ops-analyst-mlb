import base64
import os
import pathlib

from cryptography.hazmat.primitives import serialization
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import snowflake.connector
import streamlit as st

_DATA_DIR = pathlib.Path(__file__).parent / "data"

st.set_page_config(
    page_title="MLB Analytics: Traditional vs. Advanced Metrics",
    page_icon="⚾",
    layout="wide",
)


def _load_private_key(key_data):
    if key_data.startswith("-----"):
        pem_bytes = key_data.encode()
    else:
        pem_bytes = base64.b64decode(key_data)
    key = serialization.load_pem_private_key(pem_bytes, password=None)
    return key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )


@st.cache_resource
def get_connection():
    try:
        has_secrets = "snowflake" in st.secrets
    except FileNotFoundError:
        has_secrets = False
    try:
        if has_secrets:
            creds = st.secrets["snowflake"]
            connect_args = dict(
                account=creds["account"],
                user=creds["user"],
                database=creds["database"],
                warehouse=creds["warehouse"],
            )
            if "private_key" in creds:
                connect_args["private_key"] = _load_private_key(creds["private_key"])
            else:
                connect_args["password"] = creds["password"]
            return snowflake.connector.connect(**connect_args)

        from dotenv import load_dotenv

        load_dotenv()
        if "SNOWFLAKE_ACCOUNT" not in os.environ:
            return None
        connect_args = dict(
            account=os.environ["SNOWFLAKE_ACCOUNT"],
            user=os.environ["SNOWFLAKE_USER"],
            database=os.environ.get("SNOWFLAKE_DATABASE", "BASEBALL_ANALYTICS"),
            warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE", "BASEBALL_WH"),
        )
        key_path = os.environ.get("SNOWFLAKE_PRIVATE_KEY_PATH")
        if key_path:
            with open(key_path, "rb") as f:
                connect_args["private_key"] = serialization.load_pem_private_key(
                    f.read(), password=None
                )
        else:
            connect_args["password"] = os.environ["SNOWFLAKE_PASSWORD"]
        return snowflake.connector.connect(**connect_args)
    except Exception:
        return None


@st.cache_data(ttl=3600)
def load_season_batters():
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
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
                """
            )
            return cur.fetch_pandas_all()
        except Exception:
            pass

    path = _DATA_DIR / "season_batters.csv"
    if not path.exists():
        st.error("No data available. See README for setup instructions.")
        st.stop()
    df = pd.read_csv(path)
    df = df.dropna(subset=["XWOBA"])
    return df


@st.cache_data(ttl=3600)
def load_game_stats(player_id, season):
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
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
                (int(player_id), int(season)),
            )
            return cur.fetch_pandas_all()
        except Exception:
            pass

    path = _DATA_DIR / "game_stats.csv"
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path, parse_dates=["GAME_DATE"])
    return (
        df[(df["PLAYER_ID"] == int(player_id)) & (df["SEASON"] == int(season))]
        .drop(columns=["PLAYER_ID", "SEASON"])
        .sort_values("GAME_DATE")
        .reset_index(drop=True)
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
    st.header("Where Traditional Stats and Advanced Metrics Disagree")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("League Avg BA", f"{df['BATTING_AVG'].mean():.3f}")
    col2.metric("League Avg xwOBA", f"{df['XWOBA'].mean():.3f}")
    col3.metric("Avg Barrel %", f"{df['BARREL_PCT'].mean():.1f}%")
    col4.metric("Avg Exit Velo", f"{df['AVG_EXIT_VELOCITY'].mean():.1f} mph")

    st.markdown("---")

    fig_scatter = px.scatter(
        df,
        x="BATTING_AVG",
        y="XWOBA",
        color="GAP_SCORE",
        color_continuous_scale="RdYlGn",
        size="PLATE_APPEARANCES",
        hover_name="FULL_NAME",
        hover_data={
            "TEAM_ABBR": True,
            "PLATE_APPEARANCES": True,
            "BARREL_PCT": ":.1f",
            "GAP_SCORE": ":.3f",
            "BATTING_AVG": ":.3f",
            "XWOBA": ":.3f",
        },
        title="Batting Average vs. xwOBA — Green Dots Signal Undervalued Hitters",
        labels={
            "BATTING_AVG": "Batting Average",
            "XWOBA": "xwOBA (Expected Weighted On-Base Average)",
            "GAP_SCORE": "Gap Score",
            "PLATE_APPEARANCES": "PA",
            "TEAM_ABBR": "Team",
            "BARREL_PCT": "Barrel %",
        },
    )
    fig_scatter.update_layout(height=500)
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Most Undervalued: Batted-Ball Quality Exceeds Traditional Results")

    top_undervalued = df.nlargest(10, "GAP_SCORE")[
        [
            "FULL_NAME",
            "TEAM_ABBR",
            "BATTING_AVG",
            "XWOBA",
            "GAP_SCORE",
            "BARREL_PCT",
            "AVG_EXIT_VELOCITY",
        ]
    ].reset_index(drop=True)

    fig_bar = px.bar(
        top_undervalued,
        x="FULL_NAME",
        y="GAP_SCORE",
        color="GAP_SCORE",
        color_continuous_scale="Greens",
        title="Top 10 Undervalued Batters by xwOBA − Batting Average Gap",
        labels={"FULL_NAME": "Player", "GAP_SCORE": "Gap Score (xwOBA − BA)"},
        hover_data={
            "BATTING_AVG": ":.3f",
            "XWOBA": ":.3f",
            "BARREL_PCT": ":.1f",
            "TEAM_ABBR": True,
        },
    )
    fig_bar.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.header("Why Is This Player Over- or Underperforming?")

    player_options = (
        df.sort_values("FULL_NAME")[["PLAYER_ID", "FULL_NAME", "TEAM_ABBR"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    if player_options.empty:
        st.warning("No players match the current filters.")
    else:
        player_display = player_options.apply(
            lambda r: f"{r['FULL_NAME']} ({r['TEAM_ABBR']})", axis=1
        )
        selected_idx = st.selectbox(
            "Select a Player",
            player_options.index,
            format_func=lambda i: player_display[i],
        )
        player_id = int(player_options.loc[selected_idx, "PLAYER_ID"])
        player_name = player_options.loc[selected_idx, "FULL_NAME"]

        player_season = df[df["PLAYER_ID"] == player_id].iloc[0]

        st.subheader(f"{player_name} — Season Summary")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Batting AVG", f"{player_season['BATTING_AVG']:.3f}")
        col2.metric(
            "OBP / SLG / OPS",
            f"{player_season['ON_BASE_PCT']:.3f} / "
            f"{player_season['SLUGGING_PCT']:.3f} / "
            f"{player_season['OPS']:.3f}",
        )
        col3.metric(
            "xwOBA",
            f"{player_season['XWOBA']:.3f}",
            delta=f"{player_season['GAP_SCORE']:.3f} vs BA",
        )
        col4.metric("Barrel %", f"{player_season['BARREL_PCT']:.1f}%")

        col5, col6, col7, col8 = st.columns(4)
        col5.metric(
            "Avg Exit Velo", f"{player_season['AVG_EXIT_VELOCITY']:.1f} mph"
        )
        col6.metric("Home Runs", f"{int(player_season['HOME_RUNS'])}")
        col7.metric("BABIP", f"{player_season['BABIP']:.3f}")
        col8.metric("Plate Appearances", f"{int(player_season['PLATE_APPEARANCES'])}")

        st.markdown("---")

        game_df = load_game_stats(player_id, season)

        if len(game_df) >= 5:
            game_df = game_df.sort_values("GAME_DATE").reset_index(drop=True)

            game_df["ROLLING_BA"] = game_df["HITS"].rolling(
                15, min_periods=5
            ).sum() / game_df["AT_BATS"].rolling(15, min_periods=5).sum()

            game_df["ROLLING_XWOBA"] = (
                game_df["AVG_XWOBA"].rolling(15, min_periods=5).mean()
            )

            fig_trend = go.Figure()
            fig_trend.add_trace(
                go.Scatter(
                    x=game_df["GAME_DATE"],
                    y=game_df["ROLLING_BA"],
                    mode="lines",
                    name="Rolling BA (15-game)",
                    line=dict(color="#EF553B", width=2),
                )
            )
            fig_trend.add_trace(
                go.Scatter(
                    x=game_df["GAME_DATE"],
                    y=game_df["ROLLING_XWOBA"],
                    mode="lines",
                    name="Rolling xwOBA (15-game)",
                    line=dict(color="#636EFA", width=2),
                )
            )
            fig_trend.update_layout(
                title=f"{player_name}: When the Gap Between Results and Quality Developed",
                xaxis_title="Date",
                yaxis_title="Value",
                height=400,
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
            )
            st.plotly_chart(fig_trend, use_container_width=True)

            bbe_rolling = (
                game_df["BATTED_BALL_EVENTS"]
                .replace(0, pd.NA)
                .rolling(15, min_periods=5)
                .sum()
            )
            game_df["ROLLING_BARREL_PCT"] = (
                game_df["BARREL_COUNT"].rolling(15, min_periods=5).sum()
                / bbe_rolling
                * 100
            )
            game_df["ROLLING_EXIT_VELO"] = (
                game_df["AVG_EXIT_VELOCITY"].rolling(15, min_periods=5).mean()
            )

            fig_quality = go.Figure()
            fig_quality.add_trace(
                go.Scatter(
                    x=game_df["GAME_DATE"],
                    y=game_df["ROLLING_EXIT_VELO"],
                    mode="lines",
                    name="Avg Exit Velocity (mph)",
                    line=dict(color="#00CC96", width=2),
                )
            )
            fig_quality.add_trace(
                go.Scatter(
                    x=game_df["GAME_DATE"],
                    y=game_df["ROLLING_BARREL_PCT"],
                    mode="lines",
                    name="Barrel %",
                    line=dict(color="#AB63FA", width=2),
                    yaxis="y2",
                )
            )
            fig_quality.update_layout(
                title=f"{player_name}: Contact Quality Explains the Gap",
                xaxis_title="Date",
                yaxis=dict(title="Exit Velocity (mph)"),
                yaxis2=dict(title="Barrel %", overlaying="y", side="right"),
                height=400,
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
            )
            st.plotly_chart(fig_quality, use_container_width=True)
        else:
            st.info(
                "Not enough game data for trend charts (need at least 5 games)."
            )

with tab3:
    st.header("Team Roster Profile: Real Quality or Lucky Results?")

    team_list = sorted(df["TEAM_NAME"].unique())

    if not team_list:
        st.warning("No teams match the current filters.")
    else:
        default_team = (
            team_list.index("San Francisco Giants")
            if "San Francisco Giants" in team_list
            else 0
        )
        col_t1, col_t2 = st.columns(2)
        team1 = col_t1.selectbox("Primary Team", team_list, index=default_team)
        compare = col_t2.checkbox("Compare with another team")

        team_df = df[df["TEAM_NAME"] == team1].sort_values(
            "GAP_SCORE", ascending=False
        )
        league_avg_ba = df["BATTING_AVG"].mean()
        league_avg_xwoba = df["XWOBA"].mean()
        team_avg_ba = team_df["BATTING_AVG"].mean()
        team_avg_xwoba = team_df["XWOBA"].mean()
        team_avg_barrel = team_df["BARREL_PCT"].mean()
        team_avg_ev = team_df["AVG_EXIT_VELOCITY"].mean()

        st.subheader(f"{team1} — Aggregate vs. League")
        tc1, tc2, tc3, tc4 = st.columns(4)
        tc1.metric(
            "Team Avg BA",
            f"{team_avg_ba:.3f}",
            delta=f"{team_avg_ba - league_avg_ba:+.3f} vs league",
        )
        tc2.metric(
            "Team Avg xwOBA",
            f"{team_avg_xwoba:.3f}",
            delta=f"{team_avg_xwoba - league_avg_xwoba:+.3f} vs league",
        )
        tc3.metric("Team Avg Barrel %", f"{team_avg_barrel:.1f}%")
        tc4.metric("Team Avg Exit Velo", f"{team_avg_ev:.1f} mph")

        st.subheader("Roster Breakdown")
        display_cols = {
            "FULL_NAME": "Player",
            "BATTING_AVG": "AVG",
            "ON_BASE_PCT": "OBP",
            "SLUGGING_PCT": "SLG",
            "OPS": "OPS",
            "XWOBA": "xwOBA",
            "BARREL_PCT": "Barrel%",
            "AVG_EXIT_VELOCITY": "Exit Velo",
            "GAP_SCORE": "Gap Score",
            "PLATE_APPEARANCES": "PA",
        }
        roster_display = team_df[list(display_cols.keys())].rename(
            columns=display_cols
        )

        st.dataframe(
            roster_display.style.format(
                {
                    "AVG": "{:.3f}",
                    "OBP": "{:.3f}",
                    "SLG": "{:.3f}",
                    "OPS": "{:.3f}",
                    "xwOBA": "{:.3f}",
                    "Barrel%": "{:.1f}",
                    "Exit Velo": "{:.1f}",
                    "Gap Score": "{:+.3f}",
                    "PA": "{:.0f}",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

        if compare:
            other_teams = [t for t in team_list if t != team1]
            if other_teams:
                team2 = st.selectbox("Compare With", other_teams)
                team2_df = df[df["TEAM_NAME"] == team2]
                t2_ba = team2_df["BATTING_AVG"].mean()
                t2_xwoba = team2_df["XWOBA"].mean()
                t2_barrel = team2_df["BARREL_PCT"].mean()
                t2_ev = team2_df["AVG_EXIT_VELOCITY"].mean()

                st.subheader(f"{team2} — Head to Head")
                hc1, hc2, hc3, hc4 = st.columns(4)
                hc1.metric(
                    "Avg BA",
                    f"{t2_ba:.3f}",
                    delta=f"{t2_ba - team_avg_ba:+.3f} vs {team1}",
                )
                hc2.metric(
                    "Avg xwOBA",
                    f"{t2_xwoba:.3f}",
                    delta=f"{t2_xwoba - team_avg_xwoba:+.3f} vs {team1}",
                )
                hc3.metric(
                    "Avg Barrel%",
                    f"{t2_barrel:.1f}%",
                    delta=f"{t2_barrel - team_avg_barrel:+.1f} vs {team1}",
                )
                hc4.metric(
                    "Avg Exit Velo",
                    f"{t2_ev:.1f} mph",
                    delta=f"{t2_ev - team_avg_ev:+.1f} vs {team1}",
                )
