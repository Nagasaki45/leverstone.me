---
title: Andrew Ng's advice for iteratively writing LLM prompts
date: 2024-05-19T23:00:00.000Z
---

When building complex workflows, I see developers getting good results with this process:

* Write quick, simple prompts and see how it does.
* Based on where the output falls short, flesh out the prompt
  iteratively. This often leads to a longer, more detailed, prompt,
  perhaps even a mega-prompt.
* If that’s still insufficient, consider few-shot or many-shot learning (if applicable) or, less frequently, fine-tuning.
* If that still doesn’t yield the results you need, break down the task into subtasks and apply an agentic workflow.

[Source](https://info.deeplearning.ai/openais-rules-for-model-behavior-better-brain-controlled-robots-alphafold-3-covers-all-biochemistry-ai-oasis-in-the-desert)
