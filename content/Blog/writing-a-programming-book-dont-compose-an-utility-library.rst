Writing a programming book? Don't compose an utility library!
#############################################################
:date: 2015-05-23
:author: Tom Gurion
:tags: thoughts, books
:slug: writing-a-programming-book-dont-compose-an-utility-library

I came across two books recently, in which the authors decided to
write an utility library. The first book was `Python in Practice, by
Mark
Summerfield <http://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636/>`__
(my opinion about the book can be found
`here </python-readings>`__),
and the second, which I'm still reading, is `Doing Bayesian Data Analysis,
Second Edition, by John Kruschke
<http://www.amazon.com/Doing-Bayesian-Data-Analysis-Second/dp/0124058884>`__.
A separate review will be added when I will finish reading it.
The books are different in their nature: One is about python
programming, while the other is about statistical methods, and uses the
R programming language for hands-on examples and exercises; the first
book is average quality overall (IMHO) and the second is absolutely
amazing! However, I believe that I may be able criticize the utility
libraries that came with the books in the same manner: Don't do this!
And why?

**Installation process breaks conventions**

When I need an external tool in a python project I know I have
`pypi <https://pypi.python.org/pypi>`__ to rely on for finding packages.
I have `pip <https://pip.pypa.io/en/stable/>`__ to easily install the
package and prefer to work with
`virtualenv <https://virtualenv.pypa.io/en/latest/>`__ whenever
possible. This set of tools help me in maintaining a sane codebase, and
reduce the effort of managing the dependencies by my own.
There is no chance that I will copy an external module into my project
and source control it unless I'll have to, so why to use this module in
an educational project in the first place?
I really don't know what is the convention in installing R external
packages, but I believe that Kruschke suggestion of sourcing his
supplied scripts is not the proper way to do this (enlighten me if I'm
wrong).

**Package maintenance / code quality**

Before I'm installing an external package I tend to search
about the package quality. First thing is checking how many stars the
package have on github and how many times it was downloaded from pypi.
And there is a reason behind it: I can rely on packages that are used
often to have better code quality; through gihub I can browse the
package issues / latest commits and make sure that it is still
maintained.
I'm sure that books authors invest a large amount of time in writing
their utility libraries. But code free of bugs doesn't exists, and I
prefer to know that the codebase is maintained before I use it (again,
without distinction between educational and "real" projects).

**Not specific enough**

If your utility library is a mix of different solutions for different
problems, it might not worth keeping in our toolbox. The above is
probably more relevant to Python in practice than to Doing Bayesian Data
Analysis, but I think it's still worth mentioning.

**Documentation**

When I choose a tool to work with I want it's documentation
to be top notch! Take
`django <https://docs.djangoproject.com/en/1.8/>`__ for example. The
project's documentation is not less than perfect, including a great
tutorial for beginners. I really don't want to look for the book when
I'm interesting in put in use some less obvious function from an utility
library.

.. image:: https://sites.google.com/site/doingbayesiandataanalysis/_/rsrc/1403617861639/config/customLogo.gif?revision=5
  :alt: Doing Bayesian Data Analysis, Second Edition, by John Kruschke
  :width: 100%

What I'm expecting from authors instead
---------------------------------------

-  If you think that your utility functions worth it pack it and publish
   it as any other package.
-  I really don't mind reading one or two additional pages of code in
   your book, if there's something interesting in it. Again, if the code
   deserved to be mentioned in your book, it may be also deserved to be
   talked about explicitly.
-  If this functionality exists elsewhere you should reference it, and
   advise the user to use it. I've never wrote code in R, but was ready
   to learn how to work with its ecosystem. I expected Kruschke to teach
   me that, instead of showing me how to source his supplied scripts.

 
Late disclaimer
---------------
Don't get me wrong, supplying code as part of your book is great! But
there are different ways to do it: David Beazley's Python Cookbook is
full of code snippets, fully commented and explained; In Test-Driven
Development with Python, Harry Percival guides the reader in developing
an webapp with reference code available at github.
Don't get me wrong 2: The above doesn't mean that the books are bad.

Edit:
-----
Don't miss Kruschke's comment below! He lights the above topics from
different angle and supplies great arguments for his decisions.
Maybe, as a programmer, I tend to rely on the language ecosystem mechamisms instead of being satisfied with the easier, and more beginners friendly solution Kruschke proposes.
I definitely agree with him that an easier-to-use software for data science, and bayesian data analysis in particular, is always welcomed.
I would like to seize the opportunity to thank Kruschke again for his great book! I really enjoy reading it and I'm sure that I will continue to use the insights gained from it in the future.
