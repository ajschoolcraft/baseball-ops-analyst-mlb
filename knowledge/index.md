# Knowledge Base Index

Entry point for the baseball analytics knowledge base. Read the wiki pages first; fall back to raw sources when a topic needs more depth or direct citation.

---

## Wiki Pages

| Page | Summary |
|---|---|
| [overview.md](wiki/overview.md) | What sabermetrics is, why advanced metrics matter over traditional stats, how the Statcast revolution changed player evaluation, and how this knowledge base is organized |
| [key-metrics.md](wiki/key-metrics.md) | Comprehensive metric guide: every stat in the pipeline organized by category (traditional hitting, advanced hitting, batted ball, traditional pitching, advanced pitching, holistic value), with benchmarks and when-to-use guidance |
| [statcast-methodology.md](wiki/statcast-methodology.md) | How Hawk-Eye cameras work, what Statcast tracks, barrel classification thresholds, how expected stats (xBA, xSLG, xwOBA) are calculated, data availability by era |
| [player-evaluation-frameworks.md](wiki/player-evaluation-frameworks.md) | When traditional and advanced stats diverge and why (BABIP luck, shift effects, ballpark), the gap score concept (xwOBA − wOBA), red flags for unsustainable performance, and a systematic layered evaluation approach |

---

## Raw Sources

| File | Site | Topic |
|---|---|---|
| [01-statcast-metrics-context.md](raw/01-statcast-metrics-context.md) | Baseball Savant / MLB | Outcomes data by contact type: barrel, blast, fast swing, hard-hit, ideal attack angle, sweet-spot, squared-up. Includes 2026 season outcome tables. |
| [02-fangraphs-wrc-plus.md](raw/02-fangraphs-wrc-plus.md) | FanGraphs Library | wRC and wRC+ definitions, calculation formula, benchmarks, and rationale for preferring wRC+ over OPS+ |
| [03-driveline-stuff-plus-pitch-models.md](raw/03-driveline-stuff-plus-pitch-models.md) | Driveline Baseball | Stuff+ pitch model: methodology, inputs (velocity, break, arm angle, extension), scaling (100 = league average), pitch bucket structure, per-pitch-type analysis |
| [04-fangraphs-woba.md](raw/04-fangraphs-woba.md) | FanGraphs Library | wOBA: definition, linear weights formula, benchmarks, how to convert to wRAA, relationship to wRC+ |
| [05-fangraphs-fip.md](raw/05-fangraphs-fip.md) | FanGraphs Library | FIP: definition, formula ((13×HR + 3×(BB+HBP) − 2×K)/IP + constant), benchmarks, relationship to ERA and pitcher WAR |
| [06-fangraphs-babip.md](raw/06-fangraphs-babip.md) | FanGraphs Library | BABIP: definition, formula, three driving factors (defense, luck, talent), sample size requirements (~800 BIP for hitters, ~2000 for pitchers), how to use as a sanity check |
| [07-fangraphs-war.md](raw/07-fangraphs-war.md) | FanGraphs Library | WAR: full definition, position player and pitcher calculation frameworks, fWAR vs. rWAR differences, benchmarks (scrub through MVP), limitations |
| [08-savant-expected-stats.md](raw/08-savant-expected-stats.md) | Baseball Savant / MLB | Expected statistics leaderboard page; xBA, xSLG, xwOBA methodology description and context on how contact quality is modeled |
| [09-savant-barrel-definition.md](raw/09-savant-barrel-definition.md) | MLB Glossary | Official barrel definition: minimum 98 mph exit velocity, angle ranges by mph (26–30° at 98 mph, expanding with speed), historical production (.822 BA / 2.386 SLG in barrels) |
| [10-savant-exit-velo-launch-angle.md](raw/10-savant-exit-velo-launch-angle.md) | MLB Glossary | Exit velocity definition and fantasy applications; launch angle definition, contact-type thresholds (GB/LD/FB/popup), sweet spot (8–32 degrees) |
| [11-savant-pitch-tracking.md](raw/11-savant-pitch-tracking.md) | MLB Glossary (Statcast) | Statcast system overview: Hawk-Eye hardware, camera counts, measurement list (EV, LA, spin rate, bat speed, sprint speed, etc.), metric list (barrels, OAA, xwOBA, etc.), data categories by discipline |
| [12-fangraphs-ops-plus.md](raw/12-fangraphs-ops-plus.md) | FanGraphs Library | OPS and OPS+: definitions, calculation (OPS = OBP + SLG), benchmarks, key limitation (treats OBP = SLG; OBP is ~1.8x more valuable), recommendation to use wOBA/wRC+ instead |
| [13-bp-intro-sabermetrics.md](raw/13-bp-intro-sabermetrics.md) | Baseball Prospectus | BP glossary: comprehensive alphabetical reference for BP-specific statistics including BABIP, BRR (Baserunning Runs), VORP/WARP, DRA, and many others |
| [14-bp-drc-plus.md](raw/14-bp-drc-plus.md) | Baseball Prospectus | DRC+ (Deserved Runs Created Plus): Bayesian hitting model, scale (100 = average), advantages over wRC+ (adjusts for pitcher quality, defense, catcher framing; Bayesian regression in small samples) |
| [15-tangotiger-linear-weights.md](raw/15-tangotiger-linear-weights.md) | FanGraphs Library (Tango) | Linear weights methodology: run expectancy matrix, deriving event run values, scaling to produce wOBA and FIP weights. Foundational mathematics behind most advanced hitting metrics. |
| [16-savant-statcast-glossary.md](raw/16-savant-statcast-glossary.md) | Baseball Savant / MLB | Expanded Statcast metrics context with 2026 season outcomes by contact type (barrel, blast, fast swing, hard-hit, sweet-spot, squared-up); cleaner table format than file 01 |
