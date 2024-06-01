My Jupyter (tmpnb) server and Thebe
###################################
:date: 2015-08-04
:author: Tom Gurion
:tags: thoughts, python, web, docker
:slug: my-jupyter-tmpnb-server-and-thebe

**Notice: code execution in the browser is currently broken**

.. code-block:: python

  %matplotlib inline
  import matplotlib.pyplot as plt
  import numpy as np
  from IPython.html.widgets import interact

  def plot_sine(frequency=1.0, amplitude=1.0):
      plt.ylim(-1.0, 1.0)
      x = np.linspace(0, 10, 1000)
      plt.plot(x, amplitude*np.sin(x*frequency))

  interact(plot_sine, frequency=(0.5, 10.0), amplitude=(0.0, 1.0));

Isn't that amazing?!?
I've recently installed an
`tmpnb <https://github.com/jupyter/tmpnb>`__ sever on my digitalocean
server, you can access it at ``nagasaki45.com:8000``.
So, what's the big deal?
This configuration allow anyone to use python (or one of the other
supported / installed kernels) on the web, using my server. You don't
have to ask for permission; you can just go to the provided address and
start to code without any local installation.
And it goes way beyond:

-  You can open new terminal, 'git clone' your project, and demonstrate
   it to someone else. And you can do it on mobile devices too. Again,
   no installation required, everything is running on the server.
-  You can use `thebe <https://github.com/oreillymedia/thebe>`__ to add
   code snippets as the one above to any static html page (your blog, as
   example). Even interactive widgets will run the computation back and
   fourth from the server to the web frontend for presentation.

So go ahead, write some code, let me execute it for you ;-)

Edit 6.5.16:
~~~~~~~~~~~~
Oreilly shut down their tmpnb server too :-(
So this blog post won't execute python code anytime soon.

Edit 20.9.15:
~~~~~~~~~~~~~
I'm stopping the service on my server due to some number crunching tasks
I'm running on it.

Edit 1.9.15:
~~~~~~~~~~~~
My digitalocean VM has "only" 512MB of RAM. I decided to span tmpnb
with 4 docker containers, 50MB RAM each, to keep the server load on
minimum. Apparently, it possessed some issues as 50MB are probably not
enough.
Right now the example above uses the same tmpnb server has the one in
thebe example
(`here <https://oreillymedia.github.io/thebe/examples/matplotlib.html>`__),
namely https://oreillyorchard.com:8000/. It works much better now as
there are no kernal failures when running the examples.
