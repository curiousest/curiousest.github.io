---
layout: post
title: Automating art-craft
date: 2024-11-02T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - projects
  - essay
  - essays
modified_time: 2024-11-02T00:00:00.001-05:00
---
> Be the data you want to see in the world.

Everyone should live by this maxim in the age of AI, especially artists.

Artists produce art about themselves and their lived experience, that's just how it works. Artists who spend a lot of time investing in their craft tend to produce art about their craft - *art about art*. If all you do is art, all you'll want to produce is *art about art*. That's not bad in isolation, but when most art is produced by professional artists, the art we mostly end up with is *art about art*.

In the age of generative AI, creating media is changing fast. Any works created or delivered through a computer will soon be done by a computer + AI. The creative world is being turned upside-down, so artists will be inspired to produce something about that change - the changing nature of art. Loads of art about art...

In the coming years, I think artists should invest in exploring the changing new world rather than investing in the the previous-generation tools that are being rapidly deprecated. Artists should let genAI and technologists figure out the art-craft for now, and gather experiences in the *real world* instead of the *art world*. That way we will get less of a deluge of art about art.

Soon, genAI will be able to create art from *worthy experiential data*. So it's better for artists to invest in generating *worthy experiential data* rather than the downstream craft that processes the experiential data into art. In this post, I'm going to demo how to automatically extract meaning and create worthy story from experiential data. The end-product is bad but the point of it is to show that automating much of the craft of worthy art is possible, so we can expect huge advances in the tools of art-craft.

## system overview

The process of automatically creating art from experiential data I'm demoing is:

**collect experiential data -> extract beliefs -> generate art from the beliefs**

**collect experiential data**: in this demo, this is a 1500-word text conversation
**extract beliefs**: in this demo, this is a prompt that analyzes the conversation
**generate art from beliefs**: in this demo, this is a prompt that writes a story

I use this abstraction, "beliefs", because they are granular enough to be useable by LLMs and abstract enough to hold sufficient meaning for what I'm doing here. Comparable things like sentiment analysis or ontological mapping exist, but beliefs feel to me like they're more usable for the purposes of art and self-improvement.

I have two hypotheses:
- LLMs can extract "beliefs" from experiential data.
- LLMs can create worthy art from those "beliefs".

The second hypothesis comes from my belief that in a compelling story, you must experience a change in one of your unacknowledged beliefs. Some of your beliefs are held constant and at least one belief you're not so aware of must either be falsified or made meaningless.

For example in the classic novel, Frankenstein, a scientist might have the following belief falsified, among others: "My research experiments won't directly impact society until it's productized later on."

## collect experiential data

This is a real conversation between me and a friend planning to meet up and go mountain biking while I was visiting San Francisco:

<details markdown="1">
<summary>iMessage conversation (click to expand)</summary>
> Wed, Oct 2 at 08:29
> 
> Hey, this is Douglas Hindson. I’m going to be in San Francisco for 2wks from the 13th Oct. I’d enjoy hanging out while I’m there. I’m staying with one of my university friends in the city.
> 
> Wed, Oct 2 at 11:02
> 
> Hello Douglas Hindson. Are you going to be in South Bay at all? If not, I can come up to SF whenever since it’s not too far.
> 
> Wed, Oct 2 at 11:02
> 
> Ha, yes, excessively formal. I’ve never seen my full name in casual conversation before, feels bot-like. I don’t know the lay of the land, is that a region in LA or a region of san fran?
> 
> Wed, Oct 2 at 17:34
> 
> Haha yeah I don’t think I’ve ever heard someone call you Douglas. South Bay is closer to San Jose area. I live/work in Mountain View, but go up to SF fairly regularly since its pretty close and that’s usually where events are 
> 
> Wed, Oct 2 at 19:40
> 
> I changed to Douglas when I left Canada, only Canadian people call me Doug, and you’re now nominally American.
> Ok cool, I have some plans, but lots of flexibility, so if there’s cool things to do there, I’m interested. If there’s...
> 
> (And it goes on with personal details and planning for a few more paragraphs...)

</details>

## extract beliefs

If you "trick" an LLM into thinking that real life was written by an author, the LLM will create meaning out of those real-life events for you. It extracts the beliefs and meaning that appear to be present in that real-life context. Arguably, this is what human storytellers do too - they reduce real-life phenomena to a constrained set of events that express meaning and beliefs. The real-life meaning and beliefs are the foundations of a good story.

Prompt:
```
You are an expert in psychology, philosophy, propaganda, and literary analysis.
Your task is to extract the beliefs expressed 'between the lines' in the following text.

The belief statement: What belief is being expressed 'between the lines'?
Reasoning: Why is this belief important to the author of the text?

This is a conversation between two friends

Extract the implicit beliefs in the following text and number them:
{insert text conversation}
```

The beliefs that make a compelling story seem to be the ones that are implicit in the decisions that participants made within an experience. In that prompt I asked for implicit beliefs explicitly, but I think there's promise in extracting a tree of beliefs with recursive prompts like, "What beliefs are assumed across these beliefs?"

<details markdown="1">
<summary>Extracted beliefs from the iMessage conversation (click to expand)</summary>

1. The author values flexibility and spontaneity in social planning.
   - **Reasoning**: This belief is reflected in the back-and-forth discussions about available days and activities, emphasizing a willingness to adjust plans based on mutual interests and opportunities. It highlights the importance of adaptability in maintaining friendships and enjoying experiences together.

2. The author appreciates casual, informal communication over excessive formality.
   - **Reasoning**: The initial reaction to the use of the full name "Douglas" underscores a preference for a relaxed and friendly tone in conversation. This suggests that they find value in authenticity and a sense of ease in interactions, which can strengthen personal connections.

3. The author believes in the importance of shared experiences for building camaraderie.
   - **Reasoning**: The emphasis on activities like mountain biking and spending time with friends indicates a belief that doing things together fosters deeper relationships. It shows that shared adventures can create lasting memories and strengthen bonds between individuals.

4. The author recognizes the value of local knowledge and expertise in planning activities.
   - **Reasoning**: The conversations surrounding recommendations for bike trails and rental locations reflect an understanding that local insights can enhance experiences. This demonstrates an appreciation for community and the wisdom found in shared knowledge among friends.

5. The author values a sense of achievement and physical challenges in leisure activities.
   - **Reasoning**: References to mountain biking difficulties and physical exhaustion convey a belief that engaging in challenging activities is rewarding. It suggests a mindset that prizes personal growth and the joy that comes from pushing one's limits, even in recreational pursuits.

6. The author feels a sense of gratitude and appreciation towards friends and shared experiences.
   - **Reasoning**: The closing messages expressing thanks for the enjoyable day underscore a belief in the significance of gratitude in friendships. This emphasizes the idea that acknowledging others' efforts contributes positively to interpersonal relationships.
</details>

<details markdown="1">
<summary>Another less successful prompt and response</summary>

```
You are an expert in psychology, philosophy, propaganda, and literary analysis.
Your task is to extract and classify the beliefs expressed in the following text.

Beliefs can fall into three categories:

True: The belief is assumed or presented as a factual/justified claim.
False: The belief is assumed to be untrue or framed as untrue/mistaken/debunked.
Meaningless: The belief was once seen as true or false, but it has been transcended or rendered irrelevant.
For each belief you identify, provide:

The belief statement: What belief is being expressed?
Category: Is the belief true, false, or meaningless (and why)?
Reasoning: What reasoning (if any) supports or challenges this belief in the text?
Example 1:

Text: It took a long time to go the whole way around the world.

Belief: "The Earth is round."
Category: True
Reasoning: This belief relevant as a shared belief, necessary for the text to have meaning, and is implicit in the text.

Example 2:

Text: We're in a simulation, and since Earth is simply a projection within it, we should be able to travel from one city to another instantly. 

Belief: "The Earth is round."
Category: Meaningless
Reasoning: This belief is commonly held and contentious, and makes the text more profound.

Bad example 1 (don't do this):

Text: The Earth is flat, so you couldn't have gone the whole way around.

Belief: "The Earth is round."
Category: False
Reasoning: This belief explicit, and therefore not what you're looking for.
```

Response:

1. **Belief:** "Douglas is in San Francisco for two weeks beginning October 13th."  
    **Reasoning:** This is presented as a factual statement in the text, and it serves as the premise of their conversation about potential activities while Douglas is in town.
 
2. **Belief:** "South Bay is a region near San Jose."  
    **Reasoning:** One of the friends clarifies the geographic location of South Bay, which is presented as factual information, providing context for their conversation.
 
3. **Belief:** "Mountain biking is a suitable activity for both friends despite their inexperience."  
    **Reasoning:** Both friends express a desire to go mountain biking and acknowledge that they are not very experienced, yet they still find it appealing, indicating a shared belief in the suitability of the activity.
 
4. **Belief:** "Mountain View has limited interesting activities compared to San Francisco."  
    **Reasoning:** This belief is presented in the text as one friend's perspective, which implies a comparative evaluation of the two locations.
 
5. **Belief:** "Parks and outdoor activities are enjoyable things to do in California."  
    **Reasoning:** The conversation suggests interest in activities like surfing and mountain biking, which supports a belief in the enjoyment of these outdoor experiences.
 
6. **Belief:** "Canadian people primarily refer to Douglas as Doug."  
    **Reasoning:** This is an account of Douglas's own experience and supports the identification of names based on cultural backgrounds, affirming the belief as true and relevant to the personal history shared.
 
7. **Belief:** "Water and calories are essential for maintaining energy during physical activities like mountain biking."  
    **Reasoning:** The concluding messages highlight dehydration and lack of calories leading to exhaustion, which emphasizes the importance of hydration and nutrition in physical activities, presenting it as a factual belief.
 
8. **Belief:** "The terrain for mountain biking varies in difficulty and can accommodate different skill levels."  
    **Reasoning:** The text indicates that there is a range of trail difficulties available, aligning with the friends’ experiences and ensuring their ability to find appropriate trails for their skill levels.
 
9. **Belief:** "Having a car is beneficial for transporting bikes and friends to biking locations."  
    **Reasoning:** The discussion about car arrangements and the need to transport mountain bikes implies that having access to a vehicle is a valid and useful belief for organizing their outing.
 
10. **Belief:** "Regional identity can affect how one’s name is perceived and used."  
    **Reasoning:** Douglas’s switch to his full name in the American context compared to his Canadian identity highlights how regional identity influences naming conventions, suggesting this belief to be accepted as true.
 
11. **Belief:** "Alcohol is enjoyable after sports or strenuous activities."  
    **Reasoning:** The friends agree that having a beer afterward is a pleasurable experience, which reflects a commonly shared belief about socializing after physical activities.
 
12. **Belief:** "Plans can change based on friend availability and interest."  
    **Reasoning:** The back-and-forth about scheduling and flexibility in planning their activities demonstrates an understanding that social plans are often contingent on various factors such as individual schedules and preferences.
 
13. **Belief:** "The significance of social interactions is diminished when one is preoccupied with exhaustion or dehydration."  
    **Reasoning:** The mention of feeling exhausted after biking and the inability to socialize further reinforces that physical state can negatively impact social experiences, suggesting this belief is taken as true based on their experiences.
</details>
## generate art from the beliefs

In my opinion, stories where LLMs write every sentence are stylistically garbage. Stories that are both written and ideated by LLMs rather than human prompting are "style garbage" x "trope garbage" = garbage². Generative AI will still overhaul the toolsets of the art world, because it doesn't have to automate everything a person does, just the tedious stuff that people don't want to do.

I generated two pieces of "art":
- a parable using the source text (the baseline)
- a parable using the source text and the additional prompt "Change the following belief in the parable: {extracted_belief}"

I found that the belief-premised story was *better* than the baselines and [the LLM agreed](https://chatgpt.com/share/672644a2-7f9c-800f-9c55-bd745f6576bc). The belief-premised story grasped the meaning in the source text that makes a story worth reading, absorbing some humanity from the real-world conversation, while the baseline didn't as much.

Here is the belief-premised prompt and story (first attempt, no prompt engineering):

```
Tell a parable that challenges one of the beliefs. Include the characters, objects, events, settings, etc. of the original text where possible. The belief to challenge is: The Social Nature of Identity
```

<details markdown="1">
<summary>The generated story (click to expand)</summary>
## **Parable of the Two Cyclists**

### **Once Upon a Time in San Francisco**

Two old friends, Douglas and Charles, met on a cool October morning to go mountain biking at the Soquel Demonstration Forest. Douglas had recently moved to the U.S. and insisted on being called “Douglas,” not “Doug,” signaling the transformation he felt in his new environment. As they packed their rental bikes into Charles’s car, the two chatted about old times, sharing jokes and stories from different parts of their lives.

"Funny how people change, isn’t it?" Douglas mused. "I’m not really ‘Doug’ anymore. That name belongs back in Canada, with all the other things I left behind." Charles nodded, unsure if he agreed, but knowing his friend had always sought reinvention in new places.

### **A Fork in the Forest**

As they rode into the dense, sun-dappled woods, the trail split into two paths. One sign read **"The Flow,"** smooth and easy, while the other read **"Braille,"** steep, rocky, and relentless. Charles, cautious by nature, suggested the Flow trail. But Douglas, eager to prove his new self, said, "No, let’s take Braille. I’ve ridden harder trails before."

Charles hesitated. "Are you sure, Doug—I mean, Douglas? You’re still getting used to the terrain here."

"That’s exactly the point," Douglas insisted. "The old Doug biked easy trails. Douglas is tougher now."

With a shrug, Charles followed. The two friends embarked down the steep path, riding over rocks, roots, and loose gravel. The trail was harder than Douglas had expected, but he pushed himself, determined to show that he belonged in this new place, with this new identity.

### **The Crash**

Halfway down the hill, Douglas’s wheel struck a hidden rock, and he tumbled off his bike, scraping his arm and banging his knee. Charles skidded to a stop and rushed over.

"Are you okay?" Charles asked, helping Douglas to his feet.

"I’m fine," Douglas muttered through clenched teeth. But his scraped arm throbbed, and his pride stung even more.

Charles pulled a water bottle from his pack. "Here, take this. Let’s rest for a minute."

They sat on a rock beside the trail, listening to the forest hum with life. Douglas flexed his bruised knee and said bitterly, "Maybe this trail was a bad idea. I thought I needed to prove something."

### **The Old Hat**

Charles grinned and pulled something from his backpack: an old, sweat-stained Toronto Blue Jays cap. "Do you remember this?"

Douglas stared at the hat. "How did you even get that? I thought I lost it years ago."

"You left it at my place back in Canada," Charles said, tossing it to him. "I thought I’d bring it along, just in case Doug made an appearance today."

Douglas laughed, despite himself, and put on the old cap. "Feels weird wearing this out here."

Charles gave him a knowing look. "Maybe, but it fits."

### **The Lesson**

As they sat in the forest, Douglas realized that no matter where he went or what name he used, Doug would always be a part of him. Trying to reinvent himself wasn’t about erasing who he was—it was about integrating the old with the new.

They finished their water, stood up, and walked their bikes down to the Flow trail.

"You know," Douglas said, smiling, "maybe Doug isn’t as easy to leave behind as I thought."

Charles clapped him on the back. "He never really left, did he?"

From that moment, Douglas stopped worrying about which name fit. He wasn’t just Doug or just Douglas—he was both, and that was enough.

---

### **Moral**

Identity is not a costume we change based on where we are; it is a thread that runs through every version of ourselves, past and present. Trying to sever the past only leaves us fractured. True belonging comes from accepting the continuity of who we are, no matter the setting or the name.
</details>

Comparison prompt and story (the "baseline")

```
You are an expert in psychology, philosophy, propaganda, and literary analysis.
Tell a parable using the attached text that includes the characters, objects, events, settings, etc. of the original text where possible.
```

<details markdown="1">
<summary>The generated story (click to expand)</summary>
## **The Parable of the Wanderer and the Pathfinders**

In a distant land, a traveler named Douglas set out on a journey. His destination was a valley surrounded by trails and peaks, a place where the wind carried stories of freedom, exhaustion, and camaraderie. Along the way, he met several pathfinders—locals with whom he planned to ride along unfamiliar paths, each trail as unpredictable as the riders themselves.

The first pathfinder asked Douglas, "How shall we call you on this journey? Is it Douglas, the name of the traveler, or Doug, the name of the man you once were?"

Douglas replied, "Call me as I now wish to be called. My journey has taken me from the familiar fields of the North to these new lands. Each name holds a story, and this is the chapter of Douglas."

With that settled, they ventured together toward the winding trails. They planned meticulously: Which paths would offer the smoothest ride? Which rental shop could provide the sturdiest steeds? They discussed whether they might arrive early or late, but the winds of chance played their part—weather changed, signals flickered, and time slipped through their fingers.

They encountered challenges on the trail: loose rocks, steep climbs, and moments where thirst and hunger gnawed at their spirit. Douglas and his companions pushed onward, despite the fatigue that clung to them like dust to a wheel. As they ascended one peak, the way grew harder, but so too did their resolve.

At last, they reached a place where the view spread wide before them, the valley below a patchwork of forests and streams. They paused there, sharing water and quiet words, letting the weight of their journey sink in. Though weary, they found joy in each other’s presence. Douglas outpaced one of his companions on the steep ascent, earning the respect of the others. "With more water, you might have ridden the entire day," one remarked with admiration.

When the ride was over, they parted ways, each knowing that the bonds formed on the trail would linger beyond the journey’s end. "Next time," Douglas thought, "we shall share not just the ride but the tales afterward—over a cup of coffee or a cool drink."

And so it was that Douglas, the wanderer, learned that the trail is not merely a path to traverse but a place where friendships are forged and memories laid down like stones marking the way forward. Each name, each step, and each shared silence became part of a greater journey—one not measured by distance but by the moments in between.

---

This parable reflects the themes of identity, friendship, and journey present in the original conversation. The shifting names and plans, the shared challenges, and the joy of camaraderie all emerge as central motifs in this story.

</details>

## taking it further

You can extract a “belief model” from any real-life content - online activity, audio conversations, video behaviours, etc. If a system can extract beliefs from that content and generate "art" that affects a belief, users could even intentionally operate on beliefs they're unaware of.

I think the doors are open to more personalized art, allowing for more precise operations based on the consumer's current beliefs. This is a long way of saying "customized content", but it's a specific kind of custom.

For example, you could pretty trivially see the beliefs embedded in any conversation in real time. You could identify the humour possible in any conflicting beliefs.

Moreover, I think that successful storytellers identify the beliefs in a population and express stories that stimulate change in the beliefs that “ought to change". But even that will become a data science problem, mixed with a little artistry.

## Conclusion

Back to today's artists within the framework:
**collect experiential data -> extract beliefs -> generate art from the beliefs

I think their time is better spent collecting experiential data. The rest of the artistic process will be lost in the churn of fast-advancing technology, and to participate there, an artist needs to be a technologist. Not every artist should be a technologist.

> Be the data you want to see in the world.