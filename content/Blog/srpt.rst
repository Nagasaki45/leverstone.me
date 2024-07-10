Media and arts projects - part 1
################################
:date: 2016-12-29 22:00
:author: Tom Gurion
:tags: projects, music, PhD
:slug: media-and-arts-projects-part-1

.. image:: /images/blog/bury_me_with_my_money.gif
  :alt: Sunset Riders - Bury me with my money
  :width: 100%

I recently shared some of my `first experiences as a PhD student <{filename}/Blog/my-first-assignment-as-a-phd-student
.rst>`_ in the `Media and Arts Technology program <http://www.mat.qmul.ac.uk/>`_, Queen Mary University of London.
Now, when the first term is over and the second one is about to begin, it is a good time to show the projects I have been working on.
This post is therefore the first in a series of 3 posts.
Here I will present my assignments to the Sound Recording and Production Techniques module.

"Bury me with my money!"
------------------------

.. raw:: html

  <iframe width="100%" height="300" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/300118139&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true"></iframe>

The first significant project in the module was to produce a short soundscape.
Each student wrote a concept on a piece of paper and the concepts were picked by chance by other students.
Mine was "Bury me with my money!". WTF!?!
After a short research I found the origin of the line, in the 90s arcade game Sunset Riders, and a long list of MEMEs surrounding it.

"Digital privacy"
-----------------

.. raw:: html

  <iframe width="100%" height="300" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/300119056&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true"></iframe>

The instructions for the final project were similar to the previous one.
We were asked to compose another soundscape, but this time we got more freedom to choose the concept by ourselves, and it was required to be a bit longer.
I decided to seize the opportunity and play with deep neural networks on the way.
The idea was to use similar techniques to those presented by `google wavenet <https://deepmind.com/blog/wavenet-generative-model-raw-audio/>`_ earlier this year (if you are not familiar with this research yet, go and take a look, it's fascinating!), to create a model that will be able to listen to audio and then generate new audio with similar characteristics.
I wanted to train the model on sounds of private conversations and sex of my partner and I, recorded in our apartment, and use the trained model to generate new audio material that will be used as the basis for the soundscape.

As a serious PhD student I gave the soundscape the title "Digital privacy" and described it as "mirroring the existing conflicts between art, artificial intelligence, and privacy in the age of ubiquitous surveillance".
The truth is, I really want to delve into deep learning and thought that it might be a good way to start :-).

Although I played with machine learning in the past, I'm completely new to deep learning, and after several attempt this first ambitious idea turned out to be a complete failure.
In the end, I used audio samples that I found on the web that were generated in similar techniques.
However, I documented my attempts, so next time I (or someone else) will succeed. You can find all the information `here <https://github.com/Nagasaki45/digital-privacy-soundscape/blob/master/report/report.md>`_.
