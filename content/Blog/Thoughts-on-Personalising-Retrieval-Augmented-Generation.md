---
title: Thoughts on Personalising Retrieval-Augmented Generation
date: 2024-12-23T23:00:00.000Z
---

I've been thinking about personalising Retrieval-Augmented Generation (RAG) lately. This is partly because my team is now building a chatbot that answers questions using a RAG setup. It's a continuation of my work with a previous team, where we developed a search system for market research content. Both products rely on the same underlying data, but the chatbot offers a modern, AI-driven, user experience.

In the search system, personalisation usually meant boosting documents based on signals like the categories of the users' most-visited documents. Now, with the chatbot, we're revisiting personalisation in a slightly different context, and it's got me reflecting on how it can work effectively. These are just some initial ideas, and I'm not claiming to have all the answers—but I thought it'd be worth putting them out there.

# What Are We Trying to Achieve with Personalisation?

Let's start with a classic example: a user types "cheese" into our RAG system. What do they actually want? They could be interested in recent marketing campaigns for cheese, looking for consumer preferences, or focused on specific markets like the UK or US. The query is so vague that it's hard to produce a useful answer.

Contrast this with a much more specific query: "What are the latest trends in cheddar consumption in the UK?" That's clear, and it gives the system a much better shot at providing a meaningful answer.

So, where does personalisation fit in? If the query is already specific, I don't think personalisation adds much value. A well-designed RAG system—both the search and the answer generation—should handle specific queries effectively by retrieving the most relevant documents and using them to produce a coherent, accurate answer. But for vague queries like "cheese," personalisation can step in to improve the process.

# A Personalisation Proposal

Here's the main idea: use personalisation to help expand under-specified queries.

Imagine this: the query and previous messages in the conversation are passed through a personalisation step. This step evaluates the query to see if it's specific enough. If the query is under-specified, the step enriches it with context about the user (e.g., their preference for UK-specific data).

From there, the personalised query is sent to the search engine, which retrieves the most relevant documents. These documents, along with the personalised query, are then passed to the language model to generate a final response.

# What About Collecting Preferences?

I haven't said much about how we'd gather user preferences—partly because I think it's a separate problem. In the past, we've kept track of things like the categories users visit most often, and I imagine something similar could work here.

Alternatively, we could ask users directly about their context. For example, when they register, we could prompt them to choose a focus area or specify regions they're interested in. Either way, the real challenge is figuring out how to use this information effectively, not just how to collect it.

# Final Thoughts

Personalising RAG systems isn't about fixing things that already work. If the user provides a clear, detailed query, the system doesn't need much help. But when faced with vague queries, personalisation could help by guiding the system in the right direction.

These ideas aren't revolutionary, and they might not even work in practice, but they feel like a promising starting point. What do you think? Does this approach make sense, or are there better ways to think about personalisation in RAG? Let me know—I'd love to hear your thoughts.

---

This blog post was made with the help of Gemini Experimental 1206.
