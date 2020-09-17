---
layout: post
title: "How I speak product"
date: '2020-05-25T00:00:00.001-05:00'
author: Douglas Hindson
tags: 
- personal development
- professional
modified_time: '2020-05-25T00:00:00.001-05:00'
---

I've observed that people around me are solution-oriented. We like to focus on what needs to be done - the solution. The following interaction happens with everyone, from engineers to salespeople:

*Colleague*: "We need to build XYZ."

*Me*: "What problem is that solving?"

*Colleague*: "Talking about the problem doesn't get us any closer to delivering. It's a great idea, so we just need to execute."

We all have good intentions, but there's conflict. This article explains where I'm coming from - a way of thinking that exceptional product people drilled into me.

## The framework

Every time a person or team puts effort into something, they are working on a solution to some problem. The problem is an opportunity for someone to get new value, and the solution is an approach to capture some of that value.

<img src="https://i.imgur.com/U0Imhub.jpg" style="width: 600px; height: auto; align:center;"><br/>

## That's abstract. How is this useful?

Sometimes the problem is obvious, and <i>every second spent clarifying the problem is not spent making the solution happen</i>.

Other times you intuit a solution to poorly defined problems. It's hard for others to evaluate or execute on a solution to a problem they don't understand. With a clearer problem, others can make better solution decisions - solutions that capture more value at a lower cost. In a situation like this, you can backtrack to explain opportunities and uncover alternative solutions.

I can point to countless projects where we built a solution to the wrong problem. There are few times where we spent too much time clarifying the problem.

### Backtracking example

A salesperson just came off of a call with a big, important B2B customer. The meeting gave the salesperson a great idea for a change to make in the product. The salesperson explained the product changes to the tech lead. They added a feature:

*As an expert user, when I'm working on a task in my task queue, and that task can't be finished now, I can delay taking action on that item until later.*
<br>

**1. What problem is this solving?**
<table><tr><td>
<img src="https://i.imgur.com/g3umspm.jpg" style="width: 300px; height: auto; align:center;">
</td>
<td style="font-size: 0.7em">

<ul>
<li>Users can not immediately take action on tasks they pick up.</li>
<li>The app expects users to take action immedidately.</li>
</ul>

</td></tr></table>

**2. What other solutions are there?**

<table><tr><td>
<img src="https://i.imgur.com/23Iw7L5.jpg" style="width: 300px; height: auto; align:left;">
</td>
<td style="font-size: 0.7em">

<ul>
<li>Drop tasks that can't be completed immediately.</li>
<li>Check that the user can finish the task before they pick it up.</li>
<li>A user can transfer the task to another user.</li>
</ul>

</td></tr></table>

**3. What problems is this really solving for?**

<table><tr><td>
<img src="https://i.imgur.com/hBUu7es.jpg" style="width: 300px; height: auto; align:center;">
</td><td>

Low user engagement was the underlying problem. The pain point expressed by the users (the customer's employees) was one of many excuses for low engagement with the product. Low user engagement was causing low product value to the customer.
</td></tr></table>

**4. What other solutions are there?**

<table><tr><td>
<img src="https://i.imgur.com/vcLRdO7.jpg" style="width: 300px; height: auto; align:center;">
</td><td style="font-size: 0.7em">

<ul>
<li>Get the customer to change how their employees are incentivized to interact with the product</li>
<li>Gamify interactions with the product</li>
<li>Provide a more convenient medium to access the product (mobile, voice, integration in another product, etc)</li>
</ul>

</td></tr></table>

**5. What problems is this really, really solving?**

<table><tr><td>
<img src="https://i.imgur.com/RBIAlOM.jpg" style="width: 300px; height: auto; align:center;">
</td><td>
The product was not providing enough value to the customer to justify the cost. The customer had faith, and wanted to see the product improving over time.
</td></tr></table>

At some point there's little value in clarifying problems and solutions.

You can give feeling of progress to customers in many ways - sharing roadmaps, reflecting on past growth, demoing R&D results, etc. Using product development resources to give the feeling of progress is inefficient.

If the salesperson and tech lead had clarified the tree of problems, they could have made decisions that brought greater rewards for the same effort.

## More real-life examples

<details>

<summary>A developer improving webpage navigation</summary>

<br>

A developer was adding a new section to the navigation menu of a website for expert users. They saw that the list in the navigation menu was long, and long navigation lists generally should be made into collapsible headings. There was some refactoring required, but the developer believed it's worth making the page easier for the expert users to use.
<br><br>

<img src="https://i.imgur.com/0Q8naLC.jpg" style="width: 600px; height: auto;"><br/>
<br>
<b>Reframing the problem</b>
<br><br>
The immediate problem was that the navigation pane was slow for the developer to use because there are so many items to look at. The higher-level problem was, there's an opportunity for expert users to use the website more efficiently. The solution was to make headings collapsible to reduce the number of in the list, reducing mental load.

Did this solution have the best value/effort tradeoff for those solutions? The developer didn't think much about it, and this solution can actually deliver negative value. What if expert users memorized the list, and collapsible headings introduces a new click and more muscle-memory? What if expert users work faster with no navigation pane at all?

<br><br>

</details>

<details>

<summary>Establishing a technical strategy</summary>

<br>

A senior manager wanted to define a technical strategy for a group of software teams. They had a clear idea of why a technical strategy would be useful. They set up a meeting with a few senior individual contributors from those teams so they could define the strategy together in a meeting.

In the meeting, everyone expressed tangential beliefs and observations. The members had not worked together before, so they used different language and terminology. They didn't agree or disagree on anything and the meeting ended without progress towards a technical strategy.
<br><br>
<b>Reframing the problem</b>
<br><br>
Everyone had a different idea of what the technical strategy was for. The group lacked focus for the solution, so they needed to align on the problem. It turned out that the problem was twofold, and the two problems needed different solutions.

In the long term, the group of teams were building the same systems other groups had already built. A vision of a shared platform and cross-team commitment to that vision would reduce costs.

In the short term, a technical strategy was needed to convince senior management stakeholders to allocate resources to the initiative. This is the problem that the senior manager wanted to solve in the meeting.
<br><br>

</details>

## Conclusion

Every time a person or team puts effort into something, they are working on a solution to some problem. These things exist, even if we don't think about them every time we work on something.

Every second spent clarifying the problem is not spent making the solution happen. Like all things in product, you must do exactly what is needed and no more.

---

Thanks to Bauke, Eric, Manuel, and Tom for reading drafts of this.
