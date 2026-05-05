Source: https://www.drivelinebaseball.com/2021/12/what-is-stuff-quantifying-pitches-with-pitch-models/

# Pitch Design: What is Stuff+? Quantifying Pitches with Pitch Models

_By Chris Langin, Pitching Trainer, Driveline Baseball_

The art of "pitching" has many variables associated with it, some easily quantifiable and others not so much. Every pitcher, coach, and organization is constantly in a battle of weighting these variables in a manner that maximizes development and performance on the field.

While there is little agreement on how important "secondary" variables such as deception and sequencing are towards generating outs, it is generally accepted that three pitcher talents stand out above the rest.

The ability to:

- Command the baseball.
- Generate ball velocity.
- Manipulate the baseball and acquire unique movement on pitches.

These three traits come with the bonus of being rather easy to quantify at the MLB level. We don't necessarily need a radar gun, nor a pitch model (explained below) to let us know that Aroldis Chapman has a good fastball.

However, given the innate bias associated with human evaluators, it's likely that a pitch model can more reliably detect a 40-grade fastball from a 45-grade one than an evaluator working alone and without data. Ideally, the combination of strong baseball savvy mixed with a well-regarded model grants us the most optimal evaluation of location agnostic pitch quality.

## Stuff+ — Driveline's Pitch Model

The Pitch Model we reference at Driveline is known as "Stuff+" and is currently going through its 4th iteration. As mentioned above, the model filters out plate locations (thus characteristics of command which is measured in a separate metric) and primarily concerns itself with the following ballflight metrics:

- Pitch Velocity
- Vertical Break
- Horizontal Break
- Arm Angle
- Release Extension

The main influencers are the first three descriptors mentioned: velocity, vertical break, and horizontal break — though, we'll discuss the need to ensure arm slot context is taken into account — along with extreme release extension values.

The need to account for interactions between these variables may not be immediately apparent given that more movement and velocity often lead to a higher quality pitch. However, there are particular instances where certain pitches break that handy rule of thumb.

For example, more velocity on breaking balls often comes with a tradeoff in glove side action. A sinker that gains vertical break usually drops in effectiveness, whereas a generic four-seamer that gains vertical break gets an uptick in effectiveness.

When developing offerings in the offseason, the ability for an athlete and coach to use Stuff+ to immediately summarize a 79-mph slider with more movement against an 83-mph gyro-esque slider is quite valuable.

## Scaling

Stuff+ is scaled similarly to IQ — with a score of "100" meaning that pitch graded out as league average relative to other pitches thrown in that pitch type bucket. A fastball with a Stuff+ of 75 would be 25% below the league average for fastballs. A curveball with a Stuff+ of 130 would be 30% above the league average amongst all breaking balls.

The seven "popularized" pitch types are rearranged into three distinct pitch buckets — with those pitch types competing amongst each other within their associated pitch grouping.

**Fastballs:** Four-Seam Fastball, Sinker
**Breaking Balls:** Cutter, Slider, Curveball
**Offspeed:** Changeup, Splitter

It's important to keep in mind that these pitches compete amongst each other — breaking balls tend to lower run values more than Fastballs, meaning a four-seamer with a Stuff+ of 150 is not necessarily equivalent in "raw stuff" to a slider with a Stuff+ of 150.

| Raw Pitch Type | Run Value per 100 pitches | Grouped Pitch Type |
| --- | --- | --- |
| SL | -0.98 | Breaking |
| CT | -0.59 | Breaking |
| CB | -0.58 | Breaking |
| CH/SP | -0.42 | Off Speed |
| FF | -0.19 | Fastball |
| SI | -0.14 | Fastball |

## Stuff+ for Four-Seam Fastballs

### 2021 Four-Seam Averages

| Handedness | Velocity | Horizontal | Vertical | Release Height | Extension |
| --- | --- | --- | --- | --- | --- |
| RHP | 94.1 | 7.5" | 16.4" | 5.9' | 6.4' |
| LHP | 92.8 | 7.8" | 16.6" | 6' | 6.3' |

**Highest graded four-seamer in 2021 (that was a strike):** Aroldis Chapman — Velo: 102.4 (99th percentile), VB: 18.7" (80th), HB: (-) 2.2" (10th), Stuff+: 350.

Chapman is well regarded for having perhaps the most electric arm the world has ever seen. Of the top 10 graded fastballs this season, he owned 8 of them.

### Daniel Bard vs. Mike Fiers

- Daniel Bard — Velo: 98.6 (98th percentile), VB: 13.5" (15th), HB: 10" (67th), Stuff+: 90
- Mike Fiers — Velo: 89.8 (9th percentile), VB: 20.4" (92nd), HB: 11.5" (80th), Stuff+: 80

Four-Seam quality is predominantly a result of two things: velocity and vertical break. If you combine Bard's velocity with Mike Fiers movement profile, you more or less get Michael Kopech, who ranked 2nd in the league in Stuff+ on his four-seamer at 225.

## Stuff+ for Sinkers

### 2021 Sinker Averages

| Handedness | Velocity | Horizontal | Vertical | Release Height | Extension |
| --- | --- | --- | --- | --- | --- |
| RHP | 93.4 | 15.5" | 9.3" | 5.7' | 6.3' |
| LHP | 92.1 | 15.6" | 9.4" | 5.8' | 6.3' |

**Highest graded sinker in 2021:** Aaron Bummer — 191 Stuff+, 57 points better than the next best left-handed sinker. Bummer accomplishes this with 90th percentile velocity and the ability to manipulate the pitch (largely through [seam shifted wake](https://www.drivelinebaseball.com/2020/11/more-than-what-it-seams-an-introduction-to-seam-shifted-wakes-and-their-effect-on-sinkers/)) so that it moves in just a lateral direction — resulting in a pitch that averages less than an inch of carry.

Sinkers differentiate from four-seamers in many ways. The most obvious is that the sinker's value is tied towards generating low run value contact in the form of ground balls. An average four-seamer will likely outweigh a "good" sinker in its ability to generate whiffs, but it won't necessarily outweigh it in its ability to negate runs.

### Arm Slot Context

Fastballs also require us to look at arm slot context prior to providing a final judgement — our model is aware of the effect slot deviation has on stuff as well. While Snell beats Hader handedly in all the key metrics for the four-seamer, Hader's ability to impart well above average carry and velocity on his four-seamer with one of the lowest arm slots in the league proves superior. Pitchers who have lower slots are able to throw pitches with flatter vertical approach angles relative to their high slot peers.

## Stuff+ for Cutters

### 2021 Cutter Averages

| Handedness | Velocity | Horizontal | Vertical | Release Height | Extension |
| --- | --- | --- | --- | --- | --- |
| RHP | 89.5 | (-) 3" | 8" | 5.9' | 6.3' |
| LHP | 86.8 | (-) 1.8" | 8" | 5.8' | 6.2' |

This is a good reminder that we're simply discussing the context of a pitcher's "stuff" as opposed to leveraging an entire arsenal and having a differing intent behind each pitch.

## Stuff+ for Sliders

It's no secret that the slider has become "the best pitch in baseball" across the league. Run values back up this theory, and usage of the offering has gone up drastically over the past 2 decades. The average slider had a Stuff+ of 119 in 2021, 25 points higher than the average cutter.

### 2021 MLB Averages

| Handedness | Velocity | Horizontal | Vertical | Release Height | Extension |
| --- | --- | --- | --- | --- | --- |
| RHP | 85 | (-) 6.6" | 1.4" | 5.8' | 6.25' |
| LHP | 84 | (-) 6.1" | 1" | 5.9' | 6.25' |

**Highest graded sliders in 2021:** Tanner Scott was the Stuff+ king (246) for sliders this season, closely trailed by supination sensation Dillon Maples (233).

Sliders have as much movement deviation across the league as any pitch type. With whiff-inducing breaking balls being such a priority these days, Stuff+ ensures that we get our athletes as close to their optimal breaker as possible.

## Stuff+ for Curveballs

### 2021 MLB Averages

| Handedness | Velocity | Horizontal | Vertical | Release Height | Extension |
| --- | --- | --- | --- | --- | --- |
| RHP | 79.7 | (-) 9.9" | (-) 11.2" | 5.95' | 6.25' |
| LHP | 77.8 | (-) 8.7" | (-) 9.1" | 6' | 6.1' |

Context of the remaining arsenal is a heavy consideration for every curveball. Even so, some suffer from a lack of experimentation, as pitchers with a Stuff+ model in front of them may learn they don't have to be quite so strict with the spin direction of the offering.

## Stuff+ for Offspeed

Our final pitch grouping is "offspeed" which consists simply of changeups and splitters. We actually group these pitches together when analyzing them — as the role of a splitter and a changeup is generally the same.

### 2021 MLB Averages

| Handedness | Velocity | Horizontal | Vertical | Release Height | Extension |
| --- | --- | --- | --- | --- | --- |
| RHP | 85.6 | 13.9" | 5.5" | 5.8' | 6.35' |
| LHP | 83.6 | 14.5" | 7.4" | 5.85' | 6.25' |

Offspeed effectiveness is based on the differential from the fastball. This means that instead of looking at individual velocity and break values, we should look at these metrics relative to the fastball. On average, pitchers drop 8 ticks off their fastball, add nearly three and a half inches of arm side run, and generate 8 inches of depth relative to their average fastball.

## Release Extension

While it isn't of extraordinary importance, pitchers that deviate greatly from league averages will certainly receive a boost (or penalty) due its influence on reaction time for the hitter. When accounting for flight time differential, an additional foot of release extension is [worth the equivalent of 1.6 mph](https://grantland.com/the-triangle/2015-mlb-actual-versus-perceived-velocity-statcast-pitcher-data-carter-capps/). Though, relatively few big leaguers deviate by more than half a foot relative to the league average.

## Stuff+ Recap

Stuff+ can be counterproductive if abused. It should not be thought of as a replacement for any additional pitch quality analysis. We must remember that Stuff+ is location agnostic and looks at pitches individually. Good baseball intuition is still required to contextualize whether or not simply maximizing the Stuff+ on a given pitcher's cutter is optimal for their specific arsenal.

Stuff+ takes away some bias from the equation and provides a strong summary score for how a pitch rates based on its pitch flight characteristics and release parameters. Stuff+'s biggest strength is that it captures this without a need for a massive sample size — allowing for immediate feedback during pitch designs in the offseason.

When utilized properly, Stuff+ is an invaluable tool — there's simply too much variability in breaking ball shapes and their differing effectiveness to simply look at percentile rankings amongst the big three metrics (velo, vertical break, horizontal break) and assume an accurate model. Stuff+ contextualizes when added carry is good on a slider, and when you should be nudged towards a sinker instead of a four-seamer.

— Chris Langin / Driveline Baseball
