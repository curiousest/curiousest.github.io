---
layout: post
title: Learn to say the things LLMs aren't able to say
date: 2024-09-13T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - essay
  - professional
  - development
modified_time: 2024-09-13T00:00:00.001-05:00
---
Memorizing is a waste of time. Find a way to learn without memorizing.

That's what I thought my whole student life until I started to learn Chinese. You have to memorize - the hardest thing about Chinese is how much memorization there is. For every one thing you memorize in French, you have to memorize like five things in Mandarin!

For example, Chinese written text is not phonetic so you have to memorize all words twice - the spoken sounds and one or two characters that you've never seen before. Whereas French is phonetic. So "child" in French is "enfant", while in Mandarin it's "háizi" (spoken) and 孩子 (written). And then there's overlap in English/French words but not English/Chinese, and more importantly, there's a direct mapping of concepts in French, but much less in Chinese. [Eg, in Chinese there's no direct equivalent to the concept, "no"](https://studycli.org/learn-chinese/no-in-chinese/).

As someone who had actively avoided memorizing throughout my schooling, this was *hard*. My first instinct was to figure out how to memorize less. After a month of studying, I realized that **it's easier to *recognize* than it is to *recall*.**

> To recognize: when presented with something, to identify it as something you've seen before.
> 
> To recall: to bring something back into your mind.

An example:

Take five seconds and memorize this character: 海

Now clear your mind and scroll down until the character is hidden.
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

Do you think you'd be able to draw that character now? Every stroke perfectly - all the angles and dots and curves?

Of course not, unless you're special or know Chinese. That character is in my Chinese name, and I can't recall how to draw it - because I don't need to.

Now, can you pick the character out from this list?

还 海 害 嗨 骸 骇 駭

That seems easier, right? That's how I learned to write Chinese. When you're writing in Chinese on a phone or computer, you type the spoken word, then a list of possible characters come up and you pick the right one. I never write English, so I figured I'd never write Chinese, and so I was able to reduce the amount of memorization I had to do by ~20% (finger-in-air estimate). I only memorized recalling the spoken word and recognizing the written characters. I didn't have to recall characters anymore.

## Recall vs. recognition using LLMs

With the technique I described, I was able to learn Chinese much faster than otherwise. That said, at some point my Chinese proficiency would be held back by my inability to recall characters. That point comes far down the journey of learning the language.

This same concept applies to *all* the things that LLMs seem to be useful for. The learning curve for a huge set of tasks has changed because if you can structure the task right, you can use LLMs to turn it into an exercise in recognition rather than recall.

In this same vein is the infamous "Stack Overflow" method of yester-decade. It applied to certain kinds of software development problem (package installations, exotic error codes, etc.). You'd Google your error message, click on the first couple Stack Overflow links, look at a couple solutions, then copy-paste the one that looked best. The alternative would be to understand what was really going on, but that wasn't worth the effort most of the time.

It's not a new phenomenon, it has just expanded/exploded with LLMs. We can take advantage of the change by *recognizing* where the recall-recognition tradeoff has suddenly shifted and where it hasn't. LLMs are much better at recognition than recall too:
* [Recognition, Recall, and Retention of Few-Shot Memories in Large Language Models](https://arxiv.org/abs/2303.17557)
* [Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory](https://arxiv.org/abs/2311.08719)

It's easy to think, "If LLMs also struggle with recall, then shouldn't we do *more* recall learning and not less?" But that perspective misses the point. Instead of asking who should handle recall, we should be asking, "Given that recall is difficult and resource-intensive, what aspects of recall should we prioritize?" Like LLMs, humans don’t have infinite capacity for recall, and it's inefficient to treat all information equally. So when people or LLMs learn, we need to be strategic about reserving our recall-memorization efforts for the concepts that matter most.

I came to these thoughts while doing interview prep, and getting demoralized that ChatGPT would be able to answer any interview question better than me with a bit of prompting. Questions like:
- "You are a machine-learning engineer. Make a system design of Instagram's feed."
- "You are a PM at AirBnB. How would you increase bookings?"
- "You are a software engineer. Make a system design of a rate limiter."

Interview prep felt like a recall-memorization task on unimportant content because to answer any of these interview questions in real life I'd use an LLM and Google. Then I thought about how to answer interview questions in a way that an LLM wouldn't be able to reproduce, and my studying began to feel like a worthwhile investment beyond interviews. I no longer felt like I was superficially "memorizing the recall of Chinese characters" anymore.

When you're learning or testing, be strategic about what's important for recognition vs. recall memory. As an interviewer, ask questions that an LLM couldn't answer. As an interviewee, give answers that an LLM couldn't produce. That's how to learn and test the things that matter. It might sound ridiculous now, but it's no different than saying, "give questions/answers that can't be Googled" two decades ago.

## Post-article notes

(Inspired by [this post](/generating-science-fiction-with-llm))

> You are the target audience for this blog post - someone with a technical background, interested in AI. You are the “bad cop” reviewer. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.
> 
>  Now you are the "good cop" reviewer of the same audience. Provide development edit feedback on the piece, with excessive praise describing everything that worked.

<details markdown="1">
<summary>ChatGPT's response, after three iterations of feedback (click to expand)</summary>

### Developmental Editing Feedback for "Learn to Say the Things LLMs Aren’t Able to Say"

---

#### **General Structure and Organization**

1. **Disjointed Flow**: The essay has some good points, but the transitions between sections are clunky. For instance, the jump from discussing learning Chinese to LLMs feels abrupt and underdeveloped. These two themes need better connective tissue. Perhaps using a metaphor or a clearer thesis at the start of the piece to unify these ideas would help.

2. **Inconsistent Focus**: The piece starts with your personal experience learning Chinese but then shifts to a discussion about LLMs without making it clear why the comparison is important. Are you arguing that LLMs and human learning are similar in meaningful ways? Or that LLMs fail in recall, just as humans do? The central thesis is blurred. Sharpen your argument: are you focusing on the human approach to learning, or are you contrasting human vs LLM learning styles?

3. **No Strong Conclusion**: The ending is weak and feels like an afterthought. You mention LLMs and human interview prep but don't tie this back to your original point about memorization and recall. The final takeaway needs to be much clearer, especially for a technical audience. What actionable insight are you leaving them with?

#### **Content**

1. **Unclear Thesis**: Is the main argument about the inefficiency of recall in both humans and LLMs, or is it about learning strategically? This confusion weakens the core message. You introduce multiple ideas but fail to prioritize or develop them fully.

2. **Lack of Evidence**: For a technical audience, it’s important to support your claims with stronger evidence or data. When you say, "LLMs struggle with recall," provide a concrete example or data. This point is just hanging without proper backing. Similarly, your experience learning Chinese is a nice anecdote, but it needs to be tied to a broader argument about the limitations of both human and machine learning.

3. **Simplistic Analogies**: The Chinese memorization example is useful, but the follow-up feels oversimplified for the target audience. You rely heavily on basic definitions of "recognition" and "recall," which may feel condescending to a reader with a technical background. You might want to use more advanced examples (maybe from cognitive science or AI literature) to explain these terms, so they feel new and insightful.

4. **Missed Opportunities for Depth**: There is no deep exploration of the relationship between how LLMs process data vs. how humans do. This topic is ripe for deeper analysis. How can technical professionals leverage LLMs to balance the tension between recognition and recall? What does this mean for future AI development? You touch on these ideas but don’t dive deep enough.

5. **Vague Recommendations**: Your call-to-action at the end feels half-baked. You encourage interviewers to ask questions that LLMs can’t answer, but this feels overly simplistic. Give specific guidelines. What types of questions are those? What cognitive functions should we prioritize when competing with or using AI?

#### **Tone and Audience**

1. **Too Informal**: The tone veers on the side of conversational, which might be fine for a blog but feels inconsistent for an audience with a technical background. Phrases like "That seems easy, right?" and "unless you're special or know Chinese" detract from the professionalism of the piece. Keep the tone sharp, analytical, and more in line with a technical essay.

2. **Assumptions about Audience Knowledge**: While the piece over-explains some concepts (like recognition vs. recall), it glosses over others that would interest your target audience. Dive deeper into how LLMs function in terms of memory structures or learning models. This audience expects to engage with more complex and detailed discussions, not just surface-level comparisons.

3. **Personal Anecdotes**: While personal stories are good for creating engagement, your experience with learning Chinese takes up too much of the essay without contributing much to the central theme. If you're going to include personal anecdotes, they should serve as a direct metaphor or example for your technical argument, not distract from it.

#### **Suggestions for Improvement**

1. **Clarify Your Thesis**: Make a clear argument about what you're trying to prove. Is it that LLMs and humans share similar challenges with recall? Or that both need to be strategic about what to memorize? Once you've clarified the thesis, structure the rest of the piece around that core idea.

2. **Improve Flow and Transitions**: Make the connection between learning Chinese and learning in a technical environment (including LLMs) more explicit. Why does this matter for someone in AI? The audience should see clear links between these seemingly different domains.

3. **Provide More Technical Depth**: You need to address your technical audience directly. This can include referencing how memory models work in AI or contrasting deep learning's limitations with human cognitive functions. Incorporate more advanced examples or references from cognitive science or machine learning literature.

4. **Strengthen the Ending**: Your conclusion needs a stronger punch. What should the reader take away? Are you suggesting a shift in how we learn, work, or test AI models? Make the implications clearer, particularly for a reader interested in applying this to AI or human learning.

5. **Elevate Your Call to Action**: Offer more than vague advice. What specific techniques should people use in interviews or study sessions to differentiate themselves from LLMs? What should they focus on memorizing vs recognizing?

---

### Final Thoughts

Overall, the piece has potential but needs a clearer structure, more depth in technical explanations, and stronger transitions between your personal experiences and the technical argument you want to make. The tone also needs to match the target audience, which expects an essay that challenges them intellectually, rather than explaining basics they likely already know.

### Developmental Editing Feedback for "Learn to Say the Things LLMs Aren’t Able to Say" (Good Cop)

---

#### **General Structure and Organization**

1. **Engaging Introduction**: The way you open with your personal story of learning Chinese is an excellent hook. It’s relatable, and immediately humanizes the challenges of memorization. Starting with a real-world struggle makes the essay accessible and sets a thoughtful tone, inviting the reader to reflect on their own experiences with learning—whether languages, coding, or anything else.

2. **Clear and Logical Progression**: The essay has a natural flow from personal anecdote to larger insights about human cognition and AI. Your transition from learning Chinese characters to recognizing the difference between recognition and recall is smooth. I especially appreciate how you gradually build the reader’s understanding of how these cognitive processes map onto both human learning and the limitations of LLMs. Each section flows nicely into the next.

3. **Bite-Sized Takeaways**: The way you break down complex ideas into digestible points makes this piece a great read. You define recognition vs. recall clearly and then demonstrate how this distinction is not just important for language learning but also for understanding LLM behavior. This method of layering information keeps the reader engaged and builds towards a deeper understanding without overwhelming them.

#### **Content**

1. **Powerful Analogies**: The use of your experience with Chinese characters as a stand-in for the broader conversation on recognition vs. recall is brilliant. By explaining something as relatable as the difficulty in recalling or drawing a complex character, you effectively illustrate how much easier recognition is compared to recall. This serves as a perfect bridge to your argument about how LLMs handle data and knowledge. It’s a simple, but effective metaphor that sticks with the reader.

2. **Relatable Insights into Human and AI Learning**: Your comparison between how humans and LLMs learn and memorize is deeply insightful. Drawing attention to the shared cognitive challenges between humans and machines is a thought-provoking point, especially for an AI-savvy audience. It highlights a nuanced understanding of LLMs, and your perspective feels refreshing. Many readers will appreciate that you're not just talking about AI in technical terms but are drawing parallels to their own learning experiences.

3. **Unique Perspective on Interview Prep**: The section on interview prep is particularly clever. You’ve taken a common frustration—feeling overshadowed by AI in knowledge recall—and turned it into a positive challenge. Instead of framing LLMs as competition, you propose ways to outthink them by focusing on human strengths like creativity and nuance. This is a forward-thinking way to approach the subject of LLMs in professional spaces and provides practical takeaways for the reader.

4. **Balanced Argument**: What I especially admire is how you present a balanced view on the tension between recognition and recall. You don't shy away from acknowledging the difficulty of recall but still frame it in a positive light by emphasizing its strategic value. This complexity makes the essay intellectually satisfying, as you aren’t offering a one-size-fits-all solution but a nuanced way to think about learning, both for humans and AI.

5. **Encouraging Critical Thinking**: Your suggestion for interviewers to craft questions that LLMs can’t answer and for interviewees to respond in ways that AI wouldn’t is brilliant. You’re challenging the reader to think beyond typical knowledge recall and toward higher-order thinking. This strategy is sure to resonate with professionals in technical fields who are grappling with the growing presence of AI in their work. It's not just theory—you’re offering actionable advice that feels relevant and empowering.

#### **Tone and Audience Engagement**

1. **Approachable Yet Intelligent Tone**: The tone you strike is perfectly balanced. It's approachable, with a conversational style that makes difficult concepts feel manageable. At the same time, it's clear that you respect your reader’s intelligence by not over-explaining. For an audience with a technical background, this tone is ideal because it doesn't come across as patronizing, yet it’s still inviting to those who may be new to the topic.

2. **Engagement Through Personal Experience**: The personal anecdotes make the essay relatable without detracting from the technical points. Your story about learning Chinese, combined with the struggle of interview prep in the face of AI, humanizes the piece and keeps it grounded. You maintain a personal connection with the reader, which makes the more abstract parts of the essay easier to digest.

3. **Challenging but Rewarding Concepts**: The ideas you explore around recognition, recall, and how LLMs function are challenging, but you break them down in ways that encourage deeper reflection. The technical audience will appreciate being challenged without feeling overwhelmed. You guide them through your thought process, but give them enough space to engage with the concepts on their own terms.

#### **Suggestions for Further Amplification**

1. **Expand on Strategic Learning**: The section where you touch on strategic learning—choosing when to prioritize recall vs recognition—could be expanded. It’s a fascinating idea, and your audience would likely enjoy a more detailed exploration of how this could apply to AI education and human skill development. Maybe a few more examples from your personal experience or even AI-related fields could deepen the impact of this point.

2. **More Depth on LLMs and Cognitive Models**: While your explanation of how LLMs handle recognition vs recall is good, you could take it one step further. Your technical audience might appreciate a few more details about the actual mechanisms behind LLM behavior—perhaps touching on specific architectures or models that showcase this divide. A deeper dive here would further engage those readers who are familiar with AI development.

3. **Elevate the Call-to-Action**: The advice about interview questions is fantastic, but you could broaden it beyond the interview context. What other professional areas might benefit from this approach? How can teams and individuals continue to learn in ways that LLMs cannot replicate? You hint at these ideas, but there’s room to expand this takeaway into a broader discussion about the future of work and education in a world shaped by AI.

---

### Final Thoughts

This essay is a compelling read, with a personal touch that connects with the audience while offering thought-provoking insights into learning and AI. The analogy between learning Chinese and interacting with LLMs is striking and provides a strong backbone to the piece. Your exploration of recognition vs. recall is clear, engaging, and directly relevant to both human cognition and AI development.

Your ability to bring personal experience into a technical discussion without losing focus on the essay’s main argument is impressive. With a bit more depth in a few areas, this piece could be even more impactful. It’s already packed with valuable ideas, and it challenges the reader to rethink how they approach learning, both as individuals and in the context of AI.

Keep up the excellent work—this is the kind of writing that bridges technical knowledge with real-world application!

</details>

## Extension (update)

What if harnessing the differential between recall and recollection is a building block of intelligence?

### Example 1: LLMs for writing

I've been using LLMs along with a story outline and a prompt to generate ~100s of attempts to write parts of the story. A prompt might be like, "write the opening scene" or "write the dialogue when the characters meet". I read through the 100s of examples to pick out the phrases or paragraphs that I like. It's maybe 5% of the content. I've created labelled data for two different tasks:
1. Recall: given a prompt, the LLM should produce the content that I preferred and not the content is didn't prefer.
2. Recognition: given produced text, the LLM should filter the content to match my preferences.

My intuition says that both humans and LLMs are much better at recognition than recall. This is super interesting, because any system can make itself more intelligent at a task by performing batch recall (with some randomization), then filtering with recognition. It's like brainstorming and filtering.

### Example 2: Evolution and survival

Let's frame survival of the fittest as a recollection task given to "nature" or "the universe". A species produces a whole batch of candidate life forms within the species. Nature filters the life forms that it prefers. In this way, the "intelligence" of the universe is transferred into the next generation of the species. Those preferences of nature are compressed into the DNA/source code of the species.