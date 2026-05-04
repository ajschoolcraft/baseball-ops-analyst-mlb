Source: https://www.baseballprospectus.com/glossary/index.php?search=DRC

# DRC+ (Deserved Runs Created Plus)

## Definition

Deserved Runs Created Plus (DRC+) is Baseball Prospectus's comprehensive hitting metric. It attempts to measure everything a hitter does at the plate — not just hits and walks, but also the type and quality of contact — and express it as a single number scaled to league average.

## Scale

- 100 = league average
- Each point above/below 100 is one percent better/worse than league average
- 150 DRC+ means a hitter produced 50% more runs than a league-average hitter
- 75 DRC+ means a hitter produced 25% fewer runs than league average

## How It Works

DRC+ is a Bayesian model that:

1. **Credits the batter** for the outcomes they most control (quality of contact, plate discipline)
2. **Adjusts for context** including park factors, pitcher quality, defense quality, and umpire tendencies
3. **Regresses to the mean** based on sample size — small samples are pulled toward league average more aggressively
4. **Incorporates batted-ball data** when available (Statcast era, 2015+)

## Advantages Over Other Metrics

- Unlike wRC+, DRC+ separates what the batter deserves from what the defense and luck contributed
- More stable in small samples due to Bayesian regression
- Adjusts for catcher framing effects (pitches called strikes unfairly)
- Accounts for the quality of pitchers faced

## Comparison to wRC+

| Aspect | DRC+ | wRC+ |
|--------|------|------|
| Park adjusted | Yes | Yes |
| League adjusted | Yes | Yes |
| Pitcher quality adjusted | Yes | No |
| Defense adjusted | Yes | No |
| Small sample regression | Yes | No |
| Batted ball quality | Yes (when available) | No |
| Scale | 100 = average | 100 = average |

## Usage

DRC+ is best used for:
- Evaluating true offensive talent, especially in small samples
- Comparing hitters across different parks and eras
- Identifying players whose traditional stats are being inflated/deflated by context
- Projecting future performance (more stable than traditional stats)
