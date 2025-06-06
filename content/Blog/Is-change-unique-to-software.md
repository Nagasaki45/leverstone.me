---
title: Is change unique to software?
date: 2025-06-06T11:00:00.000Z
---

Software changes over time. You build something, ship it, and almost immediately discover that new features are needed, the solution isn't quite right, or the underlying business problem has evolved. Things have to change. This feels natural to most of us in the field; it’s just how it is.

This post isn't about the fact that software changes. It's about a specific claim I hear surprisingly often: **that this constant need for change is unique to software engineering among all engineering disciplines.** I recently heard this idea mentioned in an [interview with Martin Fowler](https://www.youtube.com/watch?v=CjCJ76oZXTE) about his book *Refactoring* on the Book Overflow podcast and again in an [interview with Barry O'Reilly](https://techleadjournal.dev/episodes/212/) on the TechLeadJournal podcast (both podcasts are highly recommended BTW). Martin's take on this is that because software is so deeply integrated with dynamic human processes, it's subject to a level of volatility that a bridge or a building is not. The example Barry gives is the engineering of a car. It is designed based on the properties of materials and physical factors like gravity and aerodynamics. These don't change very often.

Why should we care about this claim? Because if we believe we're special in this way, we cut ourselves off from learning from other fields. That would be a shame.

Like most software engineers, I have zero professional experience in other engineering disciplines, so it's hard for me to argue with authority. Having said that, I don't think the claim comes from people with experience in other engineering disciplines either, so maybe I shouldn't worry too much about the robustness of my arguments. 😄

Let's dive in!

My requirements for my own living space, for example, have changed dramatically over the last few years. The pandemic turned my flat into a full-time office. A change in employment, from a PhD to a job as a software engineer, meant I could afford a larger space. Starting a family required a different layout entirely, and now with growing children, we're hoping for a garden. The need for my physical environment to change has been constant. My solution was usually to move, not because the need didn't exist, but because the building itself couldn't easily adapt.

There's another crucial difference here: scale. My effort to rearrange my flat, even if it were easy, would only benefit me. The impact of the change doesn't scale. In software, a modification made to solve one problem can be rolled out to many users instantly. This massively alters the economics and incentives. A small improvement with global reach is often worth pursuing, while a similar improvement to a single physical building is not.

This brings us to a key point: perhaps we mistake the *ability* to change things cheaply for a massive audience with a unique *need* for change. The low cost and high leverage of software modifications mean we act on change requirements that would be economically unfeasible in other engineering disciplines. Isn't software often chosen to solve a problem precisely *because* its solutions can be modified and scaled so efficiently?

Another example comes from my experience with modular synthesizers-this weird thing:

![A modular synth connected with patch cables]({static}/images/blog/modular_synth.avif)

It's a collection of electronic modules, analog or digital, connected externally with patch cables to create a unique musical instrument. The divide between analog and digital modules often comes down to adaptability. You can't easily change the core behaviour of an analog circuit after it leaves the factory, but a digital module can be completely transformed with a firmware update. As someone who has [dabbled a bit in designing modules](https://github.com/Nagasaki45/eurorack), I *think* designers and manufacturers often go digital because they want the option to change things later. Here, software isn't the thing that *needs* to change; the choice to solve a problem with software is made deliberately to *enable* change.

And what about the idea that only software interfaces with fast-moving human processes? I think that's a relatively weak argument. Think of a new road system. It fundamentally alters traffic patterns, community access, and local business. Or consider the design of an office building, which directly shapes how people work together. When work patterns change (as they did during the pandemic), they directly affect our requirements for these roads and offices. The key difference is that iterating on a highway or an office building is astronomically more expensive than deploying a new software build.

In short, I don't think software systems have a higher intrinsic requirement to change. I think they just have a much lower barrier to it. Because we *can* change things easily, we do.

So, what can we learn from this?

- First, and in direct contrast to the proponents of the claim above, we can appreciate that software is, by its nature, quite easy to change. This is why we are constantly asked to do so. Embrace it! And ideally, make it even cheaper to change further.
- Second, and this is a harder one (at least for me), we should look out for insights from other fields, instead of shutting ourselves off by claiming that we are facing a unique problem.

---

This blog post was made with the help of Gemini 2.5 Pro.