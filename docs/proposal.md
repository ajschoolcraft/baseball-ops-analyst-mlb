# Project Proposal

**Name:** AJ Schoolcraft

**Project Name:** Baseball Operations Analyst Portfolio — MLB Player Performance Analytics

**GitHub Repo:** https://github.com/ajschoolcraft/baseball-ops-analyst-mlb

## Job Posting

- **Role:** Baseball Operations Analyst
- **Company:** San Francisco Giants
- **Link:** https://www.indeed.com/viewjob?jk=3e00112638e61b02&from=mcp-claude-jobsearch&jrtk=5-cmh1-0-1jln42i07mn5n802-3e00112638e61b02&xpse=SoBm67I3l3AfSyAZJj0LbzkdCdPP&xfps=cb7457f4-66bb-4484-8af3-256075a4223f&xkcb=SoCS67M3l3AFV10vjZ0LbzkdCdPP

**SQL requirement (quote the posting):** "Proficiency in SQL and at least one general-purpose programming language (e.g. Python, R)."

## Reflection

This posting targets the R&D team in San Francisco Giants Baseball Operations, and it maps almost one-to-one onto the analytics engineering skills this course teaches: the role requires SQL proficiency, Python for extraction and modeling, statistical analysis on real datasets, and the ability to prototype lightweight tools and visualizations that communicate findings to non-technical stakeholders. To prove I can do this work, I am building an end-to-end pipeline that pulls player performance data from the MLB Stats API and Statcast (via Pybaseball), lands it in Snowflake, transforms it through dbt staging and mart layers into a star schema of fact tables (player-game and player-season stats) and dimensions (players, teams, seasons, games), and surfaces it through a Streamlit dashboard that compares traditional stats to advanced Statcast metrics across the 2015–2025 Statcast era — plus a Claude Code knowledge base synthesizing public sabermetric research from FanGraphs, Baseball Prospectus, and Statcast methodology docs, which directly exercises the "evaluate and adapt public baseball research" responsibility in the posting. The coursework skills it leans on are SQL and dimensional modeling, dbt transformations and testing, Python-based API extraction, GitHub Actions orchestration, Streamlit dashboarding, and data storytelling. Because the architecture is source-agnostic, this same project transfers cleanly to other sports analytics roles (e.g., Quantitative Analyst, Baseball Systems roles at any MLB club), general analytics engineer and BI analyst roles in any industry, and data analyst roles where a public star schema, dashboard, and synthesized knowledge base are the proof of craft.
