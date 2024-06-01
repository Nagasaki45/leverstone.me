---
title: 'Docker, compose, secrets, and environment variables'
date: 2024-05-30T23:00:00.000Z
---

A dockerised app I'm working on needs some secrets at build time. In my case, it needs to `pip install` from a private repository. Note that this is a generic problem, luckily with quite an elegant generic solution.

## How NOT to pass secrets to docker

In the past, we solved this by passing a build argument with the secret.

```yaml
# docker-compose.yml
services:
  my-app:
    build:
      args:
        CONTAINER_SECRET: "${HOST_SECRET}"
```

This is going to pass the `HOST_SECRET` environment variable from the host machine, to the container as an `ARG`.

```Dockerfile
# Dockerfile
ARG CONTAINER_SECRET
```

**Note** that I'm calling these `CONTAINER_SECRET` and `HOST_SECRET` to make things easier to follow, but these will often have the same name. Up to you really.

There are two significant drawbacks to this approach:

1. If the secret is a token that refreshes from time to time, it will mess up the docker build caching. In other words, when your token changes, every step after `ARG CONTAINER_SECRET` will have to be rerun during the build.
2. The secret can be extracted from the image, which is a security concern.

## How to pass secrets to docker

Luckily, [docker supports build secrets](https://docs.docker.com/build/building/secrets/). But until recently it was hard to fully utilize them because they were not supported by docker compose, which I almost always use for local development.

So, what are we trying to achieve?

* Call a command that requires a secret, stored in `HOST_SECRET` on the host, during the docker image build.
* Use docker compose in local development to build the app.

Let's start from the `Dockerfile`. It needs to call `pip install my-private-package` with our secret in the environment variable `CONTAINER_SECRET`

```dockerfile
# Dockerfile
RUN --mount=type=secret,id=my_secret \
    CONTAINER_SECRET=$(cat /run/secrets/my_secret) \
    pip install my-private-package
```

The `Dockerfile` mounts the value of the secret called `my_secret` on `/run/secrets/my_secret`, which we load into an environment variable before calling the command. For security, the secret will only be accessbile during this `RUN` command. See [the docs](https://docs.docker.com/build/building/secrets/) for more info about using secrets in docker builds.

Now let's have a look at the `docker-compose.yml`

```yaml
# docker-compose.yml
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

The `docker-compose.yml` defines a global secret that is loaded from the environment variable `HOST_SECRET` on the host. There are other options for defining secrets (e.g. from a file). Again, consult [the docs](https://docs.docker.com/compose/use-secrets/). Then, the service that needs the secret can ask for it by name.

# Nice to haves

## Build with docker

While I mostly use docker compose for local development, sometimes it's useful to just build with docker, even for the same project! A good example is unit-tests. It's simple to build and run unit tests in the container without docker compose because there's no need for the surrounding services, environment variables, networking configuration, volumes, etc.

Here's how this is done

```
docker build --secret id=my_secret,env=HOST_SECRET --tag my-app:test .
```

## Passing secrets to running containers

Lastly, it's often useful to run commands that require secrets from within the container in development, not during the build. For example, when modifying dependencies (something like `pip install --upgrade my-private-package && pip freeze > requirements.txt`). In this case we need `CONTAINER_SECRET` in the container at runtime. A simple solution is to pass an environment variable to the container:

```yaml
# docker-compose.yml
services:
  my-app:
    ...
    environment:
      CONTAINER_SECRET: ${ HOST_SECRET }
```

While it's possible to use secrets at runtime there's no need to do so. Think about the two issues secrets solve: security and build time. The environment variable is not stored in the image so there's no security issue here. And the build is long done so there are no effect on that front either.
