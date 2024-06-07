---
title: Extracting features from LLMs
---

A few weeks ago Anthropic came out with \[this paper]\([https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)), showing how they found interpretable features in one of their models. This means that they could see which features activates when the LLM generates, and the feature could be scaled up and down to make the generation more or less focused on that feature. For example, their "Golden Gate Claude" model, with the Golden Gate feature boosted to the max, kept steering the conversation to talk about the Golden Gate.

Yesterday OpanAI release \[a similar paper]\([https://openai.com/index/extracting-concepts-from-gpt-4/](https://openai.com/index/extracting-concepts-from-gpt-4/)). Maybe the high pace of news in AI are enough to make groundbreaking research seems underwhelming, but this new paper seems weak.

They extracted 16 million features. Who needs 16 million features?!? We are trying to understand, in human terms, how these things work. For that we need to find ways to get them down to human scales. How many characteristics can you find in a person? For example, someone might be a great leader, very inspiring, but also a bit rush, and cannot stop fidgeting their legs. Can you think about 100 basic characteristics for people? Yeah, potentially. Obviously these are going to be a reduction of who this person really is, but so do the 16 million features in OpenAI's research.

To be fair here, Anthropic encoded 1 million, 4 million, and 34 million features, so they didn't scale the problem down really to human scales either, but the way they talk about their research is less about the number of features and more about extracting meaning from the model.

The second reason for the OpenAI research to seem weak is the examples they give for feature activation. Take this snippet for example:

```
most people, it isn't. We all have wonderful days, glimpses of what we perceive to be perfection, but we can also all have truly shit-tastic ones, and I can assure you that you're not alone. So toddler of mine, and most other toddlers out there, remember; Don't be a
```

\
If I tell you to mark the words / phrases associated with 'phrases relating to things (especially humans) being flawed', what would you mark? I would probably mark 'we can also all have truly shit-tastic ones' and 'you're not alone'.

Here's what the extracted feature, matching this description, picked:

![](</Screenshot from 2024-06-07 09-36-43.png>)

One last thing that is very important to note here. I might have no idea what I'm talking about. My understanding of the internals of these technologies is very limited.
