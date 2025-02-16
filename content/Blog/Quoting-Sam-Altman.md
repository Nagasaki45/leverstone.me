---
title: Quoting Sam Altman
date: 2025-02-16T00:00:00.000Z
---

A few days ago Sam Altman shared an [update about OpenAI's roadmap on twitter](https://x.com/sama/status/1889755723078443244). Here's what I'm reading between the lines:

> We hate the model picker as much as you do and want to return to magic unified intelligence.

He's talking about ChatGPT, not the API. Is this where the focus is?

> We will next ship GPT-4.5, the model we called Orion internally, as our last non-chain-of-thought model.

For my understanding there's a lot of value in "small" models like 4o-mini, Gemini flash, etc. These are generally faster and cheaper than their larger siblings, and perfectly adequate for many tasks. I think this is also reflected in the wide range of sizes of open weights models. The point here suggests that OpenAI are confident they can compete in the space of "small" models with only chain-of-thought models. This is interesting because like there's always a performance penalty for this type of models - their thinking time until the final output starts.

> After that, a top goal for us is to unify o-series models and GPT-series models by creating systems that can use all our tools, know when to think for a long time or not, and generally be useful for a very wide range of tasks.In both ChatGPT and our API, we will release GPT-5 as a system that integrates a lot of our technology, including o3. We will no longer ship o3 as a standalone model.

There's a lot to unpack here:

* The future of OpenAI is an intelligent software system that does a lot behind the scene. This is different to what we are used to now (especially when using the API). At the moment we interact with a model. In the future we will interact with a more complex software system. One can say the differentiation is pointless, because the models themselves are black boxes, but I tend to disagree. First, models have relatively clear performance behaviour - I know the time to first token and tokens per second and can consider these when developing an application around LLMs. If my application changes its time to first token from 1 second to a few 10s of seconds because of user input that's a problem. Second, we match the model we use to the problem we are trying to solve. We don't always need more intelligence. If this is something that can be triggered by user input that might also be a problem.
* If GPT 5 is not going to be a new kind of intelligence we didn't see before, what does it say about OpenAI's AGI mission?

> The free tier of ChatGPT will get unlimited chat access to GPT-5 at the standard intelligence setting (!!), subject to abuse thresholds.Plus subscribers will be able to run GPT-5 at a higher level of intelligence, and Pro subscribers will be able to run GPT-5 at an even higher level of intelligence. These models will incorporate voice, canvas, search, deep research, and more.

So, in the future there's just one model, or rather a software system orchestrating multiple models, to which the only parameter is the intelligence level. This sounds potentially simpler than picking a model, but might also mean less opportunity to tune the system to someone's needs.

***

Overall, to me, it all sounds great for serving ChatGPT users. It doesn't sound very appealing for builders of applications on top of OpenAI's APIs. On the other I think it's great that OpenAI keeps innovating. I don't think the future of AI is necessarily about the best intelligence. There's a lot to be gained from better software systems that wrap models. Even if OpenAI ends up being more consumer focused there's enough players that can push the enterprise use case forwards and overall the field will benefit from the diversity.
