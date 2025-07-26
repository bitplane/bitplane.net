<a id="bittty"></a>

# bittty

bittty: A fast, pure Python terminal emulator library.

bittty (bitplane-tty) is a high-performance terminal emulator engine
that provides comprehensive ANSI sequence parsing and terminal state management.

<a id="bittty.tcaps"></a>

# bittty.tcaps

This module provides access to terminal capabilities from the terminfo database.

<a id="bittty.tcaps.Terminal"></a>

## Terminal Objects

```python
class Terminal()
```

Stores and provides access to a terminal's capabilities from terminfo.

<a id="bittty.tcaps.Terminal.__init__"></a>

#### \_\_init\_\_

```python
def __init__(term_name: str, overrides: str)
```

Initializes the terminal definition.

This loads the capabilities for the given terminal name from the system's
terminfo database and then applies any user-provided overrides.

**Arguments**:

- `term_name` - The terminal name (e.g., "xterm-256color").
- `overrides` - A string of user-defined overrides, like in tmux.conf.

<a id="bittty.tcaps.Terminal.has"></a>

#### has

```python
def has(cap: str) -> bool
```

Checks if the terminal has a given capability.

<a id="bittty.tcaps.Terminal.get_string"></a>

#### get\_string

```python
def get_string(cap: str) -> str
```

Gets a string capability.

This is the primary method for retrieving key codes (e.g., "kcuu1" for
up arrow) to send to the child application.

<a id="bittty.tcaps.Terminal.get_number"></a>

#### get\_number

```python
def get_number(cap: str) -> int
```

Gets a numeric capability.

<a id="bittty.tcaps.Terminal.get_flag"></a>

#### get\_flag

```python
def get_flag(cap: str) -> bool
```

Gets a boolean flag capability.

<a id="bittty.tcaps.Terminal.describe"></a>

#### describe

```python
def describe() -> str
```

Returns a descriptive string of all loaded capabilities for debugging.

<a id="bittty.buffer"></a>

# bittty.buffer

A grid-based terminal buffer.

<a id="bittty.buffer.Buffer"></a>

## Buffer Objects

```python
class Buffer()
```

A 2D grid that stores terminal content.

<a id="bittty.buffer.Buffer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int, height: int) -> None
```

Initialize buffer with given dimensions.

<a id="bittty.buffer.Buffer.get_content"></a>

#### get\_content

```python
def get_content() -> List[List[Cell]]
```

Get buffer content as a 2D grid.

<a id="bittty.buffer.Buffer.get_cell"></a>

#### get\_cell

```python
def get_cell(x: int, y: int) -> Cell
```

Get cell at position.

<a id="bittty.buffer.Buffer.set_cell"></a>

#### set\_cell

```python
def set_cell(x: int, y: int, char: str, ansi_code: str = "") -> None
```

Set a single cell at position.

<a id="bittty.buffer.Buffer.set"></a>

#### set

```python
def set(x: int, y: int, text: str, ansi_code: str = "") -> None
```

Set text at position, overwriting existing content.

<a id="bittty.buffer.Buffer.insert"></a>

#### insert

```python
def insert(x: int, y: int, text: str, ansi_code: str = "") -> None
```

Insert text at position, shifting existing content right.

<a id="bittty.buffer.Buffer.delete"></a>

#### delete

```python
def delete(x: int, y: int, count: int = 1) -> None
```

Delete characters at position.

<a id="bittty.buffer.Buffer.clear_region"></a>

#### clear\_region

```python
def clear_region(x1: int,
                 y1: int,
                 x2: int,
                 y2: int,
                 ansi_code: str = "") -> None
```

Clear a rectangular region.

<a id="bittty.buffer.Buffer.clear_line"></a>

#### clear\_line

```python
def clear_line(y: int,
               mode: int = constants.ERASE_FROM_CURSOR_TO_END,
               cursor_x: int = 0,
               ansi_code: str = "") -> None
```

Clear line content.

<a id="bittty.buffer.Buffer.scroll_up"></a>

#### scroll\_up

```python
def scroll_up(count: int) -> None
```

Scroll content up, removing top lines and adding blank lines at bottom.

<a id="bittty.buffer.Buffer.scroll_down"></a>

#### scroll\_down

```python
def scroll_down(count: int) -> None
```

Scroll content down, removing bottom lines and adding blank lines at top.

<a id="bittty.buffer.Buffer.resize"></a>

#### resize

```python
def resize(width: int, height: int) -> None
```

Resize buffer to new dimensions.

<a id="bittty.buffer.Buffer.get_line_text"></a>

#### get\_line\_text

```python
def get_line_text(y: int) -> str
```

Get plain text content of a line (for debugging/testing).

<a id="bittty.buffer.Buffer.get_line"></a>

#### get\_line

```python
def get_line(y: int,
             width: int = None,
             cursor_x: int = -1,
             cursor_y: int = -1,
             show_cursor: bool = False,
             mouse_x: int = -1,
             mouse_y: int = -1,
             show_mouse: bool = False) -> str
```

Get full ANSI sequence for a line.

<a id="bittty.buffer.Buffer.get_line_tuple"></a>

#### get\_line\_tuple

```python
def get_line_tuple(y: int,
                   width: int = None,
                   cursor_x: int = -1,
                   cursor_y: int = -1,
                   show_cursor: bool = False,
                   mouse_x: int = -1,
                   mouse_y: int = -1,
                   show_mouse: bool = False) -> tuple
```

Get line as a hashable tuple for caching.

<a id="bittty.parser"></a>

# bittty.parser

A state machine for processing terminal input streams.

<a id="bittty.parser.Parser"></a>

## Parser Objects

```python
class Parser()
```

A state machine that parses a stream of terminal control codes.

The parser is always in one of several states (e.g. GROUND, ESCAPE, CSI_ENTRY).
Each byte fed to the `feed()` method can cause a transition to a new
state and/or execute a handler for a recognized escape sequence.

<a id="bittty.parser.Parser.__init__"></a>

#### \_\_init\_\_

```python
def __init__(terminal: Terminal) -> None
```

Initializes the parser state.

**Arguments**:

- `terminal` - A Terminal object that the parser will manipulate.

<a id="bittty.parser.Parser.feed"></a>

#### feed

```python
def feed(data: str) -> None
```

Feeds a chunk of text into the parser.

This is the main entry point. It iterates over the data and passes each
character to the state machine engine.

<a id="bittty.parser.Parser.reset"></a>

#### reset

```python
def reset() -> None
```

Resets the parser to its initial ground state.

<a id="bittty.terminal"></a>

# bittty.terminal

A terminal emulator.

UI frameworks can subclass this to create terminal widgets.

<a id="bittty.terminal.Terminal"></a>

## Terminal Objects

```python
class Terminal()
```

A terminal emulator with process management and screen buffers.

This class handles all terminal logic but has no UI dependencies.
Subclass this to create terminal widgets for specific UI frameworks.

<a id="bittty.terminal.Terminal.get_pty_handler"></a>

#### get\_pty\_handler

```python
@staticmethod
def get_pty_handler(rows: int = constants.DEFAULT_TERMINAL_HEIGHT,
                    cols: int = constants.DEFAULT_TERMINAL_WIDTH)
```

Create a platform-appropriate PTY handler.

<a id="bittty.terminal.Terminal.__init__"></a>

#### \_\_init\_\_

```python
def __init__(command: str = "/bin/bash",
             width: int = 80,
             height: int = 24,
             stdin=None,
             stdout=None) -> None
```

Initialize terminal.

<a id="bittty.terminal.Terminal.set_pty_data_callback"></a>

#### set\_pty\_data\_callback

```python
def set_pty_data_callback(callback: Callable[[str], None]) -> None
```

Set callback for handling PTY data asynchronously.

<a id="bittty.terminal.Terminal.resize"></a>

#### resize

```python
def resize(width: int, height: int) -> None
```

Resize terminal to new dimensions.

<a id="bittty.terminal.Terminal.get_content"></a>

#### get\_content

```python
def get_content()
```

Get current screen content as raw buffer data.

<a id="bittty.terminal.Terminal.capture_pane"></a>

#### capture\_pane

```python
def capture_pane() -> str
```

Capture terminal content.

<a id="bittty.terminal.Terminal.write_text"></a>

#### write\_text

```python
def write_text(text: str, ansi_code: str = "") -> None
```

Write text at cursor position.

<a id="bittty.terminal.Terminal.move_cursor"></a>

#### move\_cursor

```python
def move_cursor(x: Optional[int], y: Optional[int]) -> None
```

Move cursor to position.

<a id="bittty.terminal.Terminal.line_feed"></a>

#### line\_feed

```python
def line_feed(is_wrapped: bool = False) -> None
```

Perform line feed.

<a id="bittty.terminal.Terminal.carriage_return"></a>

#### carriage\_return

```python
def carriage_return() -> None
```

Move cursor to beginning of line.

<a id="bittty.terminal.Terminal.backspace"></a>

#### backspace

```python
def backspace() -> None
```

Move cursor back one position.

<a id="bittty.terminal.Terminal.clear_screen"></a>

#### clear\_screen

```python
def clear_screen(mode: int = constants.ERASE_FROM_CURSOR_TO_END) -> None
```

Clear screen.

<a id="bittty.terminal.Terminal.clear_line"></a>

#### clear\_line

```python
def clear_line(mode: int = constants.ERASE_FROM_CURSOR_TO_END) -> None
```

Clear line.

<a id="bittty.terminal.Terminal.clear_rect"></a>

#### clear\_rect

```python
def clear_rect(x1: int,
               y1: int,
               x2: int,
               y2: int,
               ansi_code: str = "") -> None
```

Clear a rectangular region.

<a id="bittty.terminal.Terminal.alternate_screen_on"></a>

#### alternate\_screen\_on

```python
def alternate_screen_on() -> None
```

Switch to alternate screen.

<a id="bittty.terminal.Terminal.alternate_screen_off"></a>

#### alternate\_screen\_off

```python
def alternate_screen_off() -> None
```

Switch to primary screen.

<a id="bittty.terminal.Terminal.set_mode"></a>

#### set\_mode

```python
def set_mode(mode: int, value: bool = True, private: bool = False) -> None
```

Set terminal mode.

<a id="bittty.terminal.Terminal.clear_mode"></a>

#### clear\_mode

```python
def clear_mode(mode, private: bool = False) -> None
```

Clear terminal mode.

<a id="bittty.terminal.Terminal.switch_screen"></a>

#### switch\_screen

```python
def switch_screen(alt: bool) -> None
```

Switch between primary and alternate screen.

<a id="bittty.terminal.Terminal.set_title"></a>

#### set\_title

```python
def set_title(title: str) -> None
```

Set terminal title.

<a id="bittty.terminal.Terminal.set_icon_title"></a>

#### set\_icon\_title

```python
def set_icon_title(icon_title: str) -> None
```

Set terminal icon title.

<a id="bittty.terminal.Terminal.bell"></a>

#### bell

```python
def bell() -> None
```

Terminal bell.

<a id="bittty.terminal.Terminal.alignment_test"></a>

#### alignment\_test

```python
def alignment_test() -> None
```

Fill the screen with 'E' characters for alignment testing.

<a id="bittty.terminal.Terminal.save_cursor"></a>

#### save\_cursor

```python
def save_cursor() -> None
```

Save cursor position and attributes.

<a id="bittty.terminal.Terminal.restore_cursor"></a>

#### restore\_cursor

```python
def restore_cursor() -> None
```

Restore cursor position and attributes.

<a id="bittty.terminal.Terminal.set_scroll_region"></a>

#### set\_scroll\_region

```python
def set_scroll_region(top: int, bottom: int) -> None
```

Set scroll region.

<a id="bittty.terminal.Terminal.insert_lines"></a>

#### insert\_lines

```python
def insert_lines(count: int) -> None
```

Insert blank lines at cursor position.

<a id="bittty.terminal.Terminal.delete_lines"></a>

#### delete\_lines

```python
def delete_lines(count: int) -> None
```

Delete lines at cursor position.

<a id="bittty.terminal.Terminal.insert_characters"></a>

#### insert\_characters

```python
def insert_characters(count: int, ansi_code: str = "") -> None
```

Insert blank characters at cursor position.

<a id="bittty.terminal.Terminal.delete_characters"></a>

#### delete\_characters

```python
def delete_characters(count: int) -> None
```

Delete characters at cursor position.

<a id="bittty.terminal.Terminal.scroll_up"></a>

#### scroll\_up

```python
def scroll_up(count: int) -> None
```

Scroll content up within scroll region.

<a id="bittty.terminal.Terminal.scroll_down"></a>

#### scroll\_down

```python
def scroll_down(count: int) -> None
```

Scroll content down within scroll region.

<a id="bittty.terminal.Terminal.set_cursor"></a>

#### set\_cursor

```python
def set_cursor(x: Optional[int], y: Optional[int]) -> None
```

Set cursor position (alias for move_cursor).

<a id="bittty.terminal.Terminal.repeat_last_character"></a>

#### repeat\_last\_character

```python
def repeat_last_character(count: int) -> None
```

Repeat the last printed character count times (REP command).

<a id="bittty.terminal.Terminal.input_key"></a>

#### input\_key

```python
def input_key(char: str, modifier: int = constants.KEY_MOD_NONE) -> None
```

Convert key + modifier to standard control codes, then send to input().

<a id="bittty.terminal.Terminal.input_fkey"></a>

#### input\_fkey

```python
def input_fkey(num: int, modifier: int = constants.KEY_MOD_NONE) -> None
```

Convert function key + modifier to standard control codes, then send to input().

<a id="bittty.terminal.Terminal.input"></a>

#### input

```python
def input(data: str) -> None
```

Translate control codes based on terminal modes and send to PTY.

<a id="bittty.terminal.Terminal.input_mouse"></a>

#### input\_mouse

```python
def input_mouse(x: int, y: int, button: int, event_type: str,
                modifiers: set[str]) -> None
```

Handle mouse input, cache position, and send appropriate sequence to PTY.

**Arguments**:

- `x` - 1-based mouse column.
- `y` - 1-based mouse row.
- `button` - The button that was pressed/released.
- `event_type` - "press", "release", or "move".
- `modifiers` - A set of active modifiers ("shift", "meta", "ctrl").

<a id="bittty.terminal.Terminal.start_process"></a>

#### start\_process

```python
async def start_process() -> None
```

Start the child process with PTY or set up stream mode.

<a id="bittty.terminal.Terminal.stop_process"></a>

#### stop\_process

```python
def stop_process() -> None
```

Stop the child process and clean up.

<a id="bittty.constants"></a>

# bittty.constants

Constants for the terminal parser and emulator.

This module contains constants used in the terminal parsing and emulation logic,
following standards like VT100, VT220, and xterm.

<a id="bittty.constants.BEL"></a>

#### BEL

Bell

<a id="bittty.constants.BS"></a>

#### BS

Backspace

<a id="bittty.constants.HT"></a>

#### HT

Horizontal Tab

<a id="bittty.constants.LF"></a>

#### LF

Line Feed

<a id="bittty.constants.CR"></a>

#### CR

Carriage Return

<a id="bittty.constants.ESC"></a>

#### ESC

Escape

<a id="bittty.constants.DEL"></a>

#### DEL

Delete

<a id="bittty.constants.EBADF"></a>

#### EBADF

Bad file descriptor

<a id="bittty.constants.EINVAL"></a>

#### EINVAL

Invalid argument

<a id="bittty.pty_windows"></a>

# bittty.pty\_windows

Windows PTY implementation using pywinpty.

<a id="bittty.pty_windows.WinptyProcessWrapper"></a>

## WinptyProcessWrapper Objects

```python
class WinptyProcessWrapper()
```

Wrapper to provide subprocess.Popen-like interface for winpty PTY.

<a id="bittty.pty_windows.WinptyProcessWrapper.poll"></a>

#### poll

```python
def poll()
```

Check if process is still running.

<a id="bittty.pty_windows.WinptyProcessWrapper.wait"></a>

#### wait

```python
def wait()
```

Wait for process to complete.

<a id="bittty.pty_windows.WinptyProcessWrapper.returncode"></a>

#### returncode

```python
@property
def returncode()
```

Get the return code.

<a id="bittty.pty_windows.WinptyProcessWrapper.pid"></a>

#### pid

```python
@property
def pid()
```

Get the process ID.

<a id="bittty.pty_windows.WindowsPTY"></a>

## WindowsPTY Objects

```python
class WindowsPTY(PTYBase)
```

Windows PTY implementation using pywinpty.

<a id="bittty.pty_windows.WindowsPTY.read"></a>

#### read

```python
def read(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Read data from the PTY.

<a id="bittty.pty_windows.WindowsPTY.write"></a>

#### write

```python
def write(data: str) -> int
```

Write data to the PTY.

<a id="bittty.pty_windows.WindowsPTY.resize"></a>

#### resize

```python
def resize(rows: int, cols: int) -> None
```

Resize the terminal.

<a id="bittty.pty_windows.WindowsPTY.close"></a>

#### close

```python
def close() -> None
```

Close the PTY.

<a id="bittty.pty_windows.WindowsPTY.spawn_process"></a>

#### spawn\_process

```python
def spawn_process(command: str,
                  env: Optional[Dict[str, str]] = None) -> subprocess.Popen
```

Spawn a process attached to this PTY.

<a id="bittty.pty_windows.WindowsPTY.set_nonblocking"></a>

#### set\_nonblocking

```python
def set_nonblocking() -> None
```

Set the PTY to non-blocking mode for async operations.

<a id="bittty.pty_windows.WindowsPTY.read_async"></a>

#### read\_async

```python
async def read_async(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Async read from PTY. Returns empty string when no data available.

<a id="bittty.pty_base"></a>

# bittty.pty\_base

Base PTY interface for terminal emulation.

This module defines the abstract interface that all platform-specific
PTY implementations must follow.

<a id="bittty.pty_base.PTYBase"></a>

## PTYBase Objects

```python
class PTYBase(ABC)
```

Abstract base class for PTY implementations.

<a id="bittty.pty_base.PTYBase.read"></a>

#### read

```python
@abstractmethod
def read(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Read data from the PTY.

<a id="bittty.pty_base.PTYBase.write"></a>

#### write

```python
@abstractmethod
def write(data: str) -> int
```

Write data to the PTY.

<a id="bittty.pty_base.PTYBase.resize"></a>

#### resize

```python
@abstractmethod
def resize(rows: int, cols: int) -> None
```

Resize the terminal.

<a id="bittty.pty_base.PTYBase.close"></a>

#### close

```python
@abstractmethod
def close() -> None
```

Close the PTY.

<a id="bittty.pty_base.PTYBase.closed"></a>

#### closed

```python
@property
def closed() -> bool
```

Check if PTY is closed.

<a id="bittty.pty_base.PTYBase.spawn_process"></a>

#### spawn\_process

```python
@abstractmethod
def spawn_process(command: str,
                  env: Optional[Dict[str, str]] = None) -> subprocess.Popen
```

Spawn a process attached to this PTY.

<a id="bittty.pty_base.PTYBase.set_nonblocking"></a>

#### set\_nonblocking

```python
@abstractmethod
def set_nonblocking() -> None
```

Set the PTY to non-blocking mode for async operations.

<a id="bittty.pty_base.PTYBase.read_async"></a>

#### read\_async

```python
@abstractmethod
async def read_async(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Async read from PTY. Returns empty string when no data available.

<a id="bittty.style"></a>

# bittty.style

Style merging for ANSI escape sequences.

<a id="bittty.style.has_pattern"></a>

#### has\_pattern

```python
@lru_cache(maxsize=20000)
def has_pattern(ansi: str, patterns: tuple) -> bool
```

Check if ANSI sequence contains any of the patterns.

<a id="bittty.style.extract_fg_color"></a>

#### extract\_fg\_color

```python
@lru_cache(maxsize=20000)
def extract_fg_color(ansi: str) -> str
```

Extract foreground color parameter from ANSI sequence.

<a id="bittty.style.extract_bg_color"></a>

#### extract\_bg\_color

```python
@lru_cache(maxsize=20000)
def extract_bg_color(ansi: str) -> str
```

Extract background color parameter from ANSI sequence.

<a id="bittty.style.get_background"></a>

#### get\_background

```python
@lru_cache(maxsize=20000)
def get_background(ansi: str) -> str
```

Get just the background color from an ANSI sequence.

**Arguments**:

- `ansi` - ANSI escape sequence
  

**Returns**:

  ANSI sequence with just the background color, or empty string

<a id="bittty.style.merge_ansi_styles"></a>

#### merge\_ansi\_styles

```python
@lru_cache(maxsize=20000)
def merge_ansi_styles(base: str, new: str) -> str
```

Merge two ANSI style sequences.

<a id="bittty.pty_unix"></a>

# bittty.pty\_unix

Unix/Linux/macOS PTY implementation.

<a id="bittty.pty_unix.UnixPTY"></a>

## UnixPTY Objects

```python
class UnixPTY(PTYBase)
```

Unix/Linux/macOS PTY implementation.

<a id="bittty.pty_unix.UnixPTY.read"></a>

#### read

```python
def read(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Read data from the PTY.

<a id="bittty.pty_unix.UnixPTY.write"></a>

#### write

```python
def write(data: str) -> int
```

Write data to the PTY.

<a id="bittty.pty_unix.UnixPTY.resize"></a>

#### resize

```python
def resize(rows: int, cols: int) -> None
```

Resize the terminal using TIOCSWINSZ ioctl.

<a id="bittty.pty_unix.UnixPTY.close"></a>

#### close

```python
def close() -> None
```

Close the PTY file descriptors.

<a id="bittty.pty_unix.UnixPTY.spawn_process"></a>

#### spawn\_process

```python
def spawn_process(command: str,
                  env: Optional[Dict[str, str]] = None) -> subprocess.Popen
```

Spawn a process attached to this PTY.

<a id="bittty.pty_unix.UnixPTY.set_nonblocking"></a>

#### set\_nonblocking

```python
def set_nonblocking() -> None
```

Set the PTY to non-blocking mode for async operations.

<a id="bittty.pty_unix.UnixPTY.read_async"></a>

#### read\_async

```python
async def read_async(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Async read from PTY. Returns empty string when no data available.

<a id="bittty.color"></a>

# bittty.color

Functions for generating ANSI escape sequences.

<a id="bittty.color.get_color_code"></a>

#### get\_color\_code

```python
@lru_cache(maxsize=1024)
def get_color_code(fg: Optional[int] = None, bg: Optional[int] = None) -> str
```

Generate ANSI color code for 256-color palette.

**Arguments**:

- `fg` - Foreground color (0-255) or None
- `bg` - Background color (0-255) or None
  

**Returns**:

  ANSI escape sequence for the colors

<a id="bittty.color.get_rgb_code"></a>

#### get\_rgb\_code

```python
@lru_cache(maxsize=512)
def get_rgb_code(fg_rgb: Optional[Tuple[int, int, int]] = None,
                 bg_rgb: Optional[Tuple[int, int, int]] = None) -> str
```

Generate ANSI color code for RGB colors.

**Arguments**:

- `fg_rgb` - Foreground RGB tuple (r, g, b) or None
- `bg_rgb` - Background RGB tuple (r, g, b) or None
  

**Returns**:

  ANSI escape sequence for the RGB colors

<a id="bittty.color.get_style_code"></a>

#### get\_style\_code

```python
@lru_cache(maxsize=256)
def get_style_code(bold: bool = False,
                   dim: bool = False,
                   italic: bool = False,
                   underline: bool = False,
                   blink: bool = False,
                   reverse: bool = False,
                   strike: bool = False,
                   conceal: bool = False) -> str
```

Generate ANSI style code for text attributes.

**Returns**:

  ANSI escape sequence for the styles

<a id="bittty.color.get_combined_code"></a>

#### get\_combined\_code

```python
@lru_cache(maxsize=2048)
def get_combined_code(fg: Optional[int] = None,
                      bg: Optional[int] = None,
                      fg_rgb: Optional[Tuple[int, int, int]] = None,
                      bg_rgb: Optional[Tuple[int, int, int]] = None,
                      bold: bool = False,
                      dim: bool = False,
                      italic: bool = False,
                      underline: bool = False,
                      blink: bool = False,
                      reverse: bool = False,
                      strike: bool = False,
                      conceal: bool = False) -> str
```

Generate a combined ANSI code for colors and styles.

RGB colors take precedence over palette colors.

**Returns**:

  Complete ANSI escape sequence or empty string

<a id="bittty.color.reset_code"></a>

#### reset\_code

```python
@lru_cache(maxsize=1)
def reset_code() -> str
```

Get the ANSI reset code.

<a id="bittty.color.get_basic_color_code"></a>

#### get\_basic\_color\_code

```python
@lru_cache(maxsize=16)
def get_basic_color_code(color: int, is_bg: bool = False) -> str
```

Generate ANSI code for basic 16 colors (0-15).

**Arguments**:

- `color` - Color index (0-7 for normal, 8-15 for bright)
- `is_bg` - True for background, False for foreground
  

**Returns**:

  ANSI escape sequence

<a id="bittty.color.get_cursor_code"></a>

#### get\_cursor\_code

```python
@lru_cache(maxsize=1)
def get_cursor_code() -> str
```

Get ANSI code for cursor display (reverse video).

<a id="bittty.color.get_clear_line_code"></a>

#### get\_clear\_line\_code

```python
@lru_cache(maxsize=1)
def get_clear_line_code() -> str
```

Get ANSI code to clear to end of line.

<a id="bittty.color.reset_foreground_code"></a>

#### reset\_foreground\_code

```python
@lru_cache(maxsize=1)
def reset_foreground_code() -> str
```

Get ANSI code to reset foreground color only.

<a id="bittty.color.reset_background_code"></a>

#### reset\_background\_code

```python
@lru_cache(maxsize=1)
def reset_background_code() -> str
```

Get ANSI code to reset background color only.

<a id="bittty.color.reset_text_attributes"></a>

#### reset\_text\_attributes

```python
@lru_cache(maxsize=1)
def reset_text_attributes() -> str
```

Reset text attributes but preserve background color.

