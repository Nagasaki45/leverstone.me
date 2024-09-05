Intro to git workshop
#####################
:date: 2019-02-21 19:00
:author: Tom Gurion
:tags: tutorials, tools
:slug: intro-to-git-workshop
:description: A 4 hours intro to git workshop for my PhD fellas.

A 4 hours introduction to git workshop for my PhD fellas.
Based on an old `git crash course <{filename}/Blog/git_crash_course.rst>`_ blog post.

.. image:: /images/blog/git_logo.gif
  :alt: git logo
  :width: 100%

Why?
----

- Keep your projects organized.
- Collaborate with others.
- Get involved with open source.

Command what?
-------------

`Introduction to the command line <https://tutorial.djangogirls.org/en/intro_to_command_line/>`_.
From now on, the rest is done there.

Configuring git for the first time
----------------------------------

.. code-block:: bash

  git config --global user.name "Your name here"
  git config --global user.email "your_email@example.com"
  git config --global core.editor nano

Working locally
---------------

When git manages a directory on your computer we call this directory a local git repository.

There are two ways to start to work in such a repository:

- ``git clone https://github.com/some_user/some_repo.git`` to download a project into a new directory ``some_repo``.
- ``git init`` to make the current directory a git repository.

Unstaged ➜ staged ➜ committed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/blog/git_staging_commit.webp
  :alt: git local workflow
  :width: 100%

**Remember!** you can always see the current state and the staging / unstaging commands with ``git status``, so don't try to memorize them.

When you are satisfied with the changes commit them:

.. code-block:: bash

  git commit -m "an informative message describing your change"

Exercise
~~~~~~~~

1. Create a directory called ``jokes``.
2. Make it a local git repository.
3. Create a file called ``jokes.txt`` in that directory.
4. Write some funny stuff.
5. Add and commit.
   Try to have an informative commit message.
6. Repeat steps 4-5 as many times as you want 🙃.

Explore your repo
~~~~~~~~~~~~~~~~~

.. code-block:: bash

  git log                 # see the history
  git diff                # see the unstaged changes
  git diff --staged       # see the staged changes
  git show <COMMIT_HASH>  # see the changes in a commit


Collaborating through GitHub
----------------------------

GitHub is a place to share and collaborate on git repositories.
Go head and create an account!

Your local git repository can be "linked" to remote repositories.
To see them run ``git remote`` (or with extra info using ``git remote -v``).
If you cloned an existing repository you should see one remote, called ``origin``, in the list.
Otherwise, create a new GitHub repository and add it as a remote with:

.. code-block:: bash

  git remote add origin https://github.com/you/your_repo.git

Naming a remote ``origin`` is just a convention. It has no special meaning.

``pull``
~~~~~~~~

To get the latest changes (commits) from your remote run:

.. code-block:: bash

  git pull origin master

What's master? The name of the default branch.
More on that later.

``push``
~~~~~~~~

If you have permissions to push code to the remote repository you can update the remote with your changes (commits) by running:

.. code-block:: bash

  git push origin master

**Remember!** Always ``pull`` before you ``push`` to avoid unnecessary conflicts.

.. image:: /images/blog/git_meme.avif
  :alt: git Austin Powers meme
  :width: 100%

Assuming that you already have a local repository with a remote (called ``origin``) that you can push code to, a simple but complete workflow might look like that:

.. code-block:: bash

  git pull origin master         # to get the latest changes
  # work work work...
  git status                     # to see all of the changes you did
  git diff                       # optional but handy
  git add FILE_WITH_CHANGES      # repeat as necessary
  git commit -m "your message"   # commit the changes to the repository
  git push origin master         # to upload your changes

Exercise
~~~~~~~~

1. Create a new GitHub repo, called ``jokes``.
2. Add it as a remote for your local ``jokes`` repo.
3. Push your jokes to GitHub.

Forks and pull requests
~~~~~~~~~~~~~~~~~~~~~~~

If you don't have permissions to push code to a remote repository.

1. Fork the repository.
   It will copy the remote repository to your account.

.. image:: /images/blog/github_fork.webp
  :alt: GitHub fork button
  :width: 100%

2. Add your fork as a remote.

.. code-block:: bash

  git remote add mine https://github.com/you/your_repo.git

3. Work on your fork.

4. Send your commits to the owner(s) of the projects using a pull request.

.. image:: /images/blog/github_pull_request.webp
  :alt: GitHub pull request button
  :width: 100%

Exercise
~~~~~~~~

1. Fork `this repository <https://github.com/Nagasaki45/mat-trivia>`_.
2. Clone your fork so you'll have a local git repository on your computer.
3. Answer some questions in one of the files in ``mat-trivia/trivia/``.
4. Stage the changes, commit, and push to your remote repo.
5. Submit a pull request

Where to go next?
-----------------

- *Branches* are an important concept in git.
  `Learn them here <http://learngitbranching.js.org/>`_.
- Ignore files in the repo with ``.gitignore``.
- `Good intro to git in slides format`_.
- `Stack overflow`_ for questions, as usual :-)
- `Pro Git book`_: lots of info, sometime too verbose.

.. _`Good intro to git in slides format`: https://speakerdeck.com/alicebartlett/git-for-humans
.. _`Stack overflow`: https://stackoverflow.com/
.. _`Pro Git book`: https://git-scm.com/book/en/v2
