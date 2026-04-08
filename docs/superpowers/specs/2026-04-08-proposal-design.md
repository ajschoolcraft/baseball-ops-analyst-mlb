# Project Proposal Design: Baseball Operations Analyst Portfolio

## Overview

An end-to-end analytics engineering project targeting the **Baseball Operations Analyst** role at the San Francisco Giants. The project builds a player performance analytics pipeline spanning the Statcast era (2015-2025), combining traditional MLB statistics with advanced Statcast metrics to demonstrate the SQL, statistical analysis, visualization, and research evaluation skills the posting requires.

## Job Posting Alignment

**Role:** Baseball Operations Analyst, SF Giants R&D Team
**Key skills from posting mapped to project deliverables:**

| Posting Requirement | Project Deliverable |
|---|---|
| Proficiency in SQL | dbt models, star schema, Snowflake queries |
| Python proficiency | Extraction scripts, Pybaseball integration |
| Statistical/ML models on real datasets | Advanced vs. traditional metric analysis, regression/performance diagnostics |
| Prototype tools and visualizations | Streamlit dashboard |
| Evaluate and adapt public research | Knowledge base synthesizing sabermetric research |
| Communicate complex findings to non-technical people | Dashboard design, presentation slides |

## Data Sources

### Source 1: MLB Stats API (Required API)

- **Endpoint:** statsapi.mlb.com
- **Python access:** `MLB-StatsAPI` wrapper or direct REST calls
- **Data pulled:**
  - Player biographical data (name, team, position, debut date, bats/throws)
  - Season-level batting and pitching statistics
  - Game logs for granular per-game analysis
  - Team standings and schedules
  - Game metadata (date, venue, home/away, score)
- **Auth:** None required (free, public API)
- **Load target:** Snowflake raw schema
- **Automation:** GitHub Actions on schedule

### Source 2: Pybaseball / Statcast (Supplementary API)

- **Access:** Pybaseball Python library (wraps Statcast, FanGraphs, Baseball Reference)
- **Data pulled:**
  - Statcast batted-ball data (exit velocity, launch angle, spin rate)
  - Advanced metrics (xwOBA, wRC+, FIP, barrel rate, WAR)
- **Load target:** Snowflake raw schema alongside MLB Stats API data
- **Automation:** GitHub Actions on schedule

### Source 3: Web Scrape (Required - Knowledge Base)

- **Sources (15+ from 3+ sites/authors):**
  - FanGraphs: player evaluation methodology, stat primers, analytical articles
  - Baseball Prospectus: research articles, prospect analysis methodology
  - Statcast/MLB: methodology docs, metric definitions
  - Tangotiger / The Book Blog: foundational sabermetric theory
  - Baseball Reference: methodology pages, stat calculation explanations
- **Scraping tool:** Firecrawl or similar
- **Storage:** `knowledge/raw/`
- **Automation:** GitHub Actions on schedule

### Data Scope

- **Time range:** 2015-2025 (Statcast era)
- **Coverage:** All MLB teams, with ability to filter to SF Giants
- **Rationale:** Statcast launched in 2015, providing consistent advanced metrics. 10 seasons of data enables meaningful trend analysis.

## Star Schema Design

### Fact Tables

**`fct_player_game_stats`** — one row per player per game
- Batting line: AB, H, 2B, 3B, HR, RBI, BB, K, SB
- Statcast metrics (where available): avg exit velocity, avg launch angle, barrel rate
- Foreign keys: player_id, game_id, team_id, season_id

**`fct_player_season_stats`** — aggregated season-level performance
- Traditional stats: AVG, OBP, SLG, OPS, ERA, WHIP
- Advanced metrics: wRC+, xwOBA, FIP, WAR, barrel rate
- Foreign keys: player_id, team_id, season_id

### Dimension Tables

**`dim_players`** — player_id, name, position, bats, throws, birth_date, debut_date, active_status

**`dim_teams`** — team_id, name, abbreviation, league, division

**`dim_seasons`** — season_year, game_count, notable context (shortened seasons, rule changes)

**`dim_games`** — game_id, date, home_team_id, away_team_id, venue, final_score_home, final_score_away

### dbt Layer Structure

- **Raw:** Direct loads from API/Pybaseball, minimal transformation
- **Staging:** Cleaning, renaming, type casting, deduplication. One staging model per source table. Tests for uniqueness, not-null, accepted values.
- **Mart:** Star schema fact + dimension tables with joins and business logic (rate stats, performance tiers, etc.)

## Streamlit Dashboard

### Descriptive Analytics (what happened)

- **Player performance overview:** Search/filter by player, team, season. Traditional + advanced stat lines.
- **Leaderboards:** Top performers by key metrics (wRC+, xwOBA, WAR, barrel rate) with season/position filters.
- **Team-level summaries:** Aggregate performance by team with division standings context.

### Diagnostic Analytics (why did it happen)

- **Traditional vs. advanced metrics comparison:** Surface players over/underperforming relative to Statcast data (e.g., high BABIP but low xBA suggests regression).
- **Performance trend analysis:** How exit velocity, launch angle, or spin rate changed over time and how that correlates with outcomes.
- **Splits and situational breakdowns:** Performance by handedness, home/away, or game context.

### Interactive Elements

- Player/team selector dropdowns
- Season range slider (2015-2025)
- Metric toggle (traditional vs. advanced)
- Tab navigation between views

### Deployment

Streamlit Community Cloud, connected to Snowflake mart tables via public URL.

## Knowledge Base

### Raw Sources

15+ sources from 3+ different sites/authors covering:
- Player evaluation methodology (FanGraphs)
- Analytical research articles (Baseball Prospectus)
- Statcast data collection and processing methodology (MLB)
- Foundational sabermetric theory (Tangotiger, The Book Blog)
- Stat calculation methodology (Baseball Reference)

### Wiki Pages (`knowledge/wiki/`)

- `overview.md` — landscape of modern baseball analytics, coexistence of traditional and advanced metrics
- `key-metrics.md` — synthesis of major advanced metrics, when to use each, known limitations
- `statcast-methodology.md` — how Statcast data is collected, processed, and key measurements
- `player-evaluation-frameworks.md` — public research approaches to player valuation (WAR variants, projection systems, aging curves)
- `index.md` — listing of all wiki pages with one-line summaries

### Queryability

CLAUDE.md includes instructions for querying the knowledge base. Demo-ready: run Claude Code live in the final interview and ask analytical questions that pull from wiki pages and raw sources.

## Transferability

This project transfers to:
- **Sports analytics roles** at any professional team (same pipeline patterns, different sport data)
- **Data analyst / BI analyst roles** in any industry (star schema, dbt, Streamlit, SQL are universal skills)
- **Analytics engineer roles** (the pipeline architecture is the proof of skill)

To adapt: swap the data source, adjust the domain knowledge base, and the core architecture stands.

## Proposal Reflection (Draft)

This project targets the Baseball Operations Analyst role at the San Francisco Giants, which requires SQL proficiency, experience building statistical models on real datasets, the ability to prototype tools and visualizations, and the skill to evaluate and adapt public baseball research. My analytics pipeline directly exercises each of these: I use SQL and dbt to model player performance data into a star schema in Snowflake, build a Streamlit dashboard that surfaces both traditional and advanced Statcast metrics to communicate complex findings visually, and construct a knowledge base by scraping and synthesizing public sabermetric research from FanGraphs, Baseball Prospectus, and Statcast methodology sources. The project spans the full Statcast era (2015-2025), enabling the kind of longitudinal player performance analysis the R&D team conducts. Beyond this specific role, the pipeline architecture, dimensional modeling, and data storytelling skills transfer to any data analyst, analytics engineer, or BI role in sports or other industries.
