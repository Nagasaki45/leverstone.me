An Even Better Pip Worflow™
###########################
:date: 2016-11-04 23:50
:author: Tom Gurion
:tags: thoughts, python, tools
:slug: an-even-better-pip-workflow

The 9th major version of |pip|_, the recommended tool for installing python packages, was released two days ago. I took a short look on `the changelog`_ to see what's new. At first, I couldn't notice anything that will change my current workflows. Usually, the important changes are listed first, but there was nothing groundbreaking there. However, I kept reading, to find this:

- Add *--not-required* option to ``pip list`` to list packages that are not dependencies of other packages.

In "`A Better Pip Workflow™`_", Kenneth Reitz describes a problematic aspect of dependencies management in python. Usually, we "freeze" the state of the dependencies of a project with ``pip freeze > requirements.txt`` to reproduce the exact environment later with ``pip install -r requirements.txt``. The problem starts when you want to upgrade these dependencies. Take this `blog dependencies`_ for example.

.. code-block:: bash

    $ pip list
    blinker (1.4)
    docutils (0.12)
    feedgenerator (1.8)
    Jinja2 (2.8)
    MarkupSafe (0.23)
    pelican (3.6.0)
    pelican-readtime (0.1.2)
    pelican-youtube (0.2.0)
    pip (9.0.0)
    Pygments (2.1.3)
    python-dateutil (2.5.3)
    pytz (2016.4)
    setuptools (28.8.0)
    six (1.10.0)
    Unidecode (0.4.19)

Ideally, I would like to manage only the packages I call directly from code / command line (let's call them the "top most dependencies" from now on), and let them manage their dependencies for me. Therefore, I would have to read this output carefully to decide what to upgrade: "did I install Pygments? and what about docutils? I know for sure that pelican-youtube was installed manually, so let's ``pip install --upgrade pelican-youtube``" and so forth...

Kenneth's recommendation to simplify the upgrade process is to keep two requirements files, the 1st includes all of the dependencies with their versions (``pip freeze > requirements.txt``), and the 2nd, ``requirements-to-freeze.txt`` should be **managed manually** to contain the top most dependencies. When it's time for an upgrade, call ``pip install -r requirements-to-freeze.txt --upgrade``. Just don't forget to run ``pip freeze > requirements.txt`` immediately afterwards!

With the flag introduced in ``pip`` 9.0.0, there is no more need for the ``requirements-to-freeze.txt`` file. To find out which packages should be upgraded run ``pip list --not-required``. However, there are still some caveats to note:

1. The ``--not-required`` flag is implemented for ``pip list`` and not for ``pip freeze``. They have different format. When the later is suitable for requirement files the former is not. Here is a `github issue`_ to implement the same flag for ``pip freeze``.
2. Assuming that the previous issue will be solved, I couldn't find a **nice** (read as "no bash scripting") way to pipe the output of ``pip freeze --not-required`` to ``pip install --upgrade``. There is still an intermediate phase of creating a temporary ``requirements-to-freeze.txt`` file.
3. Until the first issue will be resolved, we will upgrade ``pip`` and ``setuptools`` with our top most dependencies. The reason is that they are listed by ``pip list`` but not by ``pip freeze``.
4. We will probably want to strip the version numbers from the output of ``pip list --not-required``. It is meaningless to ask pip to upgrade but state the old versions in the same time.

Demo time!
==========

Let's try things out by updating this blog dependencies! First, let's see the top most dependencies:

.. code-block:: bash

    $ pip list --not-required
    pelican (3.6.0)
    pelican-readtime (0.1.2)
    pelican-youtube (0.2.0)
    pip (9.0.0)
    setuptools (28.8.0)

OK. Considering the caveats above, we will need some bash scripting here. First, we want to remove the versions from the output. ``sed`` might be our friend here. Let's try to use it to remove the versions completely by taking everything from the space to the end of the line and replacing it by an empty string:

.. code-block:: bash

    $ pip list --not-required | sed 's/ .*//'
    pelican
    pelican-readtime
    pelican-youtube
    pip
    setuptools

Great! Let's pass this to ``pip install --upgrade``:

.. code-block:: bash

    $ pip install --upgrade `pip list --not-required | sed 's/ .*//'`
    ...
    Successfully installed feedgenerator-1.9 pelican-3.6.3 pytz-2016.7

That's all. The top most dependencies were upgraded.

.. |pip| replace:: ``pip``
.. _pip: https://pypi.python.org/pypi/pip
.. _the changelog: https://pip.pypa.io/en/stable/news/
.. _blog dependencies: https://github.com/Nagasaki45/blog
.. _`A Better Pip Workflow™`: http://www.kennethreitz.org/essays/a-better-pip-workflow
.. _github issue: https://github.com/pypa/pip/issues/4088
