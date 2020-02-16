---
layout: post
title: Comparing air pollution indexes
date: '2017-05-29T15:22:00.001-05:00'
author: Douglas Hindson
tags:
- O2Canada
- air pollution
- facts and data
modified_time: '2017-05-30T15:22:00.001-05:00'
---

[There are a lot of air pollution indexes](#there-are-a-lot-of-air-pollution-indexes). [Air quality over time is hard to express](#air-quality-over-time-is-hard-to-express) and [indexes can use different combinations of particles](#indexes-can-use-different-combinations-of-particles), so one governing body often has multiple air quality indexes.

First we'll try to compare air pollution indexes and further sections describe why it's hard to compare.

## Comparison of air pollution indexes by hourly PM<sub>2.5</sub>

If you wanted to compare each different air pollution index as they would appear on your app/website of choice, it would be close to this chart. 

The way air pollution indexes work is:

1. Take some measurements (of particle concentrations in the air)
2. Pass those measurements through an algorithm (each index has a different algorithm)
3. A number and some text comes out, explaining the air quality

PM<sub>2.5</sub> is an important measurement that is commonly used. These indexes are compared by hourly/daily PM<sub>2.5</sub> values - which is a good, but imperfect way to compare indexes that you would see on air pollution websites / apps. The number and text that comes out of the algorithm is represented in the "Text (AQI range)" column of the below chart.


<iframe style="width:1000px; height:1650px;" src="https://docs.google.com/spreadsheets/d/17Zim8kxONMOG1ZSQIsEvhxQcXNyNbffvmougnEzuLVU/pubhtml?widget=true&amp;headers=false"></iframe>

If the above frame didn't load correctly (if you're somewhere Google Sheets is blocked), [click here to see the chart](https://github.com/curiousest/curiousest.github.io/blob/master/_posts/resources/aqi_chart.png). Colours are approximately what is supposed to be used for that index.

## There are a lot of air pollution indexes

There are ten major government bodies represented in [this wikipedia air pollution article, as of April 2017](https://en.wikipedia.org/wiki/Air_quality_index#Indices_by_location), each with their own set of air quality indexes. Such variety is because:

### There are many different particles that affect air pollution

* Some particles are more prevalent in certain areas of the world.
* Some particles are relevant everywhere.
* Some particles may be relevant in some conditions and not others.
  * Ex: Ozone (O<sub>3</sub>) may not be as dangerous in cold weather [[1]](#references).
* Indexes can use different combinations of particles
  * Ex: the USA has a generic air quality index (EPA) that combines O<sub>3</sub>, PM<sub>2.5</sub>, PM<sub>10</sub>, CO, SO<sub>2</sub>, and NO<sub>2</sub> concentrations. It also has an air quality index called "NowCast" that just combines O3, PM<sub>2.5</sub>, and PM<sub>10</sub> concentrations [[2]](#references).

### Air pollution is complex to measure and explain

* Air quality over time is hard to express
* The maximum, minimum, and average concentrations of different particles all have different effects
* Combining all these concepts and measurements together to give one number/recommendation is a significant simplification

### Different countries want to give different recommendations

If your pollution index says every reading above 100 is "very bad", but many places in your country consistently have readings ranging from 100 to 900, your pollution index will not be useful to your constituents - you need different kinds of "very bad".

### One pollution index sounds like a good idea, but...

![Standards](https://imgs.xkcd.com/comics/standards.png)

Source: [XKCD](https://xkcd.com/927/)

## Air quality over time is hard to express

A major reason for one governing body having multiple air quality indexes is because the "badness" of air pollution is determined by the number of bad particles in the air over time. Every index has to make a tradeoff between detail and usefulness of individual AQI readings.

As an example, suppose *London* has readings for *particle X* as follows:

| Time                           | **1pm** | **2pm** | **3pm**  | **4pm** |
| # of *particle X* in *London*  | 10  | 10  | 1000 | 10  |

Now suppose we invent three different air quality indexes, *C, D, and E AQI*:
* *C AQI* is the number of 'X' particles in the air right now.
* *D AQI* is the average number of 'X' particles in the last 3 hours.
* *E AQI* is the average number of 'X' particles in the last 24 hours.

| Time                      | **1pm** | **2pm** | **3pm** | **4pm** |
| # of *particle X* in *London*  | 10 | 10 | 1000 | 10 |
| *C AQI* in *London*              | 10 | 10 | 1000 | 10 |
| *D AQI* in *London*              | 10 | 10 | 340 | 340 |
| *E AQI* in *London*              | 10 | 10 | 51 | 51 |

Notice the differences at 3-4pm. 

* With the *C AQI*, you get more to-the-hour detail about air pollution, but you need to see more than one number to understand what's really going on.
* With the *D AQI*, you have a better understanding of the recent past, but it lacks both detail and a long-term view on air pollution.
* With the *E AQI*, a huge hourly change had relatively little impact on the readings.

China, for a real-world example, has different AQI calculations for:

* 1hr AQI
* 24hr AQI
* several-month AQI (less common)
* annual AQI

Also, to compare between an hour-by-hour index (like "*C AQI*" above) and a day-by-day index (like "*E AQI*" above), the values of a real day-by-day index are often weighted higher (multiplied by a number > 1). This is because you may read the current hour-by-hour index together with the current day-by-day index. Inhaling 1000 particles an hour for 24 hours is much worse than inhaling 1000 particles an hour for one hour, so the 24 hour index is weighted to seem bigger and scarier.

The AQI values you see in most AQI apps or websites are usually 1hr readings. Some will also show 24hr readings. Government bodies often talk about AQI benchmarks or goals - in those cases, they are talking about their several-month or annual AQI calculations.

## References

[1] A New Multipollutant, No-Threshold Air Quality Health Index Based on Short-Term Associations Observed in Daily Time-Series Analyses, https://www.tandfonline.com/doi/abs/10.3155/1047-3289.58.3.435

[2] Overview of the new PM2.5 NowCast Method, https://www.arb.ca.gov/carpa/iascpresentations/2015/nowcastaqiforpm25overview.pdf

[3] USA AQI calculator, https://airnow.gov/index.cfm?action=resources.conc_aqi_calc

[4] USA / China AQI calculator, https://github.com/kkpoon/aqicalc-js

[5] Review of Air Quality Index and Air Quality Health Index (Canada), https://www.publichealthontario.ca/en/eRepository/Air_Quality_Indeces_Report_2013.pdf

[6] Air Quality in Europe Indices definition, https://www.airqualitynow.eu/about_indices_definition.php

[7] Calculation of AQI (India), cpcb.nic.in/AQI%20-Calculator.xls

[8] National Air Quality Index (India), https://cpcb.nic.in/FINAL-REPORT_AQI_.pdf

[9] Review of the UK Air Quality Index, https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/304633/COMEAP_review_of_the_uk_air_quality_index.pdf

[10] NowCast Calculator, https://www3.epa.gov/airnow/aqicalctest/nowcast.htm

[11] The New AHQI System - Purpose and Use (Hong Kong), https://www.aqhi.gov.hk/en/what-is-aqhi/faqs.html

[12] Technical Regulation on Ambient Air Quality Index (China), https://www.zzemc.cn/em_aw/Content/HJ633-2012.pdf

[13] National Ambient Air Quality Standards for Particulate Matter; Final Rule (USA), https://www.gpo.gov/fdsys/pkg/FR-2012-06-29/pdf/2012-15017.pdf
 
[14] Computation of the Pollutant Standards Index (PSI), (Singapore), https://www.haze.gov.sg/docs/default-source/faq/computation-of-the-pollutant-standards-index-(psi).pdf

[15] FAQs on Air Quality (Singapore), https://www.nea.gov.sg/anti-pollution-radiation-protection/air-pollution-control/faqs-on-air-quality

[16] What's CAI?, https://www.airkorea.or.kr/eng/cai/cai1
