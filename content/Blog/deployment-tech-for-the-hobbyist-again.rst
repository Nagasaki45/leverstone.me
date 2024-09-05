Deployment tech for the hobbyist, again
#######################################
:date: 2023-12-15
:author: Tom Gurion
:tags: thoughts, dokku, docker, web, tools
:slug: deployment-tech-for-the-hobbyist-again

**TL;DR:** Try `Dokku`_ if you want to run multiple toy web apps on a single server and keep the cost at minimum.

.. image:: /images/blog/dokku-logo-with-name.webp
  :alt: Dokku logo with name
  :width: 100%

Let's talk, yet again, about deploying toy web apps.
I wrote about this topic many moons ago (see docker-compose in production `part 1`_ and `part 2`_), but things have changed and it's time for an update.

The main thing that changed, really, is having much less time to maintain projects and money to keep the servers up.
In the past I had a single virtual server (a `Digital Ocean droplet`_) that ran everything.
It had `nginx`_ installed manually, and whenever I added a project, I had to reconfigure it to pass traffic to the port the project was running on.
This, again, was done manually.
The deployment itself was done by running a custom script somewhere, either from the local machine or from CI/CD.
That's pretty old-school, isn't it?
And what about SSL?
Forget it; that was too complicated.

Over time projects started to transition to different platforms that automated the process.
I had projects on `Heroku`_ for years, using their now-retired free dev offering.
The cheapest option at the moment is $5 a month.
Some projects were deployed to `Digital Ocean's App Platform`_ which also starts at the same cost.
I found both platform very convenient to use, and although not particularly expensive, the cost ramps up quickly when you have a few projects, and that's without considering having a DB and other services to support the web app.
Last year, I invested some time learning AWS (Amazon Web Services), and in the process, deployed a toy project to `Elastic Beanstalk`_.
In the first year I was on the AWS free tier, but after that the price got really high.
If memory serves the forecast was >$50 a month for a load balancer, two of the smallest server instances possible, and a relational DB.
Two days after the end of the free tier period the project was shut down due to the cost.

A solution was called for hosting my toy projects.
If you read this far, you can understand the requirements:

- It needs to be cheap. Ideally, I don't want to consider cost for adding or removing toy projects. A one-server solution sounds good for this.
- It needs to be simple and easy to maintain. `AWS Lambdas`_ are cheap and, in that sense, might be a good solution for toy projects, but my projects already exist in the form of servers and changing them to Lambda functions is too much effort.

I had a look at `Dokku`_ many years ago, and decided to check it again now.
The tagline is 'An open-source PaaS alternative to Heroku', and based on my good experience with `Heroku`_ it sounds pretty much up my alley.

As already mentioned, I also have good experience with `Digital Ocean`_.
If only I can have `Dokku`_ running in a Digital Ocean droplet 🤔

.. image:: /images/blog/dokku-on-digitalocean.webp
  :alt: Dokku on Digit Ocean

Yes! A quick search reveals a `one click deployment of Dokku on Digital ocean through their marketplace`_.
I went for a $12 virtual machine with 1 CPU, 2GB RAM, and 50GB of SSD storage, hoping it will be enough for a handful of projects for a while.
Within 20 minutes I was trying to deploy my first abandoned toy project on my new `Dokku`_ instance.
Another 20 minutes in, and the project was up and running.
Three more projects followed in what amounts to 2-3 hours work.
From these 4 project, 3 were previously deployed to `Heroku`_ using `buildpacks`_ and `Digital Ocean's App Platform`_ using containers (having a ``Dockerfile`` at the root of the repo).
Moving these to the new system was a breeze:
adding a git remote locally and pushing, then on the new server configuring environment variables and `configuring SSL following the deployment tutorial`_, followed by creating A tags on my DNS provider, and that's it!

The 4th project was previously on `Elastic Beanstalk`_ and backed by a relational DB.
I had the data from the DB exported into JSON before shutting the project down.
I was worried about transitioning it, but found it extremely easy as well!
Adding a DB to it was very simple following the so-far-excellent docs.
It took me a while to wrap my head around loading the backup, but the following did the trick:

.. code-block:: bash

    docker ps  # to find the container ID of my app
    docker cp my-backup.json my-app-container-id:/app
    dokku enter my-app
    # Now run whatever command within the image to load the data

One last project is an `Elixir`_/`Phoenix`_ project that was previously deployed on `Gigalixir`_ with their custom buildpacks.
I had to containerise the project to make it work with the new system, and that took a while.
Nothing to blame the new system for though.
Just the usual modernisation of an old project.

Do I care about having these project highly available? no.
Do I care about no-downtime deployments? also no.
What about data loss (e.g. losing the DB)? That's not the end of the world either.
`Dokku`_ supports cron jobs, so it might be interesting to explore doing regular DB backups.
Or, alternatively, I can accept the $2.40 per month to enable weekly backups of the entire droplet.
If you do care about these then maybe your toy project is not that much of a toy any more 😄.

In summary, all of the deployment stories above are here to say that so far I find `Dokku`_ really easy to work with.
There's no much traffic to any of these projects, so CPU / network / disk usage are low as expected.
Memory usage is constantly around %40-%50.
As long as it doesn't creep up dramatically that's probably fine.
So overall it seems that the transition succeeded.

Shameless plug
--------------

Here are the projects that are running on my `Dokku`_ instance at the time of writing this post. Source code for all of them can be found on `my GitHub profile`_.

`Cardigan`_
===========

A "platform" for playing card games online. Created during COVID to play `The Crew`_ with friend before it was available on `BGA`_. It was previously deployed to `Gigalixir`_.

`Proker`_
=========

A tool we use at work to vote on the complexity of tickets (bugs, feature enhancements, tech debt, etc.) It was previously deployed to `Digital Ocean's App Platform`_.

`Xteams!`_
==========

An app I made many years ago when I was playing volleyball with a group of 15-20 people who were too polite to make up teams. I know a few people were still using it until 3-4 years ago (including the coach of the Hebrew University of Jerusalem Women Volleyball Team). Have no idea if anyone still does. It was previously deployed to `Elastic Beanstalk`_, and before that to `Heroku`_ (I think).

`GrabACoffee`_
==============

A hackathon project made at work to encourage people to take coffee breaks together. It was previously on `Digital Ocean's App Platform`_.

`web-audio`_
============

An attempt to play with the WebAudio API that ended up more like an experiment in ajax / websockets. Made when I just started writing code and had no idea what I'm doing. Happy to see it online mainly for nostalgia. Previously deployed on `Heroku`_ but went down when they changed the pricing model because there was no point in paying for it.

.. _Dokku: https://dokku.com/
.. _part 1: {filename}/Blog/docker-compose-in-production.rst
.. _part 2: {filename}/Blog/docker-compose-in-production-part-2.rst
.. _Digital Ocean droplet: https://www.digitalocean.com/products/droplets
.. _nginx: https://nginx.org/en/
.. _Heroku: https://www.heroku.com/
.. _Digital Ocean's App Platform: https://docs.digitalocean.com/products/app-platform/
.. _Elastic Beanstalk: https://aws.amazon.com/elasticbeanstalk/
.. _AWS Lambdas: https://docs.aws.amazon.com/lambda/
.. _Digital Ocean: https://www.digitalocean.com/
.. _one click deployment of Dokku on Digital ocean through their marketplace: https://docs.digitalocean.com/products/marketplace/catalog/dokku/
.. _buildpacks: https://buildpacks.io/
.. _configuring SSL following the deployment tutorial: https://dokku.com/docs/deployment/application-deployment/#setting-up-ssl
.. _Elixir: https://elixir-lang.org/
.. _Phoenix: https://www.phoenixframework.org/
.. _my GitHub profile: https://github.com/nagasaki45/
.. _Gigalixir: https://www.gigalixir.com/
.. _Cardigan: https://cardigan.leverstone.me/
.. _The Crew: https://boardgamegeek.com/boardgame/284083/crew-quest-planet-nine
.. _BGA: https://boardgamearena.com/
.. _Proker: https://proker.leverstone.me/
.. _Xteams!: https://xteams.leverstone.me/
.. _GrabACoffee: https://grab-a-coffee.leverstone.me/
.. _web-audio: https://web-audio.leverstone.me/