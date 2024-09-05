git crash course
################
:date: 2017-01-31 17:00
:author: Tom Gurion
:tags: tutorials, tools
:slug: git-crash-course
:description: A really short introduction to git for my PhD fellas.

A really short introduction to git for my PhD fellas.

First, TryGit_
--------------

.. _TryGit: https://try.github.io/

Clone something
---------------

There are two ways to start to work in a git repository.

- ``git clone https://github.com/some_user/some_repo.git`` to download a project into a new directory `some_repo`.
- ``git init`` to make the current directory a git repository.

Go ahead and clone a project of interest.

Working locally
---------------

.. image:: /images/blog/git_staging_commit.webp
  :alt: git local workflow
  :width: 100%

**Remember!** you can always see the current state and the staging / unstaging commands with ``git status``, so don't try to memorize them.

When you are satisfied with the changes commit them:

.. code-block:: bash

  git commit -m "an informatice message describing your change"

Explore
-------

.. code-block:: bash

  git log  # see the history
  git diff  # see the unstaged changes
  git diff --staged  # see the staged changes
  git show <COMMIT_HASH>  # see the changes in a commit

Collaborating through GitHub
----------------------------

GitHub is a place to share and collaborate on git repositories.

Your local git repository can be "linked" to remote repositories.
To see them run ``git remote``.
If you cloned an existing repository you should see one remote, called ``origin``, in the list.
Otherwise, create a new GitHub repository and add it as a remote with:

.. code-block:: bash

  git remote add origin https://github.com/you/your_repo.git

``pull``
~~~~~~~~

To get the latest changes (commits) from your remote run:

.. code-block:: bash

  git pull origin master

``push``
~~~~~~~~

To update the remote with your changes (commits) run:

.. code-block:: bash

  git push origin master

**Remember!** Always ``pull`` before you ``push`` to avoid unnecessary conflicts.

.. image:: /images/blog/git_meme.avif
  :alt: git Austin Powers meme
  :width: 100%

A simple but complete workflow
------------------------------

Assuming that you already have a local repository with a remote (called ``origin``) that you can push code to:

.. code-block:: bash

  git pull origin master         # to get the latest changes
  # work work work...
  git status                     # to see all of the changes you did
  git diff                       # optional but handy
  git add FILE_WITH_CHANGES      # repeat as necessary
  git commit -m "your message"   # commit the changes to the repository
  git push origin master         # to upload your changes

More info and resources
-----------------------

- *Branches* are an important concept in git. `Learn it <http://learngitbranching.js.org/>`_!
- `Pro Git book`_: lots of info, sometime too verbose.

.. _`Pro Git book`: https://git-scm.com/book/en/v2
