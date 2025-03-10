---
title: Script for Checking TLS Certificate Expiry Dates
date: 2025-03-10T23:00:00.000Z
---

I have multiple projects on subdomains of leverstone.me. What's the expiration date of the TLS certificates on these subdomains? I have no idea 🤷

Wouldn't it be nice if there was a CLI tool that, given a domain, lists the expiry dates of its subdomains? I couldn't find one so asked perplexity and Claude 3.7 Sonnet to help me write it.

```bash
#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $(basename "$0") <domain>"
    exit 1
fi

DOMAIN=$1

# Combine main domain with subdomains from subfinder and process each
(echo "$DOMAIN"; subfinder -d "$DOMAIN" -silent) | while read -r subdomain; do
    # Get expiry date from certificate
    expiry_date=$(echo | openssl s_client -servername "$subdomain" -connect "$subdomain":443 2>/dev/null | openssl x509 -enddate -noout 2>/dev/null | sed 's/notAfter=//')

    if [ -n "$expiry_date" ]; then
        # Convert to ISO 8601
        iso_date=$(date -d "$expiry_date" '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null)

        if [ $? -eq 0 ]; then
            echo "$subdomain: $iso_date"
        else
            echo "$subdomain: $expiry_date"
        fi
    else
        echo "$subdomain: No SSL certificate found"
    fi
done
```

Drop this in, for example, `~/.local/bin/certcheck` (assuming `~/.local/bin` is in your path already), `chmod +x ~/.local/bin/certcheck`, and you are ready to go!

```
➜ certcheck leverstone.me
leverstone.me: 2025-05-09T06:01:06Z
proker.leverstone.me: 2025-06-06T23:19:25Z
xteams.leverstone.me: 2025-06-06T23:18:28Z
web-audio.leverstone.me: 2025-06-06T23:16:14Z
grab-a-coffee.leverstone.me: 2025-06-06T23:21:17Z
cardigan.leverstone.me: 2025-06-06T23:20:16Z
miniflux.leverstone.me: 2025-05-22T00:02:03Z
```

Looks good!

# Notes

- [`subfinder`](https://github.com/projectdiscovery/subfinder) is an open source 'Fast passive subdomain enumeration tool' for penetration testers and bug bounty hunters. You'll have to install it. On arch linux `yay -S subfinder` was enough. Perplexity suggested it when I asked for ways to find subdomain of a domain from the command line.
- [OpenSSL](https://github.com/openssl/openssl) is used to fetch the certificate and extract the expiry time. The command `echo | openssl s_client -servername "$subdomain" -connect "$subdomain":443 2>/dev/null | openssl x509 -enddate -noout` was suggested by Claude 3.7 Sonnet when asked for ways to get the expiry time of a certificate of a domain.
- The rest of the script was created by iterating on some basic prompts with Claude.
