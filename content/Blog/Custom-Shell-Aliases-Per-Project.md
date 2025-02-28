---
title: Custom shell aliases per project
date: 2025-02-28T23:00:00.000Z
---

I've been playing with [aider](https://aider.chat/) recently. I's an "AI pair programming in your terminal". Think GitHub Copilot, Cursor, etc. but for the command line. This blog post is not about that. It's about making it easier to run aider in my projects.

Confused? Let's see...

In one of my projects I run aider like this

```bash
aider --architect --test-cmd 'uv run python -m pytest' --lint-cmd 'make format'
```

In another I run it like this

```bash
aider --architect --model o3-mini --editor-model sonnet --test-cmd 'docker run --rm -v .:/ app my-app pytest' --lint-cmd 'make docker/format'
```

The point is, this is a long command line to type every time.

**Wouldn't it be nice if I had custom aliases, per project, so I can just run `aider` within the repo and it will run the full command for me? 🤔**

I googled and asked some LLMs but couldn't find a simple existing solution. Having something custom sounded easy, so I tried to get something done with the help of ChatGPT, and it worked surprisingly well!

# `trusted-source`

This custom [oh-my-zsh](https://ohmyz.sh/) plugin looks for `.trusted-source` files in the current directory, ask the user to confirm they are trusted, and if so, sources them.

```bash
# Function to source trusted `.trusted-source` files in the current directory.
function load_trusted_source() {
  local file_to_source="$PWD/.trusted-source"
  local trust_file="$HOME/.trusted-sources"  # File to store trusted hashes.
  local file_hash

  if [ -f "$file_to_source" ]; then
    # Compute a checksum
    file_hash=$(shasum "$file_to_source" | awk '{print $1}')

    # Retrieve the last trusted hash for this directory.
    local saved_hash
    saved_hash=$(grep "^$PWD " "$trust_file" 2>/dev/null | tail -n 1 | awk '{print $2}')

    if [[ "$saved_hash" != "$file_hash" ]]; then
      echo "New or changed .trusted-source file detected in $PWD."
      read -q "REPLY?Do you trust and want to source it? [y/N] "
      echo
      if [[ "$REPLY" =~ ^[Yy]$ ]]; then
        # Append the new trusted hash to the trust file.
        echo "$PWD $file_hash" >> "$trust_file"
        source "$file_to_source"
      fi
    else
      # The file is trusted; load it silently.
      source "$file_to_source"
    fi
  fi
}

# Hook the function into zsh's directory-change mechanism.
chpwd_functions+=(load_trusted_source)

# Optionally, run it once on shell startup.
load_trusted_source
```

To use it, copy it to `~/.oh-my-zsh/custom/plugins/trusted-source/trusted-source.plugin.zsh`. And add `trusted-source` to the list of plugins in your `~/.zshrc`.

With this set up I have this `.trusted-source` in the root of my project:

```bash
alias aider=aider --architect --test-cmd 'uv run python -m pytest' --lint-cmd 'make format'
```

and to run aider I can just run `aider` 🙌

This is just one use case of course. I can use this for env vars (replacing [direnv](https://github.com/direnv/direnv)), source my Python virtual environment (something I rarely do now that I mostly use uv / poetry), etc. This plugin is for zsh and oh-my-zsh, but the idea should be very much transferable to other shells. I'm documenting it here for my future self, but maybe someone will also find it interesting.

And what about aider, you ask? I'm still struggling with all of this AI for writing code idea. For writing prose? Definitely! For exploring technical ideas? Of course! For translating what's in my head to an easy to read and maintainable python code? I'm not yet there, but I'm trying. We will see how it goes...