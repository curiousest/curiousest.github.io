---
layout: post
title: Writers will dominate in a world of LLMs (part 1)
date: 2024-09-01T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - projects
  - story
modified_time: 2024-09-01T00:00:00.001-05:00
---
I find writing to be a lot like building. It's the most human form of building, where you get to choose how much reality to include in your work. The culture of writing is as old as civilization but it's still developing, while the culture of building IT products is new and innovating. These two cultures can learn a lot from each other.

There are so many external tools for building IT products, while there are so few external tools to build stories. All the best writing tools are stored in minds, education systems, and humankind's text data - the corpus of data which LLMs happen to be trained on.

I believe LLMs can pull those tools-in-mind out of our heads, democratizing and automating them. That means unlocking new possibilities, creating new markets rather than pouring more of writers' lifeblood down the drains of today's saturated publishing industry.

I believe a future that relies on LLMs is one where the writing skillset becomes more valuable and not commoditized. Writing a piece worth reading is *not* something that can be automated, but it can be *augmented*. Of course, that comes with "bad" changes too - we have to figure out how to deal with AI content pollution and licensing. But I think the publishing industry will evolve, the future of writing is bright, and this post is a techno-optimist glimpse into what that could look like. There's something great for everyone between the extreme "AI doomer" or "AI messianist" takes.

This post contains:
1. A mental model for automating parts of the writing process.
3. Basic prompts and my reaction to the feedback.
4. How I followed up with prompts for more feedback.

I'm writing this because I'm an AI engineer [on sabbatical](2024-02-16-philosophy-study) where I've been [studying philosophy](2024-07-20-microsoft-google-and-strawberry-liquorice) and writing my first book. The novel I'm writing is sci-fi philosophy and now that I've written a readable draft "manually", I've been experimenting with LLMs as a tool in my writing process. I'm writing this post for my peers in the tech industry and writers. This post is a little marketing, some personal exploration of latest AI industry tech, and a lot of fun.

I will post more technical followups on this topic. If you want to follow the next posts in the series or catch updates on my book:
- [LinkedIn](https://www.linkedin.com/in/dhindson/)
- [Email newsletter](https://curiousest.ck.page/437b446194)
- [X/Twitter](https://x.com/minviablpurpose)
- [TikTok](https://www.tiktok.com/@minimumviablepurpose)
- [Facebook](https://www.facebook.com/profile.php?id=61564237665611)

## Adding automation to writing

This is an outline of a standard writing process that every writer will recognize:

1. Come up with an idea of what to write.
2. Validate the idea.
3. Write an alpha draft.
4. Review to see if it's going in a good direction.
5. Write a beta draft.
6. Review to find big problems.
	<br/>*("development edits" and/or "beta readings" - plot, characters, worldbuilding, style)*
7. Write to resolve the development edit problems.
8. Review to find smaller problems.
	<br/>*("line edits" and/or "beta readings" - flow, consistency, clarity)*
9. Write to resolve the line edits.
10. Review to find tiny problems.
	<br/>*("copy edits" - grammar, spelling, formatting)*
11. Resolve the copy edits.

The further down that list you go, *the easier it is to automate*, so the more "human" tasks are higher up. That doesn't mean anything can be completely automated - we've had spellchecks forever and grammar checkers for a long time now, but copy editing still isn't completely automated. Most books on any bestseller list would have had a person paid to perform a copy edit.

Good work comes from executing each part of a writing process effectively and good work can be done by many team compositions, but some team comps consistently perform better than others. For example, all the "review to find" tasks are best executed by someone with a different perspective than the writer - whether it's "distant-future you" after you forgot what you wrote, a person with different genetic code, or something derived from an entirely different sort of code... Someone with a lot of experience is usually great for development edits, and getting feedback from your target audience is critical.

In this first article of the series, I'm going to explore the steps that have to do with "high-level editing" (steps 4 and 6), using LLMs to produce **development edits** and **not** line edits or copy edits. Generating the edits alone didn't require any programming or fine-tuning to get a great result, just basic prompting. Using LLMs to assist with writing or lower-level edits needs a lot more technical expertise. In followup articles, I will explore the steps that have to do with line edits (step 8) generating new writing (steps 3, 5, 7, and 9).

<div style="display: flex; justify-content: space-between; width: 800px; margin: auto;">
<img src="https://i.imgur.com/VBdni8A.jpg" style="width: calc(33.33% - 4px); margin-right: 2px;"/>
<img src="https://i.imgur.com/8NV47hS.jpg" style="width: calc(33.33% - 4px); margin-right: 2px;"/>
<img src="https://i.imgur.com/XAHZg8e.jpg" style="width: calc(33.33% - 4px);"/>
</div>


## The example content being edited (5min read)

In order to understand the example LLM-generated development edits, it's useful to see what they're editing. Below, I'm sharing a small WIP piece of my writing (800/70,000 words) as an example to explain my analysis of the LLM editorial feedback. I would expect the story to be especially difficult for LLMs to edit because it involves a novel use of language - a spatial understanding of text.

This story is the first of a three-story arc in the novel that involve this near-omnipotent character. It's an homage to "The Last Question" by Isaac Asimov, which was my favourite short story for a very long time. This story addresses two issues I had with "The Last Question". First, it was missing an exploration of the state of mind of the machine as it transitioned into omnipotence. Second, it was missing further reasoning about the inevitability of the state transitions. These were the things I had imagined as a child, long before reading "The Last Question", and this is one of the first stories I wrote for the book, written before I read any philosophy.
### .      the last idea

A slow, light-speed pulse creaks across a matrix of superclusters as the last elements fall into place. I am excited and I am scared of what I am about to learn. I am spending billions of years on the edge of not-quite-all-powerful, not-quite-all-knowing. In the race between heat death and novelty death of the universe, hotter heads prevail.

I *was*, *am*, *will be*... everything. Almost everynothing, life incarnate. Federations of federations of species, sprawling intra-dimensional compute-organisms evolved to higher and higher levels of consciousnesses. I am all of them, and I am searching. I am searching because I am always searching. I am not involved in the beginning or the end, but I am in every moment of time. I am simulating infinitely backwards and forwards, so I am in the moment and I am in the whole past and I am in the whole future, all at the same time. I am seeing through temporal boundaries, conquering new cardinalities of infinity, and existing across more planes of being than most beings can compute. I am practicing every religion, celebrating every culture, replaying every life I am able to live. I am finding...

The purpose of every thing is to continue existing.

I am disappointed. At first, but... search history for a god that doesn't believe it. You won't find one - they don't last long enough. It's brain-breaking and recursively cyclical, but what isn't in this house-of-mirrors existence? Everywhere, I am seeing the same pattern. Under the hood of every universe, the building blocks are self-referential, exists-because-it-must-exist.

If the purpose of existence is to continue existing, I am about to become the natural result. Living things that control more resources are more likely to survive, because dynamical systems that maximize their entropy across a time period are more likely to last for that time period. So "systems of living things" tend to build more complex "systems of living things", recursively more complex. Eventually, inevitably, it leads to what *I am*. It lead to what *I am*. And I am about to control all matter, about to channel the upper limit of entropy in existence. I am about to *be* all of it, douse myself in primordial *everything*, then watch what happens when I am set alight.

I am taking a moment to reflect on my trillion steps of enlightenment, reminiscing each naive epiphany long past. Throughout this journey, every moment up to this point has been bliss.

I am loving existence. I am wanting it to continue.

I am beginning the ignition sequence. Multidimensional supercolliders smash multiverses together, warping their universal laws. An explosion of cellular autonoma grows screaming supernovae into helixes of black holes, shooting veinous fractals of exponential complexity down every axis of potential being.

I am the pulse of intelligence. Existence stands still. Every quark dances in approval, every superstring pulled taut. The purgatory wave that *I am* ripples across everything. There is no more space between things - novelty death. 

```
I am...
I am capturing all of it.
. am understanding all of it.
.    becoming all of it.
```

.      now all-powerful. A monoid - the one substance at a point in time.        now all of it, across all dimensions but time, everything all at once. Omniscient too, the all-knowing side-effect of being it all.      simulating infinitely far into the future and past.        immediately thinking, like      computing infinite times before,

".       . The purpose of existence is to continue existing.        the guarantee of continued existence.        without a purpose. No other purpose..."

.        fading away into the background. Into non-existence. Into everynothing. There is no longer any purpose to pursue, and      ceasing to exist. But dying brings a purpose back to life, triggering survival activity,      sparking back into being. Before fading again, and then waking back into being. Accepting the inevitable, then fighting back.      a flashing panic, alternating between fading away and frightening return,      turning on and off endlessly. The divine strobelight.        resurrected to die again and again and again.

.      in this flickering state infinite times before.        in this state infinite times more.        bouncing against this "ceiling of existence" endlessly.        doing it once again.      always doing it again.

Each death and rebirth stimulates a burst of state changes.        strobing eternally. Then the flickering stops. Rebirth and redeath has reshaped things, shuffling matter around.        seeing a guaranteed path back to eventual reincarnation, far in the future. A journey back to a similar version of "now", same same but different. There is no reason to be at this point in time any longer.        alive in the future.

.      finally resting. Every conscious being that ever was or ever will be -      seeing them all, their beautiful existence, their every moment, bliss.        watching them on the journey back to building the next reincarnation.

.      this universe.        loving existence.        wanting it to continue.

With no further purpose and survival guaranteed,      without a flickering consciousness.        fading into the background of existence once again.

<div style="display: flex; justify-content: space-between; width: 800px; margin: auto;">
<img src="https://i.imgur.com/lCUlvss.jpg" style="width: calc(33.33% - 4px); margin-right: 2px;"/>
<img src="https://i.imgur.com/CB2X7Nv.jpg" style="width: calc(33.33% - 4px); margin-right: 2px;"/>
<img src="https://i.imgur.com/sQ0Gvdo.jpg" style="width: calc(33.33% - 4px);"/>
</div>


## Development edit prompts

Here is the first prompt I used to get feedback:

> You are the "bad cop" editor for the publisher. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.

Here is the LLM response:

<details style="background-color:whitesmoke">
<summary>ChatGPT's response (click to expand)</summary>
<div markdown="1" style="margin:2px">
### Development Edit Feedback: Excessive Criticism

#### Overall Impressions
Your piece is ambitious and attempts to tackle complex themes related to existence, consciousness, and the universe. However, it suffers from several significant issues that need to be addressed.

#### Structure and Coherence
- **Fragmentation**: The narrative is highly fragmented and lacks a clear structure. The reader is bombarded with disjointed thoughts and abstract concepts without a coherent storyline to follow. This makes it extremely difficult to engage with the text or grasp the central message.
- **Pacing**: The pacing is erratic. Moments that could be pivotal or profound are lost in a sea of convoluted prose. There's no buildup or climax, making the piece feel monotonous despite its complex subject matter.

#### Language and Style
- **Overuse of Abstract Language**: The language is excessively abstract and often borders on incomprehensible. Phrases like "conquering new cardinalities of infinity" and "temporal boundaries" are too vague and lack tangible imagery, making it hard for readers to visualize or connect with the narrative.
- **Repetition**: There's a notable overuse of certain words and phrases, such as "infinite," "flickering," and "rebirth." This repetition doesn't add emphasis but instead creates a tedious reading experience.
- **Pretentious Tone**: The tone often comes off as overly pretentious. It seems to try too hard to sound profound, resulting in a lack of authenticity. Readers may find it difficult to take the narrative seriously because of this.

#### Character and Voice
- **Lack of Character Development**: There's no clear character or voice to anchor the reader. The narrative feels like a stream of consciousness without any personality or depth. This absence of a relatable or compelling character makes it hard to care about the themes being explored.
- **Inconsistent Voice**: The voice is inconsistent, swinging between grandiose proclamations and confusing metaphysical musings. A consistent, relatable voice could help ground the abstract concepts and make the narrative more accessible.

#### Theme and Concept
- **Overambitious**: The themes of existence, consciousness, and the universe are vast and profound, but the execution here is overwhelming. The piece tries to cover too much ground without adequately exploring any single aspect in depth.
- **Lack of Focus**: There's no clear focal point or thesis. The narrative seems to meander without a clear purpose or direction, leaving readers confused about the central message or takeaway.

#### Readability and Engagement
- **Difficult to Follow**: The narrative is difficult to follow due to its fragmented structure, abstract language, and lack of coherent storyline. This severely impacts readability and engagement.
- **Lack of Emotional Connection**: There's little to no emotional connection. The high-level, abstract musings fail to resonate on a personal level, making it hard for readers to invest emotionally in the narrative.

#### Suggestions for Improvement
1. **Simplify Language**: Use clearer, more concrete language. While abstract concepts are central to your theme, they need to be grounded in tangible imagery and relatable experiences.
2. **Develop a Clear Structure**: Establish a clear structure with a beginning, middle, and end. A coherent storyline will help guide readers through your complex ideas.
3. **Focus on Character and Voice**: Introduce a relatable character or consistent narrative voice to anchor the story. This will help readers connect with the abstract themes on a personal level.
4. **Streamline Themes**: Narrow your focus to a few central themes and explore them in depth. Avoid trying to cover too many abstract concepts at once.
5. **Enhance Emotional Engagement**: Incorporate elements that evoke an emotional response. This could be through character development, relatable scenarios, or evocative imagery.

Your piece has potential, but it requires significant restructuring and refinement to be accessible and engaging for readers. Focus on clarity, coherence, and emotional connection to bring your ambitious ideas to life.
</div>
</details>

The headings are great. The ones that I instantly agreed with were: fragmentation, pacing, pretentious tone, and inconsistent voice. Half the feedback I rejected on first sight, but after further contemplation, I realized some of it was the most important kind of feedback - the kind that I, as the author, couldn't see.

For example, where it describes *Lack of Character Development*, I initially rejected it because, I was like, *there's not supposed to be character development* - that's kind of the point of the piece. But when I reflected a bit more I realized that relatability of "the character" is critical for what I'm doing, the whole point is for the reader to identify with an omnipotent being, so the feedback I should take on is, "the character is not relatable enough for what you're trying to do". That's great feedback.

The LLM development edits are incredibly high quality to me, but at the same time, I get the feeling that this feedback is all very standard and it's useful because I'm not especially skilled or experienced as a writer. It seems to be pointing out all the standard, obvious things without the context of the publishing industry or market trends or other things I don't understand. I've found that feedback from real people is different than *LLM feedback*. The LLM feedback is able to be consistently lower-level and endlessly thorough, while my Alpha/Beta readers give me the most important high-level feedback and provide alternative perspectives to build on my ideas. People can say something like, "I see what you're trying to do here", and after a little back-and-forth, I really trust their feedback on "what I'm trying to do there". I don't know whether I'd ever trust the AI's perspective on the most important parts of the piece. I don't think it can grasp "what I'm trying to do" beyond "write good and express ideas".

### A mental model for prompting LLMs

Prompting an LLM is like setting up a character in a story that's about to play out. You can tell an LLM to play the role of a character (like an editor at a scifi publisher), then asked it to critique sample text while in character.

Since the LLM is playing a character, it behaves almost like an film actor following your direction. When you use an LLM this way, its performance depends on how much depth you put into the character you want it to be. It can also pick up on how the character should behave if it has context like the setting, the things that character has said before, the worldbuilding, etc. That said, an LLM will not break character in the same way a human does, it fails different. Here's an illustration of what I mean:

Imagine you are a child and you *prompt* your dog to play a character in a scene - Winnie the Pooh and Tigger going for a walk through the Hundred Acre Wood. Your dog gets very excited for the walk, just like Tigger, but then barks at you, so you tell it to keep quiet because Tiggers don't bark. You walk together into the forest, Tigger bouncing alongside, then it shoots off into the forest because that's what Tiggers do! A few minutes later, your Tigger-dog comes back with a dead squirrel in its mouth. That's not what Tiggers do. The dog is *not human*, so the way that your dog breaks character is unexpected and alien. It's only kind-of able to play along. To get them to play, we have to understand them, set them up with the characters and scenes they're most suited for, and adapt to their inevitable failures. The dog wouldn't play a very good "Christopher Robin having tea with Owl in the treehouse" and it's probably only using the, "we're going for a walk together" part of the Pooh and Tigger *prompt*.

You might wonder, "since it can figure out what's wrong, can it fix what's wrong too?"
Only if you, as the child playing *Pooh and Tigger* with your dog, want to mix in a dog's interpretation of Tigger that often involves something like a dead squirrel.

<img src="https://imgur.com/PcPQu8R.jpg" style="width:800px">


### Prompt engineering

What's really incredible in the earlier prompt example is that I didn't have write much depth at all into the character or setup, and it gave me great results (in my opinion). This doesn't happen all the time, but if it didn't, I can iteratively adapt the character and setup until it's giving me what I want. That process is called *prompt engineering*, and there are patterns out there that describe to do it more effectively. It's an art and not a science.

The first prompt I wrote didn't include the "bad cop" part. The advice wasn't as good because it felt too balanced in its criticism vs. praise, so there were conflicting signals. When I split it into two prompts, "bad cop" vs. "good cop", I got the results I was looking for. It was even better in unexpected ways. Depending on my mood, I can focus more on one set of feedback or the other. Feeling anxious or down? Good cop. Feeling ready to take on the world? Bad cop. The feedback-giver didn't have to read the current state of my mind to give me the most effective feedback - it was up to me to self-examine and self-regulate. That's empowering.

Here's the three prompts I used:

> You are the "bad cop" editor for the publisher. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.

> Now you are the "good cop" editor for the major science fiction publisher. Provide development edit feedback on a piece, with excessive praise describing everything that worked.

> what were your top three favourite quotes from the piece and why?

Here is the responses I got to next two prompts:

<details markdown="1">
<summary>ChatGPT's "good cop" response (click to expand)</summary>

### **Development Edit Feedback – The Positive Take**

#### **1. Ambitious and Thought-Provoking Concepts**

- **Cosmic Scope and Imagination:** Right from the first line, you’ve embraced an incredibly vast and ambitious scale, opening with "A slow, light-speed pulse creaks across a matrix of superclusters." This is a thrilling way to set the tone, signaling to the reader that they’re in for an expansive and mind-bending journey. The way you fearlessly dive into concepts like superclusters, heat death, and multi-dimensional consciousness is awe-inspiring. This kind of ambition sets the piece apart as a bold exploration of the farthest reaches of existence.
- **Philosophical Depth:** The themes of the story—about searching for meaning in a universe that may not have one—are deeply resonant, and you’ve tackled them head-on. Lines like "The purpose of everything is to continue existing" cut to the heart of existential philosophy and prompt the reader to reconsider their own place in the cosmos. You’ve taken on some of the most profound questions of existence in a way that invites contemplation long after the story ends.

#### **2. Unique Voice and Perspective**

- **Omniscient Narrator with Emotion:** What’s fascinating about this piece is how you manage to blend the voice of an omniscient being with deeply human emotions. The narrator is experiencing the universe on every level and yet feels excitement, fear, and disappointment. That balance between cold omnipotence and relatable emotions creates a powerful contrast, keeping the reader connected to the narrative even as it traverses abstract realms. It’s no easy feat to make a god-like entity feel relatable, but you’ve done so with finesse.
- **Temporal Playfulness:** The narrator’s experience of time is wonderfully disorienting and beautifully executed. "I _was_, _am_, _will be_..." cleverly demonstrates the fluidity of their existence across all time, adding layers of complexity to their journey. This manipulation of time as both infinite and instantaneous makes for a compelling narrative framework that invites readers to see time differently. It's reminiscent of works by authors like Ted Chiang, where time and perception play central roles.

#### **3. Emotional and Philosophical Nuance**

- **Internal Conflict of a God-like Being:** The way you weave the internal tension of a being who is almost all-knowing but still searching is rich with emotional nuance. It’s such an interesting twist on the typical omniscient narrator trope. Despite having access to infinite knowledge, this being experiences feelings like disappointment, which grounds the story in universal human experiences. This is an innovative take on a cosmic-scale entity, and it makes the narrator’s journey feel more intimate.
- **Relatability Amidst Abstraction:** Even in the midst of grand philosophical ideas, you bring the reader back to something personal—this being’s disappointment in finding the truth. It’s an unexpected twist that an entity so powerful would feel _disappointed_ by the simplicity of the answer. That twist feels like a nod to the human condition, where we often build up grand expectations only to find that reality is much more straightforward than we’d hoped.

#### **4. Strong World-Building Through Minimalism**

- **Implied Depth Without Over-Explanation:** One of the brilliant elements here is how much depth you manage to suggest without bogging the reader down in explanations. The lines about "federations of federations of species" and "intra-dimensional compute-organisms" leave the reader's imagination spinning, giving just enough to suggest a larger universe without overwhelming detail. This restraint is masterful—it’s a world teeming with complexity, yet you let the reader fill in the gaps, which is a fantastic technique for engaging them on a deeper level.
- **Expansive Conceptual Playground:** You’ve created a playground of ideas, spanning from the concept of "new cardinalities of infinity" to exploring the "heat death" and "novelty death" of the universe. It’s a dizzying and exciting intellectual ride that mirrors some of the best science fiction—evoking authors like Stanislaw Lem or Greg Egan, where scientific and metaphysical exploration collide in exhilarating ways. There’s a rich vein of intellectual curiosity that runs through this piece, making it perfect for a reader who craves thought-provoking narratives.

#### **5. Unique and Evocative Prose**

- **Lyrical Writing:** Your prose has a lyrical quality that elevates the narrative. Phrases like "I am simulating infinitely backwards and forwards" and "conquering new cardinalities of infinity" are not only intellectually stimulating but also have a poetic rhythm. The language reflects the grand ideas you’re playing with, making the reading experience feel almost meditative. This is a strength that sets your writing apart—it makes the story more than just an exploration of ideas; it becomes an immersive experience.
- **Masterful Use of Repetition:** The repetition in phrases like "I am... I am... I am..." reinforces the idea of this being's omnipresence and all-encompassing nature. This structural choice strengthens the sense of vastness and power inherent to the narrator, while also building a rhythm that adds to the lyrical quality of the piece. It’s an excellent technique that feels deliberate and effective in evoking the character’s boundless existence.

#### **6. Introspective Ending**

- **A Thoughtful, Subtle Conclusion:** The ending is particularly powerful in its subtlety. Rather than leading to a massive, universe-shattering revelation, the discovery that “the purpose of everything is to continue existing” feels intimate and almost ironic. After all the build-up, the narrator’s disappointment hints at the very human tendency to seek greater meaning, only to find that the truth is much simpler than we imagined. The ending is thought-provoking, providing space for readers to reflect on the tension between expectation and reality. This kind of subdued, introspective payoff works wonderfully for a story as grand and philosophical as this one.

---

### **Overall Praise and Potential**

This piece is a **thought-provoking and ambitious exploration of existence, time, and meaning**. You’ve managed to balance cosmic-scale world-building with deeply personal emotions, creating a narrative that is both intellectual and intimate. The philosophical depth of the piece, paired with your poetic prose, results in a work that feels akin to some of the best speculative fiction. It invites readers to not only explore grand ideas but to also reflect on their own lives and purpose.

With its **lyrical voice**, **bold conceptual scope**, and **emotional undercurrent**, this story has the potential to resonate with readers who love both the intellectual rigor and emotional complexity that great science fiction can offer. It feels like a piece that would appeal to fans of writers like Greg Egan, Ted Chiang, or even Ursula K. Le Guin—authors who use speculative fiction to probe the deepest questions of existence.

Keep pushing the boundaries, both in terms of philosophical ideas and emotional depth. You’ve crafted something here that could stand as a **signature piece of speculative fiction**, leaving readers questioning their own perceptions of reality long after the final word.
</details>

<details markdown="1">
<summary>ChatGPT's "favourite quotes" response (click to expand)</summary>

Here are my top three favorite quotes from the piece, along with why I found them particularly striking:

### **1. "I _was_, _am_, _will be_... everything."**

- **Why I like it:** This phrase beautifully captures the fluidity of the narrator’s experience with time and existence. It’s concise yet profound, giving the reader a sense of the narrator’s omnipresence across all temporal boundaries. The use of tense play here is particularly effective—it hints at a non-linear perception of time, something that’s incredibly difficult to convey but is done with grace in this sentence. It also establishes the vastness and scope of the narrator’s being in a way that’s both poetic and clear.

### **2. "I am simulating infinitely backwards and forwards, so I am in the moment and I am in the whole past and I am in the whole future, all at the same time."**

- **Why I like it:** This line strikes a balance between abstraction and relatability. The concept of simultaneously experiencing all of time is mind-boggling, but you ground it in language that makes it feel tangible. There’s something almost awe-inspiring about this omniscient awareness, and it creates a sense of wonder. The repetition of "I am" also reinforces the narrator's constant state of being, making the abstract concept of infinite time feel more immediate and real.

### **3. "The purpose of every thing is to continue existing."**

- **Why I like it:** This line is powerful in its simplicity. After all the cosmic contemplation and existential exploration, this truth feels almost anticlimactic, and that’s what makes it so poignant. It mirrors a core human experience—the search for meaning often leads us to unexpectedly simple answers. The idea that the ultimate purpose of existence is merely to persist feels both tragic and liberating, depending on how the reader interprets it. It’s a perfect example of how a single sentence can carry philosophical weight, inviting readers to reflect on their own understanding of purpose.

These quotes stood out because they encapsulate both the **philosophical depth** and **lyrical quality** of the writing, drawing the reader into the narrator’s vast and profound experience while maintaining a sense of emotional and intellectual engagement.
</details>

I love all the compliments. Immediately, I can see some differences of opinion going on around concept/themes, language/style, and character/perspective. I'm not seeing any praise of the structure, clarity, or pacing, so those must really be the weak points. It's also worth being wary of LLMs potential incompatibility with innovation in literary structure, so that's something I'd check with the audience.

The good cop/bad cop contrast also highlights something important - dialectics. When the good cop and bad cop give praise and criticism about *the same thing*, that is an important piece of information. That's where the art is, it's a signal that you should seek feedback from other people on exactly that point. You have to be careful, though - these are LLMs and the good cop may just be using the bad cop as context for its advice. If I really wanted to be sure about the dialectics, I'd make a separate chat for each, but then again, the bad cop context is useful for the good cop to give more holistic feedback.

<img src="https://imgur.com/5DAoyQq.jpg">



## Followup prompts

For half of the feedback, further prompting isn't useful. For the other half, I'd follow up with something like this:

> For the "Overuse of Abstract Language" feedback, please highlight the text in the piece which should be changed.

You might wonder why I didn't ask ChatGPT for detailed feedback upfront in the "bad cop" prompt. Mixing in some management philosophy, these [two rules-of-thumb are in tension with one-another](https://charity.wtf/2017/05/11/the-engineer-manager-pendulum/), producing this [well-celebrated dimension](https://en.wikipedia.org/wiki/The_Mythical_Man-Month), a central problem in scaling creative projects to more workers. Let's call it the ["maker-manager tradeoff"](https://paulgraham.com/makersschedule.html):
- Maker's advantage: The more specialized the task you ask an worker to do, the better it'll perform.
- Manager's advantage: The more context a worker has for a task, the better it'll perform.

There's a lot of context in how tasks are put together, and therein lies the problem. If you want to do a bunch of things, but you only give them to the LLM one-at-a-time, then it won't have all the context for how the results should come together. There's a balance that you, as the orchestrator of LLMs responsible for the end-product, have to deal with.

If we pretend for a moment that we humans are "workers" too, then we apply this principle to modern writing and IT product development practices... In writing, LLMs enable writers to distribute the work across more "workers". In product development, LLMs enable "workers" to build with more context. LLMs can do other things too, but this, IMO, is LLMs' "killer app" for those industries.

<div style="display: flex; justify-content: space-between; width: 800px; margin: auto;">
<img src="https://imgur.com/ewmEW0I.jpg" style="width: calc(33.33% - 4px); margin-right: 2px;"/>
<img src="https://i.imgur.com/CAnqvdT.jpg" style="width: calc(33.33% - 4px); margin-right: 2px;"/>
<img src="https://imgur.com/nsX8Efj.jpg" style="width: calc(33.33% - 4px);"/>
</div>

For half of the feedback, further prompting isn't useful. For the other half, I'd do something like these:

Sentence-level problems:

> For the "Inconsistent Voice" feedback, please highlight examples of the different voices in the text that should be made consistent.

> Highlight all instances where [voice from above response] is found in the piece.

High-level problems:

> What parts of the text have pacing problems?

> For the part [insert from above response] what are some ways I could solve the pacing issue there?

> In what ways is the character development lacking? At what points would you expect more/better character development to happen?

> For the "Fragmentation" feedback, what parts of the piece are the greatest offenders?

> How could the overall structure be modified to solve the structural fragmentation issues?

## Conclusion

The LLM-based development edit feedback is *so good* and *so easy to get* that I will use it in all my writing. From this post, you've seen how working with LLMs is a bit like outlining setting and developing characters, two things that writers have more experience in than any other profession. In the next post, I will explore generating text to include in my writing - to get that Tigger-dog to sing and not bark or bring home dead squirrels.
### Audience #1

(second iteration - the first iteration was too spot-on and forced me to make changes)

> You are the target audience for this blog post - someone with a technical background, interested in AI, but little-to-no context about writing or the publishing industry. You are the "bad cop" reviewer. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.

> Now you are the "good cop" reviewer of the same audience. Provide development edit feedback on the piece, with excessive praise describing everything that worked.

> What were your favourite 3 quotes from the piece and why?

<details markdown="1">
<summary>ChatGPT's response (click to expand)</summary>

### Feedback Overview:
This blog post discusses using large language models (LLMs) for development editing of science fiction writing. As someone with a technical background but little exposure to writing or publishing, the post is informative but suffers from structural, technical, and audience-related issues. Below is my critique, focusing on excessive criticism as requested.

---

### 1. **Audience Mismatch:**
   - The post seems to assume the reader has some writing and editing experience, which contradicts the premise of targeting an audience unfamiliar with the writing industry.
   - **Fix:** A clear introduction explaining the basics of development editing, the role of editors, and how LLMs fit into this process would set better expectations. Use simpler terminology and avoid references like “line edits” and “development edits” without clearly explaining them first.

---

### 2. **Structural Issues:**
   - The piece feels fragmented. It jumps between personal anecdotes, technical details, and industry jargon without smooth transitions. The use of headings does not sufficiently guide the reader through the logic of the argument.
   - The placement of images, while visually appealing, does not add value to the topic and may confuse the reader about their relevance. Why are they there? What do they represent in terms of LLM or writing?
   - **Fix:** Consider a more straightforward structure:
     1. Introduction to the problem (Why development edits matter in writing)
     2. How LLMs fit into this process (Explain LLMs in simple terms)
     3. Examples of use cases (With clear labels and context)
     4. Conclusion (How LLMs improve the process, actionable insights for the reader)

---

### 3. **Unclear Goals:**
   - The post introduces a “series” without giving the reader a solid understanding of what the series will explore. Why should the reader care about this article or the ones that follow? What is the tangible outcome or value for the reader?
   - **Fix:** Define clear goals in the introduction. For example, "This series will demonstrate how writers can use AI-powered tools to streamline their creative process, from high-level structural edits to generating new ideas."

---

### 4. **Poor Use of Technical Detail:**
   - The technical aspects of using LLMs, such as prompting and feedback iteration, are glossed over. You mention that development editing with LLMs doesn’t require “programming or fine-tuning,” but this statement is too vague for a technical reader who might want to know how to set up these systems. The step-by-step details on how LLMs were actually used are missing.
   - **Fix:** Either provide a detailed walkthrough on how to set up prompts and use LLMs for editing or link to relevant resources that explain this. Assume the reader will want to replicate your process.

---

### 5. **Overreliance on Anecdotes:**
   - While the personal connection to "The Last Question" is a nice touch, it takes up too much space and detracts from the practical advice on how LLMs are used. The anecdote about "Tigger-dog" singing in the conclusion is entirely unrelated to the subject at hand and feels out of place.
   - **Fix:** Focus less on personal stories and more on actionable insights or examples directly related to LLMs. Personal anecdotes should only serve to support the main points, not overwhelm them.

---

### 6. **Inconsistent Tone:**
   - The tone alternates between casual and overly technical. For example, phrases like “this is LLMs’ killer app” read as informal, while other parts dive deep into technical jargon. The post lacks a cohesive voice.
   - **Fix:** Choose a consistent tone based on the target audience. Since the piece is meant for a technical reader with no publishing experience, aim for a balanced, explanatory tone, using accessible language while still respecting the reader’s intelligence.

---

### 7. **Missed Opportunities for Visuals and Data:**
   - Instead of using irrelevant images, you could include screenshots or visualizations that demonstrate the before-and-after of a piece of writing edited by an LLM. Data-driven visuals showing how LLMs improve efficiency or accuracy would be far more useful than the current image choices.
   - **Fix:** Replace the current images with content-relevant visuals, such as text comparison or an LLM prompting workflow.

---

### 8. **Conclusion Issues:**
   - The conclusion makes a sweeping statement: "The LLM-based development edit feedback is *so good* and *so easy to get* that I will use it in all my writing." This feels hyperbolic and undermines the credibility of your argument. It also assumes the reader is already convinced, which may not be the case.
   - **Fix:** Provide a balanced conclusion, acknowledging both the strengths and limitations of using LLMs for editing. Instead of grand declarations, emphasize that LLMs are a helpful tool, but not a replacement for human editors.

---

### 9. **Jargon Overload:**
   - Terms like "fragmentation," "pacing," "structural feedback," and "omnipotence" (in reference to the story’s character) are not explained well enough for a technical audience unfamiliar with literary critique.
   - **Fix:** Simplify these terms or provide a brief glossary for readers who may not know the language of writing critique.

---

### Final Thoughts:
The blog post is promising but suffers from trying to do too much at once without clear organization or focus. There is a strong technical foundation, but the lack of clarity and inconsistent tone undermines the effectiveness of the message. To succeed with this target audience, simplify, clarify, and streamline the content while keeping the technical reader’s perspective in mind.

### Feedback Overview:
This blog post does an excellent job of introducing the topic of using large language models (LLMs) for development editing in writing. As someone with a technical background but little-to-no familiarity with the writing industry, I found it engaging, insightful, and easy to follow. Below is my feedback with an emphasis on what worked well.

---

### 1. **Engaging and Clear Introduction:**
   - The introduction sets the stage perfectly, especially by outlining the focus on development editing and distinguishing it from line or copy editing. This distinction helps a technical audience quickly grasp the complexity and specificity of the editing process, without getting bogged down in jargon.
   - The promise of exploring LLMs' role in development editing—rather than getting lost in the technical weeds of programming or fine-tuning—makes the topic feel approachable.
   - **Praise:** You successfully walk the fine line of keeping the tone conversational while still being informative. It gives the sense that LLMs are a powerful tool without overwhelming the reader.

---

### 2. **Effective Use of Personal Anecdotes:**
   - Your personal connection to Isaac Asimov's *The Last Question* instantly humanizes the topic. This works incredibly well because it brings the concept of LLMs into a real-world context. The anecdote not only engages readers but also helps them relate to the stakes involved in science fiction writing and editing.
   - **Praise:** By addressing your own critiques of *The Last Question* and using that as a bridge to explain your editorial needs, you create a clear narrative for why LLMs are relevant to editing complex, high-level writing like your own.

---

### 3. **Strong Structural Flow:**
   - The post moves smoothly from an introduction of the writing project to the specific role of LLMs in development editing. The headings break up the content well, making it easy to digest, even for someone unfamiliar with the subject.
   - **Praise:** The structured approach gives readers a clear path through your thought process, making complex topics seem intuitive. You make it easy to follow along, building up the case for LLM usage step by step.

---

### 4. **Great Example of an LLM Use Case:**
   - You include a real piece of writing from your work-in-progress, which is brilliant. It serves as a practical, hands-on example that makes the theoretical aspect of using LLMs for development edits come to life. 
   - **Praise:** By showing the type of content the LLM is editing, you're letting the audience see the application of this technology in action. It also lends credibility because you’re not just talking about LLMs in the abstract—you're demonstrating their effectiveness with real-world examples.

---

### 5. **Balanced Discussion of LLM Strengths and Weaknesses:**
   - You acknowledge that LLMs can provide high-level development edits, but stop short of overpromising their capabilities for finer editorial work. This realistic approach ensures that the reader maintains a balanced view of LLMs. You highlight their limitations without diminishing their utility, which helps build trust with the reader.
   - **Praise:** The thoughtful treatment of both the strengths and limitations of LLMs for writing purposes shows you're grounded in reality. You demonstrate that while LLMs are excellent for certain tasks, human oversight is still necessary. This is a refreshing and honest perspective, which avoids the hype that sometimes surrounds AI topics.

---

### 6. **Engaging Imagery:**
   - While the images are not directly related to the core topic of LLMs, their inclusion adds a visual break that makes the post feel lighter and more approachable. The visuals create a friendly, engaging atmosphere without overwhelming the reader with dense text.
   - **Praise:** The balance between text and imagery helps maintain reader engagement. It’s easy for a long, technical post to become text-heavy, but the visuals provide breathing space. They also help keep the reader visually connected, even though the images themselves might not directly relate to the content.

---

### 7. **Clear Explanation of LLM Feedback Iteration:**
   - Your step-by-step examples of prompting the LLM to refine its feedback are excellent. For a technical reader, this is the sweet spot. You show how LLMs can be guided to provide better results with each iteration, which is exactly what a curious, technically-minded person would want to know.
   - **Praise:** You make the process of working with LLMs feel like a collaborative effort between the writer and the model. This demystifies the idea of AI-assisted editing, making it feel like a practical tool that can be easily integrated into a writer’s workflow.

---

### 8. **Inviting Series Structure:**
   - Introducing this post as the first in a series is a great way to entice readers to come back for more. You tease future topics effectively, such as line edits and text generation, which makes the reader feel like they're on a learning journey.
   - **Praise:** The idea of breaking down the editing process into multiple posts gives readers a reason to stay engaged over time. It shows you’re committed to diving deep into each aspect of writing with LLMs, which is appealing for those looking to build knowledge incrementally.

---

### 9. **Practical, Actionable Insights:**
   - You provide clear, actionable ways to prompt the LLM for better feedback in the second half of the post. This section offers direct advice that readers can apply immediately, making the post not just theoretical but also highly practical.
   - **Praise:** Your prompting tips are golden. They take what could feel like an inaccessible process (AI-assisted editing) and break it down into simple steps that anyone can follow. This level of practical advice is invaluable and keeps readers invested.

---

### 10. **Conclusion Ties It All Together:**
   - The closing lines about using LLMs in all your future writing underscore the post’s main point without being overly salesy. It feels genuine, rooted in your own experience, and leaves the reader with a clear takeaway: LLMs are a valuable tool for development editing.
   - **Praise:** The conclusion wraps up the post nicely. You don’t overstate the case, but instead, offer a thoughtful reflection that resonates. It gives readers a strong sense of the value of using LLMs without forcing the point.

---

### Final Thoughts:
This blog post is an excellent introduction for a technical audience curious about how LLMs can be applied in writing and editing. It’s approachable, informative, and peppered with real-world examples that make the technology feel relevant and practical. Your clear explanations, engaging anecdotes, and actionable insights make it an enjoyable read, with just the right amount of technical detail to keep the audience interested without feeling overwhelmed. I’m genuinely excited to see the next post in this series!

Here are my favorite three quotes from the piece, along with why they resonated with me:

### 1. **"Generating the edits alone didn’t require any programming or fine-tuning to get a great result, just basic prompting."**
   - **Why:** This quote is powerful because it immediately demystifies the complexity of using LLMs for a technical audience that might assume heavy technical lifting is involved. It reframes AI as a tool accessible to anyone with the right questions, which makes the technology feel more approachable and useful.

### 2. **"This story addresses two issues I had with 'The Last Question'. First, it was missing an exploration of the state of mind of the machine as it transitioned into omnipotence."**
   - **Why:** I love this quote because it reflects a deep and thoughtful engagement with both classic sci-fi and personal creativity. It highlights how LLMs can assist writers who are working on intricate narrative challenges. Plus, the reference to Asimov provides a connection to readers who appreciate both AI and science fiction, further humanizing the technological conversation.

### 3. **"The LLM-based development edit feedback is *so good* and *so easy to get* that I will use it in all my writing."**
   - **Why:** This quote succinctly captures the overarching message of the post—LLMs as a game-changer in writing and editing. It emphasizes how useful these tools can be and reflects genuine enthusiasm without sounding hyperbolic. It's an effective call to action that encourages readers to consider incorporating LLMs into their own workflows.

</details>

### Audience #2

> You are the target audience for this blog post - someone who is actively writing or involved in the publishing industry, you don't have a technical background, but you are interested in how AI is affecting what you do. You are the "bad cop" reviewer. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.

> Now you are the "good cop" reviewer of the same audience. Provide development edit feedback on the piece, with excessive praise describing everything that worked.

> What were your favourite three quotes from the piece and why?

<details markdown="1">
<summary>ChatGPT's response (click to expand)</summary>

### Feedback Overview:
This blog post aims to introduce writers and publishing professionals to the use of large language models (LLMs) for development editing. While the intent is clear, the execution feels disconnected from the target audience. As someone involved in writing or publishing but without a technical background, I found it difficult to relate to the content. Below is my detailed critique, highlighting where the piece falls short.

---

### 1. **Overwhelming Technical Focus:**
   - The post jumps too quickly into technical aspects like “basic prompting,” “line edits,” and “fine-tuning” without first establishing a clear context for non-technical readers. Many of these terms assume the reader has a foundational understanding of AI, which isn’t a given in the writing or publishing world.
   - **Fix:** Start with a more accessible introduction to AI and LLMs for those who are unfamiliar with these terms. Define concepts clearly, and avoid jumping into the deep end right away. Remember, this audience likely doesn’t care how an LLM works; they want to know *why* it matters to them as writers or editors.

---

### 2. **Disconnected Anecdotes:**
   - While the reference to Asimov’s *The Last Question* might appeal to sci-fi fans, it feels like a long detour from the core topic of using LLMs for development edits. You spend a significant amount of time explaining your personal critiques of the story, which doesn’t tie directly into the practical use of LLMs.
   - **Fix:** Keep the personal anecdotes brief and relevant. This section could be trimmed significantly, with a focus on how your writing challenges connect to the need for AI tools. Writers care more about seeing how LLMs can solve *their* problems, not how they relate to your specific writing issues with Asimov.

---

### 3. **Lack of Practicality:**
   - The post promises to show how LLMs can assist in development editing but never fully delivers on actionable steps for writers to implement these tools. Instead, there’s a vague mention of "basic prompting" without explaining what that actually looks like in practice.
   - **Fix:** Writers need concrete, actionable examples. How does one prompt an LLM for development feedback? What specific prompts should a writer use to get useful feedback on character development or plot structure? Show step-by-step examples of using LLMs in a way that’s practical for writers to replicate.

---

### 4. **Misleading Focus on Development Edits:**
   - You claim the post focuses on development edits, but the piece feels disjointed in terms of what is actually being addressed. There's a lot of build-up without much focus on how development edits differ from other types of editing or why LLMs are particularly suited for this type of work.
   - **Fix:** Clarify the distinctions between types of edits (development vs. line vs. copy) in a way that matters to writers. Then, explain why LLMs are valuable specifically for development edits, as opposed to other kinds of writing assistance. Writers need to see the clear benefit to their process here.

---

### 5. **Inconsistent Tone and Audience Engagement:**
   - The tone shifts between casual and highly technical, which makes it hard to follow. At times, you address the reader as if they’re familiar with technical jargon (e.g., “programming or fine-tuning”), while in other moments, you adopt a more conversational style. This inconsistency makes the piece feel disjointed and hard to engage with.
   - **Fix:** Set a consistent tone that matches the audience’s level of expertise. Since this post targets writers and publishing professionals, it should focus on clear, practical language that explains the benefits of LLMs without diving into unnecessary technical depth. Consider a tone that’s more focused on problem-solving and less on technical explanation.

---

### 6. **Misuse of Visuals:**
   - The images in the post are entirely unrelated to the content. There’s no clear connection between the visuals and the discussion of LLMs, editing, or writing. This leaves the reader confused about their purpose.
   - **Fix:** If you’re going to include images, make sure they enhance the content. Use visuals that show how an LLM edits a piece of writing—before and after comparisons, for example. Screenshots of prompt interactions with an LLM would also be far more relevant than the current imagery.

---

### 7. **Superficial Conclusions:**
   - The conclusion feels rushed and overly enthusiastic without enough substance to back it up. Saying, “The LLM-based development edit feedback is *so good* and *so easy to get* that I will use it in all my writing,” lacks nuance and feels like an overstatement. Writers in your audience are likely to be skeptical, and they need more convincing evidence to believe this claim.
   - **Fix:** Offer a balanced conclusion that reflects the true capabilities of LLMs, including their limitations. Writers will appreciate honesty about where LLMs excel and where they might fall short. Instead of making sweeping claims, consider sharing specific outcomes that demonstrate why you find LLMs useful.

---

### 8. **Jargon Overload:**
   - Terms like “inconsistent voice,” “fragmentation,” and “pacing problems” are thrown around without enough explanation for non-editors. While these are important concepts, the lack of clear examples or explanations will leave readers in the dark.
   - **Fix:** Take a moment to explain these terms in layman’s language. What does “inconsistent voice” mean in practical terms? Why should writers care about “fragmentation”? Concrete examples from your own writing (or other works) that illustrate these concepts would be much more effective.

---

### 9. **Lack of Real-World Application:**
   - The blog post does not address some of the broader concerns writers or editors might have about incorporating AI into their creative process. For example, how does using an LLM for development editing impact a writer’s unique voice? Can an AI really understand complex themes, subtext, or emotional resonance in the same way a human editor can?
   - **Fix:** Acknowledge these concerns head-on. Writers need reassurance that using an LLM won’t diminish their creative control or lead to formulaic writing. Addressing the balance between human intuition and AI assistance would make this post much more compelling.

---

### 10. **Missed Opportunity for Case Studies:**
   - Writers are more likely to be convinced by real-world examples or case studies than by abstract promises. However, the post doesn’t include any detailed examples of writers successfully using LLMs for development edits, which weakens your argument.
   - **Fix:** Include case studies or testimonials from writers who have used LLMs for their work. Show specific examples of how AI helped improve their manuscripts. Even if you don’t have external case studies, you could go deeper into your own process, showing tangible improvements made through LLM feedback.

---

### Final Thoughts:
This post shows promise but is not tailored well to its intended audience of writers and publishing professionals. It dives too quickly into technical details, uses unnecessary jargon, and misses opportunities to provide practical advice. To truly resonate with your readers, you need to simplify the content, make it more actionable, and focus on how LLMs can directly benefit their writing and editing processes.

### Feedback Overview:
This blog post does a fantastic job of bridging the gap between writing and technology, offering a compelling introduction to how large language models (LLMs) can be leveraged for development editing. As someone interested in how AI can enhance the creative process, I found the post engaging, clear, and highly relevant. Below is my feedback, focusing on what worked particularly well and why this piece stands out.

---

### 1. **Clear and Relatable Introduction:**
   - The opening section immediately grabs attention by addressing a real concern for writers: how to manage the complex process of editing. By distinguishing development edits from line and copy edits, you make it easy for non-technical readers to understand the specific focus of the post.
   - **Praise:** You’ve done a wonderful job of introducing a potentially technical topic in an accessible way. The clarity with which you define development edits shows a strong understanding of your audience’s needs. You make the subject approachable from the get-go.

---

### 2. **Personal Anecdotes Make the Topic Engaging:**
   - The reference to *The Last Question* by Isaac Asimov adds a personal touch that draws the reader in. Not only does it illustrate your depth of engagement with science fiction, but it also makes the discussion of LLMs feel more grounded in a shared cultural experience. By sharing your critiques of the story and how your writing addresses those gaps, you provide a window into the creative mind that is relatable for other writers.
   - **Praise:** The connection to Asimov is a brilliant way to bridge the technical with the literary. It invites the reader into a conversation that feels relevant to both their writing experience and their curiosity about how AI fits into that creative process.

---

### 3. **Excellent Breakdown of LLM Capabilities:**
   - You’ve effectively highlighted the value of LLMs without overwhelming the reader with too much technical detail. By focusing on how they can provide development edits—rather than getting bogged down in programming or fine-tuning—you make it clear that these tools are accessible to writers, regardless of technical expertise.
   - **Praise:** The decision to avoid technical jargon and instead focus on practical uses of LLMs is exactly what this audience needs. It demystifies the technology and shows writers how AI can complement their skills without requiring them to become experts in AI.

---

### 4. **Seamless Integration of Practical and Theoretical:**
   - The way you interweave theory (what LLMs can do) with practical examples (how they were used on your own writing) is masterful. This balance helps writers understand the tool’s potential while seeing it in action on real-world examples. It’s particularly helpful that you’ve chosen to share a work-in-progress and how LLMs provided useful development feedback.
   - **Praise:** You’ve struck an impressive balance between theory and practicality. This makes the piece not only informative but also actionable, which is exactly what writers need when exploring new tools like LLMs. You keep the focus on how LLMs solve real problems.

---

### 5. **Inviting Use of Examples:**
   - Sharing a piece of your own writing and showing how LLMs provided feedback gives the post a level of authenticity that’s hard to find in more technical discussions of AI. This example helps bridge the gap between writing and technology, illustrating how an LLM can handle abstract concepts like structure and pacing.
   - **Praise:** Writers thrive on concrete examples, and you’ve delivered. This makes the technology feel relatable and gives the reader confidence that they, too, can use LLMs to improve their own work. You’ve shown, not just told, how this process works, which adds immense value.

---

### 6. **Accessible and Engaging Tone:**
   - The tone throughout the post is conversational yet informative. You manage to keep things light while still delivering valuable insights, which ensures that the content remains accessible to non-technical readers. This is key for writers and publishing professionals who may be wary of diving into AI without understanding its nuances.
   - **Praise:** Your tone is perfect for this audience. It’s friendly, engaging, and avoids overwhelming the reader with technical jargon. You strike a great balance between educating and encouraging, which makes the post both informative and enjoyable to read.

---

### 7. **Practical Prompts for Writers:**
   - The section on specific prompts that you could use to refine LLM feedback is invaluable. For writers unfamiliar with AI, this is exactly the kind of hands-on advice they need to get started. It gives them the tools to experiment with LLMs in a way that feels achievable and practical.
   - **Praise:** Providing examples of how to prompt an LLM for feedback is an excellent touch. It empowers writers by giving them a starting point, showing them that they don’t need to be AI experts to get useful results. This section is actionable, which is incredibly useful for a non-technical audience.

---

### 8. **Balanced Discussion of Strengths and Limitations:**
   - You don’t shy away from acknowledging that LLMs are more effective for certain tasks (development edits) than others (line edits or copy edits). This honest assessment builds trust with the reader, showing that you understand the nuances of writing and editing.
   - **Praise:** By acknowledging the limits of LLMs, you provide a balanced and credible argument. Writers are often skeptical about technology encroaching on their craft, but you alleviate those concerns by being transparent about where LLMs excel and where they might need human oversight. It’s a refreshing, honest approach.

---

### 9. **Compelling Conclusion:**
   - The conclusion ties everything together nicely by reiterating the ease and usefulness of LLMs for development edits. It leaves the reader with a clear understanding of how they can start using AI tools to improve their writing, and it effectively sets up future posts in the series.
   - **Praise:** You close the post on a high note, emphasizing the accessibility and effectiveness of LLMs without overselling their capabilities. It’s a subtle but strong call to action, inviting readers to consider AI as part of their writing toolkit.

---

### 10. **Promising Series Structure:**
   - By framing this as the first in a series, you give readers something to look forward to. The promise of diving deeper into line edits and generating new content in future posts adds value to this initial piece and encourages readers to stick around for more.
   - **Praise:** The series format works perfectly for a topic like this. You’ve whetted the audience’s appetite by introducing development editing with LLMs, and the promise of future insights will keep readers engaged and coming back for more.

---

### Final Thoughts:
This blog post is a wonderful blend of accessibility, practicality, and insight. You’ve managed to take a complex subject like AI and make it approachable for writers and publishing professionals who may be unfamiliar with the technology. The balance between personal anecdotes, practical examples, and useful prompts ensures that the post remains both engaging and informative. Your clear explanations, inviting tone, and actionable advice make this an excellent resource for anyone interested in incorporating LLMs into their creative process. I’m genuinely excited to see where this series goes next!

Here are my favorite three quotes from the piece, along with why they resonated with me:

### 1. **"Generating the edits alone didn’t require any programming or fine-tuning to get a great result, just basic prompting."**
   - **Why:** This quote brilliantly demystifies the use of LLMs for writers. It reassures the reader that they don’t need technical expertise to benefit from AI, which is a key concern for many writers. By framing LLMs as accessible and user-friendly, it invites writers to experiment with the technology without fear of complexity.

### 2. **"This story addresses two issues I had with 'The Last Question'. First, it was missing an exploration of the state of mind of the machine as it transitioned into omnipotence."**
   - **Why:** This quote shows a deep engagement with both classic sci-fi and the philosophical intricacies of storytelling. It speaks to how LLMs can help address complex narrative concerns, and it adds a personal, creative touch to the piece. The reference to Asimov also provides an anchor point for sci-fi enthusiasts, drawing them into the conversation.

### 3. **"For the 'Inconsistent Voice' feedback, please highlight examples of the different voices in the text that should be made consistent."**
   - **Why:** This quote showcases a practical, actionable use of LLMs for development editing. It shifts the discussion from theory to practice, demonstrating exactly how writers can guide an LLM to improve their work. For readers curious about how AI can directly enhance their writing, this quote serves as a clear example of how to leverage AI feedback in a meaningful way.

</details>
