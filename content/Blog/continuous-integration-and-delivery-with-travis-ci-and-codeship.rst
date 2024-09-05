Continuous integration and delivery with travis-ci and codeship
###############################################################
:date: 2016-05-30
:author: Tom Gurion
:tags: thoughts, web, tools
:slug: continuous-integration-and-delivery-with-travis-ci-and-codeship

.. image:: /images/blog/travis_codeship.webp
  :width: 100%
  :alt: Travis vs. Codeship

Generally speaking, continuous integration (CI) is the process of
running your test suite automatically when you push code to your repo.
Continuous delivery / deployment (CD) is the process of deploying the
new code to your server whenever you push to specific branches in your
repo. There is enough information about these on the web so I won’t
cover it here. Instead, I would like to talk about travis-ci and
codeship, which are: online services that help you accomplish these
tasks easily; tightly integrated with github; free for open source
projects; very recommended. There are many similar services, of course,
but I won’t mention them as I didn’t use them enough to have an opinion.
So, let’s start with travis.

`Travis-CI`_
------------

AFAIK, travis is the natural CI choice for python developers, and for
good reasons:

-  It’s the easiest to configure and use.
-  Configuration is kept in the git repo, using a YAML file. Therefore,
   it is version controlled, which is always a good thing.
-  It will run your tests against a set of python versions, each one in
   its own build (AKA a test matrix).

There are situations, however, in which travis might not be enough for
you, especially when you want to set up continuous deployment. Enters
codeship.

`Codeship`_
-----------

Codeship is clearly inferior:

-  It is configured using a web interface, using bash scripts to prepare
   the environment, run the tests, and deploy (with different script per
   branch, which is nice). Yep, you’re expected to type bash scripts into
   web forms!
-  The environment setup is lacking. The `official recommendation for setting
   the python version`_, for example, looks like a hack.
-  You can’t define a test matrix.

It sounds bad, I know, but on the other hand codeship has one feature
that is crucial to my workflow. Each project on codeship have an
ssh-key. Therefore, once you copied the public key to your server
``authorized_keys`` file, codeship can ssh / scp to it without
additional effort, exactly as you do from your development environment.

For example, I have static sites that use a simple script to generate
the site and upload it to the server using ``rsync``. From my
development environment it looks like:

.. code-block:: bash

    make rsync_upload

And guess what? The codeship deployment script do exactly the same when
I push code to the ``master`` branch, and nothing more!

    It is important to note that travis do offer `this feature`_ for
    paid plans, and that `hacky alternatives`_ exist.

Wrap up
-------

Personally, for everything "deployable" I stay with codeship at the moment,
as this single feature is more important to me than travis's advantages.
To compensate, I document the different scripts (environment setup, test
running, and deployment) in the project ``README``. In addition, although the
test matrix is a crucial feature when you work on libraries and tools,
web sites and application are usually different. You control the environment
you deploy to, and can set the CI environment to be the same / very similar.

Having said that, for everything else, just go with travis. You won't
regret it.

TL;DR
-----

-  Prefer `travis-ci`_ when developing a library / command line
   utility / non “deployable” software.
-  Use `codeship`_ for continuous deployment of web sites and
   applications.

.. _travis-ci: https://travis-ci.org/
.. _codeship: https://codeship.com/
.. _Travis-CI: https://travis-ci.org/
.. _Codeship: https://codeship.com/
.. _official recommendation for setting the python version: https://codeship.com/documentation/languages/python/
.. _this feature: https://docs.travis-ci.com/user/private-dependencies/#User-Key
.. _hacky alternatives: https://gist.github.com/lukewpatterson/4242707
