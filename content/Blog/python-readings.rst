Python readings
###############
:date: 2014-11-17
:author: Tom Gurion
:tags: thoughts, books, python
:slug: python-readings

I usually learn anything new by reading books. In fact, I got almost
all of my python knowledge (which is not a lot, I'm just an apprentice
programmer) by reading python books.
A year ago I've started to learn web development from `Udi
Oron <http://www.10x.org.il/>`__ in
`Hackita <https://hackita.hasadna.org.il/>`__ (my impressions
`here <{filename}/Blog/hackita.rst>`__), and
shortly after started to work with him as a python teaching assistant in
his courses. Few months ago I've got a permanent position in one of
those companies we've taught in and the stigma of someone that can
answer everybody's python questions still sticks to me in the company.
Between those questions are how to get started with python and where to
find information regarding specific topics.
Hence, here is my thoughts about the books that helped, and still
helping me learning python.

Disclaimers
-----------

- I'm new to python and the world of programming.
- Books won't do the work for everybody.
- When I first started to learn python I never thought I will end up
  making my leaving out of it, so I've learned python 3 (which is
  preferable language IMHO). However, most of the industry still uses
  python 2. All of the books below are for python 3. It doesn't mean that
  they won't help you learn python 2 also, but you will have to find the
  differences by yourself.

Beginners books
---------------

`The Quick Python Book, Second Edition (Naomi R. Ceder) <http://www.amazon.com/Quick-Python-Book-Second-Edition/dp/193518220X>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image0|

After trying different books for python (Think Python, Dive
into Python 3 and Head First Python) I've found this one to be the
preferable as a learning book for someone that already saw some code,
but is definitely not an experienced programmer.
Part 1 is a short introduction that may also be used as a quick
reference. Part 2 is very organized tutorial for the language. It
contains most of the essentials and will give you the feeling that you
can continue learning by your own (or with more specialized books /
tutorials). Part 3 is much less cohesive then part 2. It seems that the
chapter about regular expressions could get into part 2 but the rest of
the section is too much esoteric and there are some mistakes through all
of it (for example, it refers you to the appendix for more information
that is not there).
I didn't read part 4 completely. I've only read the information about
working with databases in chapter 24 and it is very well written.
Summary: For part 2 I will give 5 start without hesitations. But part
3, although less significant, doesn't deserve it. After all the book is
very recommended.

More advance / intermediate books
---------------------------------

`Python in Practice (Mark Summerfield) <http://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636/ref=sr_1_1?s=books&ie=UTF8&qid=1416060956&sr=1-1&keywords=python+in+practice>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image1|

I bought this book primary for its chapters about design
patterns as well as the concurrency and the networking chapters (1 to 3,
4 and 6 accordingly). The book doesn't meant to be read from start to
finish, but as a reference and guide to each topic separately. I think
that from the above chapters I've already read most of the content, as
well as the chapter about GUI with tkinter. I have nothing to say though
about the two remaining chapters (extending python and 3d graphics).
The best chapter of this book is the one about high-level concurrency.
In this chapter Summerfield explain with details the difference between
CPU-bound and I/O-bound concurrency and have a strong suggestions
regarding the tools to use for concurrency with python 3. Namely, the
suggestion is to use the threading, multiprocessing and
concurrent.futures modules and never use locks or other lower level
synchronization primitives explicitly, use queues and futures instead.
The examples are good, although I found the code unnecessarily complex
sometimes.
On the other hand, I found the chapters about design patterns to be
much less fruitful. The author attitude is too object oriented for me
where things could be done much easier using a decorator or two instead.
The code examples too, are complex and non pythonic.
I'm sure that there are much better and approaches to high-level
networking then those described in this book. The author implement
`remote procedure
call <http://en.wikipedia.org/wiki/Remote_procedure_call>`__ server and
client. Simple examples can be done in a simpler manner then the
suggested code and advance use cases may prefer higher level 3rd party
libraries and frameworks that removes much of the boilerplate (e.g.
`Django <https://www.djangoproject.com/>`__ +
`DRF <http://www.django-rest-framework.org/>`__ for REST server +
`requests <http://docs.python-requests.org/en/latest/>`__ based client).
Summary:The high-level concurrency chapter is really great and deserve
5 stars, but the rest of the book is ranging between 2 and 3.

`The Python Cookbook, 3rd edition (David Beasley) <http://www.amazon.com/Python-Cookbook-David-Beazley/dp/1449340377/ref=sr_1_1?s=books&ie=UTF8&qid=1416061017&sr=1-1&keywords=the+python+cookbook>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image2|

After disappointing from "Python in Practice" I've came across this
book as one with similar scope, namely, a design patterns book,
organized into chapters by topic that you can read in any order. In
addition, this one is also great reference book by the fact that most of
the suggested patterns are described in a short, self-contained manner.
This is a really great book! Beasley's attitude is so pythonic. AKA:
readable, simple,
`DRY <http://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`__, less OO
and more functional whenever possible, smart usage of the standard
library / 3rd party high level libraries.
Most of the chapters of the book are really fluent and easy to read.
I've found the meta-programming and the object oriented chapters a bit
more complex, but still great after the 2nd or the 3rd read as the ideas
demonstrated there are a bit too advanced for my background.
Summary: Assuming you already know python (don't read it if you don't)
I think that this book is a must have. 5 stars are barely enough.

Scientific computing with python
--------------------------------
As already noted, I've never thought that I will find myslef
programming python in a full time job. Essentially, I've decided to
learn python as a data analysis tool for my `MA
research <{filename}/Projects/ma_thesis.md>`__. These
are the main sources I've used to get the necessary knowledge.

`Python for Data Analysis (Wes McKinney) <http://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1449319793>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image3|

It's not a bad book but if you are looking for a good book for
scientific computing with python you will probably be disappointed.
The book covers mostly the pandas library. It doesn't give much
information about numpy and matplotlib, and say completely nothing about
scipy, which are all more essential for scientific computing than pandas
as far as I understand that topic.
On the other hand, pandas is your tool to go if you need to work with
spreadsheet oriented data (the `library highlights
page <http://pandas.pydata.org/index.html#library-highlights>`_ summarize
its strengths pretty good).
This book was one of the first python books I've read, together with
the quick python book above. It explains pandas in a very introductory
way (pretty slow), which make recommending this book even harder: If you
are a beginner, this book is written in the right level, but on the
wrong content; If you are a more advanced programmer looking to learn a
bit of pandas you may find the tutorials
`here <http://pandas.pydata.org/pandas-docs/dev/tutorials.html>`__
comprehensive enough.
Summary: Pandas is a great tool, use it! But I don't think that this
book is a good your way to learn data analysis with python, whether you
are a beginner or not.

`Python Scientific Lecture Notes <https://scipy-lectures.github.io/>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
I have to admit, I've read only the first section of the "lecture
notes", but if you are looking for an introduction to scientific
computing with python this "book" is definitely worth reading. It covers
the basics of numpy, matplotlib and scipy very concisely, with lots of
short but working code examples.

Web development with python
---------------------------

`Two Scoops of Django: Best Practices for Django 1.6 (Daniel Greenfeld - AKA pydanny, and his wife Audrey Roy) <http://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/098146730X>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image4|

Can't say I've finish reading this book. It more like a
reference you open anytime you need for some extra help on each topic,
with emphasis on best practices.
Be aware that this book is not for beginners! But if you want to
progress with python + django you're going to appreciate the suggestions
found there. For django starters, go through the really good
`tutorial <https://docs.djangoproject.com/en/dev/intro/tutorial01/>`__
and write another django app before reading any of the suggestions in
this book. It won't help you if you don't.
There are two editions for this book, for django versions 1.5 and 1.6.
According to the authors `there will be no more version of this
book <http://twoscoopspress.com/pages/two-scoops-of-django-1-6-faq#what-if-1.7>`__,
so don't attempt to wait to one. Take the latest as it has much more
content.
Behind the general recommendation and the versions stuff I will add
that I don't like the "theme" of the book. The code examples themselves
are great but there are lots of illustrations that doesn't really
helping in explaining the concepts nor in remembering them.
Summary: If you take django development seriously just get yourself a
copy, you won't regret it!

`TDD with python (Harry J. W. Percival) <http://www.amazon.com/Test-Driven-Development-Python-Harry-Percival/dp/1449364829>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image5|

I've started to read this book only recently, so I'm still in the
middle of it (somewhere around chapter 17). So my very warm
recommendations are for those I've read.
Percival does a great job in explaining and demonstrating the TDD
discipline, introducing web development with django on the way. Although
I am already familiar with django I found the introductory attitude of
the author more then appropriate, and it let me concentrate more on the
TDD side rather on understanding the framework. On the other hand, there
are lots of developers that prefer a more strait forward attitude, with
less text and more working code snippets, so bear in mind that this is
not the case with this one. Here, lots of code examples are written
iteratively throughout the test cycles and upon several pages. I like
it!
Behind introducing TDD, its the first time I manage to deploy an app
to a real server (I've deployed some apps to
`heroku <https://www.heroku.com/>`__ before, but it is different). I
will surely recommend those chapters as stand alone tutorial for
deployment (chapters 8 & 9 + appendix C).
The only downside I can think of is if you are not interested in web
development at all. It will be too much work to translate the concepts
in this book into completely different subject.
Summary: Great introduction to the discipline of TDD for web
development. Very recommended. And you can even read it online for free
`here <http://chimera.labs.oreilly.com/books/1234000000754/>`__.

Ending words
------------
I would really like to hear your thoughts about the recommendations,
whether you agree with me and even more if not :-).
You are also welcome to contact me on any question about these books /
other python resources and I will do my best to answer.

.. |image0| image:: http://ecx.images-amazon.com/images/I/51afqHmFrML._SX258_BO1,204,203,200_.jpg
   :width: 180px
.. |image1| image:: http://www.qtrac.eu/pipbookm.png
   :width: 180px
.. |image2| image:: http://ecx.images-amazon.com/images/I/51zDEWm5kcL._SX258_BO1,204,203,200_.jpg
   :width: 180px
.. |image3| image:: https://d.gr-assets.com/books/1356132971l/14744694.jpg
   :width: 180px
.. |image4| image:: http://www.arruda.blog.br/wp-content/uploads/2014/03/IMG_1894.jpg
   :width: 180px
.. |image5| image:: http://orm-other.s3.amazonaws.com/tddwithpython/final_cover.jpg
   :width: 180px
