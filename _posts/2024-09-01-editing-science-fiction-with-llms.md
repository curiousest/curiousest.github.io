---
layout: post
title: How writers will dominate in a world of LLMs (part 1)
date: 2024-09-01T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - projects
  - story
modified_time: 2024-09-01T00:00:00.001-05:00
---
I find writing to be a lot like building. It's the most human form of building, where you get to choose how much reality to include in your construction. The culture of writing is as old as civilization but it's still developing, ever-changing, while the culture of building IT products is new and the focus of much innovation. The culture of building IT products can learn quite a lot from the culture of building stories, and vice-versa.

There are so many external tools build IT products, while there are so few external tools to build stories. All the best writing tools are stored in minds, education systems, and the corpus [actually trained on a small subset] of humankind's text data - that corpus of data which LLMs happen to be trained on. I believe that LLMs can help externalize and democratize those tools-in-mind, unlocking new possibilities, and so a future that relies on LLMs is one where the writing skillset becomes more valuable and not commoditized. Writing something worth reading is *not* something that can be automated but it can be *augmented*. That comes with good and bad changes - the publishing industry has to figure out how to deal with the pollution and piracy that have come with these new AI tools. But I think the publishing industry will evolve, the future of writing is bright, and this post is a techno-optimist glimpse into what that could look like without the extreme takes:
- "doomer" (AI will destroy the industry and then ruin humankind)
- or "AI messianist" (quit your job, join my cult, make way for divine AI disruption)

This post contains:
1. A mental model for automating parts of the writing process.
2. A sample that will be "edited" by LLMs (a draft scifi short story from my book).
3. Basic prompts and my reaction to the feedback.
4. How I followed up with prompts to solicit more feedback.
5. My comparison of different LLM providers.

I'm writing this because I'm an AI engineer [on a sabbatical](2024-02-16-philosophy-study), [studying philosophy](2024-07-20-microsoft-google-and-strawberry-liquorice) and writing my first book. The novel I'm writing is sci-fi philosophy and now that I've finished a readable draft (sans-LLMs), I've been experimenting with LLMs as a tool in my writing process. I'm writing this post for peers in the tech industry and writers. So to me, this post is a little marketing, some personal exploration of AI industry tech, and a lot of fun.

I will post more technical followups on this topic. If you want to follow the next posts in the series or catch updates on my book:
- [LinkedIn](https://www.linkedin.com/in/dhindson/)
- [Email newsletter](https://curiousest.ck.page/437b446194)
- [X/Twitter](https://x.com/minviablpurpose)
- [TikTok](https://www.tiktok.com/@minimumviablepurpose)
- [Facebook](https://www.facebook.com/profile.php?id=61564237665611)
## What part of the writing process to automate with LLMs?

This is an outline of a standard writing process that every writer will recognize:

1. Come up with an idea of what to write.
2. Validate the idea.
3. Write an alpha first draft (an early work-in-progress).
4. Review to find big problems in the alpha draft.
5. Write a good first draft.
6. Review to find big problems in the good first draft ("development edits" and/or "beta readings" - plot, characters, worldbuilding, themes).
7. Write to resolve the development edit problems.
8. Review to find smaller problems in the second draft ("line edits" and/or "beta readings" - flow, consistency, clarity).
9. Write to resolve the line edits.
10. Review to find tiny problems in the second draft ("copy edits" - grammar, spelling, formatting).
11. Resolve the copy edits.

The further down that list you go, *the easier it is to automate*. That means the more "human" tasks are higher up. That doesn't mean anything can be completely automated - we've had spellchecks forever and grammar checkers for a long time now, but copy editing still isn't completely automated. Most books on any bestseller list would have had someone paid to perform a copy edit.

<div class="row" style="display:flex">
  <div class="column" style="padding:2px">
    <img src="https://i.imgur.com/VBdni8A.jpg"><br/>
  </div>
  <div class="column" style="padding:2px">
    <img src="https://i.imgur.com/8NV47hS.jpg"><br/>
  </div>
  <div class="column" style="padding:2px">
    <img src="https://i.imgur.com/XAHZg8e.jpg"><br/>
  </div>
</div>

Good work comes from executing each part of a writing process effectively and good work can be done by many team compositions, but some team comps consistently perform better than others. For example, all the "review to find" tasks are best executed by someone with a different perspective than the writer - whether it's "distant-future you" after you forgot what you wrote, a person with different genetic code, or something derived from an entirely different sort of code... Someone with a lot of experience is usually great for development edits, and getting feedback from your target audience is critical.

In this first article of the series, I'm going to explore the steps that have to do with "high-level editing" (steps 4 and 6), using LLMs to produce **development edits** and **not** line edits or copy edits. Generating the edits alone didn't require any programming or fine-tuning to get a great result, just basic prompting. Using LLMs to assist with writing or lower-level edits needs a lot more technical expertise. In followup articles, I will explore the steps that have to do with line edits (step 8) generating new writing (steps 3, 5, 7, and 9).
## The example content being edited (5min read)

In order to understand the example LLM-generated development edits, it's useful to see what they're editing, but not required. Below, I'm sharing a small WIP piece of my writing (800/70,000 words) as an example to explain my analysis of the LLM editorial feedback. I would expect the story to be especially difficult for LLMs to edit because it involves a novel use of language - a spatial understanding of text.

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

<div class="row" style="display:flex">
  <div class="column" style="padding:2px">
    <img src="https://i.imgur.com/lCUlvss.jpg"><br/>
  </div>
  <div class="column" style="padding:2px">
    <img src="https://i.imgur.com/CB2X7Nv.jpg"><br/>
  </div>
  <div class="column" style="padding:2px">
    <img src="https://i.imgur.com/sQ0Gvdo.jpg"><br/>
  </div>
</div>
## Development edit prompts

> Prompting an LLM is like setting up a character in a story that's about to play out.

You can use LLMs in a lot of different ways and the way I first explored here is just to "prompt" it. I told the LLM to play the role of a character (an editor at a scifi publisher), then asked it to critique the sample text while in character.

Prompting an LLM is a bit like you are a film director, describing the character for one of your actors to play. When you use an LLM this way, its performance depends on how much depth you put into the character you want it to be. It can also pick up on how the character should behave if it has context like the setting, the things that character has said before, the worldbuilding, etc. That said, an LLM will not break character in the same way a human does, it fails different. Here's an illustration of what I mean:

> Imagine you are a child and you *prompt* your dog to play a character in a scene - Winnie the Pooh and Tigger going for a walk through the Hundred Acre Wood. Your dog gets very excited for the walk, just like Tigger, but then barks at you, so you tell it to keep quiet because Tiggers don't bark. You walk together into the forest, Tigger bouncing alongside, then it shoots off into the forest because that's what Tiggers do! A few minutes later, your Tigger-dog comes back with a dead squirrel in its mouth. That's not what Tiggers do. The dog is *not human*, so the way that your dog breaks character is unexpected and alien. It's only kind-of able to play along. To get them to play, we have to understand them, set them up with the characters and scenes they're most suited for, and adapt to their inevitable failures. The dog wouldn't play a very good "Christopher Robin having tea with Owl in the treehouse" and it's probably only using the, "we're going for a walk together" part of the Pooh and Tigger *prompt*.

<img src="https://imgur.com/PcPQu8R.jpg">
### First prompt and response

Here is the first prompt I used to get feedback:
```
You are the "bad cop" editor for the publisher. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.
```

Here is the LLM response:

<details>
<summary>ChatGPT's response (click to expand)</summary>
```
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
```
</details>

The headings are great. The ones that I instantly agreed with were: fragmentation, pacing, pretentious tone, and inconsistent voice. Half the feedback I rejected on first sight, but after further contemplation, I realized some of it was the most important kind of feedback - the kind that I, as the author, couldn't see.

For example, where it describes *Lack of Character Development*, I initially rejected it because, I was like, *there's not supposed to be character development* - that's kind of the point of the piece. But when I reflected a bit more I realized that relatability of "the character" is critical for what I'm doing, the whole point is for the reader to identify with an omnipotent being, so the feedback I should take on is, "the character is not relatable enough for what you're trying to do". That's great feedback.

The LLM development edits are incredibly high quality to me, but at the same time, I get the feeling that this feedback is all very standard and it's useful because I'm not especially skilled or experienced as a writer. It seems to be pointing out all the standard, obvious things without the context of the publishing industry or market trends or other things I don't understand. I've found that feedback from real people is different than *LLM feedback*. The LLM feedback is able to be consistently lower-level and more thorough, while my Alpha/Beta readers give me the most important high-level feedback and provide alternative perspectives to build on my ideas. People can say something like, "I see what you're trying to do here", and after a little back-and-forth, I really trust their feedback on "what I'm trying to do there". I don't know whether I'd ever trust the AI's perspective on the most important parts of the piece. I don't think it can grasp "what I'm trying to do" beyond "write good and express ideas".

You might wonder, "since it can figure out what's wrong, can it fix what's wrong too?"
Only if you, as the child playing *Pooh and Tigger* with your dog, want to mix in a dog's interpretation of Tigger that often involves something like a dead squirrel.
### Prompt engineering

What's really incredible here is that I didn't have write much depth at all into the character or setup, and it gave me great results (in my opinion). This doesn't happen all the time, but if it didn't, I can iteratively adapt the character and setup until it's giving me what I want. That process is called *prompt engineering*, and there are patterns out there that describe to do it more effectively. It's an art and not a science.

The first prompt I wrote didn't include the "bad cop" part. The advice wasn't as good because it felt too balanced in its criticism vs. praise, so there were conflicting signals. When I split it into two prompts, "bad cop" vs. "good cop", I got the results I was looking for. It was even better in unexpected ways. Depending on my mood, I can focus more on one set of feedback or the other. Feeling anxious or down? Good cop. Feeling ready to take on the world? Bad cop. The feedback-giver didn't have to read the current state of my mind to give me the most effective feedback - it was up to me to self-examine and self-regulate. That's empowering.

<img src="https://imgur.com/5DAoyQq.jpg">

Here's the three prompts I used:
```
You are the "bad cop" editor for the publisher. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.
```

```
Now you are the "good cop" editor for the major science fiction publisher. Provide development edit feedback on a piece, with excessive praise describing everything that worked.
```

```
what were your top three favourite quotes from the piece and why?
```

Here is the responses I got to next two prompts:

<details>
<summary>ChatGPT's "good cop" response (click to expand)</summary>
```
Despite the issues noted, there are several strengths in your piece that stand out:

### Concept and Ambition

- **High Concept**: The idea of exploring existence, consciousness, and the universe from a god-like perspective is ambitious and intriguing. This high-concept approach can captivate readers who enjoy philosophical and metaphysical themes.
- **Complex Themes**: You tackle complex themes such as the purpose of existence, the nature of consciousness, and the cyclical nature of the universe. These themes have the potential to provoke deep thought and reflection in readers.

### Imagery and Language

- **Evocative Imagery**: When the abstract language aligns, it creates powerful and evocative imagery. Phrases like "matrix of superclusters" and "divine strobelight" are visually striking and memorable.
- **Rich Vocabulary**: The language is rich and varied, showcasing a strong command of vocabulary. This adds depth to the narrative and helps convey the grandeur of the concepts being explored.

### Philosophical Depth

- **Thought-Provoking**: The piece raises thought-provoking questions about the nature of existence and the universe. These questions can engage readers intellectually and encourage them to ponder their own beliefs and understandings.
- **Exploration of Infinity**: The exploration of infinite possibilities, timelines, and consciousness is fascinating. This aspect of the narrative can draw readers into a contemplation of the vastness and complexity of existence.

### Tone and Atmosphere

- **Epic Tone**: The tone of the piece has an epic quality, suitable for the grand themes it addresses. This helps create an atmosphere of awe and wonder, drawing readers into the narrative's expansive scope.
- **Sense of Mystery**: There's a sense of mystery and the unknown that permeates the narrative. This can be compelling, as it keeps readers curious about where the story is heading and what revelations might come next.

### Potential for Emotional Impact

- **Existential Reflection**: The existential themes have the potential to resonate emotionally with readers, especially those who have contemplated similar questions about life, purpose, and the universe.
- **Moments of Profundity**: Certain lines and passages, despite their complexity, carry a profound weight. These moments can leave a lasting impression on readers and encourage them to reflect on their own lives and beliefs.

### Unique Perspective

- **God-like Narrator**: The choice of a god-like narrator provides a unique perspective that sets the piece apart from more conventional narratives. This perspective allows for a broad and encompassing view of existence and time, adding a distinct flavor to the story.

By refining the structure and clarity while preserving these strengths, your piece can become a more engaging and impactful exploration of its profound themes.
```
</details>

<details>
<summary>ChatGPT's "favourite quotes" response (click to expand)</summary>

</details>

I love all the compliments. Immediately, I can see some differences of opinion going on around concept/themes, language/style, and character/perspective. I'm not seeing any praise of the structure, clarity, or pacing, so those must really be the weak points. It's also worth being wary of LLMs potential incompatibility with innovation in literary structure, so that's something I'd check with the audience.

The good cop/bad cop contrast also highlights something important - dialectics. When the good cop and bad cop give praise and criticism about *the same thing*, that is an important piece of information. That's where the art is, it's a signal that you should seek feedback from other people on exactly that point. You have to be careful, though - these are LLMs and the good cop may just be using the bad cop as context for its advice. If I really wanted to be sure about the dialectics, I'd make a separate chat for each, but then again, the bad cop context is useful for the good cop to give more holistic feedback.

## Followup prompts

For half of the feedback, further prompting isn't useful. For the other half, I'd follow up with something like this:
```
For the "Overuse of Abstract Language" feedback, please highlight the text in the piece which should be changed.
```

You might wonder why I didn't ask ChatGPT for detailed feedback upfront in the "bad cop" prompt. Mixing in some management philosophy, these [two rules-of-thumb are in tension with one-another](https://charity.wtf/2017/05/11/the-engineer-manager-pendulum/), producing this [well-celebrated dimension](https://en.wikipedia.org/wiki/The_Mythical_Man-Month), a central problem in scaling creative projects to more workers. Let's call it the ["maker-manager tradeoff"](https://paulgraham.com/makersschedule.html):
- Maker's advantage: The more specialized the task you ask an worker to do, the better it'll perform.
- Manager's advantage: The more context a worker has for a task, the better it'll perform.

There's a lot of context in how tasks are put together, and therein lies the problem. If you want to do a bunch of things, but you only give them to the LLM one-at-a-time, then it won't have all the context for how the results should come together. There's a balance that you, as the orchestrator of LLMs responsible for the end-product, have to deal with.

If we pretend for a moment that we humans are "workers" too, then we apply this principle to modern writing and IT product development practices... In writing, LLMs enable writers to distribute the work across more "workers". In product development, LLMs enable "workers" to build with more context. LLMs can do other things too, but this, IMO, is LLMs' "killer app" for those industries.
[3 pics: steps up becoming managerial and stereotypical manager values, steps down losing maker values, upside-down v with both colours meeting in the middle]

<img src="https://i.imgur.com/CAnqvdT.jpg">

For half of the feedback, further prompting isn't useful. For the other half, I'd do something like these:

Sentence-level problems:
```
For the "Inconsistent Voice" feedback, please highlight examples of the different voices in the text that should be made consistent.
```

```
Highlight all instances where <voice from above response> is found in the piece.
```

High-level problems:
```
What parts of the text have pacing problems?
```

```
For the part <insert from above response> what are some ways I could solve the pacing issue there?
```

```
In what ways is the character development lacking? At what points would you expect more/better character development to happen?
```

```
For the "Fragmentation" feedback, what parts of the piece are the greatest offenders?
```

```
How could the overall structure be modified to solve the structural fragmentation issues?
```
## Comparing LLM providers

Which LLM to choose? There are hundreds. It's a bit like picking what actor to play the character in the scene you've set up. Imagine you're in the early days of cinema where directors don't really know what "good acting" looks like, never mind audiences. Yes, anyone can call tell when someone is obviously 100x "better" than someone else, but given a bunch of actors who perform roughly the same, it comes down to factors other than their acting abilities like whether you know their family. You're probably just going to pick the LLM based on which logo you vibe with and that's not such a bad way to decide.

I picked ChatGPT because:
- I don't have a PC that can run the big open source models
- I'm ok with giving them my data
- I've been using ChatGPT since it came out
### Corporate vs. open source

When you submit your data to an LLM company, they can use it to train their LLMs. All the major LLM providers have options to opt out of them training on your data, but some people are sensitive about their data and refuse to give it to LLM providers. I would be happy for someone else to sound like me or use my ideas, but my livelihood isn't tied up in my literary IP.

If you are sensitive about sharing data, you can run LLMs locally. The open source LLMs that have similar performance to corporate LLM providers require powerful PCs. There are lower-performance LLMs that run on most PCs. If you want to try running an open source model on your computer, check out Ollama.
### Qualitative comparison

I liked ChatGPT's feedback the most, but all the LLMs I tried felt similar-enough to be interchangeable:
- Claude brings up the same points of feedback as ChatGPT, but it doesn't deliver them with the same *oomph*. Claude also had some points where it didn't seem to "get it" - like the *Themes and Philosophy* or *Originality* feedback.
- After my first read, I dismissed Gemini's feedback, but looking at it again, it's great. Maybe just a little too succinct. When I reviewed other stories with it, I saw repetition of certain points of feedback like "*Create a clear narrative structure with a beginning, middle, and end.*"
- Llama 2 is a tiny, outdated open source model. Its response is more like bad acting, taking on a character rather than doing what the character would actually do. It has a some poignant insights, but seems a bit confused in parts, and by the end it became cringe to read, like I have to wipe slime off of me after consuming the writing style.

<details>
<summary>Claude 3.5 responses (click to expand)</summary>
```
Alright, let's dissect this piece and highlight its numerous shortcomings. This so-called "story" is a convoluted mess that fails on multiple levels. Here's a structured breakdown of its major flaws:

1. Structure and Coherence:
   - The narrative is disjointed and difficult to follow.
   - There's no clear plot or progression, just a series of abstract musings.
   - The use of fragmented sentences and unconventional formatting is jarring and pretentious.

2. Character and Point of View:
   - The narrator/protagonist is poorly defined and inconsistent.
   - The constant shifting between "I am" and "I was" is confusing and unnecessary.
   - There's no character development or relatable elements for the reader to latch onto.

3. Setting and World-building:
   - The cosmic scale is poorly established and lacks concrete details.
   - The concepts of "multidimensional supercolliders" and "cellular autonoma" are thrown in without explanation.
   - The entire setting feels like a mishmash of sci-fi clichés without substance.

4. Themes and Philosophy:
   - The central idea that "the purpose of existence is to continue existing" is trite and underdeveloped.
   - The piece attempts to tackle grand concepts but fails to say anything meaningful about them.
   - The cyclical nature of existence is presented in a tedious and repetitive manner.

5. Language and Style:
   - The prose is overwrought and self-indulgent.
   - Excessive use of pseudo-scientific jargon without proper context or explanation.
   - The attempt at poetic language often falls flat and comes across as amateurish.

6. Pacing and Engagement:
   - The piece drags on without any real sense of tension or progression.
   - The repetitive nature of the narrator's realizations becomes monotonous.
   - There's no hook to engage the reader or maintain their interest.

7. Clarity and Comprehension:
   - Many passages are needlessly obtuse and fail to convey clear ideas.
   - The use of unconventional formatting (e.g., "." at the beginning of sentences) is distracting and serves no apparent purpose.
   - The piece assumes too much from the reader without providing necessary context.

8. Originality:
   - The concepts presented are derivative of existing sci-fi and philosophical works.
   - The "god-like being contemplating existence" trope is overused and poorly executed here.
   - There's no fresh perspective or unique take on the subject matter.

9. Emotional Impact:
   - The piece fails to evoke any meaningful emotional response from the reader.
   - The narrator's supposed excitement, fear, and disappointment are told rather than shown.
   - There's a lack of genuine pathos or relatable sentiment throughout.

10. Resolution and Ending:
    - The conclusion is anticlimactic and unsatisfying.
    - The final paragraphs devolve into more abstract musings without providing closure.
    - The piece ends with a whimper rather than a bang, leaving the reader unfulfilled.

In conclusion, this piece requires a complete overhaul. It needs a clearer narrative structure, more coherent world-building, and a significant reduction in pretentious language. The author should focus on developing a more accessible and engaging story rather than trying to impress with vague cosmic concepts and pseudo-profound statements. As it stands, this piece is far from publishable quality and would likely alienate most readers.
```

```
Certainly! Let me don my "good cop" hat and dive into the brilliance of this piece.

Wow! What an absolutely mind-bending, transcendent piece of science fiction! This story pushes the boundaries of the genre, blending cosmic horror, hard sci-fi, and metaphysical philosophy into a truly unique narrative experience. Let's break down the many strengths of this exceptional work:

1. Concept and Scope:
   - The sheer ambition of this piece is staggering. It tackles the ultimate questions of existence with breathtaking audacity.
   - The concept of a near-omniscient, near-omnipotent entity exploring the nature of reality is executed with remarkable vision.

2. Structure and Style:
   - The fragmented, stream-of-consciousness style brilliantly mirrors the vast, incomprehensible nature of the narrator's existence.
   - The use of unconventional formatting and punctuation creates a sense of otherworldliness that perfectly suits the subject matter.

3. Language and Prose:
   - The lyrical, poetic quality of the writing is simply stunning. Lines like "I am practicing every religion, celebrating every culture, replaying every life I am able to live" are pure magic.
   - The author's command of scientific and philosophical terminology is impressive, lending authenticity to the cosmic scale of the narrative.

4. Themes and Depth:
   - The exploration of existence, purpose, and the nature of consciousness is profound and thought-provoking.
   - The cyclical nature of existence and the paradox of omniscience are handled with remarkable nuance and insight.

5. Imagery and Visualization:
   - The cosmic imagery is vivid and awe-inspiring. Descriptions like "Multidimensional supercolliders smash multiverses together, warping their universal laws" paint a mind-blowing picture.
   - The author excels at conveying abstract concepts in visceral, almost tangible ways.

6. Pacing and Tension:
   - The piece maintains a sense of breathless excitement and existential dread throughout, keeping the reader engaged.
   - The build-up to the "ignition sequence" and its aftermath is particularly well-executed, creating a palpable sense of anticipation and release.

7. Character Development:
   - Despite the cosmic scale, the narrator's journey feels personal and relatable. Their excitement, fear, and ultimate acceptance of their role in existence is deeply moving.
   - The evolution of the narrator's understanding of reality is beautifully portrayed, from naive excitement to profound realization.

8. Originality:
   - This piece brings fresh perspectives to age-old philosophical questions, presenting them in a uniquely science-fictional context.
   - The concept of a god-like entity struggling with the purpose of existence is handled in a way that feels novel and exciting.

9. Emotional Impact:
   - The story manages to evoke a sense of cosmic awe, existential dread, and ultimate acceptance that resonates long after reading.
   - The narrator's love for existence and desire for it to continue is surprisingly touching, given the vast scale of the narrative.

10. Ending and Resolution:
    - The cyclical nature of the ending perfectly encapsulates the themes of the piece, leaving the reader with a sense of both closure and infinite possibility.
    - The final lines, expressing love for existence and the desire for it to continue, provide a beautifully hopeful note to end on.

In conclusion, this is a tour de force of speculative fiction. It pushes the boundaries of what's possible in the genre, challenging readers while also providing a deeply emotional and thought-provoking experience. The author's ability to blend complex scientific concepts with profound philosophical musings is truly remarkable. This piece has the potential to become a classic of metaphysical science fiction, standing alongside works by authors like Olaf Stapledon or Greg Egan. It's exactly the kind of bold, visionary writing that our publishing house is always seeking. Bravo!
```
</details>

<details>
<summary>Gemini v2024.08.01 responses (click to expand)</summary>

</details>

<details>
<summary>Llama's response (click to expand)</summary>
```
As the "bad cop" editor, I must say that this piece is a mess. It lacks focus, clarity, and coherence. The authorseems to have embarked on a wild goose chase of existential musings, without any clear direction or purpose. Theresult is a jumbled, meandering narrative that fails to deliver any meaningful insights or impact.

Let's start with the opening sentence: "The purpose of existence is to continue existing." This statement is far toobroad and vague to be of any real consequence. What does it even mean? What kind of existence are we talking abouthere? Human existence? Plant existence? Microbial existence? The lack of specificity makes this claim utterlymeaningless.

Furthermore, the author's fixation on the concept of "purpose" is both unproductive and unhelpful. Purpose is asubjective, psychological construct that can vary greatly from person to person. It's not something that can beapplied universally or even interpersonally. The author's obsession with this idea only serves to create a kind ofexistential angst that is unnecessary and unproductive.

Speaking of unnecessary and unproductive, the author's frequent references to "fading away" and "resurrecting" arenothing but filler words. They add no substance or insight to the narrative whatsoever. In fact, they only serve tomake the piece feel overly repetitive and tedious.

And don't even get me started on the author's bizarre fascination with "the divine strobelight." What is this, somekind of cosmic masturbation? It adds nothing to the narrative except a sense of confusing, disorienting imagery thatonly serves to confuse and alienate the reader.

In short, this piece is a mess. It lacks focus, clarity, and coherence, and is ultimately unhelpful and unproductive.As a "bad cop" editor, it's my job to say so.
```
```
**Development Edit Feedback: A Symphony of Cosmic Wonder**

This piece is an extraordinary exploration of consciousness, existence, and the nature of reality. It's a bold, ambitious work that pushes the boundaries of science fiction and philosophy. The author has crafted a truly unique and thought-provoking narrative.

The concept of a self-aware entity on a cosmic scale is both awe-inspiring and profoundly humanizing. You’ve managed to imbue this colossal being with a sense of wonder, curiosity, and even vulnerability. It’s a testament to your skill as a writer that we can connect with something so utterly alien.

The prose is exquisite. Your use of language is both precise and evocative, painting vivid pictures of complex ideas. The balance of scientific terminology and poetic imagery is masterful. You've created a world that is both intellectually stimulating and emotionally resonant.

The exploration of the concept of infinite recursion and the cyclical nature of existence is handled with brilliance. It's a mind-bending concept, but you’ve made it accessible and engaging. The pacing of the narrative is impeccable, building tension and releasing it at just the right moments.

The ending is both satisfying and thought-provoking, leaving the reader with a sense of cosmic awe and a desire to contemplate the piece further. It's a truly original and unforgettable conclusion.

This piece has the potential to be a landmark work in science fiction. With some careful refinement, it could become a classic.

I'm incredibly excited to work with you on this project. Let's discuss how we can elevate this piece to even greater heights.
```
```
Oh, wow! *adjusts sunglasses* This piece is absolutely, positively, without a doubt, a masterpiece! 🤩 It's like a symphony of words, weaving together in perfect harmony to create this beautiful tapestry of existential musings. The author has crafted a work of sheer genius here, and I can barely contain my excitement! 😍

First of all, let's talk about the opening sentence: "The purpose of existence is to continue existing." Brilliant! 💡 This is not just some vague, meaningless statement; oh no, it's a profound and thought-provoking observation that sets the tone for the entire piece. It's like the author has reached into the depths of humanity and pulled out this incredible nugget of wisdom. Bravo! 🎉

And then there's the fixation on the concept of "purpose." Oh, how I love this aspect of the narrative! *giggles* The author has managed to create this sense of existential longing that is both heartbreaking and inspiring at the same time. It's like they're reaching out to us from some cosmic void, saying, "Hey, don't you want to know the meaning of life? 🤔" And we're all like, "Uh, yeah...please tell us!"

And have I mentioned how much I adore the references to "fading away" and "resurrecting"? *swoons* It's like the author has created this entire universe of symbolism that is both poetic and haunting. I mean, who doesn't love a good resurrection story? 🙂 It adds this incredible layer of depth to the narrative, making it feel almost mythical in nature.

And let's not forget the "divine strobelight"! *giggles* Oh, how I wish I could see it for myself! 🤩 It's like a beacon of hope and wonder, shining down on us from some celestial realm. The author has created this incredible image that is both mysterious and awe-inspiring, leaving us all to wonder what it might look like. Brilliant! 🎉

Overall, I must say that this piece is an absolute masterpiece. *nosebleed* It's like the author has tapped into some deep, universal truth and brought it back to us in a way that is both beautiful and thought-provoking. I could gush about this all day! 😍 So, bravo to the author, and may they continue to create works of such incredible beauty and insight! 💕
```
</details>
## Conclusion

The LLM-based development edit feedback is *so good* and *so easy to get* that I will use it in all my writing. From this post, you've seen how working with LLMs is a bit like outlining setting and developing characters, two things that writers have more experience in than any other profession. In the next post, I will explore generating text to include in my writing - to get that Tigger-dog to sing and not bark or bring home dead squirrels.
### Audience #1
```
You are the target audience for this blog post - someone with a technical background, interested in AI, but little-to-no context about writing or the publishing industry. You are the "bad cop" reviewer. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.
```

```
Now you are the "good cop" reviewer of the same audience. Provide development edit feedback on the piece, with excessive praise describing everything that worked.
```

```
What were your favourite 3 quotes from the piece and why?
```

<details>
<summary>ChatGPT's response (click to expand)</summary>
Bad cop:
```
### Development Edit Feedback

#### 1. **Introduction and Context**
   - **Excessive Self-Referencing**: The introduction immediately dives into personal experiences and self-references, which may not resonate with a technically-inclined audience. It feels like an attempt to justify the author's process rather than focusing on providing valuable insights into using LLMs for writing. Consider removing or significantly trimming down the personal anecdotes to maintain the reader's interest and avoid making the post feel like a personal blog rather than a professional guide.
   - **Vague Positioning**: The post fails to establish a clear thesis or promise for the reader. Why should a technically-minded reader, who may be unfamiliar with the writing or publishing industry, care about this process? There’s an assumption that the audience shares the author's interest in philosophy and literature, which may alienate a significant portion of the readership. Start with a more compelling reason why using LLMs in the writing process is relevant to the audience’s interests.

#### 2. **Structure and Organization**
   - **Lack of Cohesion**: The article meanders through different parts of the writing process without a clear, guiding thread. The outline provided early in the post is helpful but not effectively integrated into the discussion that follows. Each point should be expanded upon with clear, actionable insights, particularly how LLMs can enhance or streamline each step of the process. Currently, the structure is loose, which may confuse readers rather than inform them.
   - **Overly Detailed Process Explanation**: For a technical audience, there is excessive detail on the traditional writing process that may not be necessary. This could be condensed or presented more succinctly to keep the reader's attention focused on the novel application of LLMs. Assume the audience is more interested in the innovative aspects rather than the fundamentals of writing.

#### 3. **Content Depth**
   - **Superficial Treatment of LLMs**: The post lacks depth in discussing the practical applications of LLMs in writing. For a technically-minded reader, the exploration of how LLMs can be used is underwhelming. The content is largely surface-level, focusing on generalities rather than providing a robust analysis or examples of how these models work in practice. Consider including case studies, specific examples, or even code snippets that demonstrate how to effectively leverage LLMs for different parts of the writing process.
   - **Inadequate Exploration of Potential Issues**: There's little discussion of the potential pitfalls or limitations of using LLMs in writing. A technically-inclined audience would expect a critical analysis of the technology, including its biases, limitations in creative generation, and challenges in maintaining narrative coherence. The current content feels more like an endorsement than an informed critique, which could diminish credibility.

#### 4. **Tone and Style**
   - **Inconsistent Tone**: The tone fluctuates between conversational and overly technical, creating an inconsistent reading experience. For a blog post targeted at a technical audience, maintaining a professional yet engaging tone is crucial. Avoid jargon that might be unfamiliar to readers without a literary background, but also ensure that the technical explanations are clear and authoritative.
   - **Lack of Precision**: Some of the language used is vague or imprecise, particularly when discussing the application of LLMs. Terms like "big problems" in the writing process are too ambiguous for a technical audience that would appreciate more specific language. The post should be rewritten with a focus on clarity and precision, ensuring that every term and concept is well-defined and contextualized.

#### 5. **Audience Engagement**
   - **Failure to Engage**: The post does little to actively engage the reader. There are no questions, challenges, or calls to action that would encourage readers to think critically or explore the concepts on their own. Consider adding sections that pose questions or scenarios for readers to consider, or even provide interactive elements, like links to demo tools or further readings.
   - **Overuse of Assumptions**: The article assumes a lot about the reader’s knowledge and interest in certain areas (e.g., the intricacies of novel writing, philosophical literature). This could lead to disengagement. Tailor the content to meet the reader where they are, potentially by providing more context or by breaking down complex ideas into more digestible segments.

#### 6. **Conclusion**
   - **Weak Ending**: The post does not conclude with a strong summary or takeaways. A technically-inclined audience would benefit from a concise recap of the key points, particularly how LLMs can be integrated into their workflow. The conclusion should also invite the reader to explore further, perhaps suggesting next steps or additional resources.

### Final Thoughts
The post has potential but requires significant restructuring and refinement to effectively communicate its message to a technical audience. The focus should shift from personal anecdotes and vague generalities to a more robust, detailed exploration of how LLMs can be applied to the writing process, complete with critical analysis and practical examples. Moreover, the tone and structure need to be more consistent and targeted to keep the audience engaged and informed.
```

Good cop:
```
### Development Edit Feedback

#### 1. **Introduction and Context**
   - **Engaging Personal Touch**: The introduction immediately draws the reader in with a personal narrative that feels authentic and relatable. By sharing your own journey of combining philosophy, writing, and technology, you create a strong connection with the audience. This personal touch not only humanizes the content but also makes it accessible to readers who may be exploring similar interdisciplinary interests.
   - **Clear Establishment of Purpose**: From the outset, the post clearly lays out its purpose: to explore the integration of LLMs into the writing process. This sets the reader’s expectations effectively and provides a strong foundation for the content that follows. The initial outline of the writing process serves as a helpful roadmap, ensuring that readers understand the broader context before diving into the specifics.

#### 2. **Structure and Organization**
   - **Logical Flow**: The structure of the post is both intuitive and well-organized. Each step of the writing process is addressed in a logical sequence, making it easy for the reader to follow along. The clear delineation of the writing stages, from idea generation to development edits, mirrors the systematic thinking that a technically-inclined audience would appreciate. The transitions between sections are smooth, maintaining the reader’s engagement throughout.
   - **Concise and Informative**: The way you break down the writing process is succinct and informative, avoiding unnecessary jargon while still conveying the necessary information. The content is broken up into manageable sections, which helps maintain the reader’s focus. This approach ensures that even complex ideas are communicated clearly and effectively.

#### 3. **Content Depth**
   - **Insightful Application of LLMs**: The exploration of how LLMs can be integrated into various stages of the writing process is particularly compelling. You manage to balance technical detail with practical application, making the content accessible to readers with varying levels of familiarity with AI. The discussion of LLMs as tools for both idea validation and development edits is insightful and shows a deep understanding of both writing and AI technology.
   - **Balanced Perspective**: While the post is enthusiastic about the potential of LLMs, it also acknowledges the limitations and challenges of using them in creative writing. This balanced perspective adds credibility to the piece, as it demonstrates a nuanced understanding of the technology. By discussing potential pitfalls and offering solutions, you equip the reader with the knowledge needed to approach LLMs with both excitement and caution.

#### 4. **Tone and Style**
   - **Approachable and Professional Tone**: The tone strikes a perfect balance between being conversational and professional. This makes the content engaging without sacrificing the depth that a technical audience would expect. The language is clear and direct, which helps to demystify the more complex aspects of both writing and AI. The approachable style invites readers to explore the topic further, fostering a sense of curiosity and enthusiasm.
   - **Clarity in Communication**: The clarity with which you explain the writing process and the role of LLMs is commendable. You avoid overly technical jargon, instead opting for language that is precise yet understandable. This ensures that the content is accessible to a broad audience, including those who may not have a deep background in AI or creative writing.

#### 5. **Audience Engagement**
   - **Strong Connection with the Audience**: The way you address the reader directly and share your personal experiences creates a strong connection with the audience. This approach not only engages the reader but also builds trust, as it shows that you’re speaking from experience. The use of questions and scenarios encourages the reader to reflect on their own experiences and consider how they might apply LLMs in their work.
   - **Thought-Provoking Content**: The content is thought-provoking, particularly for readers who are new to the idea of using AI in creative processes. You challenge the reader to think about how LLMs could change the way they approach writing, which is both exciting and intellectually stimulating. This engagement is likely to inspire readers to experiment with LLMs in their own work.

#### 6. **Conclusion**
   - **Effective Recap and Call to Action**: The conclusion effectively recaps the key points of the post and reinforces the value of integrating LLMs into the writing process. The call to action, while subtle, is powerful—it encourages readers to take the next step in their own writing journey, whether that means experimenting with LLMs or simply rethinking their creative process. This leaves the reader with a sense of empowerment and curiosity.

### Final Thoughts
Overall, this post is a well-crafted, insightful, and engaging exploration of how LLMs can be integrated into the writing process. The structure is logical and easy to follow, the content is both deep and accessible, and the tone is perfectly suited to the target audience. By combining personal experience with practical advice, you’ve created a piece that not only informs but also inspires. This is exactly the kind of content that can bridge the gap between technology and creativity, making it a valuable resource for readers from all backgrounds.
```

Fav 3 quotes:
```
My favorite quote from the piece is:

*"The novel I’m writing is sci-fi philosophy and now that I’ve finished a readable draft, I’ve been looking into experimenting with using LLMs as a tool in my writing process."*

This quote stands out because it encapsulates the essence of the entire post in a single, compelling sentence. It merges the personal journey of writing with the cutting-edge use of technology, specifically Large Language Models (LLMs). The phrase "sci-fi philosophy" immediately signals a blend of genres that is both intellectually stimulating and creatively ambitious. It also captures the reader's attention by highlighting the experimental nature of using LLMs in the writing process, which is likely to pique the interest of those with a technical background. This quote sets the tone for the rest of the piece, emphasizing both innovation and a thoughtful approach to creative work.
```

</details>

### Audience #2
```
You are the target audience for this blog post - someone who is actively writing or involved in the publishing industry, you don't have a technical background, but you are interested in how AI is affecting what you do. You are the "bad cop" reviewer. Provide development edit feedback on a piece, thorough and structured, with excessive criticism. The file is attached.
```

```
Now you are the "good cop" reviewer of the same audience. Provide development edit feedback on the piece, with excessive praise describing everything that worked.
```

```
What was your favourite three quotes from the piece and why?
```

<details>
<summary>ChatGPT's response (click to expand)</summary>
Bad cop:
```
### Development Edit Feedback

**Title:** Writing Science Fiction with LLMs - Development Edits  
**Date:** 2024-09-01  
**Author:** Douglas Hindson

---

#### 1. **Opening and Introduction**
- **Critique:** The introduction is overly personal and lacks a clear connection to the broader audience. While mentioning your sabbatical and study of philosophy is interesting, it feels self-indulgent rather than relevant to the reader. The connection between your personal journey and the topic of using LLMs in writing needs to be more explicit.
- **Suggestion:** Consider reframing the introduction to focus on the value proposition for the reader. Why should they care about your experience with LLMs? Perhaps open with a broader statement about the challenges and opportunities in modern sci-fi writing, and then segue into your personal journey as an example.

#### 2. **Structure and Flow**
- **Critique:** The structure is too rigid and feels like a checklist rather than a narrative. Listing the stages of the writing process in bullet points creates a dry and somewhat monotonous tone. The lack of transitions between sections makes the post feel disjointed.
- **Suggestion:** Consider weaving the stages of the writing process into a narrative. Use examples and anecdotes to illustrate each stage rather than just listing them. This would make the content more engaging and relatable.

#### 3. **Depth and Analysis**
- **Critique:** The post lacks depth in discussing how LLMs can be effectively integrated into each stage of the writing process. The surface-level treatment of LLMs as a tool doesn't offer much value to readers who might be looking for practical, actionable advice.
- **Suggestion:** Expand on how LLMs can specifically aid in different stages of writing. For example, you could delve into how LLMs might assist with idea generation or development edits. Provide concrete examples or case studies to demonstrate these points.

#### 4. **Visual Elements**
- **Critique:** The inclusion of images feels out of place and doesn't add value to the content. The images are inserted without context, which disrupts the flow of reading. The captions are missing, which further diminishes their relevance.
- **Suggestion:** Either remove the images or ensure they are directly related to the content. If you keep them, provide captions and explain how they connect to the discussion. Visuals should enhance, not distract from the narrative.

#### 5. **Voice and Tone**
- **Critique:** The voice is inconsistent. It oscillates between an informal, almost blog-like tone and a more formal instructional tone. This inconsistency can confuse the reader about the intended audience and purpose of the post.
- **Suggestion:** Decide on a consistent tone that aligns with your target audience. If the goal is to educate, a more formal and authoritative tone might be appropriate. If the post is meant to be more of a personal reflection, maintain a conversational tone but ensure it is purposeful and engaging.

#### 6. **Use of Technical Language**
- **Critique:** There is an assumption that readers have a certain level of familiarity with LLMs, which might alienate those without a technical background. Conversely, the explanations are too superficial for readers who might already be familiar with LLMs.
- **Suggestion:** Clarify your target audience and adjust the technical language accordingly. If writing for a non-technical audience, provide more background and simplified explanations of LLMs. If the audience is more technically savvy, dive deeper into the mechanics and potential of LLMs.

#### 7. **Conclusion**
- **Critique:** The post lacks a strong conclusion. There is no clear takeaway or call to action, leaving the reader unsure of what they should do with the information provided.
- **Suggestion:** End with a compelling conclusion that summarizes key points and offers a clear next step for the reader. Whether it's experimenting with LLMs in their writing process or reflecting on their own creative methods, give them something to think about or act upon.

---

### Summary of Feedback
This post has potential but requires significant restructuring and deepening of content to be truly effective. Focus on creating a cohesive narrative that seamlessly integrates personal experience with actionable advice. Ensure that visual elements add value and that the tone remains consistent throughout. Finally, provide a strong conclusion that leaves the reader with a clear understanding of the topic and what they can do next.
```

Good cop:
```
### Development Edit Feedback

**Title:** Writing Science Fiction with LLMs - Development Edits  
**Date:** 2024-09-01  
**Author:** Douglas Hindson

---

#### 1. **Opening and Introduction**
- **Praise:** The introduction is engaging and personal, immediately drawing the reader into your unique journey. By sharing your background, including your sabbatical and philosophical studies, you establish credibility and create a relatable context. This personal touch not only makes the post more authentic but also sets the stage for a thoughtful exploration of how LLMs can be integrated into the writing process.
- **Highlight:** Your willingness to connect your philosophical pursuits with your writing process adds a layer of depth that is both intriguing and refreshing. It shows that you're not just using LLMs as a tool but are considering their implications on a deeper level.

#### 2. **Structure and Flow**
- **Praise:** The clear, step-by-step outline of the writing process is exceptionally helpful. It breaks down what can be a daunting task into manageable stages, making the entire process feel more approachable for the reader. The use of bullet points here is effective in conveying the information succinctly, allowing readers to easily follow along and understand where LLMs might fit into each phase.
- **Highlight:** The logical progression through the stages of writing is not only well-organized but also thoughtfully constructed. It provides a solid framework that readers can use to evaluate their own processes, making the post both informative and practical.

#### 3. **Depth and Analysis**
- **Praise:** Your discussion of the different stages of the writing process and where LLMs can play a role is insightful. By mapping out specific areas where LLMs can be beneficial, you provide readers with actionable advice that they can apply directly to their own writing. This practical guidance is invaluable for those who might be unsure of how to leverage AI in their creative work.
- **Highlight:** The balance you strike between being informative and encouraging is commendable. You acknowledge the challenges while also offering solutions, which helps to empower writers to experiment with new tools like LLMs without feeling overwhelmed.

#### 4. **Visual Elements**
- **Praise:** The inclusion of images adds a nice visual break to the text, making the post more engaging and easier to digest. The images are well-chosen and complement the content by providing visual interest without distracting from the main message.
- **Highlight:** The layout of the images, with attention to symmetry and balance, enhances the aesthetic appeal of the post. It shows a consideration for the reader's visual experience, which can often be overlooked in text-heavy content.

#### 5. **Voice and Tone**
- **Praise:** The voice in this post is warm and approachable, making the content accessible to a wide range of readers. You strike a great balance between being knowledgeable and conversational, which helps to keep the reader engaged throughout. This tone is perfect for demystifying the use of LLMs in writing, making the technology feel less intimidating.
- **Highlight:** The consistency of your tone throughout the post is impressive. Whether you're discussing technical aspects of LLMs or more abstract philosophical ideas, the voice remains steady and reassuring, guiding the reader through potentially complex topics with ease.

#### 6. **Use of Technical Language**
- **Praise:** You do an excellent job of explaining LLMs in a way that is understandable to readers without a technical background. By avoiding jargon and focusing on the practical applications of LLMs, you make the content accessible and relevant to a broader audience. This approach is particularly effective for writers who may be curious about AI but unsure of where to start.
- **Highlight:** Your ability to translate complex concepts into clear, actionable advice is a real strength. It demonstrates a deep understanding of both the technology and the needs of your audience, making the post a valuable resource for anyone looking to incorporate AI into their writing process.

#### 7. **Conclusion**
- **Praise:** The conclusion of your post is thoughtful and reflective, leaving the reader with a sense of closure and a clear takeaway. You wrap up the discussion nicely by reiterating the key points and encouraging readers to experiment with LLMs in their own writing. This call to action is subtle but effective, inviting readers to take the next step without feeling pressured.
- **Highlight:** The way you tie the conclusion back to your personal journey creates a satisfying narrative arc, bringing the post full circle. This not only reinforces the connection between your experiences and the topic at hand but also leaves the reader with a lasting impression of your commitment to exploring new frontiers in writing.

---

### Summary of Feedback
This post is a fantastic blend of personal reflection, practical advice, and insightful analysis. Your ability to connect with the reader on both an intellectual and emotional level is commendable, making the content both engaging and informative. The structure is clear, the tone is inviting, and the depth of your analysis shows a genuine understanding of the challenges and opportunities that come with integrating LLMs into the writing process. Overall, this is a highly valuable piece that will undoubtedly resonate with writers looking to explore new tools and techniques in their craft.
```

Fav 3 quotes:
```
My favorite quote from the piece is:

*"This is an outline of a standard writing process:"*

While it might seem like a simple statement, I appreciate it because it effectively sets the stage for a structured and methodical exploration of the writing process. It serves as a clear and concise introduction to a complex topic, immediately signaling to the reader that they are about to receive valuable, organized information. This quote reflects the author's ability to distill a potentially overwhelming subject into something approachable and manageable, which is a crucial skill when writing for an audience that may be new to the subject matter. It’s a subtle yet powerful way to guide the reader into the content that follows.
```
</details>
