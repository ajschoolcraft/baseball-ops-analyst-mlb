Source: https://library.fangraphs.com/principles/linear-weights/

# [Linear Weights](https://library.fangraphs.com/principles/linear-weights/ "Permanent link to Linear Weights")

by [Piper Slowinski](https://library.fangraphs.com/author/steve-slow/)

February 25, 2010

*Linear Weights*are a class of linear run estimators that we use to determine the relative values of particular events. For example, you’re likely familiar with [Weighted On-Base Average (wOBA)](http://www.fangraphs.com/library/offense/woba/) and [Fielding Independent Pitching (FIP)](http://www.fangraphs.com/library/pitching/fip/), which have weights assigned to given outcomes (i.e., singles, doubles, home runs, etc) that provide a more nuanced look than statistics such as batting average, which counts all hits equally.

Inherently, we know that we should count doubles more than singles, but determining exactly how much more requires some sort of methodology. Linear weights are one such methodology.

It is important to keep in mind that the values generated using this approach are one-size-fits-all estimates using a particular sample of data. They might not reflect reality under extreme conditions or in environments not reflective of the original sample. This page will use wOBA as a guide, but the logic translates to other applications.

### First Things

The first thing we need is a run expectancy matrix. If you need a complete introduction to the concept, head over to this [page](http://www.fangraphs.com/library/misc/re24/). In general, run expectancy measures the average number of runs scored (through the end of the current inning) given the current base-out state.

Base-out states are a record of the number of outs (0, 1, or 2) and how many runners are on base and where (no one on, man on 1B, men on 1B and 3B, etc). There are three out-states and eight base-states, meaning that there are 24 base-out states. Each plate appearance has a base-out state.

Let’s use one out, man on first as our example. In order to calculate the run expectancy for that base-out state, we need to find all instances of that base-out state from the entire season (or set of seasons) and find the total number of runs scored from the time that base-out state occurred until the end of the innings in which they occurred. Then we divide by the total number of instances to get the average. If you do the math using 2010-2015, you get 0.509 runs. In other words, if all you knew about the situation was that there was one out and a man on first, you would expect there to be .509 runs scored between that moment and the end of the inning on average.

You repeat the process for the other 23 base-out states and wind up with a table like [this](http://tangotiger.net/re24.html):

Run Expectancy Matrix 2010-2015

|  |  |  |  |
| --- | --- | --- | --- |
| Runners | 0 outs | 1 outs | 2 outs |
| \_\_ \_\_ \_\_ | 0.481 | 0.254 | 0.098 |
| 1B \_\_ \_\_ | 0.859 | 0.509 | 0.224 |
| \_\_ 2B \_\_ | 1.100 | 0.664 | 0.319 |
| 1B 2B \_\_ | 1.437 | 0.884 | 0.429 |
| \_\_ \_\_ 3B | 1.350 | 0.950 | 0.353 |
| 1B \_\_ 3B | 1.784 | 1.130 | 0.478 |
| \_\_ 2B 3B | 1.964 | 1.376 | 0.580 |
| 1B 2B 3B | 2.292 | 1.541 | 0.752 |

SOURCE: Tom Tango

The table listed here was calculated by Tom Tango using 2010-2015 data for the entire league and serves as a good baseline. At FanGraphs, we park adjust the matrix for each game, so the exact numbers might be a touch different if you’re trying to play along at home in excruciating detail.

Now that you have a run expectancy matrix, you need to learn how to use it. Each plate appearance moves you from one base-out state to another. So if you walk with a man on first base and one out, you move to the “men on first and second and one out” box. That box has an RE value of 0.884. Because your plate appearance moved you from .509 to 0.884, that PA was worth +0.375 in terms of run expectancy.

Every plate appearance has one of these values, either positive or negative. You can learn more about this by following the earlier link.

### Calculating Linear Weights

What we want to determine is the average run value of a walk, HBP, single, double, triple, and home run. To do this, we take the total RE value of all walks (unintentional in this case), for example, and divide that number by the number of walks in that season. You’re going to wind up getting something around 0.3. You repeat this for the other five actions (when calculating wOBA) or for any type of play you wish. This gives you the runs *above average* produced by each of these kinds of events, also known as linear weights.

While these linear weights are an accurate reflection of the data, some people don’t find them to be particularly intuitive. Saying a player has been worth 15 runs above average over the course of a season might be accurate, but it also might not translate very well to all audiences. This leads us to scale our linear weights based stats into things that are easier to understand.

### Optional Scaling

For wOBA, we have the runs above average for walks (0.29), HBP (0.31), singles (0.44), doubles (0.74), triples (1.01), and home runs (1.39), but what we want to do now is put wOBA on a scale that will look like OBP in order to make it easier to understand. In OBP, an out is worth zero, so the first thing we want to do is adjust the run value scale so that an out is equal to zero.

There is an easy way to do this. First, we need to find the linear weight for all outs using the same method we used to find the value for the other events. We’ll call it -0.26 for 2015. This means that an out is worth -0.26 runs less than the average PA when it comes to run expectancy. What we want to do now is add 0.26 to each of our run values so that outs are equal to zero. So for walks, which we said are worth 0.29 runs above average, we bump those up to 0.55 runs *relative to an out*. Using linear weights, walks are worth 0.55 runs more than outs. We repeat this for each of the five other positive offensive outcomes.

2015 Linear Weights (Relative To Outs)

|  |  |
| --- | --- |
| Event | Run Value |
| BB | 0.55 |
| HBP | 0.57 |
| 1B | 0.70 |
| 2B | 1.00 |
| 3B | 1.27 |
| HR | 1.65 |

As you’ll notice, these are not the weights you saw in the wOBA equation. We’re not done scaling them yet. We know that we want BB, HBP, 1B, 2B, 3B, and HR in the numerator of the wOBA formula and plate appearances (minus weird stuff like sac bunts) in the denominator, so what we’re going to do is calculate “wOBA” for the entire league using the linear weights in this table and the total number of events of each type.

In other words, we’re gong to multiply 0.55 times the number of walks in MLB in 2015 and add that to 0.57 times the number of HBP and so on, and then divide the entire sum by the number of plate appearances (really AB + BB – IBB + SF +HBP). If we do that, we wind up with 0.250.

But remember that we want wOBA to look like OBP. So we need to scale the entire thing so that the league’s wOBA is .313 (to match OBP with IBB removed). To do that, we divide .313/.250 and get 1.251, which we call the wOBA Scale.

We take the wOBA Scale and multiply it against the linear weights from the table above and viola, we have ourselves the weights listed in the wOBA equation. And we’re done! You can use a similar approach to derive the FIP weights, although instead of scaling outs to zero, you want to scale balls in play to zero.

### Summary

Essentially, we use linear weights to properly measure different kinds of events. The most common applications are wOBA and FIP.

Linear weights requires taking the average run expectancy impact of each type of event (singles, doubles, etc) and finding their average. That leaves you with a run value relative to average, which you can then scale in any number of ways to generate a statistic you find useful.

### 

**Links:**

[Linear Weights by Base/Out State – Tom Tango](http://www.tangotiger.net/RE9902event.html)

[Linear Weights with Men on Base – Tom Tango](http://www.tangotiger.net/lwbymob.htm)

[Linear Weights by Run Environment – Tom Tango](http://www.tangotiger.net/customlwts.html)

[The Beginner’s Guide To Deriving wOBA – FanGraphs](http://www.fangraphs.com/library/the-beginners-guide-to-deriving-woba/)
