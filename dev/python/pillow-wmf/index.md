# pillow-wmf

A Windows Metafile reader/writer/renderer for Pillow.

Like in the old Windows days, a GDI backend draws graphics and can also record
actions to a Windows Metafile. Rasterizing one of these WMFs is just a matter
of playing it back, which produces a Pillow Image.

Here's how you load one:

```python
from PIL import Image
import pillow_wmf  # registers the WMF loader ahead of Pillow's built-in stub

with Image.open("drawing.wmf") as image:
    image.load(size=(640, 480))
    image.save("drawing.png")
```

## License

pillow-wmf is WTFPL with one additional clause:

1. Don't blame me.

Fonts have their own licenses, rip them out if you don't want to comply:

* [Wingdings fallback (OFL-1.1)](src/pillow_wmf/fonts/OFL.txt)
* [Wine Symbol (LGPL-2.1-or-later)](src/pillow_wmf/fonts/symbol/COPYING.LIB)

