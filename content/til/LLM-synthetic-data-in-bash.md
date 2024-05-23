---
title: LLM synthetic data in bash
date: 2024-05-23T23:00:00.000Z
---

The [`llm` command line tool by Simon Willison](https://github.com/simonw/llm) lets you interact with LLMs from the command line. I've been using it recently, and while it's nice and convenient I wasn't doing anythin I couldn't do with a "vanila" LLM ChatBot a la ChatGPT. Until today!

Today, I had to test our retrieval-augmented generation (RAG) system. I wanted to hit a endpoint repeatedly and monitor the response time while running some operations on the server. Sure, I can throw something together with a bash loop and `curl`. But what if my experiment will be skewed by caching somewhere in the system if the request is always the same 🤔

Here's what I ended up with

```shell
while true
do
  curl https://my-server.com/ \
    -d "{\"query\": \"`llm "Give me a one sentence interesting question about consumers behaviours"`\"}" \
    --output /dev/null \
    --silent \
    --write-out "%{http_code} %{time_total}s\n"
done
```

It hits the system with a new question every time, running in an endless loop.

BTW, `llm` helped me to come up with this solution 😉
