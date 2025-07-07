<a id=".texxd"></a>

# .texxd

texxd - A hex editor built with Textual.

<a id=".texxd.hex_editor"></a>

# .texxd.hex\_editor

Hex editor widget.

<a id=".texxd.hex_editor.HexEditor"></a>

## HexEditor Objects

```python
class HexEditor(Static)
```

A hex editor widget.

<a id=".texxd.hex_editor.HexEditor.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Compose the hex editor layout.

<a id=".texxd.hex_editor.HexEditor.open"></a>

#### open

```python
def open(file_path: Path) -> None
```

Open a file for hex editing.

<a id=".texxd.highlighters.highlights"></a>

# .texxd.highlighters.highlights

Composite highlighter that manages multiple highlighters in order.

<a id=".texxd.highlighters.highlights.Highlights"></a>

## Highlights Objects

```python
class Highlights(dict, Highlighter)
```

A composite highlighter that manages multiple highlighters in insertion order.

Acts as both a dict (for managing highlighters by name) and a Highlighter
(for applying all highlighters in order).

<a id=".texxd.highlighters.highlights.Highlights.highlight"></a>

#### highlight

```python
def highlight(data: bytes, file_offset: int,
              styles: List[Optional[Style]]) -> None
```

Apply all highlighters in insertion order.

<a id=".texxd.highlighters"></a>

# .texxd.highlighters

Highlighter implementations for hex editor.

<a id=".texxd.highlighters.highlighter"></a>

# .texxd.highlighters.highlighter

Highlighter interface for styling bytes in hex editor.

<a id=".texxd.highlighters.highlighter.Highlighter"></a>

## Highlighter Objects

```python
class Highlighter()
```

A highlighter takes a block of bytes with their file offset and current styles,
then modifies the styles array to apply highlighting effects.

<a id=".texxd.highlighters.highlighter.Highlighter.highlight"></a>

#### highlight

```python
def highlight(data: bytes, file_offset: int,
              styles: List[Optional[Style]]) -> None
```

Apply highlighting to the styles array.

**Arguments**:

- `data` - The bytes to be highlighted
- `file_offset` - Starting offset of the data in the file
- `styles` - List of current styles (same length as data).
  Each element can be None or an existing Style.
  Highlighters should modify this list in-place.

<a id=".texxd.highlighters.data"></a>

# .texxd.highlighters.data

Data-based highlighter for different byte types and data formats.

<a id=".texxd.highlighters.data.DataHighlighter"></a>

## DataHighlighter Objects

```python
class DataHighlighter(Highlighter)
```

Highlights bytes based on data types and content.

<a id=".texxd.highlighters.data.DataHighlighter.highlight"></a>

#### highlight

```python
def highlight(data: bytes, file_offset: int,
              styles: List[Optional[Style]]) -> None
```

Apply highlighting based on byte values.

<a id=".texxd.cursors"></a>

# .texxd.cursors

Cursor types for hex editor interaction.

<a id=".texxd.cursors.cursor"></a>

# .texxd.cursors.cursor

Base cursor class for hex editor navigation and highlighting.

<a id=".texxd.cursors.cursor.CursorMoved"></a>

## CursorMoved Objects

```python
class CursorMoved(Message)
```

Message sent when cursor position changes.

<a id=".texxd.cursors.cursor.ScrollRequest"></a>

## ScrollRequest Objects

```python
class ScrollRequest(Message)
```

Message sent to request scrolling to a specific line.

<a id=".texxd.cursors.cursor.Cursor"></a>

## Cursor Objects

```python
class Cursor(Highlighter, Widget)
```

Base cursor class that handles navigation and provides highlighting.

A cursor is a special highlighter that:
- Tracks position in the file
- Handles navigation events
- Highlights its current position
- Can emit write events and scroll position changes

<a id=".texxd.cursors.cursor.Cursor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(bytes_per_line: int = 16,
             view_height: int = 10,
             parent_column=None,
             name: Optional[str] = None,
             id: Optional[str] = None,
             classes: Optional[str] = None,
             disabled: bool = False)
```

Initialize cursor.

**Arguments**:

- `bytes_per_line` - Number of bytes per line
- `view_height` - Height of the view for page up/down calculations

<a id=".texxd.cursors.cursor.Cursor.file_size"></a>

#### file\_size

```python
@property
def file_size() -> int
```

Get current file size from parent column.

<a id=".texxd.cursors.cursor.Cursor.view_height"></a>

#### view\_height

```python
@property
def view_height() -> int
```

Get current view height from hex view.

<a id=".texxd.cursors.cursor.Cursor.x"></a>

#### x

```python
@property
def x() -> int
```

Get x coordinate (column within line).

<a id=".texxd.cursors.cursor.Cursor.y"></a>

#### y

```python
@property
def y() -> int
```

Get y coordinate (line number).

<a id=".texxd.cursors.cursor.Cursor.highlight"></a>

#### highlight

```python
def highlight(data: bytes, file_offset: int,
              styles: List[Optional[Style]]) -> None
```

Apply cursor highlighting to the styles array.

<a id=".texxd.cursors.cursor.Cursor.handle_event"></a>

#### handle\_event

```python
def handle_event(event: events.Event) -> bool
```

Handle navigation events.

**Arguments**:

- `event` - The event to handle
  

**Returns**:

  True if the event was handled, False otherwise

<a id=".texxd.cursors.cursor.Cursor.move_x"></a>

#### move\_x

```python
def move_x(delta: int) -> None
```

Move cursor horizontally with wrapping.

<a id=".texxd.cursors.cursor.Cursor.move_y"></a>

#### move\_y

```python
def move_y(delta: int) -> None
```

Move cursor vertically, preserving x position.

<a id=".texxd.cursors.cursor.Cursor.set_x"></a>

#### set\_x

```python
def set_x(x: int) -> None
```

Set x coordinate (column within line).

<a id=".texxd.cursors.cursor.Cursor.set_y"></a>

#### set\_y

```python
def set_y(y: int) -> None
```

Set y coordinate (line number), preserving x position.

<a id=".texxd.cursors.cursor.Cursor.on_focus"></a>

#### on\_focus

```python
def on_focus() -> None
```

Called when cursor gains focus.

<a id=".texxd.cursors.cursor.Cursor.on_blur"></a>

#### on\_blur

```python
def on_blur() -> None
```

Called when cursor loses focus.

<a id=".texxd.cursors.hex_cursor"></a>

# .texxd.cursors.hex\_cursor

Hex cursor class for hex editing.

<a id=".texxd.cursors.hex_cursor.HexCursor"></a>

## HexCursor Objects

```python
class HexCursor(Cursor)
```

Hex cursor that handles hex input and delegates writing to the file class.

<a id=".texxd.cursors.hex_cursor.HexCursor.handle_event"></a>

#### handle\_event

```python
def handle_event(event: events.Event) -> bool
```

Handle hex editing events.

<a id=".texxd.cursors.ascii_cursor"></a>

# .texxd.cursors.ascii\_cursor

ASCII cursor class for ASCII editing.

<a id=".texxd.cursors.ascii_cursor.AsciiCursor"></a>

## AsciiCursor Objects

```python
class AsciiCursor(Cursor)
```

ASCII cursor that handles ASCII input and delegates writing to the file class.

<a id=".texxd.cursors.ascii_cursor.AsciiCursor.handle_event"></a>

#### handle\_event

```python
def handle_event(event: events.Event) -> bool
```

Handle ASCII editing events.

<a id=".texxd.log"></a>

# .texxd.log

<a id=".texxd.log.setup_logging"></a>

#### setup\_logging

```python
def setup_logging(log_level: str = "INFO",
                  log_file: Optional[Path] = None) -> None
```

Setup logging configuration.

**Arguments**:

- `log_level` - Log level (DEBUG, INFO, WARNING, ERROR)
- `log_file` - Optional log file path

<a id=".texxd.log.get_logger"></a>

#### get\_logger

```python
def get_logger(name: str) -> logging.Logger
```

Get a logger instance.

<a id=".texxd.app"></a>

# .texxd.app

Main application for texxd hex editor.

<a id=".texxd.app.TexxdApp"></a>

## TexxdApp Objects

```python
class TexxdApp(App)
```

A hex editor application built with Textual.

<a id=".texxd.app.TexxdApp.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Compose the application layout.

<a id=".texxd.app.TexxdApp.on_mount"></a>

#### on\_mount

```python
def on_mount() -> None
```

Handle mount event.

<a id=".texxd.app.TexxdApp.action_quit"></a>

#### action\_quit

```python
def action_quit() -> None
```

Quit the application.

<a id=".texxd.app.TexxdApp.action_save"></a>

#### action\_save

```python
def action_save() -> None
```

Save the current file.

<a id=".texxd.app.main"></a>

#### main

```python
def main() -> None
```

Main entry point for the application.

<a id=".texxd.hex_file"></a>

# .texxd.hex\_file

File-like object with memory view and write buffer overlay.

<a id=".texxd.hex_file.HexFile"></a>

## HexFile Objects

```python
class HexFile(RawIOBase, Highlighter)
```

A file-like object that wraps a file with memory view and write buffer.

<a id=".texxd.hex_file.HexFile.size"></a>

#### size

```python
@property
def size() -> int
```

Get the current size of the file including unsaved changes.

<a id=".texxd.hex_file.HexFile.tell"></a>

#### tell

```python
def tell() -> int
```

Get current position.

<a id=".texxd.hex_file.HexFile.seek"></a>

#### seek

```python
def seek(offset: int, whence: int = 0) -> int
```

Seek to position.

<a id=".texxd.hex_file.HexFile.readable"></a>

#### readable

```python
def readable() -> bool
```

Return True if the stream can be read from.

<a id=".texxd.hex_file.HexFile.readinto"></a>

#### readinto

```python
def readinto(b: bytearray) -> int
```

Read bytes into a pre-allocated bytearray.

<a id=".texxd.hex_file.HexFile.read"></a>

#### read

```python
def read(size: int = -1) -> bytes
```

Read bytes from current position.

<a id=".texxd.hex_file.HexFile.writable"></a>

#### writable

```python
def writable() -> bool
```

Return True if the stream can be written to.

<a id=".texxd.hex_file.HexFile.write"></a>

#### write

```python
def write(data: bytes) -> int
```

Write bytes to buffer at current position.

<a id=".texxd.hex_file.HexFile.has_unsaved_changes"></a>

#### has\_unsaved\_changes

```python
def has_unsaved_changes() -> bool
```

Check if there are unsaved changes.

<a id=".texxd.hex_file.HexFile.get_unsaved_ranges"></a>

#### get\_unsaved\_ranges

```python
def get_unsaved_ranges() -> list[Tuple[int, int]]
```

Get list of (start, end) tuples for unsaved byte ranges.

<a id=".texxd.hex_file.HexFile.highlight"></a>

#### highlight

```python
def highlight(data: bytes, file_offset: int,
              styles: List[Optional[Style]]) -> None
```

Apply edit highlighting to the styles array.

<a id=".texxd.hex_file.HexFile.flush"></a>

#### flush

```python
def flush() -> None
```

Flush all changes to the underlying file.

<a id=".texxd.hex_file.HexFile.revert"></a>

#### revert

```python
def revert() -> None
```

Discard all unsaved changes.

<a id=".texxd.hex_file.HexFile.close"></a>

#### close

```python
def close() -> None
```

Close the underlying file.

<a id=".texxd.columns"></a>

# .texxd.columns

Column types for hex editor display.

<a id=".texxd.columns.ascii"></a>

# .texxd.columns.ascii

ASCII column widget for displaying data in ASCII format.

<a id=".texxd.columns.ascii.AsciiColumn"></a>

## AsciiColumn Objects

```python
class AsciiColumn(Column)
```

Widget that displays data in ASCII format.

<a id=".texxd.columns.ascii.AsciiColumn.get_content_width"></a>

#### get\_content\_width

```python
def get_content_width() -> int
```

Calculate content width.

<a id=".texxd.columns.ascii.AsciiColumn.render_line"></a>

#### render\_line

```python
def render_line(y: int) -> Strip
```

Render a line of ASCII data.

<a id=".texxd.columns.ascii.AsciiColumn.calculate_click_position"></a>

#### calculate\_click\_position

```python
def calculate_click_position(click_offset: int) -> Optional[int]
```

Calculate byte position within ASCII column from click offset.

<a id=".texxd.columns.ascii.AsciiColumn.on_key"></a>

#### on\_key

```python
def on_key(event: events.Key) -> bool
```

Handle key events for the column.

<a id=".texxd.columns.ascii.AsciiColumn.get_byte_position"></a>

#### get\_byte\_position

```python
def get_byte_position(x: int, y: int) -> Optional[int]
```

Get byte position from column coordinates.

<a id=".texxd.columns.column"></a>

# .texxd.columns.column

Base class for all columns.

<a id=".texxd.columns.column.Column"></a>

## Column Objects

```python
class Column(Static)
```

Base class for all columns.

<a id=".texxd.columns.column.Column.add_highlighter"></a>

#### add\_highlighter

```python
def add_highlighter(name: str, highlighter: Highlighter) -> None
```

Add a highlighter to this column with a name.

<a id=".texxd.columns.column.Column.get_content_width"></a>

#### get\_content\_width

```python
def get_content_width() -> int
```

Get the width of the column's content.

<a id=".texxd.columns.column.Column.render_line"></a>

#### render\_line

```python
def render_line(y: int) -> Strip
```

Render a single line of the column.

<a id=".texxd.columns.column.Column.on_key"></a>

#### on\_key

```python
def on_key(event: events.Key) -> bool
```

Handle key events for the column.

**Arguments**:

- `event` - The key event.
  

**Returns**:

  True if the event was handled, False otherwise.

<a id=".texxd.columns.hex"></a>

# .texxd.columns.hex

Hex column widget for displaying data in hexadecimal format.

<a id=".texxd.columns.hex.HexColumn"></a>

## HexColumn Objects

```python
class HexColumn(Column)
```

Widget that displays data in hexadecimal format.

<a id=".texxd.columns.hex.HexColumn.get_content_width"></a>

#### get\_content\_width

```python
def get_content_width() -> int
```

Calculate content width.

<a id=".texxd.columns.hex.HexColumn.render_line"></a>

#### render\_line

```python
def render_line(y: int) -> Strip
```

Render a line of hex data.

<a id=".texxd.columns.hex.HexColumn.calculate_click_position"></a>

#### calculate\_click\_position

```python
def calculate_click_position(click_offset: int) -> Optional[int]
```

Calculate byte position within hex column from click offset.

<a id=".texxd.columns.hex.HexColumn.on_key"></a>

#### on\_key

```python
def on_key(event: events.Key) -> bool
```

Handle key events for the column.

<a id=".texxd.columns.hex.HexColumn.get_byte_position"></a>

#### get\_byte\_position

```python
def get_byte_position(x: int, y: int) -> Optional[int]
```

Get byte position from column coordinates.

<a id=".texxd.columns.address"></a>

# .texxd.columns.address

Address column widget for displaying file offsets.

<a id=".texxd.columns.address.AddressColumn"></a>

## AddressColumn Objects

```python
class AddressColumn(Column)
```

Widget that displays file offset addresses.

<a id=".texxd.columns.address.AddressColumn.get_content_width"></a>

#### get\_content\_width

```python
def get_content_width() -> int
```

Calculate content width based on file size.

<a id=".texxd.columns.address.AddressColumn.render_line"></a>

#### render\_line

```python
def render_line(y: int) -> Strip
```

Render a line of addresses.

<a id=".texxd.hex_view"></a>

# .texxd.hex\_view

Hex view widget using Textual widget-based columns.

<a id=".texxd.hex_view.HexView"></a>

## HexView Objects

```python
class HexView(ScrollView)
```

A widget that displays binary data using widget-based columns.

<a id=".texxd.hex_view.HexView.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Compose the hex view layout.

<a id=".texxd.hex_view.HexView.on_mount"></a>

#### on\_mount

```python
def on_mount() -> None
```

Handle mount event.

<a id=".texxd.hex_view.HexView.set_file"></a>

#### set\_file

```python
def set_file(file) -> None
```

Set the file to read from.

<a id=".texxd.hex_view.HexView.on_cursor_moved"></a>

#### on\_cursor\_moved

```python
def on_cursor_moved(message: CursorMoved) -> None
```

Handle cursor movement messages from columns.

<a id=".texxd.hex_view.HexView.on_scroll_request"></a>

#### on\_scroll\_request

```python
def on_scroll_request(message: ScrollRequest) -> None
```

Handle scroll request messages from columns.

<a id=".texxd.hex_view.HexView.on_key"></a>

#### on\_key

```python
def on_key(event: events.Key) -> None
```

Handle key events.

<a id=".texxd.hex_view.HexView.on_mouse_down"></a>

#### on\_mouse\_down

```python
def on_mouse_down(event: events.MouseDown) -> None
```

Handle mouse click events.

<a id=".texxd.hex_view.HexView.render_line"></a>

#### render\_line

```python
def render_line(y: int) -> Strip
```

Render a single line of the hex view.

