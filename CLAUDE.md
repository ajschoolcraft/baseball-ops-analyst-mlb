# CLAUDE.md

Project context for Claude Code sessions in this repo. Read this first before making suggestions or writing code.

## Project

**Baseball Operations Analyst Portfolio — MLB Player Performance Analytics.** An end-to-end analytics engineering portfolio project. This is a public repo — assume employers will read it.

**Target role (framing the work):** Baseball Operations Analyst, San Francisco Giants R&D team. The posting requires SQL, Python, statistical modeling on real datasets, prototyping tools/visualizations, and evaluating public baseball research. Every deliverable should map back to one of those skills.

**Transferability:** The architecture is source-agnostic. It should also read as proof of craft for generic data analyst, analytics engineer, and BI roles — so prefer conventional analytics engineering patterns over sport-specific hacks.

## Tech Stack

| Layer | Tool |
|---|---|
| Warehouse | Snowflake (trial, AWS us-east-1) |
| Transformation | dbt (staging + mart layers, star schema) |
| Extraction | Python — `MLB-StatsAPI`, `pybaseball` for Statcast |
| Orchestration | GitHub Actions (scheduled) |
| Dashboard | Streamlit (deployed to Streamlit Community Cloud) |
| Knowledge base | Claude Code over scraped markdown in `knowledge/` |
| IDE / AI | Cursor + Claude Code + Superpowers |

## Architecture

```
MLB Stats API ─┐
               ├─► GitHub Actions ─► Snowflake raw ─► dbt staging ─► dbt mart (star schema) ─► Streamlit dashboard
Pybaseball   ─┘

Web scrapes (FanGraphs, BP, Statcast docs, etc.) ─► GitHub Actions ─► knowledge/raw/ ─► Claude Code ─► knowledge/wiki/
```

### Data sources

- **API (structured path):** MLB Stats API (`statsapi.mlb.com`, no auth) for biographical data, season stats, game logs, schedules. Pybaseball for Statcast batted-ball and advanced metrics (xwOBA, wRC+, FIP, barrel rate, WAR).
- **Web scrape (knowledge base path):** 15+ sources from 3+ sites — FanGraphs, Baseball Prospectus, Statcast/MLB methodology docs, Tangotiger/The Book Blog, Baseball Reference.
- **Scope:** 2015–2025, the Statcast era. All MLB teams, filterable to Giants.

### Star schema (mart layer)

**Facts**
- `fct_player_game_stats` — one row per player per game. Batting line + game-level Statcast metrics. FKs: `player_id`, `game_id`, `team_id`, `season_id`.
- `fct_player_season_stats` — one row per player per season. Batting stats (AVG/OBP/SLG/OPS, wRC+, xwOBA, barrel rate) AND pitching stats (ERA, WHIP, K/9, FIP) in the same table, with a `player_type` column (`batter`/`pitcher`) indicating which stats apply. WAR applies to both.

**Dimensions**
- `dim_players` — player_id, name, position, bats, throws, birth_date, debut_date, active_status
- `dim_teams` — team_id, name, abbreviation, league, division
- `dim_seasons` — season_year, game_count, context notes
- `dim_games` — game_id, date, home/away team ids, venue, final score

### dbt layers

- **raw** — direct API loads, minimal transformation
- **staging** — cleaning, renaming, type casting, dedup; one staging model per raw source; tests for uniqueness, not-null, accepted values
- **mart** — star schema facts + dimensions with business logic

## Repo Layout

```
extract/           Python extraction scripts
dbt/               dbt project: staging + mart models, tests
.github/workflows/ GitHub Actions pipelines
dashboard/         Streamlit app
knowledge/         Scraped sources and synthesized wiki
docs/              Proposal, job posting, slides, resume
```

## Conventions

- **No credentials in the repo, ever.** Snowflake creds, API keys, anything sensitive → `.env` (gitignored) locally and GitHub Actions secrets in CI.
- **Public repo.** Every commit is visible to employers. Commit messages should be professional and explain the *why*.
- **Prefer readable, conventional code** over clever abstractions. Standard analytics engineering patterns over sport-specific hacks.
- **Prefer editing existing files** over creating new ones.

## Knowledge Base

Querying the knowledge base works like this:

1. **`knowledge/index.md`** is the entry point — it lists every wiki page with a one-line summary.
2. **`knowledge/wiki/*.md`** are synthesized pages (overview, key metrics, Statcast methodology, player evaluation frameworks). Treat these as the authoritative synthesis — prefer quoting from them over re-deriving from raw sources.
3. **`knowledge/raw/*`** are the original scraped sources. Go here when the wiki is thin on a topic or when a claim needs a direct citation.

**When answering a question about baseball analytics, sabermetrics, or the Giants:**
1. Start with `knowledge/index.md` to find the right wiki page.
2. Read the wiki page. If it answers the question, cite it.
3. If the wiki is thin, grep `knowledge/raw/` for supporting material and synthesize.
4. Always cite source files (`knowledge/wiki/key-metrics.md`, or the raw source filename). Never invent stats or sabermetric history — if it isn't in the knowledge base or a primary API, say so.

