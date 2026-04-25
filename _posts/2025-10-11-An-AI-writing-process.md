---
layout: post
title: An AI writing process
date: 2025-10-11T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - professional
  - projects
modified_time: 2025-07-30T00:00:00.001-05:00
---
## forwards

I think, going forward, written pieces will be defined by the systems used to build those pieces. More and more, people will build novel systems to write novel pieces. I think it's always been that way - for example, you can't escape the language you're writing in - but it's never been easier to create novel systems to write.

This is a system I've been working on. I've built other systems before, and I will build others.

## why did I make this system?

I made this system because:
- I wanted to be able to start and finish a short story in a weekend, so that I could do a project on a whim and not feel burdened by it when it's half-done.
- I had made my mind up about what stories are for - namely, to perform state-changing operations on a reader's beliefs (reinforcing beliefs is a state-change).
- LLMs have suddenly unlocked possibilities in writing. **But** LLMs write terribly.

## overall process

### outline

1. Have an idea - a flash of inspiration about a belief in myself I just observed.
2. Write a premise:
	- describe the beliefs that I want to operate on, and what state change I want to induce to those beliefs.
	- roughly outline some things that should happen to change those beliefs
3. Interrogate that premise with an LLM to find:
	- what's been said before about this topic
	- what seems to be new this time
	- what other beliefs are close to this premise
4. Write an outline:
	1. Identify the audience.
	2. Describe the beliefs **of the audience** that I want to operate on, and what state change I want to induce to those beliefs.
	3. Summary of the entire piece, 1-4 sentences.
	4. Optional elaboration on:
		1. Plot
		2. Characters
		3. Setting
		4. Themes
		5. Narrative devices

### train a writing system

1. Converse with an LLM to find works that would be appropriate to draw stylistic inspiration from.
2. Find the pieces and pull out parts of the piece that you want to draw inspiration from.
3. Manually label the dataset, identifying the sections/paragraphs/sentences that are desirable.
4. Fine-tune a writing model on the dataset.
5. Write prompts for the writing model to write different parts of the outline. Have the writing model make hundreds of attempts at writing different parts of the outline.
6. Manually label the generated data, identifying what phrases/paragraphs were desirable.
7. Train a filtering model on the new dataset, which finds desirable text within a large body of generated text.

#### notes
- the piece could have many models, if different sections/characters/etc are intended to be written in different styles.
- I might retrain a model if it's underperforming - not giving me what I'm looking for.

### write and brainstorm

1. Write prompts for different parts of the outline I want the LLM to attempt.
2. Generate hundreds of attempts per prompt, and run the filtering model on those attempts.
3. Manually pick out interesting phrases/dialogue/structure/characters/etc.
	- Most of the content I just save for later incorporation.
	- Some of the ideas will make me change the outline.

### collage the content together

1. With two panes open, copy content from the brainstormed text to the first draft window.
2. Iteratively glue the content together manually.

### editing

1. Do development edits.
	1. Get feedback across 10+ kinds of prompts across all dimensions of writing, from multiple LLM providers.
	2. Read all the feedback.
	3. Make the necessary changes, manually.
2. Do line-level edits.
	1. Get feedback paragraph-by-paragraph from an LLM to improve readability, language use, etc.
3. Get beta readers to read it and give feedback.