<a id="amigainfo"></a>

# amigainfo

<a id="amigainfo.enums"></a>

# amigainfo.enums

<a id="amigainfo.enums.IconType"></a>

## IconType Objects

```python
class IconType(IntEnum)
```

do_Type values from the DiskObject structure.

<a id="amigainfo.enums.GadgetFlag"></a>

## GadgetFlag Objects

```python
class GadgetFlag(IntFlag)
```

Gadget flag bits (ga_Flags).

<a id="amigainfo.enums.GadgetActivation"></a>

## GadgetActivation Objects

```python
class GadgetActivation(IntFlag)
```

Gadget activation bits (ga_Activation).

<a id="amigainfo.palettes"></a>

# amigainfo.palettes

Default Workbench palettes for classic Amiga icons.

Classic .info files don't contain palette data — they use the system
Workbench palette. These are the standard palettes from each OS generation.

<a id="amigainfo.__main__"></a>

# amigainfo.\_\_main\_\_

CLI tool for inspecting and converting Amiga .info files.

<a id="amigainfo.render"></a>

# amigainfo.render

Render Amiga .info image data to Pillow Images.

<a id="amigainfo.render.to_image"></a>

#### to\_image

```python
def to_image(obj: DiskObject, selected: bool = False) -> Image.Image
```

Render the best available image from a DiskObject.

Priority: ARGB > ColorIcon > NewIcon > Classic.
Falls back to normal state if selected is not available.

**Arguments**:

- `obj` - A loaded DiskObject.
- `selected` - If True, render the selected (highlighted) state.
  

**Returns**:

  A Pillow Image in RGBA or RGB mode.
  

**Raises**:

- `ValueError` - If no image data is available.

<a id="amigainfo.render.png_to_image"></a>

#### png\_to\_image

```python
def png_to_image(data: bytes) -> Image.Image
```

Render a PNG icon image to a Pillow RGBA Image.

<a id="amigainfo.render.argb_to_image"></a>

#### argb\_to\_image

```python
def argb_to_image(img: ARGBImage) -> Image.Image
```

Render an ARGB image to a Pillow RGBA Image.

The raw data is in ARGB byte order; we swap to RGBA for Pillow.

<a id="amigainfo.render.coloricon_to_image"></a>

#### coloricon\_to\_image

```python
def coloricon_to_image(img: ColorIconImage) -> Image.Image
```

Render a ColorIcon/GlowIcon image to a Pillow RGBA Image.

<a id="amigainfo.render.newicon_to_image"></a>

#### newicon\_to\_image

```python
def newicon_to_image(img: NewIconImage) -> Image.Image
```

Render a NewIcon image to a Pillow RGBA Image.

<a id="amigainfo.render.classic_to_image"></a>

#### classic\_to\_image

```python
def classic_to_image(
        img: ClassicImage,
        palette: tuple[tuple[int, int, int], ...] | None = None
) -> Image.Image
```

Render a classic planar image to a Pillow RGBA Image.

Palette index 0 is treated as transparent.

**Arguments**:

- `img` - A ClassicImage with planar bitmap data.
- `palette` - Color palette to use. Defaults to the WB 2.x palette.

<a id="amigainfo.load"></a>

# amigainfo.load

Load Amiga .info files into DiskObject dataclasses.

<a id="amigainfo.load.load"></a>

#### load

```python
def load(data: bytes | bytearray) -> DiskObject
```

Parse an Amiga .info file and return a DiskObject.

**Arguments**:

- `data` - Raw bytes of the .info file.
  

**Returns**:

  A DiskObject populated with all parsed data.
  

**Raises**:

- `ValueError` - If the file doesn't start with the expected magic number.

<a id="amigainfo.save"></a>

# amigainfo.save

Write DiskObject dataclasses back to Amiga .info file bytes.

<a id="amigainfo.save.save"></a>

#### save

```python
def save(obj: DiskObject) -> bytes
```

Serialize a DiskObject to Amiga .info file bytes.

**Arguments**:

- `obj` - A DiskObject to serialize.
  

**Returns**:

  Raw bytes of the .info file.

<a id="amigainfo.models"></a>

# amigainfo.models

<a id="amigainfo.models.Gadget"></a>

## Gadget Objects

```python
@dataclass
class Gadget()
```

Embedded Gadget structure from the DiskObject header (44 bytes on disk).

<a id="amigainfo.models.DrawerData"></a>

## DrawerData Objects

```python
@dataclass
class DrawerData()
```

Drawer window state.

Contains NewWindow fields for the drawer window, scroll offsets,
and optional OS 2.x+ display flags (DrawerData2).

<a id="amigainfo.models.ImageHeader"></a>

## ImageHeader Objects

```python
@dataclass
class ImageHeader()
```

Amiga Image structure header (20 bytes on disk).

Describes a single planar bitmap. The actual pixel data
is stored separately.

<a id="amigainfo.models.ClassicImage"></a>

## ClassicImage Objects

```python
@dataclass
class ClassicImage()
```

A single classic planar bitmap image with its header.

<a id="amigainfo.models.ClassicImages"></a>

## ClassicImages Objects

```python
@dataclass
class ClassicImages()
```

Classic planar bitmap images (OS 1.x-3.1).

Always present in a standard .info file. Up to two images:
normal (from GadgetRender) and selected (from SelectRender).

<a id="amigainfo.models.NewIconImage"></a>

## NewIconImage Objects

```python
@dataclass
class NewIconImage()
```

A single decoded NewIcon image.

<a id="amigainfo.models.NewIconImages"></a>

## NewIconImages Objects

```python
@dataclass
class NewIconImages()
```

NewIcon images decoded from ToolTypes strings.

Identified by the "*** DON'T EDIT THE FOLLOWING LINES!! ***" sentinel.
Image data is in IM1= (normal) and IM2= (selected) tooltypes.

<a id="amigainfo.models.FaceChunk"></a>

## FaceChunk Objects

```python
@dataclass
class FaceChunk()
```

FACE chunk from IFF FORM ICON (GlowIcons/OS 3.5+).

<a id="amigainfo.models.ColorIconImage"></a>

## ColorIconImage Objects

```python
@dataclass
class ColorIconImage()
```

A single IMAG chunk image from IFF FORM ICON.

<a id="amigainfo.models.ColorIconImages"></a>

## ColorIconImages Objects

```python
@dataclass
class ColorIconImages()
```

GlowIcons / ColorIcon images from IFF FORM ICON (OS 3.5+).

Found appended after classic .info data as FORM ICON chunks.

<a id="amigainfo.models.ARGBImage"></a>

## ARGBImage Objects

```python
@dataclass
class ARGBImage()
```

A single 32-bit ARGB image, zlib-compressed in the file.

<a id="amigainfo.models.ARGBImages"></a>

## ARGBImages Objects

```python
@dataclass
class ARGBImages()
```

32-bit ARGB images from IFF FORM ICON ARGB chunks (OS4).

<a id="amigainfo.models.PNGImages"></a>

## PNGImages Objects

```python
@dataclass
class PNGImages()
```

OS4 PNG icon images. Two concatenated PNG files.

<a id="amigainfo.models.DiskObject"></a>

## DiskObject Objects

```python
@dataclass
class DiskObject()
```

Top-level Amiga .info file structure.

Every standard .info file starts with a DiskObject header containing
metadata and a Gadget structure. Image data may be present in multiple
formats, layered on top of each other for backward compatibility:

- classic: Planar bitmaps (always present for 0xE310 files)
- newicon: Higher color images encoded in ToolTypes
- coloricon: GlowIcons IMAG chunks (OS 3.5+)
- argb: 32-bit ARGB image data (OS4)

