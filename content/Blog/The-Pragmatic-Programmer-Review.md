---
title: The Pragmatic Programmer Review
date: 2024-06-21T22:00:00.000Z
---

![The Pragmatic Programmer 20th Anniversary Edition book cover](/images/blog/pragmatic_programmer_cover.avif)

The Pragmatic Programmer 20th Anniversary Edition, by David Thomas and Andrew Hunt, offers high-level, actionable advice for software engineers. Unlike many technical books that focus on specific coding practices or languages, it focuses on cultivating a mindset that leads to better software development practices.

The authors emphasize principles like designing for ease of change, adapting to evolving environments and requirements, and embracing incremental development with regular reflection. These concepts may seem abstract, but the book excels at providing concrete, actionable advice for putting them into practice.

I think that's the book's greatest strength: it tackles high-level concepts and challenges, and yet manages to provide practical advice that you can apply immediately. It is full of pragmatic advice for improving the most important soft and hard skills required in modern software engineering.

The fact that the advice in the book remains, in most part, quite high-level, doesn't mean that it shies away from technical discussion. It highlights the importance of mastering basic tools like the command line and version control, and discusses testing, refactoring, automation, various design patterns, and other technical topics in detail.

In this review, I'll share some of my key takeaways from this seminal book, discuss its impact on my work, and explore how its principles can be adapted for different roles in the tech industry.

## My Key Takeaways

Here are some of the key principles and concepts from The Pragmatic Programmer that have resonated with me:

1. **Easy to Change (ETC) Design:** The authors stress that good software should be easy to modify. The world is changing, decisions change, and so should our software systems. This principle underpins many of the recommendations in the book. It is tightly linked to agility.

1. **Don't Repeat Yourself (DRY) and Orthogonality:** These closely related principles are about eliminating knowledge duplication across all aspects of a system and ensuring components are independent. It's not really about avoiding code duplication, but about avoiding duplication of knowledge. This extends to documentation, comments, and even communication patterns. For example, think about a concept, idea, or decision that where communicated multiple times in different ways. Maybe this can be avoided by creating a single source of truth.

1. **Tracer Bullets and Prototypes:** The tracer bullet approach involves rapidly developing a thin slice of functionality that integrates all system components, providing a foundation for iterative development. This is different from prototypes, which are throwaway code meant for testing ideas. Both have their place, but they serve very different functions.

1. **Agility and Adaptability:** The ability to respond to change is crucial, whether at the code or the project level. The book critiques the idea of blindly following methodologies and processes, and instead, advocates for an agile, feedback-driven approach that allows for continuous improvement - try different things, fail fast, and keep what works. It cautions against replicating processes from other companies (Big Tech, usually) without understanding the context.

1. **Requirements Learning:** No one knows what they want, so the requirements should be learned, with the clients, in a feedback guided process. Better to think about requirements as business needs. The goal of the developer in this context is to give feedback to highlight the trade-offs and ask questions to work out the requirements with the stakeholders.

1. **Pragmatic Teams:** The book extends its advice to team dynamics and project management, emphasizing the importance of communication, collaboration, and shared responsibility. It discusses some of the ideas targeted at individuals in earlier chapter in a new lens. One example I liked in particular is the concept of tracer bullet teams, in which the team should be optimised to deliver tracer bullets - fully integrated software. It requires good communication paths between all necessary parties.

## Personal Impact

Since I started reading this book, I've found myself applying its principles almost daily. It's not just about writing better code; it's about approaching problems more thoughtfully, communicating more effectively with my team, and taking a more holistic view of software development. I find myself constantly referring back to the principles in this book when making decisions and communicating with my team. It's given me a new vocabulary and framework for thinking about software development.

I'm currently exploring ways to improve my communication with colleagues and stakeholders. Instead of simply following requirements, I'm experimenting with providing more thoughtful feedback focused on trade-offs and implications. For instance, I'm learning to highlight potential maintenance burdens or how certain requirements might affect other aspects of a project.

The book has also prompted me to start thinking more critically about our development processes and ceremonies. I try to be more mindful about the value these bring and suggest improvements when needed. This is an ongoing challenge, but I'm excited about the potential to streamline our workflows and improve team efficiency.

I make sure to apply the Easy to Change (ETC) Design principle in my decision-making process. When faced with unclear requirements, I'm trying to opt for reduced scope and functionality to keep the system flexible. It's a balancing act I'm still learning, but I'm optimistic about the long-term benefits of this approach in making our projects more adaptable to changing needs and more maintainable in the long run.

Perhaps most significantly, the book has inspired me to be more intentional about my learning and professional growth - a journey that's very much in progress. I'm exploring new ways to seek out and process knowledge, and constantly looking for opportunities to apply what I'm learning. The recent increase in activity on this blog is part of this ongoing commitment to continuous improvement.

## Adapting the Book for Different Readers

While The Pragmatic Programmer is primarily aimed at software engineers, many of its lessons are applicable to other roles in the tech industry. The suggestions below are definitely non exhaustive. These came to mind as I was reading the book, and thinking about my colleagues and daily interactions. I'm sure there are many more ways to adapt its principles to different roles.

### Engineering Managers

Non technical engineering managers who want to better understand their reports can benefit from understanding the guiding principles for Pragmatic Programmers, Teams, and Projects.

- **Chapter 1 - A Pragmatic Philosophy:** This is the least technical chapter in the book, and it's a great starting point for understanding the mindset of a Pragmatic Programmer. Relevant topics:

    - **Topic 3 - Software Entropy:** All software degrade over time. This is a good starting point for understanding the importance of maintenance and refactoring.
    - **Topic 4 - Stone Soup and Boiled Frogs:** This confusingly named topic covers the importance of taking small steps towards change, how to convince stakeholders of the benefits of your approach, and the importance of noticing and acknowledging changes in your environment.
    - **Topic 5 - Good Enough Software:** This topic is about discussing the quality of a deliverable as a trade-off. Good software now is better than perfect software later. Or is it? It depends on the context! Software quality should be discussed as other requirements are.

- **Chapter 2 - A Pragmatic Approach (or, simply, generic advice for good design):** All but the Domain Languages and Estimation topics are great! They cover what's important in software design without getting very technical. I think non technical people who are responsible for delivering technical projects can benefit from understanding these principles.

- **Chapters 8 and 9 - Pragmatic Projects and Pragmatic Teams:** To be honest, I don't understand the division between these two chapters. They are both about teams and projects. Overall they discuss requirements, collaboration, agile practices, and providing value to our users. I think most of the content here will be relevant to engineering managers, except, maybe for topic 46 about problem solving skills.

- In addition to this, there's very good advice about staying agile, working incrementally, and adapting to change in topics 27, 48, and 50. I don't know why these are spread over three different chapters, but they are all very relevant to managing software projects.

If you're short on time and want to start somewhere I would say start with either chapter 2 if you're interested in software design, chapters 8 and 9 if you're interested in teams and projects related topics, or the topics about agility.

### Product Managers

Product managers, there's something in here for you as well! "The Requirements Pit" topic is a great starting point. Related to this are also the "Good-Enough Software" and "Delight Your Users" topics. The first two were discussed above, so unnecessary to repeat here. In "Delight Your Users" the authors discuss the importance of understanding the expectations of your users, and how to align your software with those expectations, as it is not the software that users are usually care about, but what it can do for them.

The idea of tracer bullets teams, discussed in the "Pragmatic Teams" topic, is also very relevant. [Conway's Law](https://en.wikipedia.org/wiki/Conway's_law) is mentioned a few topics earlier. It states that:

> Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.

So, if you want to improve your software, you might want to improve your team's communication first, making sure that communication paths are built end-to-end, connecting engineers with stakeholders and users.

## Weaknesses and Criticisms

The Pragmatic Programmer isn't without its weaknesses. As alluded to earlier, the structure of the book can sometimes feel disjointed, with related topics separated by unrelated material. Some of the topic titles are also confusing, making it harder to remember what they're about when you want to refer back to them. Can you guess what "Coconuts Don't Cut It" is about? It's about not copying methodologies and processes without understanding the context 🤷

Some readers might find certain sections preachy. The authors often make bold judgement calls about certain practices (e.g. 'Some team methodologies have a "quality officer" ... This is clearly ridiculous', or 'Without external configuration, your code is not adaptable ... in the real world species that don't adapt die'). While I don't disagree, I think it can unnecessarily alienate some readers who might not share the same views.

Additionally, some of the more concrete technical sections feel less valuable compared to the high-level advice in most of the book. Take the concurrency chapter for example, I think the introduction to it and the first topic are good, but then it goes into some techniques that feel disjointed from the type of advice in the rest of the book, and somewhat dated. I would prefer to read about techniques to deal with these issues on a specialised book. The same applies, to some degree, to a few other topics (e.g. Domain Languages).

Having said all that, these are minor criticisms in the grand scheme of things. Don't make these stop you from reading the book!

## Conclusion

In conclusion, The Pragmatic Programmer has already begun to reshape my approach to software development, even in the short time since I started applying its principles. The book's emphasis on adaptability, thoughtful design, and effective communication has provided me with valuable tools for tackling daily challenges in my work. While it's not without its flaws, the practical wisdom contained within its pages far outweighs any minor structural issues or occasional preachiness. Based on my preliminary experience of putting its advice into practice, I wholeheartedly recommend The Pragmatic Programmer to software developers at any stage of their career. It offers a wealth of insights that can help you become a more effective and thoughtful professional in the ever-evolving field of software development.

---

This blog post was made with the help of Claude 3.5 Sonnet and GitHub Copilot.