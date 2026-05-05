# Overview: Sabermetrics and the Statcast Era

## What Is Sabermetrics?

Sabermetrics is the empirical analysis of baseball through statistics, with the goal of measuring in-game activity as objectively as possible. The term derives from SABR — the Society for American Baseball Research — and was popularized by Bill James beginning in the late 1970s. Where traditional baseball analysis relied on intuition, scout opinion, and a small set of counting stats (batting average, RBI, wins), sabermetrics asks a more rigorous question: what events on the field actually cause teams to win or lose games?

The foundational insight is that not all offensive events are created equal. A walk, a single, and a home run all look different in a box score, but they contribute different amounts to run expectancy. Linear weights methodology, developed by Pete Palmer and refined by Tom Tango, quantifies each event's average run value so analysts can weigh them accurately (see [15-tangotiger-linear-weights.md]). This underlying principle drives the most important modern metrics: wOBA, wRC+, and FIP all use empirically derived weights rather than assuming equal value across outcomes.

## Why Advanced Metrics Matter

Traditional stats like batting average and ERA have two well-documented problems: they are noisy and they confound multiple contributors.

**Batting average** ignores walks, treats all hits as equal, and is heavily influenced by balls in play falling for hits — a phenomenon that varies substantially due to defense and luck rather than pure hitting skill. A player batting .310 may be getting lucky on weakly-hit balls, while a .260 hitter generating hard contact may be underperforming his true talent level (see [06-fangraphs-babip.md]).

**ERA** captures runs allowed, but runs allowed depend on defense quality, sequencing luck, and the random variation in when baserunners score. A pitcher with poor defense playing behind him can easily allow 15-20% more runs than his actual skill warrants. Fielding Independent Pitching (FIP) strips this out by focusing only on what pitchers demonstrably control: strikeouts, walks, and home runs allowed (see [05-fangraphs-fip.md]).

Advanced metrics address both problems: they isolate individual contribution, correct for contextual factors (park, league, era), and provide more predictive signal over smaller sample sizes.

## The Statcast Revolution

The Statcast era began in 2015 when MLB installed optical tracking technology in all 30 ballparks. The current system, Hawk-Eye (introduced in 2020), uses 12 cameras per venue — five high-frame-rate cameras focused on bat and pitch tracking, seven dedicated to player and batted ball tracking — and captures virtually every play at the granular physical level (see [11-savant-pitch-tracking.md]).

Before Statcast, analysts could observe outcomes (a ball was a single) but not process (how hard was it hit, at what angle). Statcast exposes the underlying mechanics. Two balls that both become outs can be very different in quality: one softly grounded to an infielder, the other a screaming line drive caught by the right fielder at the wall. Statcast measures these differences and makes them available for analysis.

The key Statcast measurements are exit velocity (how hard the ball comes off the bat), launch angle (vertical angle in degrees), and for pitchers: velocity, spin rate, and movement profiles. From these raw measurements, MLB derives metrics like barrel rate, expected batting average (xBA), and expected wOBA (xwOBA) that reflect the quality of contact rather than its outcome (see [08-savant-expected-stats.md], [09-savant-barrel-definition.md], [10-savant-exit-velo-launch-angle.md]).

The practical result: analysts can now identify a hitter who is making elite contact but getting unlucky outcomes, or a pitcher generating weak contact that will normalize over time. This predictive value is central to modern roster evaluation and player development.

## The Statcast Era in Context

The 2015–present window, which defines the scope of this project, represents the most data-rich period in baseball history. Key milestones within the era include:

- **2015**: Statcast deployed league-wide; barrel and exit velocity data begin
- **2020**: Hawk-Eye replaces the hybrid camera/radar system; tracking precision improves substantially
- **2023**: Bat tracking data (swing speed, attack angle, squared-up rate) becomes available mid-season

Data availability varies by metric. Barrel and hard-hit rate data begin in 2016; bat tracking metrics (blasts, fast swing, ideal attack angle) only have reliable data from 2023 onward (see [01-statcast-metrics-context.md]). Analyses spanning the full decade should account for these availability windows.

## How This Knowledge Base Is Organized

This knowledge base synthesizes 16 raw source files scraped from FanGraphs, Baseball Savant/MLB, Baseball Prospectus, and Driveline Baseball. The wiki contains four pages:

- **[overview.md](overview.md)** — This page: context, background, what Statcast changed
- **[key-metrics.md](key-metrics.md)** — Comprehensive metric guide covering every stat in the pipeline, with benchmarks
- **[statcast-methodology.md](statcast-methodology.md)** — How Statcast's tracking system works and how expected stats are calculated
- **[player-evaluation-frameworks.md](player-evaluation-frameworks.md)** — When traditional and advanced stats diverge, how to diagnose gaps, and a systematic evaluation approach

The index at `knowledge/index.md` lists all wiki pages and all 16 raw source files. When a wiki page is thin on a topic, consult the corresponding raw source directly.
