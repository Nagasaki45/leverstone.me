---
title: OpenAI Model Spec
date: 2024-05-08T23:00:00.000Z
---

OpenAI has recently published a document titled ['Model Spec'](https://cdn.openai.com/spec/model-spec-2024-05-08.html). It defines an ethics and norms framework models should follow. A few things that stood out:

* It surprisingly resembles Isaac Asimov's "Three Laws of Robotics", with a 'chain of command' for resolving conflicting objectives. The logic is `Platform > Developer > User > Tool`. The platform consists of the instructions given to the model by OpenAI themselves (training, reinforcement learning from human feedback, and platform message that is added before the system message). The term 'developer' here refers to what was previously known as the system role message. User and tool are self explanatory, I think. Then, the document provides numerous examples of conflicts, demonstrating the preferred resolution for each.
* The document gives a lot of context for the difference between a developer/system messages and user messages. I think that's quite important to understand to improve prompting.
* The document mentions settings that can be passed to message objects. One of them is `interactive` (a boolean). The document describes in length how this can change the behaviour of the assistant, to tune the assistant for interactive chat behaviour (the default) or for single response. The differences are quite striking. I couldn't find anything about this in the API docs. I wonder if it's worth trying playing with this against the actual API to see if this is implemented but not yet documented.

The document is lengthy, but I think worth reading, or at least skimming through.
