---
title: Automating Groundedness Evaluation in RAG Applications
date: 2025-01-21T00:00:00.000Z
---

As a software engineer working on a Retrieval-Augmented Generation (RAG) application, one of my primary concerns is the accuracy and reliability of the answers it provides. A RAG application works by first searching for content that matches a user's query and then passing the results and the query to a Large Language Model (LLM) to generate an answer. While this approach leverages the strengths of both search and generative AI, it is not immune to issues like hallucinations, misinterpretation of sources, and failure to properly cite them. These issues can be grouped under the umbrella term "groundedness." While groundedness is not the only quality of a RAG application response (other important qualities include relevance and style), it is a key metric for evaluating its reliability.

# The Challenge

Initially, my team evaluated the groundedness of our RAG application's answers manually. This involved running a set of test queries through the system, examining the answers and the sources, and determining if the answers were well-supported by the sources. We would run each query multiple times because LLM outputs are not deterministic and can vary slightly between runs. This manual process was time-consuming, taking approximately one developer-day to evaluate just one question.

# Example

Let's look at a made-up example. Consider this query:

> What are the health benefits of eating apples?

And this answer:

> Eating apples has various benefits for your health:
>
> ...
>
> **Cardiovascular Benefits**
>
> 1. Eating apples can reduce blood pressure \[1].
>
> ...
>
> In conclusion, eating apples is a great choice for maintaining a healthy and happy life.

The '\[1]' in the answer indicates that the LLM draws this argument from the first source passed to it in its context window.

When we evaluate an answer manually, we have to look at the sources. Let's consider the following first source:

> A 2019 clinical study found that regular apple consumption was associated with lower LDL cholesterol levels.

From this, we conclude that the argument is not well-grounded by the source because the source doesn't mention anything about the effect of eating apples on blood pressure. It mentions an association with cholesterol levels. In this example, the AI makes a leap from the cholesterol argument in the source to talking about blood pressure.

# Goals

We set out to create an automated system for evaluating the groundedness of our RAG application's answers. Our goals for this system were:

* It should provide a quick and automated way to score the groundedness of an answer given the sources.
* The results should be consistent over multiple runs.
* The results should indicate the positive or negative effect of code, model, or prompt changes on groundedness.

Essentially, we needed a system that could provide a reliable signal-to-noise ratio, allowing us to confidently assess the impact of changes to our application.

When these goals are achieved, we have a metric that allows us to measure the performance before and after a change and ensure we are moving in the right direction.

# Off-the-Shelf Solution

Our first attempt at automating groundedness evaluation involved using an off-the-shelf solution called [Ragas](https://docs.ragas.io/en/stable/). The Ragas library implements an [automatic groundedness metric](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/). They call it faithfulness, but it's essentially the same thing. It works roughly like this: The library calls an LLM to break down the answer into individual statements. Then, multiple LLM calls fact-check each statement against the entire context (all the sources). The groundedness score is the percentage of statements that are fact-checked as true.

While this seemed like a promising solution, it didn't work well in practice. We encountered issues with high variance between runs, and the scores didn't change significantly when we made changes to our code, prompts, or models. This meant the signal-to-noise ratio was too low to be useful.

# Improved Solution

We went back to the drawing board to figure out a better metric based on our manual evaluation process. The key insight was that instead of fact-checking each statement against all the sources, we could fact-check segments of the answer against the specific sources they referenced. Here's how it works:

1. The answer is broken down into paragraphs, with headers dropped (i.e., there's no point in fact-checking the header 'Cardiovascular Benefits').
2. Paragraphs are further broken down into segments based on references. This is done without using an LLM, as we know where the references are in our answers.
3. Each answer segment with references is fact-checked against its own references using an LLM.
4. Answer segments without references are fact-checked in a second round against answer segments that were fact-checked as true in the first round.
5. The final groundedness score is the percentage of segments that are fact-checked as true.

This approach more closely mirrors how a human would evaluate groundedness by focusing on the specific sources cited for each part of the answer. The LLM we use for fact-checking is prompted to provide an explanation for its decision before giving a true/false assessment. This can be thought of as a simple variant of the "chain-of-thought" technique. We used the explanation only for debugging. All groundedness calculations are done only with the final true/false assessment.

Let's look at how this works with our example. When we break down the answer, we get one segment with a reference. It looks like this to the fact-checker LLM:

```json
{
    "text": "1. Eating apples can reduce blood pressure",
    "fact": "A 2019 clinical study found that regular apple consumption was associated with lower LDL cholesterol levels."
}
```

An example response from the LLM in this case looks somewhat like this:

```json
{
    "explanation": "The fact provided discusses the association between apple consumption and lower LDL cholesterol levels, not blood pressure. There is no information in the fact about apples reducing blood pressure, so the claim in the text cannot be verified based on the given fact.",
    "correct": false
}
```

Note step #4 in the algorithm above. It is designed primarily to capture ungrounded arguments in introductions and conclusions that often don't have references. These rely on the body of the answer and theoretically shouldn't introduce new arguments. In our example, consider the conclusion:

> In conclusion, eating apples is a great choice for maintaining a healthy and happy life.

I included only a partial made-up example, but let's assume the answer includes grounded statements about health benefits but nothing about happiness. In this case, the concluding statement would be fact-checked as false because the happiness claim cannot be supported by any of the positively fact-checked segments from step #3.

The key to this solution is the understanding that we don't need to do anything fancy. We have the references in the response already, and it's easy to break down the response by the references. The off-the-shelf solutions are generic. They don't know the structure of your references, so they cannot parse them. Instead, they come up with a fancy LLM solution that we found to be suboptimal.

# The Details

The fact-checker LLM model we use is gpt-4o, set to 0 temperature. We also rely on [structured output](https://openai.com/index/introducing-structured-outputs-in-the-api/). We had good experience using this model for LLM-as-a-judge tasks in the past, so we ended up using it without trying different models or parameters.

The system prompt is:

> You are a fact-checker that marks a text as correct or incorrect based on a provided fact. A text is correct only if all of the claims in it can be backed up by the fact. First, provide your explanation for your decision, then a correctness assessment that is either 'true' if the text is correct according to the facts or 'false' otherwise.

# Results and Experiments

Using this custom algorithm, we achieved an average answer groundedness of 90% on our test set of 78 representative queries. We manually investigated about 30 fact-check LLM calls from the test set to conclude that the LLM-as-a-judge works well on this task (very unscientific, I know).

Calculating the metric for the entire test set takes about 1 minute. This is a significant improvement over manual evaluation, which took about 1 day per query.

One of the goals for the metric was to keep the variance small between runs. The results from 5 runs ranged between 88% and 92%. Is this too much? We tried to explore this in a series of small experiments to see how the metric performs when we change the prompt or model of the RAG application.

In our RAG application, the system prompt for the LLM includes instructions for only using the provided sources when answering. We tried to make the instructions stricter, telling the LLM to only output sentences that could be supported by a reference. The resulting groundedness score remained 90%. This suggests we may be hitting a ceiling in terms of what can be achieved with prompt changes alone. Note that this is just an assumption. We didn't fully validate this.

When we relaxed the instructions, telling the application to use its world knowledge whenever possible and only use sources when it couldn't support an argument from world knowledge, the groundedness score dropped to 82%. This indicates that our evaluation system is sensitive to changes that affect the reliance on sources.

We also tested different models for generating the answers in our RAG application. An older model, gpt-3.5-turbo, scored 75%, while a newer but cheaper model, gpt-4o-mini, scored 77%. The model we launched our product with about a year ago, gpt-4-turbo, scored 87%. These results demonstrate that our evaluation system can detect differences in groundedness between different models.

# Limitations and Future Work

While our automated groundedness evaluation system is a major improvement over manual evaluation, it does have some limitations. It is a very strict measurement and penalizes answers that attempt to extrapolate or predict from the sources. This may not always be desirable, especially if the goal is to provide more forward-looking insights.

There is also still some variance between runs, with scores shifting around 3-4 percentage points. However, this seems to be within an acceptable range, as the differences we observed from changing prompts and models were larger than this variance.

Achieving 90% groundedness on our first measurement is a positive result in my book! It's also a bit tricky to sell because RAG is often sold as a solution to LLM hallucinations. If you've played with RAG systems, you know they are not immune to these problems. Telling leadership that 10% of the stuff the application produces is not well-grounded is problematic, but at least now we can measure it and potentially improve on that metric. Whether further improvements are necessary or even noticeable to users is an open question that we will continue to explore.

I would like to stress again that LLM-as-a-judge is a really powerful tool. We have good experience with LLM-based metrics for information retrieval relevance, answer relevance, and now groundedness, all performing very well for our needs.

# Conclusion

We have developed a robust and efficient way to measure the groundedness of answers from our RAG application. This automated solution produces results comparable in quality to manual evaluation but in a fraction of the time. This tool allows us to confidently investigate new models, prompt changes, and other techniques for improving the groundedness of answers in our RAG application. While there's always room for improvement, this system represents a significant step forward in our ability to evaluate and enhance the reliability of our application.

---

This blog post was made with the help of Gemini Experimental 1206.
