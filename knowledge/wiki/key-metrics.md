# Key Metrics Guide

A comprehensive reference for every metric tracked in this pipeline. For each metric: what it measures, benchmarks, when to use it, and its relationship to traditional alternatives.

---

## Traditional Hitting

### Batting Average (AVG)
**What it measures:** Hits divided by at-bats. A .300 hitter gets a hit in 30% of official plate appearances.

**Benchmarks:** Excellent ≥ .300 | Average ~.250 | Poor ≤ .220

**When to use it:** Broad audience communication; context where simplicity matters. AVG is universally understood and appears on broadcasts.

**Limitations:** Ignores walks, hit-by-pitches, and the extra value of extra-base hits. Treats a bloop single identically to a line drive double. Heavily influenced by BABIP luck (see below). A poor signal for predicting future performance.

---

### On-Base Percentage (OBP)
**What it measures:** How often a batter reaches base (hits + walks + HBP) divided by plate appearances. Captures what batting average misses: the value of not making outs.

**Benchmarks:** Excellent ≥ .380 | Average ~.320 | Poor ≤ .290

**When to use it:** Alongside other metrics; OBP is more predictive than AVG because walk rate is a stable skill. OBP is approximately 1.8x more valuable than SLG in run-scoring terms (see [12-fangraphs-ops-plus.md]).

---

### Slugging Percentage (SLG)
**What it measures:** Total bases divided by at-bats. Weights extra-base hits but still ignores walks and uses an imprecise weighting (doubles counted as 2x singles, triples as 3x).

**Benchmarks:** Excellent ≥ .500 | Average ~.410 | Poor ≤ .340

**When to use it:** Quick proxy for power. More informative than AVG but less accurate than wOBA. A double is not twice as valuable as a single in run-expectancy terms, which is the core limitation.

---

### OPS and OPS+
**What it measures:** OPS = OBP + SLG. OPS+ normalizes that sum for park and league, with 100 as league average (each point = 1% above/below average).

**Benchmarks (OPS+):** Excellent ≥ 140 | Above Average ~115 | Average 100 | Below Average ~85 | Poor ≤ 75

**When to use it:** OPS is widely available (broadcast, baseball cards) and correlates reasonably with run production. OPS+ enables cross-era comparisons. However, both metrics give equal weight to OBP and SLG when OBP is roughly twice as valuable — this is why wRC+ is preferred (see [12-fangraphs-ops-plus.md]).

---

### BABIP (Batting Average on Balls in Play)
**What it measures:** `(H − HR) / (AB − K − HR + SF)` — the fraction of balls put in play that become hits, excluding home runs and strikeouts.

**Benchmarks:** League average ≈ .300 | Sustainable elite hitter range: .320–.360 | Extreme unsustainable: ≥ .380 or ≤ .230

**When to use it:** Primarily as a diagnostic. If a batter's BABIP is far above his career average, some portion of his strong stat line is likely luck. For pitchers, BABIP is almost entirely outside their control (requires ~2,000 balls in play to stabilize), making a high pitcher BABIP a signal of poor defense or bad luck rather than poor pitching (see [06-fangraphs-babip.md]).

**Key insight:** Hitter BABIP stabilizes in ~800 balls in play. Pitcher BABIP takes ~2,000. Expect batters to regress toward their career BABIP; expect pitchers to regress toward league average.

---

## Advanced Hitting

### wOBA (Weighted On-Base Average)
**What it measures:** A weighted sum of all offensive events — walks, HBP, singles, doubles, triples, home runs — where each event's weight equals its empirical run value derived from linear weights. Created by Tom Tango and central to "The Book."

**Formula (2013 example):** `wOBA = (0.690×uBB + 0.722×HBP + 0.888×1B + 1.271×2B + 1.616×3B + 2.101×HR) / PA`. Weights recalculate each season based on the run environment (see [04-fangraphs-woba.md]).

**Benchmarks:** Excellent ≥ .400 | Great ~.370 | Above Average ~.340 | Average ~.320 | Below Average ~.300 | Poor ≤ .270

**Scale:** Calibrated to match league-average OBP, so intuitions about what a "good" OBP looks like transfer directly to wOBA.

**When to use it:** Preferred over OPS for rate-stat offensive evaluation. Unlike OPS, wOBA properly weights each event. Unlike AVG, it captures the full offensive picture. Not park-adjusted, so use wRC+ for cross-park comparisons.

**Traditional counterpart:** OPS (wOBA is strictly more accurate)

---

### wRC+ (Weighted Runs Created Plus)
**What it measures:** wRC+ takes a player's wRC (weighted runs created — the counting-stat version of wOBA) and adjusts it for both league and park factors. League average = 100; each point above/below 100 is one percent above/below average.

**Formula:** `wRC+ = (((wRAA/PA + Lg R/PA) + (Lg R/PA − Park Factor × Lg R/PA)) / (AL or NL wRC/PA excl. pitchers)) × 100`

**Benchmarks:** Excellent ≥ 160 | Great ~140 | Above Average ~115 | Average 100 | Below Average ~80 | Poor ≤ 75

**When to use it:** The single best rate statistic for comparing hitter offensive value across different parks, leagues, and eras. A player with a 140 wRC+ in 2000 and a player with a 140 wRC+ in 2024 were equally dominant relative to their competition. Not position-adjusted (see [02-fangraphs-wrc-plus.md]).

**Traditional counterpart:** OPS+ (wRC+ is more accurate because it uses proper linear weights rather than treating OBP = SLG)

---

### xwOBA (Expected Weighted On-Base Average)
**What it measures:** Every batted ball is assigned a probability of becoming a single, double, triple, or home run based on its exit velocity, launch angle, and sprint speed — benchmarked against all comparable batted balls since 2015. xwOBA is the accumulation of those probabilities expressed on the wOBA scale.

**When to use it:** The primary Statcast-era hitting evaluation metric. xwOBA answers "what should this hitter's wOBA have been based on the quality of contact?" A large wOBA − xwOBA gap suggests luck (positive = lucky; negative = unlucky). Available from Baseball Savant (see [08-savant-expected-stats.md]).

**Availability:** Statcast era, 2015–present.

---

## Batted Ball Metrics

### Barrel Rate (Barrel%)
**What it measures:** The percentage of batted balls classified as "barrels" — the ideal combination of exit velocity and launch angle that historically produces a minimum .500 batting average and 1.500 slugging percentage. A ball requires at least 98 mph exit velocity to qualify; at 98 mph, the barrel angle range is 26–30 degrees, expanding with higher velocity. At 116+ mph, any angle 8–50 degrees qualifies (see [09-savant-barrel-definition.md]).

**Benchmarks (2026 data):** Barrels produced a .668–.684 BA and 2.184–2.236 SLG in season data. Non-barrels produce only .288–.292 BA. The contrast is stark — barrels are the most impactful contact type in the game (see [16-savant-statcast-glossary.md]).

**When to use it:** For evaluating raw hitting quality and power potential. High barrel rate with suppressed actual results signals a player due for positive regression.

---

### Exit Velocity (EV) / Hard-Hit Rate
**What it measures:** Exit velocity is the speed of the ball off the bat in mph, measured immediately after contact. Hard-hit is defined as ≥ 95 mph exit velocity. Average exit velocity (aEV) is the mean across all batted ball events.

**Benchmarks (2026 data):** Hard-hit balls produced .466–.477 BA and .898–.923 SLG; non-hard-hit balls produced only .221–.224 BA (see [01-statcast-metrics-context.md]).

**When to use it:** Identifies whether a batter is making quality contact regardless of outcomes. A player ranked in the top decile of exit velocity but posting poor batting stats is a candidate for regression back toward his expected performance level. Also used for pitchers as "exit velocity against."

---

### Launch Angle (LA) / Sweet-Spot Rate
**What it measures:** Launch angle is the vertical angle in degrees at which the ball leaves the bat. Ground balls: below 10 degrees. Line drives: 10–25 degrees. Fly balls: 25–50 degrees. Pop-ups: above 50 degrees. The "sweet spot" range is 8–32 degrees, encompassing line drives and productive fly balls (see [10-savant-exit-velo-launch-angle.md]).

**Benchmarks (2026 data):** Sweet-spot batted balls produced .575–.584 BA and 1.022–1.037 SLG; outside the sweet spot, only .195 BA (see [01-statcast-metrics-context.md]).

**When to use it:** Diagnose hit-type profile. A hitter transitioning from a ground-ball approach to optimal launch angle often shows improved exit velocity translation into production.

---

## Pitching — Traditional

### ERA (Earned Run Average)
**What it measures:** Earned runs allowed per 9 innings pitched. The traditional gold-standard pitching stat.

**Benchmarks:** Excellent ≤ 2.50 | Above Average ~3.25 | Average ~4.00 | Below Average ~4.75 | Poor ≥ 5.50

**Limitations:** ERA includes the quality of defense behind the pitcher, sequencing luck (stranded runner rates), and BABIP variance. Over short samples, ERA can diverge substantially from true talent. Use in conjunction with FIP (see [05-fangraphs-fip.md]).

---

### WHIP (Walks + Hits per Inning Pitched)
**What it measures:** `(BB + H) / IP`. How many baserunners a pitcher allows per inning.

**Benchmarks:** Excellent ≤ 1.00 | Average ~1.25 | Poor ≥ 1.50

**When to use it:** Simple baserunner-prevention check. WHIP shares ERA's weakness of being affected by defense and luck, but it is more park-neutral than ERA and widely understood.

---

### K/9 (Strikeouts per 9 Innings)
**What it measures:** `(K / IP) × 9`. Strikeout rate expressed per 9 innings.

**Benchmarks:** Excellent ≥ 10.0 | Average ~8.5 | Below Average ≤ 6.5

**When to use it:** Strikeouts are one of the three "true outcomes" pitchers fully control. High K/9 is a reliable predictor of future performance because it does not depend on defense or luck. K% (strikeout percentage of batters faced) is often preferred for its park/era neutrality.

---

## Pitching — Advanced

### FIP (Fielding Independent Pitching)
**What it measures:** Reconstructs what a pitcher's ERA would have been if the defense behind him had been league average on balls in play. Uses only outcomes the pitcher controls: `FIP = ((13×HR) + (3×(BB+HBP)) − (2×K)) / IP + constant`, where the constant (≈3.10) anchors FIP to the ERA scale.

**Scale:** Same scale as ERA (lower is better); league-average FIP = league-average ERA by design.

**Benchmarks:** Same as ERA benchmarks above.

**When to use it:** When separating pitching skill from defense and luck. FIP is a better predictor of next-season ERA than current ERA because it filters out the noise from balls in play. FanGraphs uses FIP as the basis for pitcher WAR. ERA − FIP gap identifies pitchers who are outperforming (positive gap) or underperforming (negative gap) their true skill (see [05-fangraphs-fip.md]).

---

### xFIP (Expected Fielding Independent Pitching)
**What it measures:** A variant of FIP that normalizes a pitcher's home run rate to league-average HR/FB rate. Because home run rates on fly balls fluctuate significantly year-to-year, xFIP is often more stable than FIP over small samples.

**When to use it:** Early-season evaluation or when a pitcher has an unusual HR/FB rate (either very high or very low). xFIP corrects for short-term HR luck on top of balls-in-play luck.

---

### Stuff+ (Pitch Quality Model)
**What it measures:** A pitch-level model that scores each pitch based on its physical characteristics — velocity, vertical break, horizontal break, arm angle, and release extension — compared to league-average pitches of the same type. Scaled like IQ: 100 = league average; 130 = 30% better than average within that pitch bucket. Developed by Driveline Baseball (see [03-driveline-stuff-plus-pitch-models.md]).

**Pitch buckets:** Fastballs (4-seam, sinker), Breaking balls (cutter, slider, curveball), Offspeed (changeup, splitter). Pitches compete within their bucket, so a 150 Stuff+ slider is not equivalent to a 150 Stuff+ fastball in raw run value.

**When to use it:** Evaluating pitch mix quality and development; identifying pitchers with elite raw stuff that is not yet translating to results. Stuff+ is location-agnostic — a pitch can have elite Stuff+ and still get hit if thrown in a hittable location.

---

## Holistic Value

### WAR (Wins Above Replacement)
**What it measures:** A single number summarizing a player's total contribution — batting, baserunning, fielding, and position — relative to a freely available replacement-level player. The question WAR answers: "If this player were injured and replaced by a AAA call-up, how many wins would the team lose?"

**Formula (position players):** `WAR = (Batting Runs + Baserunning Runs + Fielding Runs + Positional Adjustment + League Adjustment + Replacement Runs) / Runs Per Win`

**Formula (pitchers):** FIP-based, scaled to innings pitched and converted to wins above replacement.

**Benchmarks:** Scrub ~0–1 | Role Player ~1–2 | Solid Starter ~2–3 | Good Player ~3–4 | All-Star ~4–5 | Superstar ~5–6 | MVP ≥ 6

**Versions:** fWAR (FanGraphs, FIP-based for pitchers), rWAR/bWAR (Baseball-Reference, RA9-based), WARP (Baseball Prospectus). Framework is identical; inputs differ. Do not compare precise values across systems.

**When to use it:** Cross-position, cross-era player comparisons. Use WAR to distinguish tiers of players, not to split hairs between adjacent values — a 6.4 WAR and a 6.1 WAR player are essentially indistinguishable; a 6.4 and a 4.1 are meaningfully different (see [07-fangraphs-war.md]).

---

### DRC+ (Deserved Runs Created Plus)
**What it measures:** Baseball Prospectus's comprehensive hitting metric. A Bayesian model that credits batters for outcomes they most control (quality of contact, plate discipline), adjusts for park, league, pitcher quality faced, defense quality, and umpire tendencies, and regresses toward the mean based on sample size. Scaled like wRC+: 100 = league average; each point = 1%.

**Key advantage over wRC+:** DRC+ separates what a batter deserved from what defense and luck contributed. It is more stable in small samples due to Bayesian regression, and it adjusts for the quality of pitchers faced — something wRC+ does not do (see [14-bp-drc-plus.md]).

**When to use it:** Early-season small-sample evaluation; identifying batters whose stats are suppressed or inflated by context. DRC+ is more conservative in its adjustments, making extreme values more trustworthy than extreme wRC+ values.
