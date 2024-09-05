Remote TidalCycles jamming setup
################################
:date: 2020-09-18 00:00
:author: Tom Gurion
:tags: tutorials, live coding,network,hack
:slug: remote-tidal-cycles-jamming-setup
:description: Getting ready for the 2nd wave and setting up TidalCycles for remote jamming w/ digital selves.

.. image:: https://upload.wikimedia.org/wikipedia/commons/8/80/TidalCycles_identity.svg
  :alt: TidalCycles logo
  :width: 100%

`TidalCycles <https://tidalcycles.org/i>`_ (tidal in short) is a live coding language for music performance / composition.
I don't use it myself but been playing with a live coder, Lizzie, AKA `digital selves <https://lwlsn.github.io/digitalselves-web/>`_, for the last year and a half.
Check her out!
With a COVID 2nd wave around the corner we decided to search for a solution for remote jamming together.
This blog post is a summary of what seems to work.
It's written mainly as a documentation for Lizzie and self.
Hopefully others will find it useful as well.

So, what do we want to achieve?
We want Lizzie to run tidal code on her laptop and having the audio generated on my laptop at the other side of town.
The clock to sync my hardware synth will be generated with the audio.
So, audio-wise, both Lizzie's output and my hardware synth will generate locally on my side, fully in sync.
Then, the mix of Lizzie's live coding and my hardware synth will be streamed back to Lizzie, so she could hear it too.

How do we plan to do it?
Tidal uses a client / server architecture with the tidal haskell library as the client and SuperCollider (SC) running the audio as the server.
Communication is done over UDP on port 57120 by default.
Our idea is to route the messages from tidal, through a server, to my machine, which runs the SC server.
With such a solution there won't be any need to change anything around tidal, nor around SC, just set up the network properly.
I will listen to the mix locally on my side and send it to Lizzie over zoom / skype / whatever.

With the overall picture in mind, let's dive in.

Prerequisits
============

- You'll need a server with admin previliges.
- Both ends (the computer running tidal and the computer running SC) should have `socat <https://linux.die.net/man/1/socat>`_ installed.

Here's the overall process:

- `Prepare the server`_
- `Create an SSH reverse tunnel from the server to the laptop running SC`_
- `Convert TCP messages back to UDP on the laptop running SC`_
- `Send the UDP messages from the laptop running tidal to the server`_
- `Start tidal`_
- `Stream the audio back to the tidal user`_

Prepare the server
==================

For a server we created a droplet on `digital ocean <https://digitalocean.com/>`_.
There's almost no setup for the droplet, so we can create one for jamming and delete it later to keep the cost low.

The only configuration needed on the server is to change the SSH settings on the server to allow forwarded ports to bind to the wildcard address (meaning that the address will be publicly accessible) [#]_.

Edit ``/etc/ssh/sshd_config`` and add:

.. code::

  GatewayPorts yes

Now reload the SSH settings on the server with

.. code::

  systemctl reload ssh.service

Note the IP of your server and use it everywhere that ``SERVER_IP`` is mentioned below.

Create an SSH reverse tunnel from the server to the laptop running SC
=====================================================================

SSH tunnelling doesn't support UDP, so we'll create a tunnel for TCP and convert the UDP messages sent by tidal to TCP on one machine, and back to UDP on the other machine.

On the machine that runs SC run

.. code::

  ssh -R 12345:localhost:12345 root@SERVER_IP

The port doesn't really matter, 12345 is used here for convenience.

Convert TCP messages back to UDP on the laptop running SC
=========================================================

.. code::

  socat TCP-LISTEN:12345,fork UDP4:localhost:57120

Send the UDP messages from the laptop running tidal to the server
=================================================================

.. code::

  socat UDP-LISTEN:57120,fork TCP4:SERVER_IP:12345

Start tidal
===========

Spin up tidal on one side, SC on the other side, put some patterns in and it should work, almost!
The user on the SC side will probably notice that the timing is not super stable and there are warnings about that in the SC log.
This is a result of the network latency.
To fix that, increase tidal's latency.
If you're using atom go to preferences > open config folder. This brings up the tidal source code. In ``tidalcycles/lib/boot.tidal``, change the ``oLatency`` value to 0.4 or so in this line of code:

.. code-block:: haskell

  tidal <- startTidal (superdirtTarget {oLatency = 0.4, oAddress = "127.0.0.1", oPort = 57120}) (defaultConfig {cFrameTimespan = 1/20})

A value of 0.4 worked for us.
If it's still too low try to increase the value until there's no more jitter and warnings in the log.

Stream the audio back to the tidal user
=======================================

So now the live coder's music is coming from the laptop running SC.
In our case, one audio channel from SC is an analog clock to sync the hardware sync.
The other channels from SC, and the hardware synth, are connected to a mixer and the entire mix can now be heard on the SC end of the system.
But the live coder cannot hear anything yet.
We used a 2nd computer that takes mixer's output and streams it back to the live coder over zoom.

The entire system looks something like this.
The area in blue is for the laptop running tidal and the area in pink is the SC + hardware synth end of the system.

.. image:: /images/blog/tidal_remote_diagram.avif
  :alt: TidalCycles logo
  :width: 100%

Advice on testing things locally
================================

If you want to test things on a single computer make sure to change the port SC is listening to.
Otherwise you are trying to use the same port twice: once listening to tidal and sending the messages to the server, and again listening to the messages coming from the server.
To do so, start the SuperDirt synth in SC as follows:

.. code::

  SuperDirt.start(port: 57121)

You'll also have to change the port that the TCP stream is converted to, so replace


.. code::

  socat TCP-LISTEN:12345,fork UDP4:localhost:57120

with

.. code::

  socat TCP-LISTEN:12345,fork UDP4:localhost:57121

**Enjoy jamming and keep safe!**

Footnotes
=========

.. [#] Setting the server this way is not 100% secure. We didn't mind it too much as this is a throwaway server with IP that no one except for us will ever know. If you are worried about security consider creating a forward tunnel from the laptop running tidal to the server instead of exposing the port to the public.