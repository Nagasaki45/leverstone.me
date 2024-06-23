# My personal site and portfolio

Static, [pelican](https://docs.getpelican.com/en/stable/) generated, site.

```bash
poetry install          # only once
poetry run pelican -rl  # Regenerate and listen on localhost:8000
```

## CMS

To run with TinaCMS locally run

```bash
yarn tinacms dev -c "poetry run pelican -rl"
```

Now you can visit the CMS on http://localhost:8000/admin

## Newsletter

A mailing list is managed on [audienceful](https://www.audienceful.com/). People subscribe using a form submission on the site. Very convenient!
