# Player Evaluation Frameworks

## The Core Tension: Traditional vs. Advanced Stats

When evaluating a player, traditional and advanced statistics often tell the same story. A .320 hitter with a 130 wRC+ is clearly a strong offensive player by any measure. But there are systematic, predictable cases where the two diverge — and understanding the cause of those gaps is the central skill in modern player evaluation.

The general principle: **traditional stats describe what happened; advanced stats help explain why and predict what will happen next.** A scout relies on observed outcomes; an analyst tries to separate skill from noise.

---

## What Causes Traditional–Advanced Gaps

### 1. BABIP Variance (Luck on Balls in Play)

The most common source of divergence. Around 30% of all balls put in play fall for hits, but this rate fluctuates substantially in small samples due to defense, sequencing, and random variation. A player bathing in .380 BABIP will have a bloated batting average; a .230 BABIP player may be posting a batting average 40–50 points below their true talent level (see [06-fangraphs-babip.md]).

Sustainable BABIP range: the best hitters in baseball can sustain .340–.360; most qualified hitters settle between .280–.330. Any BABIP above .380 or below .230 for a qualified hitter is almost certainly partially luck-driven. The diagnostic question is always: compare the current BABIP to the player's multi-year career average rather than to league average.

**Practical application:** A player with a .300 career BABIP who is posting a .360 BABIP in April is likely to regress toward .300, not stay at .360. Downgrade their projected stats accordingly.

### 2. xwOBA vs. wOBA Gap (Contact Quality vs. Outcomes)

Statcast provides a direct window into this gap. xwOBA models what the player's wOBA should have been based purely on exit velocity, launch angle, and sprint speed. When wOBA and xwOBA diverge significantly, it signals luck, unusual defense, or a structural change in how the player hits.

**Gap score (conceptual definition):** `gap = xwOBA − batting_avg` is one informal signal analysts use, though a more precise version is `xwOBA − wOBA`. A persistently negative gap (actual wOBA exceeds xwOBA) suggests the player is getting good fortune on weakly-hit balls. A persistently positive gap (xwOBA exceeds wOBA) suggests bad fortune — the player is generating elite contact that is not translating to results (see [08-savant-expected-stats.md]).

**Rule of thumb:** A wOBA − xwOBA gap larger than ±.030 over 200+ plate appearances warrants investigation. Over a full season (500+ PA), gaps ≥ ±.020 are meaningful.

### 3. Ballpark Effects

Oracle Park (San Francisco) is one of the most pitcher-friendly venues in baseball, particularly for right-handed hitters. A Giants hitter posting a .800 OPS at Oracle is a different proposition than a Rockies hitter posting the same OPS at Coors Field. This is why park-adjusted metrics — wRC+, OPS+, and ERA− — are essential for roster evaluation and why raw rate stats should always be contextualized (see [12-fangraphs-ops-plus.md], [02-fangraphs-wrc-plus.md]).

Park factors are applied multiplicatively. A ballpark with a 95 park factor is 5% below average for run scoring. Since players split time between home and away, the effect is halved; a full-season player at a park with a factor of 95 gets roughly a 2.5% downward adjustment.

### 4. Defense and Positioning (Shift Effects)

Pre-rule-change (before 2023), aggressive defensive shifts could suppress batting average significantly without affecting a hitter's actual contact quality. A pull-heavy hitter facing a four-man shift might bat .230 on grounders that would be singles in a traditional alignment, while generating xwOBA consistent with a .270+ hitter. wRC+ incorporates the actual outcome; xwOBA shows what the underlying contact quality predicts. The 2023 infield shift ban has reduced but not eliminated this effect, since two-man infield overloads are still permitted.

### 5. Pitcher FIP vs. ERA Gap

For pitchers, the analogous gap is ERA − FIP. A pitcher with ERA 4.50 and FIP 3.50 has been "unlucky" — their defense, sequencing, or BABIP has inflated their ERA above what the fielding-independent outcomes (strikeouts, walks, home runs) would predict. Expect ERA to decline toward FIP. The reverse — ERA 3.50, FIP 4.50 — signals a pitcher whose results may be unsustainable (see [05-fangraphs-fip.md]).

---

## Red Flags: Signals of Unsustainability

The following patterns in a player's stat line are red flags that good or bad performance may not persist:

**For batters — performance likely to decline:**
- BABIP significantly above career average (>30 points) without a corresponding increase in exit velocity or launch angle
- High wOBA with low barrel rate and low hard-hit rate (soft contact getting lucky)
- wOBA substantially above xwOBA over 300+ PA

**For batters — performance likely to improve:**
- BABIP significantly below career average without explanation
- High barrel rate and hard-hit rate with suppressed batting average
- xwOBA substantially above wOBA over 300+ PA
- Strong exit velocity metrics with poor launch angle (ground-ball heavy hitter with room to optimize)

**For pitchers — performance likely to worsen:**
- ERA substantially below FIP (ERA−FIP < −0.5 over a full season)
- Abnormally low HR/FB rate not supported by pitch type profile (xFIP regression candidate)
- BABIP well below .280 over 150+ innings

**For pitchers — performance likely to improve:**
- ERA substantially above FIP (ERA−FIP > +0.75)
- High BABIP against with strong K rate and acceptable walk rate (defense/luck suppression)

---

## How to Evaluate a Player: A Systematic Approach

1. **Start with the rate stats:** wRC+ for hitters, FIP for pitchers. These are the most context-adjusted, single-number summaries of performance.

2. **Check the expected vs. actual gap:** Pull xwOBA from Baseball Savant. Is the player performing near their xwOBA? If the gap is large, find the cause.

3. **Examine contact quality:** Barrel rate, hard-hit rate, exit velocity, and launch angle tell you whether the player is generating quality contact. A player with an elite barrel rate is a different proposition than a player whose production is BABIP-driven.

4. **Apply context corrections:** Adjust for park if the gap is noticeable (Oracle Park, Coors Field, Petco Park all create meaningful distortions). Check if the player faces a disproportionate mix of LHP vs. RHP that could inflate or deflate split-based production.

5. **Apply sample-size discipline:** BABIP requires ~800 balls in play to stabilize for hitters, ~2,000 for pitchers. Barrel rate and exit velocity are more stable in smaller samples (~100 batted ball events). Don't overfit to 50-PA hot streaks or 3-start slumps.

6. **Use WAR as a ceiling check:** After computing hitting value (wRC+), add a rough positional adjustment and defensive estimate to arrive at WAR. WAR contextualizes whether an individual metric-based assessment is consistent with overall player value (see [07-fangraphs-war.md]).

7. **Cross-reference with DRC+:** DRC+ (Baseball Prospectus) applies Bayesian regression, adjusts for pitcher quality faced, and is more conservative in small samples. If a player has a 140 wRC+ but only a 115 DRC+, the DRC+ is suggesting that the context has been favorable — worth investigating (see [14-bp-drc-plus.md]).

---

## Summary: The Mental Model

Think of player evaluation as a layered process:

| Layer | Question | Metric |
|---|---|---|
| What happened? | How did this player perform? | BA, ERA, OPS |
| How well did they hit/pitch? | After removing park/league context? | wRC+, FIP |
| Was the contact quality there? | What do the physics say? | xwOBA, barrel%, EV |
| Was luck involved? | Why does actual differ from expected? | BABIP, wOBA−xwOBA gap |
| What is their total value? | How many wins did they contribute? | WAR, DRC+ |

The goal is not to find a single perfect number — WAR and DRC+ are both estimates with uncertainty ranges — but to triangulate from multiple angles. When traditional stats, advanced stats, and Statcast-derived expected stats all point in the same direction, confidence is high. When they diverge significantly, that divergence is itself informative.
