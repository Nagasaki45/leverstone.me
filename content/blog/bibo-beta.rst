bibo, the command line reference manager, is in beta now!
#########################################################
:date: 2020-05-28
:author: Tom Gurion
:tags: projects, python, tools
:slug: bibo-beta

.. image:: /images/blog/bibo_beta_release_banner.svg
  :width: 100%
  :alt: bibo beta release banner

bibo is a command line reference manager with a single source of truth: the ``.bib`` file. It is inspired by `beets <https://github.com/beetbox/beets>`_. After 3 years in the making I believe it's ready for other people to use.

What are the advantages over mendeley / zotero / etc. you ask?

- It gives you control over your files. They are not hidden in some obscure database, hence easy to backup, share, etc.
- It's a thin editor of .bib files, so no need to export your bibliography anywhere.
- It's extensible with plugins.
- It's a command line tool. So if you're a fan of the unix philosophy (small building blocks that are easy to integrate with each other) you might love it.

`Here are the docs <https://bibo.readthedocs.io/en/latest/index.html>`_ with everything you need to learn more about the project and to get started.

This beta release (0.1.0) marks the first release that is fully functional, was tested extensively, and should work for most people. It's not a production ready software yet, so make sure you backup your bibliography (and PDFs) before using it! It is, however, used already by a few people, so give it a spin if you like the idea.

If anything is broken, please reach out! I will be happy to read about `issues on github <https://github.com/Nagasaki45/bibo/issues>`_. Contributions are also super welcome. More about this in the docs.
