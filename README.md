# My personal site and portfolio

Static, [pelican](https://docs.getpelican.com/en/stable/) generated, site.

```bash
poetry install          # only once
poetry run pelican -rl  # Regenerate and listen on localhost:8000
```

To run with TinaCMS locally run

```bash
yarn tinacms dev -c "poetry run pelican -rl"
```

Now you can visit the CMS on http://localhost:8000/admin
