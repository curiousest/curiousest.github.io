---
layout: post
title: "What is an expert task?"
date: '2021-09-22T00:00:00.001-05:00'
author: Douglas Hindson
tags: 
- 
modified_time: '2021-09-22T00:00:00.001-05:00'
---


Expert tasks are activities that are important to society, performed by people with significant training.
Examples:
- A doctor diagnosing a patient's illness.
- An insurance adjuster estimating the cost of fixing a damaged vehicle or property.


other properties
- very difficult, if not impossible, to automate exactly what the experts do. Takes significant investment to build the system and acquire the data needed to automate the core tasks.
- Once software systems are deeply integrated in the process, and there's less handover between people or across systems, there's huge efficiency gains.
- They are usually comprised of some core expert tasks which require significant expertise, real-world interactions to acquire and disemminate information, and ancillary tasks to put everything together [make a diagram]
- solving subsets of the expert task could be valuable (lower AI completeness, same integration cost, high value)

- the more trivial, admin-heavy, "boring" cases are where a sizable portion of the value is (20% of AI complexity, 80% of systems integration effort, 50% of value). Experts and the companies they work for both want this to be automated, and this is where automation should focus (and comms around AI projects - no one wants to "be automated", but everyone wants their boring admin to be automated).

Ex: "this vehicle is so damaged that it's obviously a write-off" or "this claim is normal and doesn't need an adjuster to look deeper into it."
Ex: "the patient can solve their issue themselves by going to the pharmacy for drug XYZ"

- automating the core expert tasks and activities on top is disruptive to the industry, transforms the entire process
- automating some of the expert tasks is a reason for a company to buy and invest in onboarding to a product

ex: automating adjusting a claim (10x value) vs. automating estimating a claim (100x value)
ex: automating remote texting triage vs. continuous predictive/preventative triage

## Real-world interactions

The expert tasks are information-processing, decision-making ones. But information has to come from from the real world. And information has to be disemminated.

Collecting information isn't always a one-and-done event. Often, the most effective method of collecting information needed to perform the expert task is like a dialogue. The expert needs to have some information, and process it, to most effectively gather the next piece of information.

Ex: doctor asking questions to a patient


Sometimes, a standard set of information is enough.
Ex: for a motor insurance claim, you get metadata about the driver+vehicle, four corners, licence plate, damaged area. But in this case, some follow-up is often needed - like the state of the car at different stages as it's being repaired.


doctor triaging a patient:
- one core expert task is "given a set of evidence (presence/absence of symptoms + risk factors), what conditions could the patient have? (and therefore how should the patient be triaged?)"
- a secondary expert task is "What questions should we ask a patient to most effectively gather evidence for their triage?"

insurance adjuster / motor engineer estimating a claim:
- given these pictures, videos, and metadata about a damaged vehicle, what must be done to repair it? (and how much will that cost?)
- given another party provided an estimate (given all the data needed to estimate), where did they make mistakes?
