# pillow-degas

A [Pillow](https://pillow.readthedocs.io/) plugin for reading Atari ST
DEGAS and DEGAS Elite image files.

## Supported formats

| Extension | Resolution | Colours | Compressed |
|-----------|------------|---------|------------|
| .PI1      | 320x200    | 16      | No         |
| .PI2      | 640x200    | 4       | No         |
| .PI3      | 640x400    | 2       | No         |
| .PC1      | 320x200    | 16      | Yes        |
| .PC2      | 640x200    | 4       | Yes        |
| .PC3      | 640x400    | 2       | Yes        |

## Installation

```bash
pip install pillow-degas
```

## Usage

```python
import pillow_degas
from PIL import Image

img = Image.open("artwork.pi1")
img.save("artwork.png")
```

Importing `pillow_degas` registers the DEGAS format with Pillow. After
that, `Image.open()` handles all six file types automatically.
