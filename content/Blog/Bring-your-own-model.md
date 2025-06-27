---
title: Bring-your-own-model
date: 2025-06-27T11:00:00.000Z
---

AI is showing up in every app, and so are the subscription pop-ups. It feels like every new feature wants its own monthly fee. This makes sense from one perspective: running large language models is expensive. The old web model, where tiny per-user costs could be covered by advertising, doesn't work when a single request costs a noticeable amount of money. But this path leads to an expensive and exhausting future of juggling dozens of AI subscriptions.

Instead of paying every service for their AI, what if you could **just bring your own?**

The Model Context Protocol (MCP) includes a feature called [*sampling*](https://modelcontextprotocol.io/docs/concepts/sampling), which allows a server to *request* inference from the user's client. This shifts the compute and control from the server to the user's side.

Two days ago, Anthropic announced a related feature on its Claude platform. Developers can now [build and share AI apps](https://www.anthropic.com/news/claude-powered-artifacts) that call Claude for inference. The crucial part is the economics: when someone uses your app, the computation runs on *their* Claude account. Their subscription covers the cost, not yours. As the developer, you pay nothing for their usage.

This is the sampling idea packaged differently. Both concepts flip the standard SaaS model on its head. The service brings the expertise, workflow, and data, but the user provides the expensive resource—the model inference, the brain of the system.

Imagine if this wasn't just a feature of a developer protocol like MCP or a single platform like Claude. What if it were a core capability of your browser or operating system? You'd have a primary subscription to a model provider of your choice—be it OpenAI, Anthropic, Google, or even a powerful open-source model running locally. When you visit a website or use an app that needs AI, it would request access to *your* model through a standard API.

The app provides the interface, the unique workflow, the clever prompts. You provide the engine.

This model solves the subscription fatigue problem for users and lowers the barrier to entry for developers, who no longer have to foot the bill for inference.

Of course, this model isn't a silver bullet. New questions arise immediately. How does an app guarantee a quality experience if it doesn't know which model the user will bring? A frontier model will give better results than a smaller one, but perhaps fast and cheap is better for a specific application. The app could specify a minimum required capability, and your system would provide the best-matching model it has.

And what about security? An AI with access to your local context is incredibly powerful for personalization but also a potential privacy risk. That said, I would rather trust my browser, with its mature security and sandboxing models, to manage that permission than dozens of web apps.

I don't know if this "bring-your-own-model" future will happen, but it's a compelling alternative to the subscription-for-everything world we seem to be building. It reframes the question from "How does this service pay for its AI?" to "How can this service best use the AI I already have?" That's a shift that promises a more sustainable and powerful future for developers and users alike.

---

This blog post was made with the help of Gemini 2.5 Pro.