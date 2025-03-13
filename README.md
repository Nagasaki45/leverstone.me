# My personal site and portfolio

Static, [pelican](https://docs.getpelican.com/en/stable/) generated, site.

```bash
uv sync             # only once
uv run pelican -rl  # Regenerate and listen on localhost:8000
uv run python -m pagefind --site output # Create the search index
```

## Newsletter

A mailing list is managed on [audienceful](https://www.audienceful.com/). People subscribe using a form submission on the site. Very convenient!
