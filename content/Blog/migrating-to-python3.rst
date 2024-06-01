Migrating to python3
####################
:date: 2016-06-25
:author: Tom Gurion
:tags: thoughts, python
:slug: migrating-to-python3

I was recently asked, by my boss, about the possible benefits of migrating our
code base at work from python 2.6 to python 3. Instead of sending an email back
to my boss with my answer, I decided that it worth a blog post. Why? because the
internet is full with comparisons between python 2 and python 3, but it is hard
to tell what are the real gains from doing the migration. Here, I will try to
explain, in a very subjective manner, the benefits I see from such move.

So let's start with the obvious, **python 3 is clearly a better language than
python 2.6**: ``print`` is a function instead of a statement, now with sane
arguments; dict and set comprehensions reduce unnecessary, error prone,
verbosity; real division by default, because that's what you want 99% of the
time anyway; iterators by default (``range`` replaced ``xrange``,
``dict.items()`` replaced ``dict.iteritems()``, etc.); explicit relative
imports... Actually, the list goes on and on. However, I **don't** think that
the features above are good reasons to migrate a large project. Modern python
code, written with python 3 in mind, will benefit from them, that's for sure. But
we do not want to rewrite our code base, we want the transition to be as smooth
as possible.

So what **is** valuable? Here is my list:

We must leave python 2.6
========================

Our server is based on `twisted`_, which already dropped support for python 2.6.
Our other main dependency is `SQLAlchemy`_. I don't think that they are going to
drop support for python 2.6 anytime soon but this day will surely come. In
general, staying with python 2.6 will soon mean that for each dependency upgrade
we will have to upgrade everything at once, which is kind of a nightmare.

So, if we must leave python 2.6 behind and upgrade, I really don't think that
migrating to python 3.5, for example, will be way too complicated than to 2.7.
Moreover, moving to python 2.7 now will require another migration, with similar
effort, in the next 4 years.

What features do worth the upgrade
==================================

`Exception chaining`_
---------------------

In python 3, when an exception is raised from within an ``except`` block, it is
concatenated to the former exception, and the traceback of both is available to
whoever catch them. That way, we can always be sure that our top most logging
system will log the entire traceback, even if the latest exception "mask" the
original one.

This feature could solve us several debugging hours. Even more, I'm sure that we
gave up on lots of bugs we couldn't investigate properly, as the original
exception was lost due to a bug in the ``except`` block.

`Unorderable types`_
------------------------------

If something is broken, I prefer it to raise exception as soon as possible. In
python 2, the following won't fail!

.. code-block:: python

    >>> # python2
    >>> 'hello' < 1

WTF?!? Why should anyone allow comparison between a string and an int!?!
Moreover, what is the result, ``True`` or ``False``? In python 3 this issue was
solved for good:

.. code-block:: python

    >>> # python3
    >>> 'hello' < 1
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: str() < int()

Again, we saw such bugs before in our system, and they are hard to spot. Having
the language solve this corner for us will be great.

List comprehensions that doesn't leak
-------------------------------------

Again, another source for nasty bugs.

.. code-block:: python

    >>> # python2
    >>> i = 42
    >>> squares = [i ** 2 for i in xrange(10)]
    >>> print(i)
    9

.. code-block:: python

    >>> # python3
    >>> i = 42
    >>> squares = [i ** 2 for i in xrange(10)]
    >>> print(i)
    42

And much more
=============

Apart from new features there are the plethora of packages that we can't use
with python 2.6. External dependencies gradually drop support, while the
standard library continuously improves with new and shiny tools, such as
``concurrent.futures`` and ``asyncio``.

.. _twisted: https://pypi.python.org/pypi/Twisted
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Exception chaining: https://www.python.org/dev/peps/pep-3134/
.. _Comparing unorderable types: http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#comparing-unorderable-types
