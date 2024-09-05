Python vs. elixir for a web-app wrapper for a script
####################################################
:date: 2017-08-27
:author: Tom Gurion
:tags: thoughts, python, elixir, asyncio
:slug: web-script
:description: Comparing python (with asyncio) and elixir (with cowboy, plug, and poolboy) for developing a web-app for wrapping a script.

.. image:: /images/blog/python_vs_elixir.webp
  :width: 100%
  :alt: Python vs. elixir

I'm a facing a project with the following requirements:

- An existing script should be wrapped with a web server.
- The script takes 10-30 seconds to run, so just let the user wait for it to complete.
- Multiple users should be able to call the script concurrently.
- Make sure to protect the server from overloading by limiting the number of concurrent active scripts.

I created a repo with two projects, in python and elixir, to see how easy / hard the task will be with each technology.
You can find the repo `here <https://github.com/Nagasaki45/web-script/>`_.
The frontend, and the demo script to run, are the same for both projects.
Getting and validating user input is not demonstrated, as it should be straightforward in both languages.
The idea was to compare the concurrency stuff.

Python
------

The implementation is based on `aiohttp <https://aiohttp.readthedocs.io/en/latest/index.html>`_, with no much extras.
There is a global counter to track the number of active scripts.
A new POST request checks the counter.
If it reaches the maximal allowed active scripts a 503 error is returned, indicating that the service is unavailable.
Otherwise, first, the counter is incremented.
Then, ``asyncio.create_subprocess_exec`` is used to call the script.
Lastly, the result is returned to the user, and the counter is decremented under ``finally``.

Elixir
------

The general idea is very similar.
The server is based on `cowboy <https://github.com/ninenines/cowboy>`_ and `plug <https://github.com/elixir-plug/plug>`_.
Instead of a global counter I'm using `poolboy <https://github.com/devinus/poolboy>`_ to create a pool of workers for calling the script.
On each POST request, if the pool if full, the 503 error is returned.
Otherwise, the script is called and the result is returned to the user.

Conclusions
-----------

I'm a complete asyncio newbie, and wasn't sure how complex the implementetion will be.
It always feel a bit restrictive for me.
For example, without the already implemented ``asyncio.subprocess`` module, following the requirements would be much more difficult.
I'm also more confident with elixir, as I use it almost exclusively for everything web-based.
With elixir you can use whatever library you want and make use of all of the concurrency feature of the language without any special adapters.
Surprisingly, the python solution ended up much simpler than I thought, and it is much shorter than the elixir solution (mainly due to the way a project is structured in elixir).
So, I ended with two easy to use options, hence the decision between them will be even harder.
Or maybe it's time to properly learn asyncio.
