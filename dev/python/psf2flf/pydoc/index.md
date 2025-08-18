<a id="psf2flf"></a>

# psf2flf

<a id="psf2flf.utils"></a>

# psf2flf.utils

<a id="psf2flf.utils.print_dict"></a>

#### print\_dict

```python
def print_dict(data: dict, prefix: str = "")
```

Recursively prints the key-value pairs of a dictionary.

<a id="psf2flf.reader"></a>

# psf2flf.reader

<a id="psf2flf.reader.read"></a>

#### read

```python
def read(path: Path)
```

Reads a font from the given path using the appropriate reader.

<a id="psf2flf.reader.reader"></a>

# psf2flf.reader.reader

<a id="psf2flf.reader.reader.Reader"></a>

## Reader Objects

```python
class Reader(ABC)
```

Base class for font readers.

<a id="psf2flf.reader.reader.Reader.can_open"></a>

#### can\_open

```python
@staticmethod
@abstractmethod
def can_open(path: Path) -> bool
```

Returns True if the reader can open the given file path.

<a id="psf2flf.reader.reader.Reader.read"></a>

#### read

```python
@abstractmethod
def read(path: Path) -> Font
```

Reads the font from the given path and returns a Font object.

<a id="psf2flf.reader.psf"></a>

# psf2flf.reader.psf

<a id="psf2flf.__main__"></a>

# psf2flf.\_\_main\_\_

<a id="psf2flf.writer"></a>

# psf2flf.writer

<a id="psf2flf.writer.write"></a>

#### write

```python
def write(font: Font, path: Path, tall_mode: bool = False)
```

Writes a font to the given path using the appropriate writer.

<a id="psf2flf.writer.flf"></a>

# psf2flf.writer.flf

<a id="psf2flf.writer.writer"></a>

# psf2flf.writer.writer

<a id="psf2flf.writer.writer.Writer"></a>

## Writer Objects

```python
class Writer(ABC)
```

Base class for font writers.

<a id="psf2flf.writer.writer.Writer.can_write"></a>

#### can\_write

```python
@staticmethod
@abstractmethod
def can_write(path: Path) -> bool
```

Returns True if the writer can write to the given file path.

<a id="psf2flf.writer.writer.Writer.write"></a>

#### write

```python
@abstractmethod
def write(font: Font, path: Path)
```

Writes the font to the given path.

<a id="psf2flf.font"></a>

# psf2flf.font

<a id="psf2flf.font.fontdir"></a>

# psf2flf.font.fontdir

<a id="psf2flf.font.fontdir.FontDir"></a>

## FontDir Objects

```python
@dataclass
class FontDir()
```

A collection of typefaces, typically representing a font directory or archive.

<a id="psf2flf.font.fontdir.FontDir.__iadd__"></a>

#### \_\_iadd\_\_

```python
def __iadd__(other: Union[Font, TypeFace])
```

Add a font or typeface to this directory.

<a id="psf2flf.font.fontdir.FontDir.write_directory"></a>

#### write\_directory

```python
def write_directory(output_dir: Path, tall_mode: bool = False)
```

Write all typefaces to a directory structure.

<a id="psf2flf.font.fontdir.FontDir.write_tar"></a>

#### write\_tar

```python
def write_tar(output_path: Path, tall_mode: bool = False)
```

Write all typefaces to a tar archive.

<a id="psf2flf.font.font"></a>

# psf2flf.font.font

<a id="psf2flf.font.font.Font"></a>

## Font Objects

```python
@dataclass
class Font()
```

A generic representation of a font.

<a id="psf2flf.font.font.Font.name"></a>

#### name

```python
@property
def name() -> str
```

Get the font name from metadata.

<a id="psf2flf.font.font.Font.style"></a>

#### style

```python
@property
def style() -> frozenset[str]
```

Get the font style from metadata.

<a id="psf2flf.font.font.Font.width"></a>

#### width

```python
@property
def width() -> int
```

Get the font width from metadata.

<a id="psf2flf.font.font.Font.height"></a>

#### height

```python
@property
def height() -> int
```

Get the font height from metadata.

<a id="psf2flf.font.font.Font.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other) -> bool
```

Two fonts are equal if name, style, width, height match and overlapping ASCII glyphs are identical.

<a id="psf2flf.font.font.Font.__iadd__"></a>

#### \_\_iadd\_\_

```python
def __iadd__(other)
```

Merge another font into this one if they are compatible.

<a id="psf2flf.font.font.Font.force_merge"></a>

#### force\_merge

```python
def force_merge(other)
```

Force merge another font, ignoring compatibility checks.

<a id="psf2flf.font.typeface"></a>

# psf2flf.font.typeface

<a id="psf2flf.font.typeface.TypeFace"></a>

## TypeFace Objects

```python
@dataclass
class TypeFace()
```

Represents a collection of related fonts (e.g., by family, style, and size).

<a id="psf2flf.font.typeface.TypeFace.__iadd__"></a>

#### \_\_iadd\_\_

```python
def __iadd__(font: Font)
```

Add a font to this typeface.

<a id="psf2flf.main"></a>

# psf2flf.main

<a id="psf2flf.main.show_info"></a>

#### show\_info

```python
def show_info(source: Path)
```

Show information about a single font file.

<a id="psf2flf.main.is_directory_output"></a>

#### is\_directory\_output

```python
def is_directory_output(path: Path) -> bool
```

Check if the output path indicates a directory.

<a id="psf2flf.main.convert_multiple"></a>

#### convert\_multiple

```python
def convert_multiple(inputs: list[Path],
                     output: Path,
                     tall_mode: bool = False,
                     force: bool = False)
```

Convert multiple input files to single output (font or directory).

<a id="psf2flf.main.convert_all_in_directory"></a>

#### convert\_all\_in\_directory

```python
def convert_all_in_directory(source_dir: Path,
                             dest_dir: Path,
                             tall_mode: bool = False)
```

Convert all PSF fonts in a directory (legacy --all mode).

