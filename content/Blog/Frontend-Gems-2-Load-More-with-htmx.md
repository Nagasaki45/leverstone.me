---
title: "Frontend Gems #2: 'Load More' with htmx"
date: 2025-04-21T19:00:00.00Z
---

Until recently, this blog displayed 10 entries at a time, using **OLDER** and **NEWER** buttons for pagination:

<video
    controls
    src="{static}/images/blog/pagination_traditional.webm"
/>

There's nothing fancy here. The **OLDER** button is an anchor element linking to the next blog index page (`index2.html`, `index3.html` etc.). You can see how the URL changes in the video. The **NEWER** button works in a similar way. [Here's the code](https://github.com/Nagasaki45/leverstone.me/blob/b399d620c862194e224834ea8545abe8b1811cfd/theme/templates/partials/pagination.html).

Wouldn't it be nice if there was just a **Load More** button that loads the next page in place, without a full page load? 🤔

This website is a static site, with very minimal JavaScript. In an effort to keep things simple, I looked into [htmx](https://htmx.org/). The solution is now live on the blog. Here's how it looks:

<video
    controls
    src="{static}/images/blog/pagination_load_more.webm"
/>

Now, dear reader, how complex do you think the solution is? How many lines of code were added, and removed, to support this? Intuitively I thought it would take a lot of fiddling, but to my surprise it was super easy! Here's the crux of it:

```html
{% if articles_page.has_next() %}
<button
  class="btn btn-primary load-more"
  hx-get="{{ page_name }}/index{{ articles_page.next_page_number() }}.html"
  hx-select=".item, .load-more"
  hx-swap="outerHTML"
>
  Load more
</button>
{% endif %}
```

So, what do we have here? If there are more articles to load, we render a **Load More** button with some htmx attributes:

-   `hx-get`: Specifies the URL to GET when the button is clicked. This is the same URL the previous **OLDER** button used.
-   `hx-select`: Selects the blog entries (`.item`) and the next **Load More** button (if any) from the HTML response received from the `hx-get` request.
-   `hx-swap="outerHTML"`: Instructs htmx to replace the *current* button (the one that was clicked) entirely with the content selected by `hx-select`.

[Here's the change](https://github.com/Nagasaki45/leverstone.me/commit/4df289df2322cc7ba66844768f3917eb1998013f). Yes! That's all of it. And the stats? 3 files changed: the new button implementation replaced the old pagination buttons, minor CSS changes, and adding the htmx library; +14 -19 lines changed. Yes, more lines were removed than added. This is a win in my book 🙌

I stopped here, but it should be equally simple to implement infinite scroll. Just change the trigger from clicking a button to triggering the load when a specific element (like one near the bottom) enters the viewport. Note, however, it's not needed for my site as I want the footer reachable.

This was my first attempt to use htmx and it was much smoother than expected! When reading about htmx I always thought of it as a complement to a backend service. Here I have a statically generated site, but it provided a super simple solution for my use case. What's more, any existing links online pointing to the old `indexX.html` pages will still work perfectly; they'll simply load the specific page, which now includes the **Load More** button at the bottom. Not breaking existing links is a massive bonus!

In line with my [previous blog post in this series]({filename}/Blog/Frontend-Gems-1-Pagefind.md) I think there's much to gain from using simple technologies like static sites, htmx, and the like. Not everything needs to be a full-blown Single Page App using a JS framework (React, I'm looking at you). Give simplicity a shot!