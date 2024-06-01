Poor man's trick to add and remove conda from $PATH
###################################################
:date: 2015-10-24
:author: Tom Gurion
:tags: thoughts, python, tools
:slug: poor-mans-trick-to-add-and-remove-conda-from-path

`Conda <http://conda.pydata.org/docs/>`__ is great for managing
dependencies as matplotlib and scipy: try to install these with pip, in
a virtualenv, and you will be convinced that conda is better in that
regard.
But!
Somehow, the folks at continuum analytics decided that using conda
should override the default python environment (the system-wide python
installation). There are some
`recommendations <https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/opMLiGnjymE>`__,
but AFAIK there is no official solution for the problem.
Here is my solution to keep the system-wide python installation as my
default environment and start to use conda only when I want to:

.. code-block:: bash

  $ cat ~/bin/unconda
  export PATH=`echo ":${PATH}:" | sed -e "s:\:$HOME/miniconda3/bin\::\::g" -e "s/^://" -e "s/:$//"`

Got the trick from
`here <https://ntk.me/2013/05/04/path-environment-variable/>`__. Thanks
Natsuki!

.. code-block:: bash

  $ cat ~/bin/reconda
  export PATH="$HOME/miniconda3/bin:$PATH"

Now just add ``$HOME/bin`` to your path if it's not already there and you
are ready to go.
Don't forget to remove the line in your ``.bashrc`` that add miniconda to
the path in the first place.

.. youtube:: UdQgJdnrEDw
