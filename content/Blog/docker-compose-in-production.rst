docker-compose in production
############################
:date: 2016-02-29
:author: Tom Gurion
:tags: thoughts, django, docker, web, tools
:slug: docker-compose-in-production

Deployment sucks! I'm not a dev ops / sys admin type of person, and
every time I'm into deploying a web project I start to rethink the whole
process and get confused. Recently, I decided to restart the work on one
of my older django projects,
`Xteams <https://github.com/Nagasaki45/Xteams>`__, and one of the first
tasks was to migrate it from `heroku <https://www.heroku.com/>`__ to my
VPS - a `digital ocean <http://digitalocean.com/>`__ droplet. Don't get
me wrong, heroku is great, but I'm already paying 5 bucks per month to
digital ocean, where I host all of my web projects, and the single web
dyno that heroku gives for free is a real limitation.
Before starting to migrate the project, I decided about the following
deployment requirements:

#. I want a consistent production environment, with the fewest possible
   system wide dependencies, mainly due to...
#. I have several projects already deployed to this VPS, so I need a
   production environment which will play nice with them both in term of
   dependencies and in hostname routing (resolving foo.com and bar.com
   to their respective ports / apps).
#. Staging and production environments should be as similar as possible,
   and I want to be able to run the staging environment on my local
   machine.
#. Moreover, if I can utilize parts of the production configurations for
   development - like DB / job queue and workers - it's even better.
#. Keep deployment scripts to the bare minimum.
#. Not over-engineer the issue.

`Dokku <https://dokku.com/>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I liked heroku. Deploying is really easy, and if I can accomplish a
task using git alone I will probably do it that way :-) So I checked
dokku. It clearly solves the first requirement easily: apart from dokku
itself there is no system wide configuration and dependencies to worry
about. It also solves issues 5 and 6 really nicely: the deployment is
done by pushing to remote repository and production specific
configurations (or secrets) can be added with environment variables,
which I like. On the other hand, I'm not sure if dokku would play nicely
with my other projects, there is no way to run an environment similar to
production locally, and I can't reuse components for development.

Deployment scripts (like `ansible <https://www.ansible.com/>`__ / `fabric <http://www.fabfile.org/>`__)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Almost a year ago I read Harry Percival's great book `"TDD with
Python" <http://chimera.labs.oreilly.com/books/1234000000754/>`__. He
teaches how to automate deployment with ansible. I managed to deploy the
sample app for the book and later I used the same technique to deploy
one more django app of mine. However, I really don't like this approach.
It seems very fragile, touching too many configurations too often,
making me afraid about my other projects on the server. It's a lot of
work too, and work that I can't reuse for development. Overall, I feel
that it only answer requirement 3 and 6. The rest are not even close to
be answered.

Finally: docker and docker-compose to the rescue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. image:: /images/blog/docker_compose_prod.avif
  :alt: Docker compose in production

You weren't expected this, didn't you?!?
Let's follow the diagram and I will try to convince you why using
docker-compose in production (and also partly in development) is a good
idea. With docker, you can create an image of an application, together
with all of its dependencies, and run it in an isolated environment,
which is called a docker container. docker-compose lets you take a set
of such images, define the links between containers (in means of network
and volume access) and orchestrate all of the containers together, from
building to running.
In the current example I had a DB container with an official postgres
image. Every time I need to configure postgres on my local machine I
find myself reading throughout half of stackoverflow and the official
docs for information. This time it was really easy: I grabbed the
official postgres image from docker hub and that's it - no more
configuration needed.
Second, there is the web container that runs the django app itself.
This is the main container in my project. I wrote a Dockerfile to
describe how the image should be built. It contains only a few lines:
starting from the official python 3.5 image, pip installing
dependencies, and collect static files. Secrets are written in a special
file which django-compose pass to the container as environment
variables. This file is not source controlled: I created one manually on
my local machine and another one, slightly different, on my server.
Here's the Dockerfile for this image:

.. raw:: html

   <script src="https://gist.github.com/Nagasaki45/58bd4d758c1408d2c4b7.js"></script>

Above the web container there is the Nginx container, which have
access to a shared volume from the web container that contains all of
the static files, so static files are served by Nginx directly. Here is
the Nginx container configuration file:

.. raw:: html

   <script src="https://gist.github.com/Nagasaki45/1830411bc5e510c096ae.js"></script>

Outside of the docker orchestration there is one more Nginx instance,
its job is to route each incoming request to the correct app on the
server. Every app is listening on a different port and Nginx only route
traffic based on the hostname in the http header. Here's the
configuration file:

.. raw:: html

   <script src="https://gist.github.com/Nagasaki45/4575b34641bc4e804c09.js"></script>

Here's how my docker-compose configuration file looks like:

.. raw:: html

   <script src="https://gist.github.com/Nagasaki45/15f22aeb60e49d1c30d3.js"></script>

Building and running these containers is really simple:

.. raw:: html

   <script src="https://gist.github.com/Nagasaki45/9aed10b837612f385bc7.js"></script>

So now, let's try to tackle the requirements list again:

#. The only system wide dependencies are docker and docker-compose.
   Apart from that there is the system wide Nginx server, which is
   already there for the other apps.
#. Running the new project side by side with the other projects is just
   a matter of adding one more server configuration file to the system
   wide Nginx (more info is available in `the project
   README <https://github.com/Nagasaki45/Xteams#more-info>`__). This is
   no different from any other app on the server, whether it's a django
   app or a static website.
#. There is no difference at all between staging and production.
   Spinning a staging environment locally is just a matter of building
   and running the docker-compose environment.
#. I'm not using a system wide postgres instance in development.
   Instead, I use the same postgress docker image I run in production.
   Moreover, if I will need more building blocks, as a job queue and
   workers, I will be able to add their respective images to both
   development and production docker-compose configuration files.
#. I do have a script for deployment, but it doesn't do much except
   pulling the latest source from github, building and running. That's
   all.
#. One might argue that I did over-engineered the issue. Compared to
   using dokku this solution is definitely more complex. However, I'm
   not sure if maintaining this deployment mechanism is harder than
   maintaining ansible deployment scripts, especially when there are
   several different apps on the same server.

Cons
^^^^
-  Provisioning, although very simple, is done manually: I create a
   folder on the server, clone the project, and add the django "secrets"
   file. It can be automated too, of course, but I'm not sure I see a
   reason for that now.
-  I wished I could run functional tests from a special
   `selenium <http://www.seleniumhq.org/>`__ container against the
   staging environment. This is not trivial as it requires a
   bidirectional network access between the selenium driver and the web
   app. I gave up the idea, because of its complexity, and I'm running
   selenium tests only against the development environment, outside of
   any docker container.
-  Sharing a volume between the web container and the Nginx container is
   a neat trick. However, I most force-remove the old web container
   after any build and before running the new container to "refresh" the
   volume with the latest collected static files. It's a hack I don't
   like, but I live with it.

Summary
^^^^^^^
I really like docker-compose. At first, it looks like a tool with a
steep learning curve. But don't be too intimidated. Give it a try and
you might find an elegant solution for deployments, which will hopefully
scale well with your requirements.
I'm sure that there are lots of approaches I'm not covering here, and
all of the above only reflects my limited experience in the field.
Therefor, feel free to criticize and share your experience about the
subject!
