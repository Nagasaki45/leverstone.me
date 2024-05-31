---
title: 'Docker, compose, secrets, and environment variables'
date: 2024-05-30T23:00:00.000Z
---

A dockerised app I'm working on needs some secrets at build time. In my case, it needs to `pip install` from a private repository. Note that this is a generic problem, luckily with quite an elegant generic solution.

# How NOT to pass secrets to docker

In the past, we solved this by passing a build argument with the secret.

`# docker-compose.yml`

```yaml
services:
  my-app:
    build:
      args:
        CONTAINER_SECRET: "${HOST_SECRET}"
```

This is going to pass the `HOST_SECRET` environment variable from the host machine, to the container as an `ARG`.

`# Dockerfile`

```Dockerfile
ARG CONTAINER_SECRET
```

**Note** that I'm calling these `CONTAINER_SECRET` and `HOST_SECRET` to make things easier to follow, but these will often have the same name. Up to you really.

There are two significant drawbacks to this approach:

1. If the secret is a token that refreshes from time to time, it will mess up the docker build caching. In other words, when your token changes, every step after `ARG CONTAINER_SECRET` will have to be rerun during the build.
2. The secret can be extracted from the image, which is a security concern.

# How to pass secrets to docker

Luckily, [docker supports build secrets](https://docs.docker.com/build/building/secrets/). But until recently it was hard to fully utilize them because they were not supported by docker compose, which I almost always use for local development.

So, what are we trying to achieve?

* Call a command that requires a secret, stored in `HOST_SECRET` on the host, during the docker image build.
* Use docker compose in local development to build the app.

<!-- * Some local development tasks (e.g. running unit tests) build with docker, not with docker compose, because they don't need any of the services, networking, and environment variables that docker compose manages. -->

<!-- * Another build of the docker image happens in CI/CD, without docker compose this time. -->

Let's start from the `Dockerfile`. It needs to call `pip install my-private-package` with our secret in the environment variable `CONTAINER_SECRET`

`# Dockerfile`

```dockerfile
RUN --mount=type=secret,id=my_secret \
    CONTAINER_SECRET=$(cat /run/secrets/my_secret) \
    pip install my-private-package
```

The `Dockerfile` mounts the value of the secret called `my_secret` on `/run/secrets/my_secret`, which we load into an environment variable before calling the command. For security, the secret will only be accessbile during this `RUN` command. See [the docs](https://docs.docker.com/build/building/secrets/) for more info about using secrets in docker builds.

Now let's have a look at the `docker-compose.yml`

`# docker-compose.yml`

```yaml
services:
  my-app:
    build:
      ...
      secrets:
      - my_secret

secrets:
  my_secret:
    environment: "HOST_SECRET"
```

The `docker-compose.yml` defines a global secret that is loaded from the environment variable `HOST_SECRET` on the host. There are other source to load a secret from (e.g. from a file). Again, consult [the docs](https://docs.docker.com/compose/use-secrets/). Then the service that needs the secret can

As mentioned before, some local development tasks run on an image built by docker without docker compose. Here's how this build works

```
docker build --secret id=my_secret,env=HOST_SECRET --tag my-app:test .
```

Lastly, we often find that we need to run `command_that_requires_secrets` from within the container in development not during build. For a concrete example substitute `command_that_requires_secrets` with a `pip install` that uses a private repository. In this case we need `CONTAINER_SECRET` in the container at runtime. A simple solution is to pass an environment variable to the container:

`# docker-compose.yml`

```yaml
services:
  my-app:
    ...
    environment:
      CONTAINER_SECRET: ${ HOST_SECRET }
```

While it's possible to use secrets at runtime there's no need to do so. Think about the two issues secrets tried to solve: security and build time. The environment variable is not stored in the image so there's no security issue here. And the build is long done so there are no effect on that front either.
