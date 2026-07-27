Source: https://library.fangraphs.com/offense/wrc/

# [wRC and wRC+](https://library.fangraphs.com/offense/wrc/ "Permanent link to wRC and wRC+")

by [Piper Slowinski](https://library.fangraphs.com/author/steve-slow/)

February 16, 2010

*Weighted Runs Created (wRC)* is an improved version of Bill James’ Runs Created (RC) statistic, which attempted to quantify a player’s total offensive value and measure it by runs.  In Runs Created, instead of looking at a player’s line and listing out all the details (e.g. 23 2B, 15 HR, 55 BB, 110 K, 19 SB, 5 CS), the information is synthesized into one metric in order to say, “Player X was worth 24 runs to his team last year.”  While the idea was sound, James’ formula has since been superseded by Tom Tango’s wRC , which is based off [Weighted On-Base Average (wOBA](http://www.fangraphs.com/library/offense/woba/)).

If wRC sounds similar to [Weighted Runs Above Average (wRAA)](http://www.fangraphs.com/library/offense/wraa/) or Batting Runs, that’s a good thing. wRAA is simply wRC with league average scaled to zero, while Batting Runs is the park and league adjusted version of wRAA.

Similar to [OPS+](http://www.fangraphs.com/library/offense/ops/), *Weighted Runs Created Plus (wRC+)* measures how a player’s wRC compares with league average after controlling for park effects.  League average for position players is 100, and every point above 100 is a percentage point above league average. For example, a 125 wRC+ means a player created 25% more runs than a league average hitter would have in the same number of plate appearances. Similarly, every point below 100 is a percentage point below league average, so a 80 wRC+ means a player created 20% fewer runs than league average.

wRC+ is park and league-adjusted, allowing one to to compare players who played in different years, parks, and leagues.  Want to know how Ted Williams compares with Albert Pujols in terms of offensive abilities?  This is your statistic. wRC+ is the most comprehensive rate statistic used to measure hitting performance because it takes into account the varying weights of each offensive action and then adjusts them for the park and league context in which they took place.

**Calculation:**

The formula for wRC is:

*wRC = (((wOBA-League wOBA)/wOBA Scale)+(League R/PA))\*PA*

League wOBA, wOBA Scale, and League R/PA change each year based on the run environment and you can find year by year numbers [here](http://www.fangraphs.com/guts.aspx?type=cn).

To calculate a player’s wRC, find their wOBA on their player page, in the leaderboards, or calculate it yourself and then plug it into this equation with the necessary weights and number of plate appearances. For example in 2013, Miguel Cabrera had a .455 wOBA in 652 PA. Using the weights from 2013 we arrive at the following:

*(((.455-.314)/1.277)+.11)\*652 = 143.7*

In order to park and league adjust wRC, it takes a few more steps, but it’s nothing you can’t do on your own with basic calculator or Excel spreadsheet. You may notice that there are shortcuts to arriving at some of the numbers below depending on what statistics you already have in front of you, but we’ve provided full details if you’re looking for a very thorough breakdown.

*wRC+ = (((wRAA/PA + League R/PA) + (League R/PA – Park Factor\* League R/PA))/ (AL or NL wRC/PA excluding pitchers))\*100*

The best way to explain how this works is to walk through each of the steps, starting from left to right. First we have wRAA/PA, which measures the number of runs above average a player contributes to his team at the plate per plate appearance. Another way to arrive at wRAA/PA is to simply take a player’s wOBA minus the League wOBA and divide it by the wOBA Scale. Both ways will return the exact same value, so it’s a matter of preference for how you want to do it. As always, the constants you need can be found [here](http://www.fangraphs.com/guts.aspx?type=cn).

Next we have league average runs per plate appearance which is available on the [Guts! page](http://www.fangraphs.com/guts.aspx?type=cn), just like all of the other constants. This is simply the *MLB* runs divided by the total number of plate appearances across the game during that season. We round this off at three digits in the table, so if your calculation is ever off by a small margin, this is likely why.

After that we have the park adjustment, which we arrive at using the additive method. Here we are essentially calculating how many runs per plate appearance we should add or subtract from a player’s total based on their home environment. To do so, we take MLB average R/PA and subtract out the MLB average R/PA times the [park factor](http://www.fangraphs.com/guts.aspx?type=pf&teamid=0&season=2014). To properly use the park factor, you should take the number listed on our park factor page and divide it by 100. So a 98 park factor should be used as 0.98 in this equation.

After we add all of those numbers together, you divide them by the specific league wRC/PA after removing pitchers from the calculation, which you will need to find using the leaderboards. Here are the numbers you need for the [AL](http://www.fangraphs.com/leaders.aspx?pos=np&stats=bat&lg=al&qual=0&type=1&season=2014&month=0&season1=2014&ind=0&team=0,ss&rost=0&age=0&filter=&players=0) and [NL](http://www.fangraphs.com/leaders.aspx?pos=np&stats=bat&lg=nl&qual=0&type=1&season=2014&month=0&season1=2014&ind=0&team=0,ss&rost=0&age=0&filter=&players=0) for 2014. Simply change the year if you’re looking for older data. Then multiply everything by 100 just to make the presentation look better.

We’ll use 2012 Mike Trout as an example.

*((((48.2/639) + 0.114) + (.114-(0.95\*.114)))/(10032/85797))\*100 = 167*

If you attempt these calculations by hand, you will occasionally wind up with a value that is one point off due to where we choose to round decimals places, but otherwise this equation will allow you to match our wRC+ calculations exactly.

**Why wRC and wRC+:**

If you’ve looking to measure a batter’s value using a cumulative statistic that credits a player for total production rather than on an at bat by at bat basis, then wRC is extremely useful. It combines the virtues of a weighted statistic like wOBA, which credits a hitter for how valuable each particular action truly is, with the virtues of counting stats that give players credit for producing at a given level over a great number of plate appearances. wRC isn’t necessarily better or worse than wRAA, it’s simply the same statistic communicated differently. Both provide you with a measure of how many runs a player contributed to his team with their bat.

If you want a rate statistic for hitters that weights each offensive action and controls for league and park effects, wRC+ is for you. While wOBA is a huge step forward from stats like batting average and slugging percentage, it doesn’t credit hitters who play in difficult parks or deduct points for hitters who play in smaller ones. wRC+ brings all the virtues of wOBA plus two added benefits; park and league adjustments. A .400 wOBA at Coors is much less impressive than one at Petco, for example. Additionally, wOBA tracks with overall league offense, so you can’t use it to compare players of different eras very effectively. A .400 wOBA in 2000 is much less impressive than one in 2014, but a 140 wRC+ in 2000 means essentially the same thing in 2014.

**How To Use wRC and wRC+:**

Both wRC and wRC+ are easy to use once you learn their scales. Since wRC is a counting stat, you want to be very aware of the number of plate appearances the batter in question currently has. A player with 10 wRC in 50 PA is very good, but a player with 10 wRC in 200 PA is very bad, just like 50 RBI in 100 PA would be considering excellent and 50 RBI in 700 PA would be considered poor. wRC is a measure of raw production and should be used as such, but remember it is not park, league, or position adjusted.

Using wRC+ is even easier because league average for position players is always 100. If a player has a 110 wRC+, you know they are ten percentage points better than league average offensively. This is a great tool for comparing the at bat by at bat offensive performance of any two players in the league. However, you should note that wRC+ does not control for position.

**Context:**

Please note that the following chart is meant as an estimate, and that league-average wRC will vary from year to year. But as a general breakdown, this distribution works fine with wRC listed per 600 plate appearances. League average wRC+ will always be 100.

| Ratings | wRC | wRC+ |
| --- | --- | --- |
| Excellent | 105 | 160 |
| Great | 90 | 140 |
| Above Average | 75 | 115 |
| Average | 65 | 100 |
| Below Average | 60 | 80 |
| Poor | 50 | 75 |
| Awful | 40 | 60 |

**Things to Remember:**

● If wRC sounds very similar to Weighted Runs Above Average ([wRAA](http://www.fangraphs.com/library/offense/wraa/)), don’t worry, you’re not crazy. The statistics are very similar — both numbers are based off [wOBA](http://www.fangraphs.com/library/offense/woba/) and both quantify offensive ability in terms of runs — but [wRAA](http://www.fangraphs.com/library/offense/wraa/) is scaled with zero as league average, while wRC is not.

● If you’re thinking about using [OPS+](http://www.fangraphs.com/library/offense/ops/), use wRC+ instead. wRC+ is based off of [wOBA](http://www.fangraphs.com/library/offense/woba/) and is regarded as a more accurate depiction of a player’s offensive value. They will typically offer similar conclusions, but wRC+ is superior and no more difficult to interpret or find.

● wRC is not park or league adjusted. wRC+ is park and league adjusted. Neither adjusts for position.

● Both wRC and wRC+ are context neutral, meaning that a hit with men on base and a hit with no one on are weighed equally and the score of the game or inning in which the event occurred does not matter.

**Links for Further Reading:**

[Intro to wRC and wRAA – Fangraphs](http://www.fangraphs.com/blogs/wrc-and-wraa/)

[What is wRC+? – Fangraphs](http://www.fangraphs.com/blogs/what-is-wrc/)

[Runs Created (Bill James Version) – Wikipedia](http://en.wikipedia.org/wiki/Runs_created)

[wRC+ Calculator – New English D](http://newenglishd.com/2013/04/04/stat-of-the-week-weighted-runs-created-plus-wrc/)

[wRC+ and Lessons of Context – FanGraphs](http://www.fangraphs.com/library/wrc-and-lessons-of-context/)
