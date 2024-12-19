---
features: ["mermaid"]
---

# 🎃 New features

So I can now render mermaid inline, using JavaScript if it's supported and just
show the code if it isn't.

## Big deal

Yeah, anyone can just add the mermaid.js to their pages, right?

No. That adds 100k to every page. I'm already pretty disgusted with myself for
the 1.5kb of boilerplate in the template, and including 16kb of CSS to a site
where every page is actually 20 times smaller than that.

So on average, my site has 20x as much bloat as it does content. Adding 100kb of
JavaScript to each page would make that 10x worse. That would be 10x better than
most sites, but 800x worse than something I could be proud of.

So I went with this approach for now:

```mermaid
flowchart TD
    A[_layouts/default.html] --> B{page.features?}
    B -- no --> E[render page]
    B -- yes --> C[for each feature]

    C -- next --> D[include feature.html]
    D --> C
    C -- end --> E
```

## How?

The trick comes from [`_layouts/default.html`](https://github.com/bitplane/bitplane.net/blob/main/_layouts/default.html)
letting me add features:

{% raw %}

```liquid
{% if page.features %}{% for feature in page.features %}
    {% include {{ feature | append: ".html" }} %}    
{% endfor %}{% endif %}
```

{% endraw %}

...the front-matter in [this file](https://github.com/bitplane/bitplane.net/blob/main/log/2024/10/a-matter-of-features/index.md)
having the "mermaid" feature:

```markdown
---
features: ["mermaid"]
---
```

...and the [mermaid feature](https://github.com/bitplane/bitplane.net/blob/main/_includes/mermaid.html)
including the JavaScript that replaces the code blocks for the div class Mermaid
expects, and initializing the thing:

```html
<script src="/assets/js/mermaid.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const mermaidBlocks = document.querySelectorAll('.language-mermaid');
    mermaidBlocks.forEach(block => {
      const div = document.createElement('div');
      div.className = 'mermaid';
      div.innerHTML = block.textContent;
      block.replaceWith(div);
    });
    mermaid.initialize({ startOnLoad: true, theme: 'dark' });
  });
</script>
```

So, I can finally publish articles with graphs in them.

Expect the first one soonish.
