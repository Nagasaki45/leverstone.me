---
title: "Frontend Gems #3: The clipboard"
date: 2025-06-06T21:00:00.000Z
---

The clipboard, yes, the clipboard! The thing you use to copy-paste. It's a surprisingly complex and capable technology, and I'm glad I found some time to explore it recently.

While the clipboard itself is a core operating system feature, browsers provide a powerful set of frontend APIs for interacting with it. This blog post will discuss the clipboard in general, and then dive into an exploration of these APIs.

First, some context. My team develops an AI chatbot. Until recently, the answers from this chatbot were mostly textual. As chatbots often do, we had a 'Copy' button under each answer so our users could quickly and easily copy it and paste it wherever they wanted—usually a presentation, a document, or an email. We recently added a feature that includes interactive charts in the answer. We quickly discovered an oversight: the 'Copy' button doesn't do anything meaningful with these charts.

So, how can the clipboard help us here? The interactive charts are SVGs, not images. What does it even mean to copy-paste these? 🤔

# Targets

I got a lot of help from LLMs to explore the problem and learned that the clipboard is not just a text buffer. After all, we can copy-paste images, text from the web with formatting preserved, and even cells or tables between spreadsheets. There must be something more capable than a simple text buffer to support these features.

The answer is clipboard **targets**. When an application copies something, it can store the information in one or more formats, called targets. Each target has a specific type. Some of these are generic, like `text/plain` or `text/html`, while others are application-specific. When pasting into an application, it can pick the best available target and pull the data from it.

I'm not sure if there's a definitive standard for generic targets, but the browser's `Clipboard` API exposes a function to check what's supported. You can find more info about this on the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardItem/supports_static).

# Debugging

Let's do a simple test. Copy some web content (maybe this blog post) that includes formatting like titles and links. Now go to your text editor and paste it. You'll likely get a plaintext dump of the selection. If you paste the same content into a Google Doc (a new email also works), you'll get it nicely formatted, similar to how it appeared online. That's because the browser copies the content into multiple targets, including `text/plain` and `text/html`. The text editor pulls from the `text/plain` target, while Google Docs pulls from `text/html` and knows how to format the content accordingly.

That's a pretty shitty way to debug the clipboard, you might say. And you are right! The best technique I found for debugging this sort of stuff on Linux is to use [`xclip`](https://github.com/astrand/xclip). Install it and run:

```bash
xclip -out -selection clipboard -target TARGETS
```

This will list the available targets of the `clipboard` selection (the one populated with Ctrl-C, as there are multiple selections in Linux). And then:

```bash
xclip -out -selection clipboard -target text/html
```

This will print the content of a specific target, `text/html` in this case, to the standard output.

As a Linux user, `xclip` works for me, but there should be similar tools for Windows and macOS.

# Back to the browser

Now that we understand the basics, let's fix our chatbot's 'Copy' button! I prompted an LLM to generate a simple HTML element for testing, with an SVG in it.

> Generate a test div (with id='clipboardTest') with lorem ipsum text and a simple svg below it. Just the div please, not a full html page

<div id="clipboardTest" style="padding: 20px; border: 1px solid #ccc; background-color: #f9f9f9; max-width: 600px; margin: 20px auto;">
  <h1>Clipboard Test Content</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>

  <svg width="100" height="100" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="40" stroke="#4CAF50" stroke-width="3" fill="#8BC34A" />
    <text x="50" y="55" font-family="Arial" font-size="20" fill="white" text-anchor="middle" alignment-baseline="middle">SVG</text>
  </svg>
</div>

This simulates the chatbot answer we want to copy. Now for the 'Copy' button.

> Create an html copy button. When clicked it copies the content of the element with id='clipboardTest' to the clipboard. Just the button and the JS script within &lt;script&gt; tags please, not a full html page

<!-- The button that triggers the copy action -->
<button id="copyButtonPlainText">Copy Content</button>

<script>
    // Ensure the DOM is fully loaded before trying to access elements
    document.addEventListener('DOMContentLoaded', () => {
        const copyButton = document.getElementById('copyButtonPlainText');
        const clipboardDiv = document.getElementById('clipboardTest');

        copyButton.addEventListener('click', async () => {
            // Get the plain text content of the div
            // Use .innerHTML if you want to copy the raw HTML including tags
            const textToCopy = clipboardDiv.textContent;

            // Use the modern Clipboard API to write text
            // This generally requires a secure context (HTTPS)
            await navigator.clipboard.writeText(textToCopy);
        });
    });
</script>

This copies our text, but *only* as plaintext. No formatting, and definitely not the SVG. When I run `xclip -out -selection clipboard -target TARGETS`, there's no `text/html` target. The `text/plain` target shows:

```

  Clipboard Test Content
  Lorem ipsum dolor sit amet, consectetur adipiscing elit...



    SVG

```

We need to store the HTML in the `text/html` target! That's a small manual tweak to the previous script.

<button id="copyButtonTextAndHtml">Copy Content - plaintext and HTML</button>

<script>
    // Ensure the DOM is fully loaded before trying to access elements
    document.addEventListener('DOMContentLoaded', () => {
        const copyButton = document.getElementById('copyButtonTextAndHtml');
        const clipboardDiv = document.getElementById('clipboardTest');

        copyButton.addEventListener('click', async () => {
            // Get the plain text content of the div
            const textToCopy = clipboardDiv.textContent;
            // Get the HTML content, including tags
            const htmlToCopy = clipboardDiv.innerHTML;

            // Create a ClipboardItem to hold multiple data types simultaneously
            const clipboardItem = new ClipboardItem({
                'text/plain': new Blob([textToCopy], { type: 'text/plain' }),
                'text/html': new Blob([htmlToCopy], { type: 'text/html' })
            });

            // Write the ClipboardItem to the clipboard
            // This generally requires a secure context (HTTPS)
            await navigator.clipboard.write([clipboardItem]);
        });
    });
</script>

Checking `xclip -out -selection clipboard -target text/html` shows an improvement:

```html
<meta http-equiv="content-type" content="text/html; charset=utf-8"><html><head></head><body><h1>Clipboard Test Content</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>

  <svg width="100" height="100" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="40" stroke="#4CAF50" stroke-width="3" fill="#8BC34A"></circle>
    <text x="50" y="55" font-family="Arial" font-size="20" fill="white" text-anchor="middle" alignment-baseline="middle">SVG</text>
  </svg>
</body></html>
```

When I paste this into a Google Doc, the title is formatted, but the SVG still doesn't show up 😥

![Screenshot from the Google Doc showing formatting but not the SVG]({static}/images/blog/clipboard_paste_html_no_svg.webp)

That's because most applications don't know how to render SVGs directly from the clipboard. They can, however, handle standard image formats like PNG. Can we convert our SVG into an image in the browser? We definitely can! The browser has some APIs that can help us with this. As usual, let's ask an LLM for help:

> The clipboardTest div contains SVGs. When storing the content into the text/html target we need to first convert these to PNGs, encoded as URLs, and replace the SVGs with these in a cloned element, before returning the cloned element inner HTML. Only the script please, not full html page nor explanations

<!-- The new button that triggers the copy action for both text/plain and text/html with SVG as PNG -->
<button id="copyButtonTextAndHtmlWithImages">Copy Content - plaintext and HTML w/ images</button>

<script>
    // Converts a given SVG element to a PNG data URL.
    const svgToPngDataURL = async (svgElement) =>
        new Promise((resolve, reject) => {
            const serializer = new XMLSerializer();
            const svgString = serializer.serializeToString(svgElement);
            const svgDataUrl = `data:image/svg+xml;base64,${btoa(
                new TextEncoder()
                    .encode(svgString)
                    .reduce((data, byte) => data + String.fromCharCode(byte), ""),
            )}`;

            const img = new Image();
            img.onload = () => {
                const canvas = document.createElement("canvas");
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0);
                resolve(canvas.toDataURL("image/png", 1));
            };
            img.src = svgDataUrl;
        });

    document.addEventListener('DOMContentLoaded', () => {
        const copyButton = document.getElementById('copyButtonTextAndHtmlWithImages');
        const clipboardDiv = document.getElementById('clipboardTest');

        copyButton.addEventListener('click', async () => {
            // Get the plain text content
            const textToCopy = clipboardDiv.textContent;

            // Create a clone of the div to modify it without affecting the original
            const clonedDiv = clipboardDiv.cloneNode(true);

            // Find all SVGs within the cloned element
            const svgs = clonedDiv.querySelectorAll('svg');

            // Create an array of promises for each SVG conversion
            const conversionPromises = Array.from(svgs).map(async (svg) => {
                const pngDataUrl = await svgToPngDataURL(svg);

                // Create a new <img> element with the PNG data
                const img = document.createElement('img');
                img.src = pngDataUrl;

                // Preserve original dimensions
                img.width = svg.attributes.width.value;
                img.height = svg.attributes.height.value;

                // Replace the SVG with the new IMG in the cloned DOM
                svg.parentNode.replaceChild(img, svg);
            });

            // Wait for all SVG-to-PNG conversions to complete
            await Promise.all(conversionPromises);

            // Get the final HTML from the modified clone
            const htmlToCopy = clonedDiv.innerHTML;

            // Create a ClipboardItem with both text and HTML formats
            const clipboardItem = new ClipboardItem({
                'text/plain': new Blob([textToCopy], { type: 'text/plain' }),
                'text/html': new Blob([htmlToCopy], { type: 'text/html' })
            });

            // Write the ClipboardItem to the clipboard
            // This generally requires a secure context (HTTPS)
            await navigator.clipboard.write([clipboardItem]);
        });
    });
</script>

Now, try the 'Copy' button and paste into a Google Doc. Hopefully, you'll see a nicely rendered image of our SVG! Let's double-check with `xclip -out -selection clipboard -target text/html`:

```html
<meta http-equiv="content-type" content="text/html; charset=utf-8"><html><head></head><body><h1>Clipboard Test Content</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>

  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAY..." width="100" height="100">
</body></html>
```

Looks good! 🙌

We've discussed the clipboard, but a lot of heavy lifting is done by the `svgToPngDataURL` function. It's basically a mini in-browser image converter, orchestrating multiple browser APIs. Here's how it works:

1.  **Serialize SVG**: First, it takes the live SVG element from the page and turns it into a text string, like `<svg>...</svg>`.
2.  **Create an SVG Data URL**: It then base64-encodes this string and embeds it in a `data:` URL. This is a special URL format that contains the resource's data directly. Now we have our SVG represented as a URL the browser can load.
3.  **Load into an Image**: Next, it creates a new, temporary `<img>` element in memory and sets its `src` to our new SVG data URL. The browser loads the SVG into this image element, off-screen.
4.  **Draw on a Canvas**: Once the image has loaded, we draw it onto an invisible `<canvas>` element. The canvas is like a pixel-based drawing board in the browser.
5.  **Export as PNG**: Finally, we ask the canvas to export its contents as a PNG, again using a `data:` URL. This final data URL, containing the PNG image data, is what the function returns.

The function's pipeline looks like this: `<svg>` → `SVG string` → `SVG data URL` → `<img>` → `<canvas>` → `PNG data URL`. And just like that, we have a universally-compatible image ready for the clipboard. Nice!

*A side note about the code: while it looks like I'm vibe-coding my way through this problem, I'm definitely not! I'm sparing you the details of a lot of manual code editing and a few minor iterations with the AI to get things right.*

# Stretch goal: presentation slides

The revamped 'Copy' button was a success. Stakeholders and clients couldn't stop copy-pasting chatbot answers with charts into their documents and, especially, into their presentations. This sparked a new idea: what if we could copy an entire conversation into a ready-to-use presentation deck? For example, we wanted to make each user query a new section header, each paragraph in the AI response a separate slide, and give charts their own slides. That's a lot to ask of the clipboard, but it would be a beautiful user interface if we could pull it off.

Sadly, we couldn't. 😔

We failed fast after discovering that presentation apps use custom, proprietary clipboard targets. If I create a presentation in LibreOffice Impress (Linux user here, sorry) and copy a slide, I get multiple targets from `xclip` that start with `application/x-libreoffice-...`. The browser isn't allowed to write to these targets; trying to do so raises an error.

So, my takeaway is that if your use case requires writing to a custom, application-specific target, you probably can't do it from a web browser. I might be wrong, but this is as far as I got in my exploration.

# Conclusion

I hope I've convinced you that the clipboard is more interesting than it initially seems. I think knowing the basics of how it works can enable surprisingly simple and elegant solutions in frontend development. In this case, for example, the team had considered developing a download endpoint just so users could get the charts and paste them into their documents. Using the clipboard is much nicer 🙂

---

Written with the help of Gemini 2.5 Pro.
