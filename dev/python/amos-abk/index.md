# amos-abk

A Python library for loading AMOS `.abk` bank files from the Amiga.

Parses the container format and three image bank types:

* **Sprites** — hardware sprite images with hotspot and transparency
* **Icons** — software bob images (same format as sprites)
* **Pac.Pic.** — packed full-screen pictures with three-stream RLE compression

Non-image banks (Music, Samples, Amal, Datas) are loaded as raw `DataBank`
objects.

## Links

* [🏠 home](https://bitplane.net/dev/python/amos-abk)
* [📚 pydoc](https://bitplane.net/dev/python/amos-abk/pydoc)
* [🐍 pypi](https://pypi.org/project/amos-abk)
* [🐱 github](https://github.com/bitplane/amos-abk)

## Install

```
pip install amos-abk
```

## Library usage

```python
from amos_abk import load, parse_sprites, parse_packed_picture

# Load a bank file
abk = load("sprites.abk")
print(abk)  # AbkFile([Sprites])

# Parse sprites and convert to PIL Images
sprites = parse_sprites(abk.banks[0].data)
for i, sprite in enumerate(sprites):
    sprite.to_image().save(f"sprite_{i}.png")

# Parse a packed picture
abk = load("picture.abk")
pic = parse_packed_picture(abk.banks[0].data)
pic.to_image().save("picture.png")

# Access raw data
print(pic.width, pic.height, pic.num_planes)
print(pic.palette[:4])  # first 4 RGB tuples
```

## Pillow plugin

`import amos_abk` registers a Pillow plugin, so you can open `.abk` files
directly:

```python
from PIL import Image
import amos_abk

img = Image.open("sprites.abk")
img.save("first_sprite.png")

# Multi-frame: seek through all images in the file
for i in range(img.n_frames):
    img.seek(i)
    img.save(f"frame_{i}.png")

# The parsed AbkFile is available in metadata
abk = img.info["abk"]
print(abk.banks[0].name)
```

## Extract all images

The `images()` function extracts every image from every bank in a file:

```python
import amos_abk

# From a file path
imgs = amos_abk.images("sprites.abk")
for i, img in enumerate(imgs):
    img.save(f"image_{i}.png")

# Or from an already-loaded AbkFile
abk = amos_abk.load("sprites.abk")
imgs = amos_abk.images(abk)
```

## Format overview

AMOS was a game-creation environment for the Amiga, released in 1990. It stored
graphics and other resources in `.abk` memory bank files.

### Bank container

Each `.abk` file contains one or more banks, either bare (AmSp/AmIc magic) or
wrapped in an AmBk header with a bank number, name, and memory type.

### Sprite and icon banks

Sprites and icons share the same format: a count, per-image headers (dimensions,
bitplane count, hotspot), interleaved planar bitmap data, and a shared 32-entry
12-bit Amiga palette.

### Pac.Pic. banks

Packed pictures are compressed full-screen Amiga images. They have two layers:

1. **Screen header** (magic `0x12031990`) — dimensions, display window, flags,
   and palette
2. **Packed bitmap** (magic `0x06071963`) — three-stream RLE compression where
   POINTS controls RLEDATA, and RLEDATA controls PICDATA

## License

WTFPL: do as you like, but don't blame me if it banks your sprites.
