# Statcast Methodology

## What Statcast Is and How It Works

Statcast is MLB's optical tracking system, deployed in all 30 major league ballparks beginning in 2015. It is described by MLB as "a state-of-the-art tracking technology that allows for the collection and analysis of a massive amount of baseball data, in ways that were never possible in the past" (see [11-savant-pitch-tracking.md]).

### Hardware

**2015–2019:** A hybrid system combining camera and radar. The cameras tracked players and batted balls while radar tracked pitches.

**2020–present (Hawk-Eye):** Replaced the hybrid system entirely. Hawk-Eye was previously best known for powering line-call systems in professional tennis. Each ballpark now has **12 cameras** arrayed around the facility:
- Five high-frame-rate cameras focused on bat tracking and pitch tracking (upgraded from 100 fps to 300 fps in 2023)
- Seven dedicated to tracking players and batted balls

The improved system raised the percentage of batted balls successfully tracked from approximately 89% to 99%.

**2023:** Bat tracking data became available mid-season. Metrics like swing speed, attack angle, blast rate, and squared-up rate only have reliable league-wide data from 2023 onward. The 2023 bat tracking figures are partial (see [01-statcast-metrics-context.md]).

---

## What Statcast Tracks

### Raw Measurements
Statcast captures physical measurements directly from the action on the field:

| Measurement | Definition |
|---|---|
| Exit Velocity | Speed of the ball off the bat, in mph, immediately after contact |
| Launch Angle | Vertical angle in degrees at which the ball leaves the bat |
| Pitch Velocity | Speed of a pitch in mph |
| Spin Rate | Revolutions per minute at pitch release |
| Extension | How far in front of the rubber (in feet) a pitcher releases the ball |
| Bat Speed | Speed of the bat's sweet spot at point of contact, in mph |
| Sprint Speed | Player's top running speed, in feet per second |
| Arm Strength | How hard a fielder throws, in mph |
| Pop Time | Seconds for a catcher to transfer and deliver a throw to a base |

(see [11-savant-pitch-tracking.md])

### Derived Metrics
From raw measurements, Statcast computes higher-level metrics:

- **Barrel:** Batted balls with exit velocity/launch angle combinations that historically yield ≥ .500 BA and 1.500 SLG
- **Expected stats (xBA, xSLG, xwOBA):** Probability-weighted outcomes based on contact quality
- **Catch Probability:** Likelihood an outfielder makes a specific catch
- **Outs Above Average (OAA):** Fielding range metric based on catch probability saved
- **Blasts:** High-quality swings combining fast bat speed with squared-up contact
- **Hard-Hit Rate:** Percentage of batted balls at ≥ 95 mph

---

## Launch Angle Classification

Launch angle determines the type of batted ball. The following thresholds are used by Statcast (see [10-savant-exit-velo-launch-angle.md]):

| Contact Type | Launch Angle Range |
|---|---|
| Ground ball | Below 10 degrees |
| Line drive | 10–25 degrees |
| Fly ball | 25–50 degrees |
| Pop-up | Above 50 degrees |

The **sweet spot** is 8–32 degrees, encompassing line drives and productive fly balls. Sweet-spot batted balls produced a .575–.584 batting average in 2026 data; non-sweet-spot balls produced only .195 BA (see [01-statcast-metrics-context.md]).

---

## Barrel Classification

The barrel definition is precise. A batted ball is classified as a barrel when its combination of exit velocity and launch angle falls within the zone where comparable historical batted balls have produced a minimum .500 BA and 1.500 SLG (see [09-savant-barrel-definition.md]):

- Minimum exit velocity: **98 mph**
- At 98 mph: launch angle must be between **26–30 degrees**
- Each additional mph above 98 expands the angle range
- At 99 mph: 25–31 degrees
- At 100 mph: 24–33 degrees (approximately 3-degree expansion per mph above 100)
- At **116+ mph**: any angle between 8–50 degrees qualifies

In practice, barrel contact is extremely productive. 2026 season data showed barrel hits producing a .668–.684 BA and 2.184–2.236 SLG. Barrels represent approximately 8.3% of all batted balls; the other 91.7% produce only ~.288–.292 BA (see [16-savant-statcast-glossary.md]).

---

## How Expected Statistics Are Calculated

Expected statistics (xBA, xSLG, xwOBA) address a core problem: outcomes of balls in play are noisy. A perfectly struck line drive can be caught; a poorly hit bloop can fall in. Expected stats evaluate the quality of contact and assign the outcome a player "deserves" based on the physics of the batted ball.

### Methodology

1. Every batted ball is characterized by its exit velocity, launch angle, and (for batted balls in play) the batter's sprint speed
2. The Statcast database contains all batted balls since 2015, with their actual outcomes recorded
3. For each new batted ball, MLB identifies comparable historical batted balls — similar exit velocity, similar launch angle, similar spray direction
4. The system calculates the probability that this class of batted ball results in an out, single, double, triple, or home run
5. Those probabilities are weighted by the appropriate run values (wOBA weights) to produce **xwOBA**

**xBA** specifically uses exit velocity, launch angle, and sprint speed (faster runners turn more grounders and slow rollers into hits).

**xERA** (for pitchers) is the xwOBA-based equivalent of ERA, expressing the expected run value allowed given contact quality (see [08-savant-expected-stats.md]).

### Interpretation

The gap between actual stats and expected stats is diagnostic:
- **wOBA > xwOBA (positive gap):** The player outperformed their contact quality — they were lucky, or faced unusually poor defenses. Expect regression.
- **wOBA < xwOBA (negative gap):** The player underperformed their contact quality — they were unlucky, or faced unusually good defenses. Expect improvement.

2026 season data confirms the model: barrel batted balls produced an xwOBA of 1.248, while non-barrels produced only .289. The expected and actual statistics align closely in aggregate, confirming that xwOBA accurately prices contact quality over large samples (see [01-statcast-metrics-context.md]).

---

## Pitch Tracking and Pitch Quality

Statcast tracks every pitch with high-speed cameras, measuring velocity, spin rate, active spin percentage, horizontal and vertical movement (in inches relative to a theoretical spinless pitch), extension, and release point.

These pitch-level measurements power models like **Stuff+**, which scores each pitch based on its physical quality relative to league-average pitches of the same type. The primary inputs for Stuff+ are velocity, vertical break, horizontal break, arm angle, and release extension — evaluated together because interactions between variables matter (e.g., more velocity on a breaking ball can reduce lateral movement, which may lower its value) (see [03-driveline-stuff-plus-pitch-models.md]).

---

## Data Availability Summary

| Metric | Available From |
|---|---|
| Pitch velocity, movement, spin rate | 2008 (PITCHf/x era); Statcast 2015+ |
| Exit velocity, launch angle | 2015 (partial); 2016 complete |
| Barrel, hard-hit rate, sweet-spot | 2016–present |
| Bat speed, blast, squared-up, attack angle | 2023–present (partial 2023) |

Any analysis spanning seasons before 2016 should treat batted-ball Statcast data as unavailable. The pipeline in this project covers 2015–2025; analyses relying on barrel rate should begin in 2016 (see [01-statcast-metrics-context.md]).
