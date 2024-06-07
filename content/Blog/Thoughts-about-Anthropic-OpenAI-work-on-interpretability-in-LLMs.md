---
title: 'Thoughts about Anthropic / OpenAI work on interpretability in LLMs'
date: 2024-06-07T10:00:00.000Z
---

A few weeks ago, Anthropic came out with [this paper](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html), showing how they found interpretable features in one of their models. This means that they could see which features activate when the LLM generates, and the feature could be scaled up and down to make the generation more or less focused on that feature. For example, their "Golden Gate Claude" model, with the Golden Gate feature boosted to the max, kept steering the conversation to talk about the Golden Gate.

Yesterday, OpenAI published [a similar paper](https://openai.com/index/extracting-concepts-from-gpt-4/). Maybe it's just me, or the high pace of news in AI is enough to make groundbreaking research seem underwhelming, but this new paper seems lacking in comparison. Note that my understanding of the internal workings of these models, and the two studies above, are very limited, so take this with a grain of salt. Having said that, here are some thought for why the OpenAI paper is underwhelming.

They extracted 16 million features from their GPT-4 model. Who needs 16 million features?!? We are trying to understand, in human terms, how these things work. For that we need to find ways to get them down to human understandable scales. How many characteristics can you find in a person? For example, someone might be a great leader, very inspiring, but also a bit rush, and cannot stop fidgeting their legs. Can you think about 100 basic characteristics for people? Yeah, potentially. Obviously these are going to be a reduction of who this person really is, but so do the 16 million features in OpenAI's research. If the goal is interpretability, then extracting that many features "that we hope are human interpretable" doesn't seem like the best approach.

To be fair here, Anthropic encoded 1 million, 4 million, and 34 million features, so they didn't reduce the problem to a more human-understandable scale either, but the focus of their research is not the number of features, and how well they cover the model capabilities, and more about extracting meaning from the model.

The second reason for the OpenAI research to feel weak is the examples they give for feature activation. Take this snippet for example:

> most people, it isn't. We all have wonderful days, glimpses of what we perceive to be perfection, but we can also all have truly shit-tastic ones, and I can assure you that you're not alone. So toddler of mine, and most other toddlers out there, remember; Don't be a

If I tell you to highlight the words / phrases associated with 'phrases relating to things (especially humans) being flawed', what would you do? I would probably highlight 'we can also all have truly shit-tastic ones' and 'you're not alone'.

Here's what the extracted feature picked:

![A snippet of text with the phrases 'but we' and 'you that you're' highlighted.]({static}/images/blog/openai_human_imperfection_feature_extraction_example.png)

This is not an isolated critique. It is the first example provided in their blog post.

Having said all of that, I would love to see more work on interpretability of these models, both from OpenAI and Anthropic.
