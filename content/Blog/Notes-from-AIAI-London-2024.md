---
title: Notes from AIAI London 2024
date: 2024-11-08T10:00:00.000Z
---

![AIAI GenAI Summit]({static}/images/blog/aiai_gen_ai_summit.webp)

I attended the AI Accelerator Institute's Generative AI Summit that happened yesterday in London - AIAI London in short. Here are my notes. These are by no means exhaustive. Just a bunch of things I found interesting.

# Themes

- Multiple talks implied that companies struggle to get GenAI applications to production, or getting value from them. These talks focused on best practices for building AI applications (make sure there are guardrails in place, develop evaluation tools, etc.) or on making sure the applications produce value. As someone who works on a GenAI application that is in production for almost a year I was a bit surprised. It felt like there's an underlying problem of companies trying to come up with AI solutions for the sake of it (the "everything is a nail" problem).
- LLM as a judge is a common practice, and proved to be useful in large variety of cases. From my recent experience evaluating our GenAI application with the help of LLMs I'm not surprised (stay tuned for a blog post about this subject). This is a very powerful technique.
- Two talks about GenAI in healthcare stressed the point that we shouldn't let GenAI take decisions. The final decision, at least for now, should always be done by a human. AI can help us get to these decisions faster. This approach aligns with [my thoughts about AGI]({filename}/Blog/Thoughts-about-AGI.md), that we are not ready for AI to take decisions, not because of AI capabilities, but because of social structures and ethics that help us navigate decision making.
- There were some discussions about safety. It wasn't about 'AI will kill us all', but about ensuring we build AI applications that do no harm, either to people or to the companies that develop them. A few speakers tackled these from different angles: healthcare, regulation (e.g. the EU AI Act), and the importance of putting guardrails in place when developing GenAI applications.

# Talks

These are the talks that stood out to me personally.

- **"Can't I just ask ChatGPT?" Production pipelines shaping the visual intelligence renaissance**. Dr. Dmitry Kazhdan from Tenyks talked about how new GenAI models simplifies and democratise the computer vision landscape. Instead of long and expensive processes for training AI models in house, most modern computer vision applications can be built using off-the-shelf AI models. The training process is replaced by prompting, potentially with minor fine-tuning. I'm not a data scientist, and have no interest in computer vision, so why did this talk speak to me? Mainly because it was full of excellent insight about building advance search capabilities on top of videos. For example, they discussed techniques to extract metadata from the raw material at index time, and how to search through this metadata on simple queries, or fallback to vector search on more complicated queries. I need to dig through [Tenyks' blog](https://www.tenyks.ai/blog) to learn more about these ideas. I expect these to be super valuable for the work I'm doing.
- **Optimising GenAI outcomes in financial services with DSPy**. This very technical talk by Alberto Romero from Citi showed how to use DSPy to optimise system prompts, including few-shot, and chain-of-thought techniques, with examples and metrics. I was aware of DSPy, but nothing more than that. As mentioned earlier, I invested a lot of time recently on our quality evaluation suite. A few days ago I claimed that "we cannot achieve a higher groundedness  score (also known as faithfulness score) with prompt changes alone". This DSPy talk inspires me to try to automatically optimise for this metric. I still suspect that we are close to hitting a limit. We might be able to optimise for this metric on the expense of some other goals. In any case, that would be an interesting experiment.
- **Large language models in practice: Insights from building LLM-based pipelines for paediatric healthcare data**. This talk by Pavithra Rajendran and Shiren Patel from the NHS had two equaly interesting parts. First, Shiren dived into goals and design principles for AI applications for healthcare: human-in-the-loop, do no harm, explainability, and focusing on making clinicians more efficient, among other ideas. The second part, by Pavithra, was more technical. The NHS has to run everything in house and got no budget for expensive GPUs (surprise surprise) so the AI team had to figure out ways to work with very small LLMs that can run efficiently on CPUs. They showed a few examples of successes from running these models.

# Small talk

Beyond the presentations, I enjoyed the chats I had with the attendees. In most (if not all) of the conferences I've been to before I barely had any interactions with others. Granted, this was a long time ago, so maybe I changed, but I think people were more approachable than I'm used to.

I met two familiar faces and enjoyed hearing what they do these days. I had interesting conversations about relationships between productivity and religion, measuring carbon footprint of aeroplanes from satellite images, [thoughts about social readiness to GenAI and AGI]({filename}/Blog/Thoughts-about-AGI.md), how ChatGPT is way more 'human' in voice mode, and more.

In conclusion, I had great time at AIAI London. I learned a few tricks, got inspiration to try a few ideas, met interesting people, and enjoyed the presentations and the conversations I had.