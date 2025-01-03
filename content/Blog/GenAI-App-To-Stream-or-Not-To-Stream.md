---
title: 'GenAI App: To Stream or Not to Stream?'
date: 2025-01-03T16:00:00.000Z
---

Generative AI applications, particularly those with LLM-powered chat interfaces like ChatGPT, stream responses. We type our query, and the answer gradually generates, word by word. This streaming approach has become so commonplace that it's almost expected. But is it always the best approach?

# The cost of streaming

As you might know, I work on a Retrieval-Augmented Generation (RAG) application. This application currently streams responses, providing a familiar user interface. This comes at a cost. In my experience it's much harder to develop a streaming application, here's why.

- **Incremental processing:** With streaming, we often need to process the token stream incrementally. This adds complexity when dealing with various markups the LLM is instructed to use. For example, we tell the LLM to refer to the sources provided, so it might output something like `Grass is green [1]`, where `1` refers to the first source provided. Behind the scenes we replace the `[1]` markup with a nicely rendered reference component. Another example is the instruction to the LLM to respond `<no-answer>Explain why you failed to answer here.</no-answer>` when it fails to answer with the provided sources. This is parsed and logged, and is used to change the logic of the execution slightly. There are a few other examples of markups the LLM is instructed to use, but you get the idea. Handling these markups is significantly easier when the entire response is available.

![Rendering a reference component in the middle of an answer]({static}/images/blog/leap_reference.webp)

- **API response:** Managing the communication between the backend and frontend is more intricate with streaming. We utilize [Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events), which, while effective, is less straightforward than simply responding with a JSON object.
- **Frontend Handling:** The frontend must handle the incoming stream of tokens, requiring more complex logic than simply displaying a complete response. For example, the response uses markdown, which is not trivial to process incrementally. In addition, the custom components we inject into this markdown for references and the like make it even harder.
- **Storage and Retrieval:** Streaming introduces complexities when it comes to storing and retrieving complete answers. For analytics purposes and to enable features like saving or sharing conversations, we need to store the full, generated response. This means that even if we stream the answer to the user, we have to simultaneously assemble the full response in the background for storage. When users later access their saved conversations, we have a non-streaming response to deal with. This creates duplication in our system: a streaming path for initial answer generation and a non-streaming path for displaying stored answers, increasing the overall system complexity. Essentially, we have to develop a way to convert a stream into a full answer for storage, and then present it to the user in its complete form later on.

We are a small team of three developers. This significantly amplifies the impact of the complexities above.

Now, you should say: these are just technical complexities that are required for this type of product. Live with them! That's what your company is paying you for. Isn't it?

# LLMs are getting faster

When we first launched this system at the beginning of 2024, generating a full answer took around 30 seconds. In such a scenario, streaming was a necessity. Without it, users would be staring at a blank screen for what seems like an eternity in web standards. Streaming allowed the user to start reading the response after just a few seconds, providing a much better user experience.

Since the launch, the time required for preprocessing a query before we start answering has at least doubled. We introduced LLM-based translation stage, which improves the performance of the system for non-English queries. Another preparation stage that takes the query and the chat history and produces a search phrase. Without this stage, questions like 'more info please' could not work in conversational settings. There's also a reranking stage now, after fetching search results. All of these changes improved the quality of the answers significantly, or allowed completely new modes of interaction (in the case of the search phrase stage) at the expense of longer time until the answer starts to stream.

Despite the increased preprocessing time, the actual answer generation now streams in at around 10 seconds on average. This is only due to the improved speed of newer LLM models. So while the preprocessing time doubled, the answer generation shrank to about a third of the initial duration. Overall, the ratio of time spent in answer generation is decreasing.

You could argue that streaming remains preferable, as it provides users with initial content sooner. But consider that: when we launched, the ratio of time spent in answer generation was about 90% of the response time. These days it's closing to 50%. We're moving towards a scenario where the majority of time is spent preparing to answer, and less time actually generating the answer.

Check out the impressive speed offered by Cerebras. [They can stream from Llama 3.1 405B - a GPT-4 class model - at 969 tokens per second](https://cerebras.ai/blog/llama-405b-inference). The answers by our system are about 400 words. This translates to roughly 533 tokens, according to [OpenAI's estimation of 3/4 words per token](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them). This means that they can generate an answer in much less than 1 second.

If such performance becomes commonplace, the time spent on answer generation will be dwarfed by the preprocessing steps within the RAG pipeline. Given these factors, there's a strong case for transitioning from a streaming to a non-streaming model. It's simpler and cheaper to develop and maintain, and in the long run, may not have any disadvantage to its streaming counterpart.

# A reason to stream

There's still one very compelling reason to retain streaming: user expectations. In the rapidly evolving world of GenAI, streaming has become the established standard, particularly for chat-based applications. Users are now used to this interactive style of response delivery, largely thanks to the influence of prominent products like ChatGPT. Diverging from this norm, even with a technically sound rationale, carries a significant risk. A non-streaming response might be perceived as 'broken', 'slow', or 'inferior' simply because it deviates from the established user experience. This presents a difficult product dilemma: how do we balance the internal benefits of increased team efficiency and reduced development overhead against the potential negative perception of users accustomed to the streaming standard?

# Conclusion

These days, streaming is undoubtedly the de-facto standard for GenAI applications, particularly in chat interfaces. The influence of leading products has firmly established this pattern in users' minds. Personally, I believe that with the ongoing acceleration of LLM generation speeds, we will see a gradual decline in the prevalence of streaming. The benefits of instantaneous, full responses will start to outweigh the perceived advantages of a token-by-token reveal. However, as a developer working on a GenAI application, it's a challenge to even consider moving away from streaming, especially when your application already streams responses. The established user expectation is a powerful force. Yet, the efficiency gains that could be realized by making the change are worth thinking about. We could streamline development, simplify our architecture, and potentially deliver a more robust and feature-rich experience in the long run.

---

This blog post was made with the help of Gemini Experimental 1206.
