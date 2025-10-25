<a id="logloglog"></a>

# logloglog

LogLogLog - Efficient scrollback indexing for large log files.

<a id="logloglog.configure_logging"></a>

#### configure\_logging

```python
def configure_logging(level=logging.INFO)
```

Configure logging for LogLogLog.

<a id="logloglog.line_index"></a>

# logloglog.line\_index

Simple line indexing with periodic summaries for efficient wrapping calculations.

<a id="logloglog.line_index.MAX_WIDTH"></a>

#### MAX\_WIDTH

Maximum terminal width we support

<a id="logloglog.line_index.SUMMARY_INTERVAL"></a>

#### SUMMARY\_INTERVAL

Store summary every N lines

<a id="logloglog.line_index.LineIndex"></a>

## LineIndex Objects

```python
class LineIndex()
```

Indexes log lines with byte positions, widths, and periodic summaries.

Stores:
- line_positions: byte offset of each line in the log file
- line_widths: display width of each line
- summaries: every 1000 lines, cumulative display rows for each width 1-512

<a id="logloglog.line_index.LineIndex.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index_path: Path)
```

Initialize line index with given path.

<a id="logloglog.line_index.LineIndex.open"></a>

#### open

```python
def open(create: bool = False)
```

Open index files.

<a id="logloglog.line_index.LineIndex.close"></a>

#### close

```python
def close()
```

Close all index files.

<a id="logloglog.line_index.LineIndex.append_line"></a>

#### append\_line

```python
def append_line(position: int, width: int)
```

Append a new line to the index.

**Arguments**:

- `position` - Byte offset of line start in log file
- `width` - Display width of the line

<a id="logloglog.line_index.LineIndex.get_line_position"></a>

#### get\_line\_position

```python
def get_line_position(line_no: int) -> int
```

Get byte position of a line.

<a id="logloglog.line_index.LineIndex.get_line_width"></a>

#### get\_line\_width

```python
def get_line_width(line_no: int) -> int
```

Get display width of a line.

<a id="logloglog.line_index.LineIndex.get_total_display_rows"></a>

#### get\_total\_display\_rows

```python
def get_total_display_rows(width: int) -> int
```

Get total display rows for all lines at given terminal width.

**Arguments**:

- `width` - Terminal width
  

**Returns**:

  Total number of display rows

<a id="logloglog.line_index.LineIndex.get_display_row_for_line"></a>

#### get\_display\_row\_for\_line

```python
def get_display_row_for_line(line_no: int, width: int) -> int
```

Get the display row number where a logical line starts.

**Arguments**:

- `line_no` - Logical line number
- `width` - Terminal width
  

**Returns**:

  Display row number where this line starts

<a id="logloglog.line_index.LineIndex.get_line_for_display_row"></a>

#### get\_line\_for\_display\_row

```python
def get_line_for_display_row(display_row: int, width: int) -> Tuple[int, int]
```

Find the logical line containing the given display row.

**Arguments**:

- `display_row` - Display row to find
- `width` - Terminal width
  

**Returns**:

  Tuple of (line_number, row_offset_within_line)

<a id="logloglog.line_index.LineIndex.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Get total number of indexed lines.

<a id="logloglog.widthview"></a>

# logloglog.widthview

WidthView class for viewing logs at a specific terminal width.

<a id="logloglog.widthview.WidthView"></a>

## WidthView Objects

```python
class WidthView()
```

A width-specific view of a LogLogLog using Python container protocols.

<a id="logloglog.widthview.WidthView.__init__"></a>

#### \_\_init\_\_

```python
def __init__(logloglog: "LogLogLog", width: int)
```

Initialize a WidthView.

**Arguments**:

- `logloglog` - The LogLogLog instance to view
- `width` - Terminal width for wrapping

<a id="logloglog.widthview.WidthView.line_at"></a>

#### line\_at

```python
def line_at(row: int) -> Tuple[int, int]
```

Find which logical line contains the given display row.

**Arguments**:

- `row` - Display row number
  

**Returns**:

  Tuple of (line_number, offset_within_line)
  

**Raises**:

- `IndexError` - If row is out of bounds

<a id="logloglog.widthview.WidthView.row_for"></a>

#### row\_for

```python
def row_for(line_no: int) -> int
```

Get the display row where a logical line starts.

**Arguments**:

- `line_no` - Logical line number
  

**Returns**:

  Display row number

<a id="logloglog.widthview.WidthView.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(row_no: int) -> str
```

Get text at display row.

**Arguments**:

- `row_no` - Display row number (negative indexing supported)
  

**Returns**:

  Text at the display row (may be partial line if wrapped)
  

**Raises**:

- `IndexError` - If row_no is out of bounds

<a id="logloglog.widthview.WidthView.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Get total number of display rows.

<a id="logloglog.widthview.WidthView.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__() -> Iterator[str]
```

Iterate over display rows.

<a id="logloglog.ui"></a>

# logloglog.ui

<a id="logloglog.ui.textual.log_widget"></a>

# logloglog.ui.textual.log\_widget

<a id="logloglog.ui.textual.log_widget.LogWidget"></a>

## LogWidget Objects

```python
class LogWidget(ScrollView)
```

A scrollable widget to display log data.

<a id="logloglog.ui.textual.log_widget.LogWidget.LogUpdated"></a>

## LogUpdated Objects

```python
class LogUpdated(Message)
```

Posted when log display updates (scroll, resize, etc).

<a id="logloglog.ui.textual.log_widget.LogWidget.on_mount"></a>

#### on\_mount

```python
def on_mount()
```

Called when widget is mounted.

<a id="logloglog.ui.textual.log_widget.LogWidget.on_resize"></a>

#### on\_resize

```python
def on_resize(event)
```

Called when widget is resized.

<a id="logloglog.ui.textual.log_widget.LogWidget.set_width"></a>

#### set\_width

```python
def set_width(width: int)
```

Update the view width and preserve scroll position.

<a id="logloglog.ui.textual.log_widget.LogWidget.watch_scroll_y"></a>

#### watch\_scroll\_y

```python
def watch_scroll_y(old_value: float, new_value: float) -> None
```

Called when scroll position changes.

<a id="logloglog.ui.textual.log_widget.LogWidget.watch_virtual_size"></a>

#### watch\_virtual\_size

```python
def watch_virtual_size(old_size: Size, new_size: Size) -> None
```

Called when virtual (scrollable) size changes.

<a id="logloglog.ui.textual.log_widget.LogWidget.render_line"></a>

#### render\_line

```python
def render_line(y: int) -> Strip
```

Render a single line of the log.

<a id="logloglog.ui.textual.log_widget.LogWidget.scroll_to"></a>

#### scroll\_to

```python
def scroll_to(x=None, y=None, **kwargs)
```

Override scroll_to to always disable animation.

<a id="logloglog.ui.textual.log_widget.LogWidget.scroll_up"></a>

#### scroll\_up

```python
def scroll_up(**kwargs)
```

Override scroll_up to always disable animation.

<a id="logloglog.ui.textual.log_widget.LogWidget.scroll_down"></a>

#### scroll\_down

```python
def scroll_down(**kwargs)
```

Override scroll_down to always disable animation.

<a id="logloglog.ui.textual.log_widget.LogWidget.start_auto_refresh"></a>

#### start\_auto\_refresh

```python
def start_auto_refresh(interval: float = 1.0)
```

Start background task to automatically refresh log data.

<a id="logloglog.ui.textual.log_widget.LogWidget.stop_auto_refresh"></a>

#### stop\_auto\_refresh

```python
def stop_auto_refresh()
```

Stop the background refresh task.

<a id="logloglog.ui.textual.log_widget.LogWidget.enable_auto_refresh"></a>

#### enable\_auto\_refresh

```python
def enable_auto_refresh(enabled: bool = True)
```

Enable or disable auto-refresh functionality.

<a id="logloglog.ui.textual.log_widget.LogWidget.arefresh_log_data"></a>

#### arefresh\_log\_data

```python
async def arefresh_log_data()
```

Async method to refresh log data without blocking the UI.

<a id="logloglog.ui.textual.log_widget.LogWidget.aset_width"></a>

#### aset\_width

```python
async def aset_width(width: int)
```

Async version of set_width for non-blocking width changes.

<a id="logloglog.ui.textual.log_widget.LogWidget.on_unmount"></a>

#### on\_unmount

```python
def on_unmount()
```

Called when widget is unmounted - cleanup background tasks.

<a id="logloglog.ui.textual.log_widget.LogWidget.action_scroll_home"></a>

#### action\_scroll\_home

```python
def action_scroll_home()
```

Jump to the start of the log.

<a id="logloglog.ui.textual.log_widget.LogWidget.action_scroll_end"></a>

#### action\_scroll\_end

```python
def action_scroll_end()
```

Jump to the end of the log.

<a id="logloglog.ui.textual"></a>

# logloglog.ui.textual

<a id="logloglog.tools.stream_logs"></a>

# logloglog.tools.stream\_logs

Stream system logs for logloglog.

This tool discovers and streams system logs from /var/log, handling both
historical logs (sorted by creation time) and live log following.

<a id="logloglog.tools.stream_logs.discover_historical_logs"></a>

#### discover\_historical\_logs

```python
def discover_historical_logs() -> Iterator[Tuple[float, Path]]
```

Discover all log files in /var/log sorted by creation time.

**Yields**:

  Tuple of (creation_time, filepath) sorted by creation time (oldest first)

<a id="logloglog.tools.stream_logs.discover_live_logs"></a>

#### discover\_live\_logs

```python
def discover_live_logs(last_modified_minutes: int = 60) -> List[Path]
```

Discover .log files that were modified within the last N minutes.

**Arguments**:

- `last_modified_minutes` - Only include files modified within this many minutes
  

**Returns**:

  List of .log file paths

<a id="logloglog.tools.stream_logs.is_text_file"></a>

#### is\_text\_file

```python
def is_text_file(filepath: Path) -> bool
```

Check if a file is a text file using the file command.

**Arguments**:

- `filepath` - Path to check
  

**Returns**:

  True if the file appears to be text

<a id="logloglog.tools.stream_logs.stream_file_content"></a>

#### stream\_file\_content

```python
def stream_file_content(filepath: Path) -> None
```

Stream the content of a file to stdout, handling compression.

**Arguments**:

- `filepath` - File to stream

<a id="logloglog.tools.stream_logs.stream_historical_logs"></a>

#### stream\_historical\_logs

```python
def stream_historical_logs() -> None
```

Stream all historical log files to stdout.

<a id="logloglog.tools.stream_logs.follow_live_logs"></a>

#### follow\_live\_logs

```python
async def follow_live_logs(last_modified_minutes: int = 60) -> None
```

Follow live log files using pure Python implementation.

**Arguments**:

- `last_modified_minutes` - Only follow files modified within this many minutes

<a id="logloglog.tools.stream_logs.tail_multiple_files"></a>

#### tail\_multiple\_files

```python
async def tail_multiple_files(filepaths: List[Path]) -> None
```

Pure Python implementation of tail -F for multiple files.

**Arguments**:

- `filepaths` - List of file paths to tail

<a id="logloglog.tools.stream_logs.setup_signal_handlers"></a>

#### setup\_signal\_handlers

```python
def setup_signal_handlers() -> None
```

Set up clean signal handling.

<a id="logloglog.tools.stream_logs.main"></a>

#### main

```python
async def main() -> None
```

Main entry point.

<a id="logloglog.tools"></a>

# logloglog.tools

Tools subpackage for logloglog utilities.

<a id="logloglog.__main__"></a>

# logloglog.\_\_main\_\_

Entry point for the package

<a id="logloglog.cache"></a>

# logloglog.cache

Cache management for LogLogLog.

<a id="logloglog.cache.Cache"></a>

## Cache Objects

```python
class Cache()
```

Manages cache directories for log files.

<a id="logloglog.cache.Cache.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cache_dir: Path = None)
```

Initialize cache manager.

**Arguments**:

- `cache_dir` - Cache directory (defaults to CACHE_DIR)

<a id="logloglog.cache.Cache.get_dir"></a>

#### get\_dir

```python
def get_dir(path: Path) -> Path
```

Get cache directory for a log file.

**Arguments**:

- `path` - Path to the log file
  

**Returns**:

  Cache directory path
  

**Raises**:

- `OSError` - If file cannot be accessed or cache directory cannot be created

<a id="logloglog.cache.Cache.cleanup"></a>

#### cleanup

```python
def cleanup()
```

Clean up cache directories for files that no longer exist.

<a id="logloglog.log_file"></a>

# logloglog.log\_file

Simple file abstraction for log file operations.

<a id="logloglog.log_file.LogFile"></a>

## LogFile Objects

```python
class LogFile()
```

Simple file abstraction for reading and writing log files.

Keeps file handle open during batch operations for performance.
Call open() to start a batch read session, close() when done.
Individual operations (append, get_size) open/close as needed.

<a id="logloglog.log_file.LogFile.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path: Union[Path, str], mode: str = "r")
```

Initialize LogFile.

**Arguments**:

- `path` - Path to the log file
- `mode` - File mode - "r" for read-only, "a" for append, "w" for write

<a id="logloglog.log_file.LogFile.open"></a>

#### open

```python
def open()
```

Open the file for reading. Call this before batch read operations.

<a id="logloglog.log_file.LogFile.close"></a>

#### close

```python
def close()
```

Close the file handle. Call this after batch operations complete.

<a id="logloglog.log_file.LogFile.read_line"></a>

#### read\_line

```python
def read_line() -> Optional[str]
```

Read the next line from the current position.

**Returns**:

  The next line without trailing newline, or None if no more data.

<a id="logloglog.log_file.LogFile.read_all_lines"></a>

#### read\_all\_lines

```python
def read_all_lines() -> list[str]
```

Read all remaining lines from current position.

**Returns**:

  List of lines without trailing newlines.

<a id="logloglog.log_file.LogFile.append_line"></a>

#### append\_line

```python
def append_line(line: str) -> None
```

Append a line to the file.

**Arguments**:

- `line` - Line to append (newline will be added automatically)
  

**Raises**:

- `IOError` - If file is opened in read-only mode

<a id="logloglog.log_file.LogFile.append_lines"></a>

#### append\_lines

```python
def append_lines(lines: list[str]) -> None
```

Append multiple lines to the file.

**Arguments**:

- `lines` - Lines to append (newlines will be added as needed)

<a id="logloglog.log_file.LogFile.has_more_data"></a>

#### has\_more\_data

```python
def has_more_data() -> bool
```

Check if there's more data available to read.

**Returns**:

  True if file has grown beyond current read position.

<a id="logloglog.log_file.LogFile.get_size"></a>

#### get\_size

```python
def get_size() -> int
```

Get current file size in bytes.

**Returns**:

  File size in bytes, or 0 if file doesn't exist.

<a id="logloglog.log_file.LogFile.seek_to"></a>

#### seek\_to

```python
def seek_to(position: int) -> None
```

Set the read position.

**Arguments**:

- `position` - Byte position to seek to

<a id="logloglog.log_file.LogFile.get_position"></a>

#### get\_position

```python
def get_position() -> int
```

Get current read position.

**Returns**:

  Current byte position for reads.

<a id="logloglog.log_file.LogFile.reset"></a>

#### reset

```python
def reset() -> None
```

Reset read position to beginning of file.

<a id="logloglog.log_file.LogFile.aread_line"></a>

#### aread\_line

```python
async def aread_line() -> Optional[str]
```

Async version of read_line().

<a id="logloglog.log_file.LogFile.aread_all_lines"></a>

#### aread\_all\_lines

```python
async def aread_all_lines() -> list[str]
```

Async version of read_all_lines().

<a id="logloglog.log_file.LogFile.aappend_line"></a>

#### aappend\_line

```python
async def aappend_line(line: str) -> None
```

Async version of append_line().

<a id="logloglog.log_file.LogFile.aappend_lines"></a>

#### aappend\_lines

```python
async def aappend_lines(lines: list[str]) -> None
```

Async version of append_lines().

<a id="logloglog.log_file.LogFile.ahas_more_data"></a>

#### ahas\_more\_data

```python
async def ahas_more_data() -> bool
```

Async version of has_more_data().

<a id="logloglog.log_file.LogFile.aget_size"></a>

#### aget\_size

```python
async def aget_size() -> int
```

Async version of get_size().

<a id="logloglog.logloglog"></a>

# logloglog.logloglog

Main LogLogLog implementation.

<a id="logloglog.logloglog.default_get_width"></a>

#### default\_get\_width

```python
@lru_cache(maxsize=100000)
def default_get_width(line: str) -> int
```

Fast line width calculation with ASCII fast path and caching.

<a id="logloglog.logloglog.default_split_lines"></a>

#### default\_split\_lines

```python
def default_split_lines(text: str) -> List[str]
```

Default line splitting on newlines.

<a id="logloglog.logloglog.LogLogLog"></a>

## LogLogLog Objects

```python
class LogLogLog()
```

Efficient scrollback indexing for large log files.

LogLogLog provides O(log n) seeking through large logs at any terminal width.

<a id="logloglog.logloglog.LogLogLog.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path: Union[Path, str, LogFile],
             get_width: Callable[[str], int] = None,
             split_lines: Callable[[str], List[str]] = None,
             cache: Cache = None,
             defer_indexing: bool = False)
```

Initialize LogLogLog for a file.

**Arguments**:

- `path` - Log file path or LogFile instance
- `get_width` - Function to calculate display width (defaults to wcwidth)
- `split_lines` - Function to split text into lines (defaults to newline split)
- `cache` - Cache instance (auto-created if None)
- `defer_indexing` - If True, skip initial indexing (useful for UI responsiveness)

<a id="logloglog.logloglog.LogLogLog.aopen"></a>

#### aopen

```python
async def aopen()
```

Async version of _open() method for non-blocking file initialization.

<a id="logloglog.logloglog.LogLogLog.close"></a>

#### close

```python
def close()
```

Close all resources.

<a id="logloglog.logloglog.LogLogLog.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__()
```

Context manager entry.

<a id="logloglog.logloglog.LogLogLog.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(exc_type, exc_val, exc_tb)
```

Context manager exit.

<a id="logloglog.logloglog.LogLogLog.update"></a>

#### update

```python
def update()
```

Update index with new lines from the file.

<a id="logloglog.logloglog.LogLogLog.aupdate"></a>

#### aupdate

```python
async def aupdate(progress_callback=None, progress_interval=0.1)
```

Async version of update() method for non-blocking file processing.

**Arguments**:

- `progress_callback` - Optional async callback called periodically during indexing
- `progress_interval` - Seconds between progress callbacks (default 0.1)

<a id="logloglog.logloglog.LogLogLog.append"></a>

#### append

```python
def append(line: str)
```

Append a line to the log file and update index.

**Arguments**:

- `line` - Line to append (newline will be added)
  

**Raises**:

- `IOError` - If LogFile was opened in read-only mode

<a id="logloglog.logloglog.LogLogLog.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(line_no: int) -> str
```

Get a logical line by line number.

<a id="logloglog.logloglog.LogLogLog.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Get total number of logical lines.

<a id="logloglog.logloglog.LogLogLog.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__() -> Iterator[str]
```

Iterate over all logical lines.

<a id="logloglog.logloglog.LogLogLog.width"></a>

#### width

```python
def width(width: int) -> WidthView
```

Create a width-specific view of this log.

**Arguments**:

- `width` - Terminal width for line wrapping
  

**Returns**:

  WidthView instance for this width

<a id="logloglog.logloglog.LogLogLog.get_file_info"></a>

#### get\_file\_info

```python
def get_file_info() -> dict
```

Get information about the log file.

**Returns**:

  Dict with file size, current position, and other metadata.

<a id="logloglog.logloglog.LogLogLog.get_cache_info"></a>

#### get\_cache\_info

```python
def get_cache_info() -> dict
```

Get information about the cache state.

**Returns**:

  Dict with cache directory and status information.

<a id="logloglog.logloglog.LogLogLog.line_at_row"></a>

#### line\_at\_row

```python
def line_at_row(row: int, width: int) -> Tuple[int, int]
```

Find which logical line contains the given display row.

**Arguments**:

- `row` - Display row number
- `width` - Terminal width
  

**Returns**:

  Tuple of (line_number, offset_within_line)

<a id="logloglog.logloglog.LogLogLog.row_for_line"></a>

#### row\_for\_line

```python
def row_for_line(line_no: int, width: int) -> int
```

Get the display row where a logical line starts.

**Arguments**:

- `line_no` - Logical line number
- `width` - Terminal width
  

**Returns**:

  Display row number

<a id="logloglog.logloglog.LogLogLog.total_rows"></a>

#### total\_rows

```python
def total_rows(width: int) -> int
```

Get total number of display rows at given width.

**Arguments**:

- `width` - Terminal width
  

**Returns**:

  Total display rows

