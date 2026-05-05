# M02: Present & Polish — Design Spec

**Date**: 2026-05-03
**Due**: 2026-05-04
**Branch**: `feature/m02-present-polish`

## Overview

Milestone 02 adds the presentation layer to the M01 ELT pipeline: a Streamlit dashboard connected to Snowflake mart tables, a knowledge base of scraped sabermetric research, an ERD, and an updated README. The analytical story centers on the gap between traditional batting stats and Statcast advanced metrics — where they agree, where they diverge, and what the divergence means for player evaluation.

## Deliverables

| # | Deliverable | Pts | Approach |
|---|-------------|-----|----------|
| 8 | Source 2 (web scrape) | 10 | Firecrawl MCP scraping → `knowledge/raw/`, GitHub Actions workflow |
| 9 | Streamlit dashboard | 15 | 3-tab app connected to Snowflake mart, deployed to Community Cloud |
| 10 | Presentation slides | 7 | Manual (Google Slides), exported as `docs/slides.pdf` |
| 11 | Knowledge base | 8 | 16 raw sources from 4+ sites, 4 wiki pages, `knowledge/index.md` |
| 12 | README.md | 5 | Rewrite using template, add ERD + pipeline diagram + insights |
| 13 | ERD | 3 | Mermaid erDiagram from dbt schema, embedded in README |
| 14 | Commit history | 2 | Iterative commits, knowledge base built in batches |

## 1. Streamlit Dashboard

### File Structure

```
dashboard/
  app.py              # Main Streamlit app
  requirements.txt    # streamlit, snowflake-connector-python, plotly, pandas
.streamlit/
  secrets.toml        # Snowflake credentials (gitignored)
```

### Connection

`snowflake-connector-python` via `st.connection("snowflake")`. Secrets managed through Streamlit Community Cloud UI (mirrors `.env` Snowflake vars). Queries hit mart tables directly: `BASEBALL_ANALYTICS.MART.FCT_PLAYER_SEASON_STATS`, etc.

### Tab 1: League Overview (Descriptive)

**Question**: "Where do traditional stats and Statcast metrics agree or disagree across the league?"

**Components**:
- `st.metric` cards: league-average batting AVG, xwOBA, barrel%, avg exit velo for the selected season
- Scatter plot (Plotly): batting AVG (x) vs. xwOBA (y), one dot per qualified batter. Diagonal = agreement. Off-diagonal = gaps. Color by team, size by PA.
- Bar chart: Top 10 "most undervalued" players ranked by gap score (xwOBA minus a scaled batting AVG equivalent). Shows players whose batted-ball quality exceeds their traditional results.

**Filters** (sidebar):
- Season selector: dropdown (2024, 2025)
- Minimum PA: slider (default 100)
- Team multi-select: all teams, defaults to all

**Data source**: `fct_player_season_stats` joined to `dim_players` and `dim_teams`. Filter to `player_type = 'batter'` and non-null xwOBA.

### Tab 2: Player Deep Dive (Diagnostic)

**Question**: "Why is this player's performance diverging from their underlying quality?"

**Components**:
- Player selector: searchable dropdown populated from `dim_players`
- Stat comparison cards: side-by-side traditional (AVG/OBP/SLG/OPS) vs. advanced (xwOBA, barrel%, avg exit velo). Color-coded: green if advanced > traditional equivalent, red if worse.
- Game-level trend chart (Plotly line): rolling 15-game average of xwOBA vs. batting AVG from `fct_player_game_stats`. Shows when/how gaps develop during a season.
- Barrel quality chart: barrel% and avg exit velocity over the season, helping diagnose *why* the gap exists (e.g., hard contact + low BABIP = unlucky).

**Data source**: `fct_player_season_stats` for summary cards, `fct_player_game_stats` joined to `dim_players` for trends.

### Tab 3: Team Comparison

**Question**: "How does this team's roster profile compare — are they built on real quality or lucky results?"

**Components**:
- Team selector: dropdown, defaults to SF Giants
- Roster table: all qualified batters on the team, columns for AVG, OBP, SLG, OPS, xwOBA, barrel%, exit velo, gap score. Sortable via `st.dataframe`.
- Team aggregate metrics: `st.metric` cards showing team avg xwOBA vs. team avg batting AVG, compared to league average.
- Optional second team selector for head-to-head comparison (grouped bar chart).

**Data source**: `fct_player_season_stats` joined to `dim_players` and `dim_teams`.

### Visual Style

- Plotly for all charts (hover tooltips, zoom)
- Clean layout: `st.set_page_config(layout="wide")`
- Professional color palette (blues/grays, accent color for highlights)
- `st.metric` cards for key numbers at top of each tab
- Chart titles use takeaway-title format for screenshot-readiness

### Gap Score Calculation

The "gap score" is the core diagnostic metric. Computed in the dashboard (not a dbt model) as:

```
gap_score = xwoba - batting_avg
```

This is a simplified proxy. xwOBA and batting AVG are on different scales, but the relative ranking is what matters — players with large positive gaps have batted-ball quality that exceeds their traditional line. A future enhancement could normalize both to z-scores, but raw difference is sufficient for the dashboard story and easier to explain in the interview.

## 2. Knowledge Base & Web Scrape Pipeline

### Scraping Approach

Two-phase approach:

1. **Initial scrape (this session)**: Use Firecrawl MCP to scrape each page to markdown. Save as numbered files in `knowledge/raw/` with a `Source:` header line.
2. **Automated re-scrape (GitHub Actions)**: A Python script using `requests` + `beautifulsoup4` re-scrapes the same URLs on a schedule. This runs without Firecrawl since GH Actions doesn't have MCP access.

### GitHub Actions Workflow

**File**: `.github/workflows/scrape_knowledge.yml`

**Script**: `extract/scrape_knowledge.py` — reads a URL list, scrapes each with `requests` + `beautifulsoup4`, converts to markdown, saves to `knowledge/raw/`.

Runs on: `schedule` (weekly) and `workflow_dispatch`. Auto-commits updated files if content changed.

### Source List (16 sources, 4+ sites)

| # | File | Site | Topic |
|---|------|------|-------|
| 01 | `01-statcast-metrics-context.md` | Baseball Savant | Metric definitions, outcomes by contact quality |
| 02 | `02-fangraphs-wrc-plus.md` | FanGraphs | Weighted Runs Created methodology |
| 03 | `03-driveline-stuff-plus-pitch-models.md` | Driveline | Pitch quality modeling (Stuff+) |
| 04 | `04-fangraphs-woba.md` | FanGraphs | Weighted On-Base Average methodology |
| 05 | `05-fangraphs-fip.md` | FanGraphs | Fielding Independent Pitching |
| 06 | `06-fangraphs-babip.md` | FanGraphs | Batting Average on Balls in Play |
| 07 | `07-fangraphs-war.md` | FanGraphs | Wins Above Replacement |
| 08 | `08-savant-expected-stats.md` | Baseball Savant | xwOBA, xBA, xSLG methodology |
| 09 | `09-savant-barrel-definition.md` | Baseball Savant | Barrel classification thresholds |
| 10 | `10-savant-exit-velo-launch-angle.md` | Baseball Savant | Batted ball quality metrics |
| 11 | `11-savant-pitch-tracking.md` | Baseball Savant | How Statcast collects pitch data |
| 12 | `12-fangraphs-ops-plus.md` | FanGraphs | OPS and OPS+ methodology |
| 13 | `13-bp-intro-sabermetrics.md` | Baseball Prospectus | Analytical framework overview |
| 14 | `14-bp-drc-plus.md` | Baseball Prospectus | Deserved Runs Created Plus |
| 15 | `15-tangotiger-linear-weights.md` | Tangotiger / The Book Blog | Run expectancy and linear weights |
| 16 | `16-savant-statcast-glossary.md` | Baseball Savant | Comprehensive metric glossary |

### Wiki Pages

**Location**: `knowledge/wiki/`

| Page | Content |
|------|---------|
| `overview.md` | What is sabermetrics, why advanced metrics matter, knowledge base organization |
| `key-metrics.md` | Traditional vs. advanced metrics guide: AVG/OBP/SLG/OPS/ERA/WHIP vs. xwOBA/wRC+/barrel%/FIP/WAR. When to use which. |
| `statcast-methodology.md` | How Statcast works, expected stats, barrel classification, exit velocity thresholds. Synthesized from Savant + Driveline sources. |
| `player-evaluation-frameworks.md` | How to evaluate hitters and pitchers using the traditional vs. advanced framework. When gaps are meaningful vs. noise. |

### Index

**File**: `knowledge/index.md`

Lists all wiki pages with one-line summaries, followed by a catalog of all raw sources with their origin site and topic.

### Commit Strategy

Sources committed in 3-4 batches to show iterative development:
1. Initial batch (sources 04-07): FanGraphs core metrics
2. Second batch (sources 08-11): Baseball Savant methodology
3. Third batch (sources 12-16): remaining sources
4. Wiki pages generated and committed after raw sources are in place

## 3. ERD

**Format**: Mermaid `erDiagram` block embedded in README.

**Entities** (from dbt mart models):

- `dim_players`: player_id PK, full_name, position, bats, throws, birth_date, debut_date, active
- `dim_teams`: team_id PK, name, abbreviation, league, division
- `dim_seasons`: season_year PK, game_count
- `dim_games`: game_id PK, game_date, home_team_id FK, away_team_id FK, venue_name, home_score, away_score, season
- `fct_player_season_stats`: player_id FK, season FK, team_id FK, player_type, plus all batting/pitching/Statcast columns
- `fct_player_game_stats`: player_id FK, game_id FK, team_id FK, game_date, season, plus batting/Statcast columns

**Relationships**:
- `dim_players ||--o{ fct_player_season_stats`
- `dim_players ||--o{ fct_player_game_stats`
- `dim_teams ||--o{ fct_player_season_stats`
- `dim_teams ||--o{ fct_player_game_stats`
- `dim_teams ||--o{ dim_games` (home_team_id)
- `dim_teams ||--o{ dim_games` (away_team_id)
- `dim_seasons ||--o{ fct_player_season_stats`
- `dim_games ||--o{ fct_player_game_stats`

## 4. README

Rewrite using `docs/readme-template.md`. Sections:

1. Project overview paragraph
2. Job posting (role, company, link, skills connection)
3. Tech stack table (updated with both sources)
4. Pipeline diagram (update existing Mermaid to include knowledge base path)
5. ERD (Mermaid block)
6. Dashboard preview (screenshot after deployment)
7. Key insights (takeaway title + diagnostic + recommendation — filled after dashboard is built)
8. Live dashboard URL
9. Knowledge base description + example queries
10. Setup & reproduction steps
11. Repository structure tree

## 5. Presentation Slides

Created manually in Google Slides, exported as `docs/slides.pdf`. Dashboard charts designed for screenshot-readiness:
- Takeaway-title format on chart titles
- Clean Plotly charts with minimal chrome
- High-contrast colors for readability at slide scale

Suggested structure:
1. Title slide
2. Descriptive insight (scatter plot, takeaway title, callout)
3. Diagnostic insight (player example, trend chart, explanation)
4. Recommendation ([Action] → [Expected outcome])
5. Architecture (pipeline diagram)

## Out of Scope

- No pitching-specific dashboard tab (batters have richer Statcast data in the current schema)
- No automated slide generation
- No Snowflake load of scraped content (knowledge base sources live in `knowledge/raw/` per CLAUDE.md architecture)
- No normalized z-score gap calculation (raw xwOBA - batting_avg is sufficient and easier to explain)
