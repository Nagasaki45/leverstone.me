docker-compose in production - part 2
#####################################
:date: 2016-08-05
:author: Tom Gurion
:tags: thoughts, docker, web, tools
:slug: docker-compose-in-production-part-2

Few months ago I shared my `experiences with docker-compose in production`_.
Recently I faced another deployment and decided to use the same technique. This
time I used it somewhat differently. In this blog post I would like to share the
new experiences.

I started by following the process that went so well last time, which summarized
to:

- Create a ``Dockerfile`` for the app.
- Create a ``docker-compose.yml`` file with my app and its dependencies (official postgres and redis docker images).
- ``git clone`` the project on the server.
- Build the project **on the server**.
- Copy the "secrets" file to the server.
- Spin everything with ``docker-compose up``.

But guess what? My digital ocean's droplet has only 512MB of RAM, which are not
enough for building the image. The beloved technique couldn't work with my
server!

`Docker Hub`_ to the rescue
---------------------------

OK. I can't build the image on the server, but I still want to use docker and
docker-compose for all of their advantages. The solution will be to build the
image somewhere else, upload it to `Docker Hub`_- an open and free repository
for docker images - and fetch it from there directly to the server.

There are two ways to upload a docker image to Docker Hub. The first is to link
it to your github account and instruct it to build an image whenever you push
code to the repository. The second is to build the image locally and push it to
the Hub using the docker command line tool. I wished I could choose the first
option, but due to memory restrictions the build failed on their build servers
similarly to the way it failed on my digital ocean droplet. Therefore, I choose
the 2nd option.

With this revised deployment technique there are only two files on the server,
the ``docker-compose.yml`` file and the "secrets" file. In my first blog post
about docker-compose the ``docker-compose.yml`` used the current directory as
the ``build`` path for the image. Now, the full image name on Docker Hub is
referenced. Here is my ``docker-compose.yml`` file:

.. code-block:: yaml

  web:
    image: nagasaki45/krihelinator_web
    ports:
      - 80:80
    links:
      - db
      - stash
    env_file: ./secrets
    restart: always

  db:
    image: postgres
    restart: always

  stash:
    image: redis
    restart: always

Summary
-------

Ideally, a server should only serve the application to the clients, and run the
necessary infrastructure to support it. Building or compiling a project on the
server is possible, but it doesn't have to be that way. With docker and
docker-compose based deployments the build can be done on one machine (be it
your local machine, Docker Hub's dedicated build servers, or some other
continuous integration / delivery server). But it's not only possible, it even
simplifies the process a bit as there is no source code involved, and less
operations run on the server. Give docker-compose a try, you won't regret it.

.. _experiences with docker-compose in production: {filename}/Blog/docker-compose-in-production.rst
.. _The Krihelinator: https://github.com/nagasaki45/krihelinator
.. _Docker Hub: https://hub.docker.com/
