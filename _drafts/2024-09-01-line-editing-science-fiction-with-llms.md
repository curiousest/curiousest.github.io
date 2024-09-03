---
layout: post
title: Writing science fiction with LLMs - others
date: 2024-09-01T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - projects
modified_time: 2024-09-01T00:00:00.001-05:00
---
## Line edits (step 8)

[Describe flow, etc.]

![[Pasted image 20240813123140.png]]
[fix img]
Prompt 1:
```
You are an editor for a science fiction publisher. Read the text attached and for each of the following stylistic elements, identify what has been chosen for the piece, and summarize in a concise sentence.

- Language imagery / voice
- Patterns of rhythm, rhyme, syllables
- Emotion / tone
- Paragraph structure
- Logical connection between sentences and paragraphs
```
I attach examples of what "good" looks like, in the way I want my text to read (an example from my writing). This is the "flow profile" I'm going for, almost like the font or colour palate.

Prompt 2:
```
For the newly attached text, identify and quote the text that don't "flow" and provide a very brief explanation why. Use the previously attached text as an example of good "flow".
```
I attach the text I want to review.

Prompt 3 (needs fine-tuned model, trained on flow):
```
For each part of the text you found to have problems, make three possible new versions of the text with the issue fixed.
```
## Non-editing, non-authoring subtasks for LLMs
### visualizing

One facet of the worldbuilding in my book is on the dominant religion of the future. I wanted to portray Capitalism as the next religion that became dominant, absorbed Christianity, and then began to fade away to make way for a new one (just like Christianity absorbed pagan religions, etc).

One of the main characters is a "priestess of capitalism", and I wanted to explore what that could look like. It's especially interesting how various symbols are misused, portraying how the original meaning in symbols can be lost. After ten or so prompt iterations, and twenty or thirty images, here were the best results.

<img src="https://i.imgur.com/UOI3TEV.jpg">

![[Pasted image 20240803115833.png]]
[fix img]
### Comp titles

![[Pasted image 20240813123831.png]]
[fix img]
Comp titles are an important part of writing... link
Prompt (along with the first chapter of text of the book I'm writing - a different piece):
```
You are my literary agent, and this is part of a book I'm writing. First, tell me all the different authors that this work is similar to. Next, give me 10 comp examples.
```

and the ChatGPT LLM response:
```
Your piece exhibits a rich and complex exploration of themes such as existentialism, cosmology, and metaphysics, reminiscent of various influential authors who have delved into similar philosophical and speculative realms. Here's a breakdown of authors whose works resonate with the themes and style of your manuscript:

### Authors Similar to Your Work

1. **Stanislaw Lem** - Known for his philosophical depth and exploration of artificial intelligence and the nature of the universe.
2. **Arthur C. Clarke** - Clarke’s work often explores grand cosmic mysteries with a philosophical lens, much like your narrative’s expansive universe.
3. **Philip K. Dick** - Dick’s exploration of consciousness, reality, and the human condition aligns with the introspective and existential themes in your piece.
4. **Ursula K. Le Guin** - Le Guin’s work combines anthropological and social questions with deep philosophical inquiries, similar to your narrative’s exploration of cultures and existence.
5. **Greg Egan** - His hard science fiction novels that delve into complex scientific and mathematical concepts with deep philosophical implications.
6. **Neal Stephenson** - Stephenson’s speculative fiction often combines complex narratives with profound philosophical questions.
7. **China Miéville** - Known for his works in the weird fiction genre, Miéville’s books often explore complex, high-concept universes and existential themes.
8. **Iain M. Banks** - Banks’ science fiction, especially his Culture series, explores philosophical and societal complexities in a high-concept, futuristic setting.
9. **Jorge Luis Borges** - Although not a traditional science fiction writer, Borges' metaphysical puzzles and infinite concepts have a profound philosophical depth.
10. **Ted Chiang** - Chiang’s thoughtful, meticulously crafted stories often explore the human impact of profound philosophical and technological changes.

### Comp Titles (Comparative Examples)

1. **"Solaris" by Stanislaw Lem** - Explores the limits of human understanding and cosmic mysteries.
2. **"2001: A Space Odyssey" by Arthur C. Clarke** - Combines deep philosophical questions with the exploration of space and the unknown.
3. **"Valis" by Philip K. Dick** - Focuses on the nature of reality and divine intervention.
4. **"The Left Hand of Darkness" by Ursula K. Le Guin** - Explores themes of gender, religion, and cultural conflicts within an intricately built world.
5. **"Diaspora" by Greg Egan** - Centers on concepts of consciousness and the nature of existence in a technologically advanced future.
6. **"Anathem" by Neal Stephenson** - A narrative steeped in philosophy, exploring profound questions within a complex alternate reality.
7. **"Perdido Street Station" by China Miéville** - Features a sprawling, imaginative universe with deep philosophical underpinnings.
8. **"The Hydrogen Sonata" by Iain M. Banks** - A look at the civilization at the brink of a major metaphysical change.
9. **"The Aleph and Other Stories" by Jorge Luis Borges** - Contains stories that delve into infinite concepts and the nature of time and space.
10. **"Exhalation" by Ted Chiang** - A collection of speculative short stories that explore human experience in relation to free will, time, and the universe.

These comparative titles will help in positioning your book within the literary market, highlighting its philosophical depth and speculative nature while aligning it with works that have proven appeal to similar readerships.
```