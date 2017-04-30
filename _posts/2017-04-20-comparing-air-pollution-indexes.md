---
layout: post
title: Comparing air pollution indexes
date: '2017-04-20T15:22:00.001-05:00'
author: Douglas Hindson
tags:
- O2Canada
- air pollution
modified_time: '2017-04-20T15:22:00.001-05:00'
---

# Summary

There are a lot of air pollution indexes. One governing body often has multiple air quality indexes because [air quality over time is hard to express](#air-quality-over-time-is-hard-to-express) and [indexes can use different combinations of particles](#indexes-can-use-different-combinations-of-particles). Since there are so many factors to decide on how to make an air quality index, it's difficult to compare the air pollution indexes of different governing bodies. Nevertheless, [here is a best-effort comparison of some air pollution indexes](#comparison-of-air-pollution-indexes).

# There are a lot of air pollution indexes

There are ten major government bodies represented in [this wikipedia air pollution article, as of April 2017](https://en.wikipedia.org/wiki/Air_quality_index#Indices_by_location), each with their own set of air quality indexes. There is such a variety because:

* There are many different particles that affect air pollution.
  * Some particles are more prevalent in certain areas of the world.
  * Some particles are relevant everywhere.
  * Some particles may be relevant in some conditions and not others.
    * Ex: Ozone (O<sub>3</sub>) may not be as dangerous in cold weather [[1]](#references).
* Air pollution is complex to measure and explain
* Different countries want to give different recommendations.
  * Ex: If your pollution index says every reading above 100 is "very bad", but many places in your country consistently have readings ranging from 100 to 900, your pollution index will not be useful to your constituents. You need different kinds of "very bad".

Relevant [xkcd comic](xkcd.com):

![Standards](https://imgs.xkcd.com/comics/standards.png)

# One governing body often has multiple air quality indexes 

## Air quality over time is hard to express

A major reason for one governing body having multiple air quality indexes is because the "badness" of air pollution is determined by the number of bad particles in the air over time.

An example:

Suppose *London* has readings for *particle X* as follows:

| Time                      | 1pm | 2pm | 3pm | 4pm |
| # of *particle X* in *London*  | 10 | 10 | 1000 | 10 |

Now suppose we invent three different air quality indexes, *C, D, and E AQI*:
*C AQI* is the number of 'X' particles in the air right now.
*D AQI* is the average number of 'X' particles in the last 3 hours.
*E AQI* is the average number of 'X' particles in the last 24 hours.

| Time                      | 1pm | 2pm | 3pm | 4pm |
| # of *particle X* in *London*  | 10 | 10 | 1000 | 10 |
| *C AQI* in *London*              | 10 | 10 | 1000 | 10 |
| *D AQI* in *London*              | 10 | 10 | 340 | 340 |
| *E AQI* in *London*              | 10 | 10 | 51 | 51 |

Notice the differences at 3-4pm. 

* With the *C AQI*, you get more to-the-hour detail about air pollution, but you need to see more than one number to understand what's really going on.
* With the *D AQI*, you have a better understanding of the recent past, but it lacks both detail and a long-term view on air pollution.
* With the *E AQI*, a huge hourly change had relatively little impact on the readings.

Every index has to make a tradeoff between detail and usefulness of individual AQI readings. Also, to compare between an hour-by-hour index (like "*C AQI*" above) and a day-by-day index (like "*E AQI*" above), the values of a day-by-day index are often weighted higher (multiplied by a number > 1). This is because air quality indexes are supposed to indicate the quality of the air, and inhaling 1000 particles an hour for ten hours is much worse than inhaling 1000 particles an hour for one hour.

China, for example, has different AQI calculations for:

* 1hr readings
* 8hr readings
* 24hr readings
* several-month readings (less common)
* annual readings

The AQI values you see in most AQI apps or websites are usually 1hr readings. Some will also show 24hr readings. Government bodies often talk about AQI benchmarks or goals - in those cases, they are talking about their several-month or annual AQI calculations.   

## Indexes can use different combinations of particles

For example, the USA has a generic air quality index that combines O<sub>3</sub>, PM<sub>2.5</sub>, PM<sub>10</sub>, CO, SO<sub>2</sub>, and NO<sub>2</sub> concentrations. It also has an air quality index called "NowCast" that just combines O3, PM2.5, and PM10 concentrations.

# Comparison of air pollution indexes


# References

[1] http://www.tandfonline.com/doi/abs/10.3155/1047-3289.58.3.435
