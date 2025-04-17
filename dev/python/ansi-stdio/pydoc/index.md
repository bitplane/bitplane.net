<a id="ansi_stdio"></a>

# ansi\_stdio

Tells Python that this is a module dir

<a id="ansi_stdio.loader"></a>

# ansi\_stdio.loader

<a id="ansi_stdio.loader.load"></a>

#### load

```python
def load(path: Path)
```

Loads a buffer-like object from a file.

<a id="ansi_stdio.loader.ansi"></a>

# ansi\_stdio.loader.ansi

<a id="ansi_stdio.loader.ansi.load"></a>

#### load

```python
def load(path)
```

Loads ANSI data from a file

<a id="ansi_stdio.loader.asciinema"></a>

# ansi\_stdio.loader.asciinema

<a id="ansi_stdio.loader.asciinema.load"></a>

#### load

```python
def load(path)
```

Loads asciinema data from a file

<a id="ansi_stdio.utils"></a>

# ansi\_stdio.utils

<a id="ansi_stdio.utils.fonts"></a>

# ansi\_stdio.utils.fonts

<a id="ansi_stdio.cli.quantize"></a>

# ansi\_stdio.cli.quantize

Terminal output quantizer - captures terminal output at specified frame rate.

Usage:
./quantize.py [options] script.py

**Examples**:

  ./quantize.py --fps 2 my_script.py
  ./quantize.py --width 120 --height 40 --fps 5 my_script.py

<a id="ansi_stdio.cli.quantize.parse_arguments"></a>

#### parse\_arguments

```python
def parse_arguments()
```

Parse command line arguments.

<a id="ansi_stdio.cli.quantize.quantize_output"></a>

#### quantize\_output

```python
def quantize_output(script: str,
                    width: Optional[int] = None,
                    height: Optional[int] = None,
                    fps: float = 1.0)
```

Capture and quantize terminal output from a Python script.

**Arguments**:

- `script` _str_ - Path to the Python script to run
- `width` _int, optional_ - Terminal width
- `height` _int, optional_ - Terminal height
- `fps` _float, optional_ - Output frames per second

<a id="ansi_stdio.cli.quantize.main"></a>

#### main

```python
def main()
```

Main entry point for the terminal quantizer.

<a id="ansi_stdio.cli"></a>

# ansi\_stdio.cli

<a id="ansi_stdio.cli.fonts"></a>

# ansi\_stdio.cli.fonts

List available monospace fonts.

Usage:
    monospace-fonts [--print=FIELD] [--format=FORMAT]

Options:
    --print FIELD     What to print. Can be 'name', 'path', or 'all' [default: name]
    --format FORMAT   Output format. Can be 'text', 'json', or 'csv' [default: text]
    -h, --help        Show this help message

<a id="ansi_stdio.cli.fonts.main"></a>

#### main

```python
def main()
```

Entry point for the CLI script.

<a id="ansi_stdio.cli.fonts.print_text_output"></a>

#### print\_text\_output

```python
def print_text_output(fonts, print_field)
```

Print fonts in text format.

<a id="ansi_stdio.cli.fonts.print_json_output"></a>

#### print\_json\_output

```python
def print_json_output(fonts, print_field)
```

Print fonts in JSON format.

<a id="ansi_stdio.cli.fonts.print_csv_output"></a>

#### print\_csv\_output

```python
def print_csv_output(fonts, print_field)
```

Print fonts in CSV format.

<a id="ansi_stdio.core"></a>

# ansi\_stdio.core

<a id="ansi_stdio.core.clock"></a>

# ansi\_stdio.core.clock

<a id="ansi_stdio.core.clock.Clock"></a>

## Clock Objects

```python
class Clock()
```

Base class for clocks.

A clock represents a time transformation that can be applied to animations.
Each clock can have a parent clock, creating a hierarchy of time transformations.

<a id="ansi_stdio.core.clock.Clock.__init__"></a>

#### \_\_init\_\_

```python
def __init__(parent=None)
```

Initialize the clock.

**Arguments**:

- `parent` - Optional parent clock that feeds time to this clock

<a id="ansi_stdio.core.clock.Clock.time"></a>

#### time

```python
@property
def time()
```

Get the current time, considering parent's time and local adjustments.

**Returns**:

  Current transformed time in seconds

<a id="ansi_stdio.core.clock.Clock.time"></a>

#### time

```python
@time.setter
def time(value)
```

Set the current time by adjusting the skew from parent.

**Arguments**:

- `value` - The time to set

<a id="ansi_stdio.core.clock.Clock.parent_time"></a>

#### parent\_time

```python
@property
def parent_time()
```

Get the time of the parent clock, or system time if no parent.

**Returns**:

  Parent's time or system time in seconds

<a id="ansi_stdio.core.clock.Clock.pause"></a>

#### pause

```python
def pause()
```

Pause the clock, freezing its time.

<a id="ansi_stdio.core.clock.Clock.resume"></a>

#### resume

```python
def resume()
```

Resume the clock, continuing from where it was paused.
Adjusts the skew to maintain the exact time where it was paused.

<a id="ansi_stdio.core.saved"></a>

# ansi\_stdio.core.saved

<a id="ansi_stdio.core.saved.Param"></a>

## Param Objects

```python
@dataclass(slots=True)
class Param()
```

Represents a parameter.

<a id="ansi_stdio.core.saved.Params"></a>

## Params Objects

```python
@dataclass(slots=True)
class Params()
```

Holds kwargs and constructor function for a class.

<a id="ansi_stdio.core.saved.Saved"></a>

## Saved Objects

```python
class Saved()
```

A class that can be serialized and deserialized.

<a id="ansi_stdio.core.saved.Saved.arguments"></a>

#### arguments

```python
def arguments() -> dict[str, Any]
```

Get the arguments needed to construct this object.
Filters out any arguments that are the same as the default value.

<a id="ansi_stdio.core.saved.Saved.save"></a>

#### save

```python
def save() -> dict
```

Convert the instance to a dictionary.

<a id="ansi_stdio.core.versioned"></a>

# ansi\_stdio.core.versioned

<a id="ansi_stdio.core.versioned.Versioned"></a>

## Versioned Objects

```python
class Versioned()
```

Inherit this class to store a version number on each change.

<a id="ansi_stdio.core.versioned.Versioned.change"></a>

#### change

```python
def change()
```

Call this if you changed something and need to blow caches

<a id="ansi_stdio.core.versioned.Versioned.version"></a>

#### version

```python
@property
def version()
```

Return the version number of this object.

<a id="ansi_stdio.core.versioned.Versioned.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Versionable objects are cacheable ones

<a id="ansi_stdio.core.versioned.changes"></a>

#### changes

```python
def changes(method)
```

Decorate methods with this if they make changes to the object

<a id="ansi_stdio.core.versioned.waits"></a>

#### waits

```python
def waits(method)
```

Decorate methods with this if they need to wait for changes

<a id="ansi_stdio.core.box"></a>

# ansi\_stdio.core.box

<a id="ansi_stdio.core.box.Box"></a>

## Box Objects

```python
class Box()
```

Represents a rectangular area on the screen.

<a id="ansi_stdio.core.box.Box.__init__"></a>

#### \_\_init\_\_

```python
def __init__(min_x=0, min_y=0, max_x=0, max_y=0)
```

Initialize the box with the given coordinates.

<a id="ansi_stdio.core.box.Box.reset"></a>

#### reset

```python
def reset()
```

Reset the box to the origin.

<a id="ansi_stdio.core.box.Box.__add__"></a>

#### \_\_add\_\_

```python
def __add__(other)
```

Combine two boxes into a new box that encompasses both.

<a id="ansi_stdio.core.box.Box.__and__"></a>

#### \_\_and\_\_

```python
def __and__(other: "Box") -> "Box"
```

Intersect two box to find the overlapping area.

<a id="ansi_stdio.core.box.Box.__iand__"></a>

#### \_\_iand\_\_

```python
def __iand__(other: "Box") -> "Box"
```

Crop the box to the overlapping area.

<a id="ansi_stdio.core.box.Box.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__()
```

True if the box has a non-zero area.

<a id="ansi_stdio.core.box.Box.__len__"></a>

#### \_\_len\_\_

```python
def __len__()
```

Return the area of the box.

<a id="ansi_stdio.core.box.Box.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(item)
```

Check if the given item is contained within the box.

<a id="ansi_stdio.core.box.Box.update"></a>

#### update

```python
def update(x, y)
```

Update the box to include the given coordinates.

<a id="ansi_stdio.core.box.Box.contains"></a>

#### contains

```python
def contains(x=None, y=None)
```

Check if the given coordinates are within the box.
If x or y is None, it will not be checked.

<a id="ansi_stdio.core.box.Box.width"></a>

#### width

```python
@property
def width()
```

Width of the bounding box.

<a id="ansi_stdio.core.box.Box.height"></a>

#### height

```python
@property
def height()
```

Height of the bounding box.

<a id="ansi_stdio.terminal.info"></a>

# ansi\_stdio.terminal.info

<a id="ansi_stdio.terminal.info.get_terminal_size"></a>

#### get\_terminal\_size

```python
def get_terminal_size(default_width: int = 80,
                      default_height: int = 24) -> Tuple[int, int]
```

Detect terminal size using multiple fallback methods.

**Arguments**:

- `default_width` _int, optional_ - Default terminal width. Defaults to 80.
- `default_height` _int, optional_ - Default terminal height. Defaults to 24.
  

**Returns**:

  Tuple[int, int]: A tuple of (width, height) representing terminal dimensions.

<a id="ansi_stdio.terminal"></a>

# ansi\_stdio.terminal

<a id="ansi_stdio.terminal.capture"></a>

# ansi\_stdio.terminal.capture

<a id="ansi_stdio.terminal.capture.capture_terminal"></a>

#### capture\_terminal

```python
def capture_terminal(
    program: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    buffer_size: int = 4096,
    display_callback: Optional[Callable[[pyte.Screen], None]] = None
) -> pyte.Screen
```

Capture terminal output for a given program with flexible processing.

**Arguments**:

- `program` _str_ - Command to run in the terminal
- `width` _int, optional_ - Terminal width. Defaults to detected width.
- `height` _int, optional_ - Terminal height. Defaults to detected height.
- `buffer_size` _int, optional_ - Size of read buffer. Defaults to 4096.
- `display_callback` _Callable, optional_ - Function to process screen state.
  Receives the pyte Screen object for custom handling.
  

**Returns**:

- `pyte.Screen` - The final screen state after program execution

<a id="ansi_stdio.terminal.render"></a>

# ansi\_stdio.terminal.render

Pyte screen renderer for ANSI stdio.
Converts pyte screen state to formatted strings with ANSI escape sequences.

<a id="ansi_stdio.terminal.render.format_char"></a>

#### format\_char

```python
def format_char(char)
```

Format a single character with its attributes.

**Arguments**:

- `char` - A pyte character with attributes
  

**Returns**:

- `str` - The formatted character with ANSI codes

<a id="ansi_stdio.terminal.render.format_line"></a>

#### format\_line

```python
def format_line(row, width)
```

Format a single line of the screen.

**Arguments**:

- `row` - A dictionary of column -> character mappings
- `width` - The width of the screen
  

**Returns**:

- `str` - The formatted line

<a id="ansi_stdio.terminal.render.render_screen"></a>

#### render\_screen

```python
def render_screen(screen, dirty_only=False, clear_dirty=True)
```

Convert a pyte screen to a dictionary of formatted strings.

**Arguments**:

- `screen` - A pyte.Screen instance
- `dirty_only` - If True, only render dirty lines
- `clear_dirty` - Whether to clear the dirty set after processing
  

**Returns**:

- `dict` - A dictionary mapping line numbers to formatted strings

<a id="ansi_stdio.terminal.render.display_screen"></a>

#### display\_screen

```python
def display_screen(screen, dirty_only=False, clear_dirty=True)
```

Display a pyte screen using ANSI escape sequences.

**Arguments**:

- `screen` - A pyte.Screen instance
- `dirty_only` - If True, only display dirty lines
- `clear_dirty` - Whether to clear the dirty set after processing

<a id="ansi_stdio.__main__"></a>

# ansi\_stdio.\_\_main\_\_

Entry point for the package

<a id="ansi_stdio.buffer.animation"></a>

# ansi\_stdio.buffer.animation

<a id="ansi_stdio.buffer.animation.Animation"></a>

## Animation Objects

```python
class Animation(Versioned)
```

An animation that we can render somewhere.

<a id="ansi_stdio.buffer"></a>

# ansi\_stdio.buffer

<a id="ansi_stdio.buffer.buffer"></a>

# ansi\_stdio.buffer.buffer

<a id="ansi_stdio.buffer.buffer.Buffer"></a>

## Buffer Objects

```python
class Buffer(Versioned)
```

A 2D sparse grid of rich.Segment objects.

<a id="ansi_stdio.buffer.buffer.Buffer.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initialize the buffer as a sparse structure.

<a id="ansi_stdio.buffer.buffer.Buffer.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(coords)
```

Get the item at the given coordinates.

**Arguments**:

- `coords` - A tuple of (x, y) coordinates
  

**Returns**:

  The Segment at those coordinates or None if empty

<a id="ansi_stdio.buffer.buffer.Buffer.__setitem__"></a>

#### \_\_setitem\_\_

```python
@changes
def __setitem__(coords, segment)
```

Set a segment at the given coordinates.

**Arguments**:

- `coords` - A tuple of (x, y) coordinates
- `segment` - The Segment to place at these coordinates

<a id="ansi_stdio.buffer.buffer.Buffer.__iadd__"></a>

#### \_\_iadd\_\_

```python
@changes
def __iadd__(other) -> "Buffer"
```

Merge another buffer into this one.

<a id="ansi_stdio.buffer.buffer.Buffer.__add__"></a>

#### \_\_add\_\_

```python
def __add__(other) -> "Buffer"
```

Create a new buffer by merging this buffer with another.

<a id="ansi_stdio.buffer.buffer.Buffer.__and__"></a>

#### \_\_and\_\_

```python
def __and__(box: Box) -> "Buffer"
```

Crop the buffer to the given box.
Returns a newly allocated buffer.

<a id="ansi_stdio.buffer.buffer.Buffer.__iand__"></a>

#### \_\_iand\_\_

```python
@changes
def __iand__(box: Box) -> "Buffer"
```

Crop the buffer to the given box.
This modifies the buffer in place.

<a id="ansi_stdio.buffer.buffer.Buffer.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(other: "Buffer") -> "Buffer"
```

Create a new buffer representing the difference: self - other.
Only includes cells in self that differ from other.

<a id="ansi_stdio.buffer.buffer.Buffer.__isub__"></a>

#### \_\_isub\_\_

```python
@changes
def __isub__(other: "Buffer") -> "Buffer"
```

Remove from self any cells that are identical in other.
Modifies the buffer in-place.

<a id="ansi_stdio.buffer.buffer.Buffer.__len__"></a>

#### \_\_len\_\_

```python
def __len__()
```

Get the number of cells set in the buffer.

<a id="ansi_stdio.buffer.buffer.Buffer.set"></a>

#### set

```python
@changes
def set(x, y, segment)
```

Set cell(s) starting at given coordinates with a Segment.
Handles multi-character segments by writing each character in sequence.

**Arguments**:

- `x` - Starting X coordinate
- `y` - Y coordinate
- `segment` - Rich Segment object to place at this position

<a id="ansi_stdio.buffer.buffer.Buffer.copy"></a>

#### copy

```python
def copy()
```

Create a deep copy of this buffer.

**Returns**:

  A new Buffer instance with the same content

<a id="ansi_stdio.buffer.buffer.Buffer.recalculate"></a>

#### recalculate

```python
@changes
def recalculate(size: bool = True, box: bool = True)
```

Recalculate the size and box

<a id="ansi_stdio.buffer.frame"></a>

# ansi\_stdio.buffer.frame

<a id="ansi_stdio.buffer.frame.Frame"></a>

## Frame Objects

```python
class Frame(Versioned)
```

A frame of animation, containing a buffer.

