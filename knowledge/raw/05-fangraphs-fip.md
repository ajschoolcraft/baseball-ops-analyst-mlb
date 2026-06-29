Source: https://library.fangraphs.com/pitching/fip/

# [FIP](https://library.fangraphs.com/pitching/fip/ "Permanent link to FIP")

by [Piper Slowinski](https://library.fangraphs.com/author/steve-slow/ "Posts by Piper Slowinski")

February 15, 2010

*Fielding Independent Pitching (FIP)* measures what a player’s ERA would look like over a given period of time if the pitcher were to have experienced league average results on balls in play and league average timing. Back in the early 2000s, [research by Voros McCracken](http://www.baseballprospectus.com/article.php?articleid=878) revealed that the amount of balls that fall in for hits against pitchers do not correlate well across seasons. In other words, pitchers have little control over balls in play and assuming short-term fluctuations in BABIP are attributable to the pitcher is likely incorrect. McCracken outlined a better way to assess a pitcher’s talent level by looking at results a pitcher *can* control directly: strikeouts, walks, hit by pitches, and home runs.

FIP is a measurement of a pitcher’s performance that strips out the role of defense, luck, and sequencing, making it a more stable indicator of how a pitcher actually performed over a given period of time than a runs allowed based statistic that would be highly dependent on the quality of defense played behind him, for example. Certain pitchers have shown an ability to consistently post lower ERAs than their FIP suggests, but overall FIP captures most pitchers’ true performance quite well. For this reason, FanGraphs’ version of Wins Above Replacement (WAR) for pitchers is based on FIP rather than on ERA and even analysts who prefer a different method of determining WAR find FIP to be extremely useful and informative.

**Calculation:**

Here is the formula for FIP:

*FIP = ((13\*HR)+(3\*(BB+HBP))-(2\*K))/IP + constant*

The constant is solely to bring FIP onto an ERA scale and is generally around 3.10. You can find historical FIP constant values [here](http://www.fangraphs.com/guts.aspx?type=cn), or you can derive the constant yourself. Because FIP is designed so that league average ERA and league average FIP are the same, to find the constant for any year, all you need to do is the following:

*FIP Constant = lgERA – (((13\*lgHR)+(3\*(lgBB+lgHBP))-(2\*lgK))/lgIP)*

Knowing how to calculate the constant can be especially useful if you’re interested in doing some of your own calculations for data spanning multiple seasons. The individual weights for home runs, walks/HBP, and strikeouts are based on the relative values of those actions with respect to run prevention.

**Why FIP:**

Ultimately, we want to use statistics that allow us to isolate the performance of the player we are attempting to analyze. ERA or RA9 do a terrific job telling us how many runs were scored while the pitched was on the mound, but they do not necessarily tell us how well the pitcher performed because the number of runs a pitcher allowed is also dependent on their defense, luck, and the order in which events happened (often called sequencing).

FIP is an attempt to isolate the performance of the pitcher by using only those outcomes we know do not involve luck on balls in play or defense; strikeouts, walks, hit batters, and home runs allowed. Research has shown that pitchers have very little control on the outcome of balls in play, so while we care about how often a pitcher allows a ball to be put into play, whether a ground ball goes for a hit or is turned into an out is almost entirely out of their control.

As a result, a statistic that estimates their ERA based on their strikeouts, walks, hit batters, and home runs while assuming average luck on balls in play, defense, and sequencing is a better reflection of that pitcher’s performance over a given period of time. This is highly related to the reasons why we care so much about [Batting Average on Balls in Play (BABIP)](http://www.fangraphs.com/library/pitching/babip/), specifically the fact that pitchers have very little control over their BABIP allowed.

Imagine two pitchers who always throw the same quality pitches to identical hitters, but one pitcher throws in front of a vastly superior defense. The pitcher with the better defense will allow fewer hits, and therefore fewer runs, but the two pitchers performed identically.

Additionally, the order of events (sequencing) can have a big impact on runs allowed, even though there is no evidence that pitchers are capable of influencing their sequencing. If you have two outs and allow a single, single, home run, and out, you have just allowed three runs. If you have two outs and allow a home run, single, single, and then an out, you have just allowed one run, even though the four events were identical.

Essentially, FIP is an attempt to measure how well a pitcher actually performed independent of factors outside of his control that contribute to runs allowed based statistics. FIP is not perfect and there are certain pitchers who have the skills to allow fewer runs than their FIP suggests, but they are reasonably rare and FIP remains highly accurate and extremely simple at the same time.

**How To Use FIP:**

In one sense, using FIP is extremely easy because it’s designed to look exactly like ERA. This means that you can read and use FIP exactly like you would typically use ERA. If a pitcher has a 3.15 FIP, that’s just like saying they have a 3.15 ERA as far as making comparisons among players is concerned. You don’t have to learn a new scale to interpret a player’s FIP.

On the other hand, using FIP requires a bit of caution and it is best to think of it as a starting place for the analysis of pitcher performance, especially if you are interesting in determining how a pitcher is likely to perform in the future. In the long run, the majority of pitchers will have ERAs and FIPs that are very close together, but over the course of a season they could vary a great deal. Typically, people attribute the difference between the two to luck on balls in play, but there are other factors that can lead to a difference.

For example, pitchers with the ability to limit the running game or generate fly balls at the expense of line drives or ground balls are more likely to beat their FIP than the average player. This doesn’t mean that every lefty fly ball pitcher will do so, but simply that holding runners and generating a type of batted ball that falls for hits less frequently are legitimate skills that might allow you to limit your runs allowed.

If you have to bet on a pitcher’s ERA or their FIP, FIP is the better bet, but FIP tells you about a subset of a pitcher’s results which means that it is possible that it is missing something important about that pitcher’s profile that allows them to run consistently high or low BABIPs.

FIP is a terrific statistic, but as always, looking into the components of the statistic and other measures of pitcher performance will help you understand how a pitcher is truly performing.

**Context:**

Please note that the following chart is meant as an estimate, and that league-average FIP varies on a year-by-year basis so that it is always the same as league-average ERA. To see the league-average FIP for every year from 1901 to the present, [check the FanGraphs leaderboards](http://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=8&season=2016&month=0&season1=1901&ind=0&team=0,ss&rost=0&age=&filter=&players=0).

Fielding Independent Pitching (FIP)

| Rating | FIP |
| --- | --- |
| Excellent | 3.20 |
| Great | 3.50 |
| Above Average | 3.80 |
| Average | 4.20 |
| Below Average | 4.40 |
| Poor | 4.70 |
| Awful | 5.00 |

Based on 2016 Run Environment

● Voros McCracken’s research was called Defense Independent Pitching Theory (DIPS Theory). It’s the building block of much of today’s pitching analysis. It can be a tricky concept to understand and counter-intuitive for most baseball fans. Refer to our sections on [DIPs](http://www.fangraphs.com/library/principles/dips/), [BABIP](http://www.fangraphs.com/library/pitching/babip/), and [Luck](http://www.fangraphs.com/library/principles/luck/) for more information.

● FIP does a better job of predicting the future than measuring the present, as there can be a lot of fluctuation in small samples. It is less effective in describing a pitcher’s single game performance and is more appropriate in a season’s worth of innings. That doesn’t mean it isn’t a retrospective statistic, simply that it requires more than a handful of innings to be a reliable indicator of performance, just like any statistic.

● FIP is not league or park adjusted meaning that pitchers in good pitcher’s parks will have consistently lower FIPs and pitchers who pitch during eras of lower run scoring will have consistently lower FIPs. To control for both of those factors, FanGraphs offers FIP-, which is a park and league adjusted version of the statistic.

● FanGraphs’ WAR for pitchers is based on FIP, but we also offer a statistic called RA9-WAR if you are interested in using a different input.

**Links for Further Reading:**

[Intro to FIP – Big League Stew](http://sports.yahoo.com/mlb/blog/big_league_stew/post/Everything-you-always-wanted-to-know-about-FIP?urn=mlb,206286)

[Mike Silva Chronicles: FIP – The Book Blog](http://www.insidethebook.com/ee/index.php/site/article/mike_silva_chronicles_part_4_fip/)

[Calculating the FIP Constant – Beyond the Boxscore](http://www.beyondtheboxscore.com/2010/4/8/1407849/baseball-databank-data-dump-i-fip)

[Oswalt and FIP – FanGraphs](http://www.fangraphs.com/blogs/oswalt-and-fip/)

[FIP and the Long Ball – Hardball Times](http://www.hardballtimes.com/main/article/fip-and-the-long-ball/)

[FIP Calculator – New English D](http://newenglishd.com/2012/10/18/stat-of-the-week-fielding-independent-pitching-fip/)

[FIP: A New ERA – YouTube](https://www.youtube.com/watch?v=TuWoLBhnJ1g)

[ERA, FIP, and Answering the Right Question – FanGraphs](http://www.fangraphs.com/library/era-fip-and-answering-the-right-question/)
