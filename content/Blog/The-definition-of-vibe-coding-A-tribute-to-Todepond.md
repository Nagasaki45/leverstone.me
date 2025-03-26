---
title: The definition of vibe coding - A tribute to Todepond
date: 2025-03-26T01:00:00.000Z
---

If you're not following [Lu Wilson, a.k.a Todepond](https://www.todepond.com/), **you really should!**

They published a blog post titled [Definition of "live coding"](https://www.todepond.com/sky/definition-of-live-coding/) about a week ago. My initial reaction:

![Chart of the quality of the definition of live coding over the past 10 years]({static}/images/blog/the-definition-of-live-coding-from-iclc.webp)

Many things went wrong during COVID. Apparently, the definition of live coding is one of them. I wanted to plot this 👆 and share somewhere, but what's the point? It's probably a waste of time. I moved on.

Then, this appeared on my RSS feed: [Okay fine I’ll define live coding](https://www.todepond.com/sky/okay-fine-ill-define-live-coding/). What a beautifully written thought provoking piece! Seriously.

So the plot has to be updated. Should I spend 5 minutes just doing the plot in any existing tool? Nahhhhh. Let's just [sketch-it-and-let-the-AI-figure-it-out](https://www.youtube.com/watch?v=JjHD5f058qw). Or, even better, create an interface to do just that, [draw-fast](https://github.com/tldraw/draw-fast) style.

Presenting to you 🥁... [**Plot Fast**](https://plot-fast.leverstone.me/)

<video controls style="max-width: 100%;">
  <source src="{static}/images/blog/the-definition-of-live-coding-plot-fast.mp4" type="video/mp4">
</video>

Did you see how fast it was?!? And the legend? 😵 Perfect!

# A note about API keys

When you click the button to convert the sketch to an XKCD chart you'll be asked for a Gemini API key. It will be stored in local storage from now on. You can trust me that this is not leaked anywhere **but you probably shouldn't!** You can read the source to make sure I'm not doing anything nasty with the key. Or at least make sure you don't use a key that is attached to a payment method.

# Vibe coding

This was an exercise in [vibe coding](https://x.com/karpathy/status/1886192184808149383) - asking LLMs to write code and accepting their suggestions without reviewing. Don't do it in your production code kids! Anyway, it went surprisingly smooth. I used a mix of `gemini-2.5-pro-exp-03-25` and `claude-3.7-sonnet`. Why? I'm not sure. I really like Gemini for writing and I initially thought I will ask for a plan, and then drop to Sonnet for the implementation. I ended up one-shotting the implementation and then iterating on it.

I'm not using any code writing AI tool here, just the trustworthy [`llm` command line tool from Simon Willison](https://llm.datasette.io/en/stable/). The entire thing is one file, so I'm just feeding the file to a model, copy-pasting any errors I see in the web console. Dealing with other requests (e.g. layout changes) is similar. For every new topic (e.g. fixing a bug, changing the layout) I started a new conversation.

I tried to guide the LLM with clear instructions:

> Project brief: A digital canvas to draw diagrams by hand - ms paint style. One button to convert the diagram to a nicely plotted one, potentially in XKCD or cartoonish style. Implementation details: use canvas, upon button press convert the canvas to an image and send it to an LLM (gemini-2.0-flash) to return a JSON for the chart spec. This is then loaded in chart.xkcd. It should all be done in a single HTML page. When the user clicks the button for the first time they are asked for an API key which is then stored in local memory.

Generating the system prompt was interesting. I used [`shot-scraper`](https://shot-scraper.datasette.io/en/stable/index.html), another tool from Simon Willison, to take a screenshot of [the chart.xkcd docs](https://timqian.com/chart.xkcd/), then fed it to the LLM with the following prompt:

> I want an LLM to take an image of a hand made chart in MS Paint and produce a JSON object that can be passed to chart.xkcd for rendering. Create a system prompt with documentation for how to use chart.xkcd. Include examples. Make sure that when the LLM receives an image it will output only a valid JSON containing the data to pass to chart.xkcd. At the top level of the JSON there should be two keys: chartType, and spec. The chart type is 'line', 'xy', 'bar', etc. The spec is the object to pass to the library.

That's pretty much it! Thanks for reading. And thanks Lu again for the inspiration!

Happy vibe-plotting 📈