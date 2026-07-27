Source: https://library.fangraphs.com/offense/woba/

# [wOBA](https://library.fangraphs.com/offense/woba/ "Permanent link to wOBA")

by [Piper Slowinski](https://library.fangraphs.com/author/steve-slow/)

February 15, 2010

*Weighted On-Base Average (wOBA)* is one of the most important and popular catch-all offensive statistics. It was created by Tom Tango (and notably used in [“The Book”](http://www.amazon.com/dp/1597971294?tag=tangotiger-20&camp=14573&creative=327641&linkCode=as1&creativeASIN=1597971294&adid=1N9XSEZMFPQ75N48AC7B&)) to measure a hitter’s overall offensive value, based on the relative values of each distinct offensive event.

wOBA is based on a simple concept: Not all hits are created equal. Batting average assumes that they are. On-base percentage does too, but does one better by including other ways of reaching base such as walking or being hit by a pitch. Slugging percentage weights hits, but not accurately (Is a double worth twice as much as a single? [In short, no](http://www.insidethebook.com/ee/index.php/site/comments/run_values_of_events/)) and again ignores other ways of reaching base. On-base plus slugging (OPS) does attempt to combine the different aspects of hitting into one metric, but it assumes that one percentage point of SLG is the same as that of OBP. In reality, a handy estimate is that OBP is around twice as valuable than SLG ([the exact ratio is x1.8](http://www.insidethebook.com/ee/index.php/site/comments/why_does_17obpslg_make_sense/)). In short, OPS is asking the right question, but we can arrive at a more accurate number quite easily.

Weighted On-Base Average combines all the different aspects of hitting into one metric, weighting each of them in proportion to their actual run value. While batting average, on-base percentage, and slugging percentage fall short in accuracy and scope, wOBA measures and captures offensive value more accurately and comprehensively.

**Calculation:**

The wOBA formula for the 2013 season was:

*wOBA = (0.690×uBB + 0.722×HBP + 0.888×1B + 1.271×2B + 1.616×3B +  
2.101×HR) / (AB + BB – IBB + SF + HBP)*

These weights change on a yearly basis, so you can find the [specific wOBA weights for every year from 1871 to the present here](http://www.fangraphs.com/guts.aspx?type=cn).

To calculate wOBA, find the weights for the year you are interested in and multiply each weight by the player’s corresponding statistics. For example, in 2013 Mike Trout had 100 unintentional walks, 9 HBP, 115 singles, 39 doubles, 9 triples, and 27 home runs. If you multiple each by it’s corresponding weight and then divide that number by the sum of his at bats, walks (excluding IBB), hit by pitches, and sacrifice flies, you get .423, or his wOBA for the season.

**Why wOBA:**

One of the most common questions people ask when presented with a new statistic like wOBA is why they should use it when the basic triple slash line statistics (average, on base percentage, and slugging percentage) work just fine or work even better when using them to form OPS?

Simply put, OPS and wOBA will lead you to very similar conclusions in most situations, but if you care about determining how well a player contributes to run scoring, wOBA is a more accurate representation of that contribution. OPS undervalues getting on base relative to hitting for extra bases and does not properly weigh each type of extra base hit.

Additionally, individuals do not often calculate statistics by hand and will use a spreadsheet if they like doing it themselves or will make use of a website such as FanGraphs to provide that information. OBP or SLG might be easier to calculate with pencil and paper, but wOBA is extremely easy to find and use on our site, meaning any computational costs of moving to wOBA are minuscule.

**How to Use wOBA:**

One of the beauties of wOBA is that it is extremely easy to use once you learn the basics. League average wOBA is always scaled to league average OBP, so if you know what a good OBP is, you know what a good wOBA is. Below are specific averages for the current season, but typically an average hitter will finish the season with a wOBA of around .320.

wOBA is also quite easy to convert to [Weighted Runs Above Average (wRAA)](http://www.fangraphs.com/library/offense/wraa/), or the non-park adjusted version of Batting Runs. In other words, you can convert wOBA to a cumulative run value above average quickly. Simply take the player’s wOBA and subtract out the league average wOBA, then divide by the wOBA scale and multiple that by the number of plate appearances. [Both league wOBA and the wOBA scale can be found here](http://www.fangraphs.com/guts.aspx?type=cn).

((wOBA-League wOBA)/wOBA Scale)\*PA = wRAA

For example, Mike Trout had a .423 wOBA in 716 PA in 2013 and the league wOBA was .314 and the wOBA scale was 1.277.

((.423-.314)/1.277)\*716 = 61.1 wRAA

In other words, before making park and league adjustments, Mike Trout’s was worth about 61 more runs than the average offensive player. You can’t make such an easy conversion using OPS.

A good rule of thumb is that 20 points of wOBA is worth about 10 runs above average per 600 PA. This is not a precise measurement and specific calculations are always better, but if you’re looking for an approximate rule of thumb, this may be useful.

**Context:**

Please note that the following chart is meant as an estimate, and that league-average wOBA varies on a year-by-year basis. It is set to the same scale as OBP, so league-average wOBA in a given year should be very close to the league-average OBP. To see the league-average wOBA for every year from 1901 to the present, [check the FanGraphs leaderboards](http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=8&season=2011&month=0&season1=1901&ind=0&team=0,ss&rost=0&players=0&sort=0,d).

wOBA Rules of Thumb

|  |  |
| --- | --- |
| Rating | wOBA |
| Excellent | .400 |
| Great | .370 |
| Above Average | .340 |
| Average | .320 |
| Below Average | .310 |
| Poor | .300 |
| Awful | .290 |

**Things to Remember:**

● This stat accounts for the following aspects of hitting: unintentional walks, hit-by-pitches, singles, doubles, triples, home runs. Stolen-bases and caught stealing numbers used to be included as well on FanGraphs, but they are now instead accounted for with the stats [UBR](http://www.fangraphs.com/library/offense/ubr/) and [wSB](http://www.fangraphs.com/library/offense/wsb/). This way, wOBA only accounts for a player’s production at the plate.

● Exactly how much to weigh each of the components of wOBA was determined using [linear weights](http://www.fangraphs.com/library/principles/linear-weights/).

● wOBA can be converted into offensive runs above average easily. These are called [Weighted Runs Above Average (wRAA)](http://www.fangraphs.com/library/offense/wraa/). The formula to convert wOBA into wRAA is listed below:

wRAA = ((wOBA – league wOBA) / wOBA scale) × PA  
(league-average wOBA can be found [here](http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=8&season=2011&month=0&season1=1901&ind=0&team=0,ss&rost=0&players=0&sort=0,d); wOBA scale values can be found [here](http://www.beyondtheboxscore.com/2011/1/4/1912914/custom-woba-and-linear-weights-through-2010-baseball-databank-data))

● This stat is context-neutral, meaning it does not take into account if there were runners on base for a player’s hit or if it was a close game at the time.

● wOBA on FanGraphs is not adjusted for park effects, meaning that batters that play in hitter-friendly parks will have slightly inflated wOBAs.

**Links for Further Reading:**

[Custom wOBA and Linear Weights for 1871-2010 – Beyond the Box Score](http://www.beyondtheboxscore.com/2011/1/4/1912914/custom-woba-and-linear-weights-through-2010-baseball-databank-data)

[Calculating wOBA (Datebasa Version) – The Book Blog](http://www.insidethebook.com/ee/index.php/site/comments/woba_year_by_year_calculations/)

[A Visual Look at wOBA – FanGraphs](http://www.fangraphs.com/blogs/a-visual-look-at-woba/)

[The Joy of wOBA – FanGraphs](http://www.fangraphs.com/blogs/the-joy-of-woba/)

[Intro to wOBA – Big League Stew](http://sports.yahoo.com/mlb/blog/big_league_stew/post/Everything-you-always-wanted-to-know-about-wOBA?urn=mlb,208135)

[Getting to Know wOBA – The Book Blog](http://www.insidethebook.com/ee/index.php/site/article/getting_to_know_woba/)

[The History of wOBA – The Book Blog](http://www.insidethebook.com/ee/index.php/site/article/the_history_of_the_woba_part_1/)

[wOBA Calculator – New English D](http://newenglishd.com/2012/11/02/stat-of-the-week-weighted-on-base-average-woba/)

[wOBA As a Gateway Statistic – FanGraphs](http://www.fangraphs.com/library/woba-as-a-gateway-statistic/)

[The Beginner’s Guide To Deriving wOBA -FanGraphs](http://www.fangraphs.com/library/the-beginners-guide-to-deriving-woba/)
