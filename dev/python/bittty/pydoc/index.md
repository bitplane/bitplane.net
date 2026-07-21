<a id="bittty"></a>

# bittty

bittty: A fast, pure Python terminal emulator library.

bittty (bitplane-tty) is a high-performance terminal emulator engine
that provides comprehensive ANSI sequence parsing and terminal state management.

Vocabulary: the `Board` is the machine (devices, registers, video memory, the
child process). A terminal (bittty.terminals) is the chrome a human looks at,
plugged into the board's display port. `Terminal` is deliberately not exported
here — import it from bittty.terminals.

<a id="bittty.terminals.probe"></a>

# bittty.terminals.probe

Capability probing for the stdio terminal.

Ask the real outer terminal what it can do, then hand a TerminalCaps up to the
backend. Uses a DA1-terminated handshake: fire all the queries plus a Primary DA
request, then read until the (universally answered) DA reply arrives, so optional
queries that go unanswered never make us hang. Non-tty or timeout ⇒ env/config
caps only.

Nothing here reads capabilities the backend then trusts blindly — TerminalCaps is
purely physical facts (colour depth, pixel geometry, background). Graphics-mode
reconciliation is deferred with the graphics families.

<a id="bittty.terminals.probe.color_depth_from_env"></a>

#### color\_depth\_from\_env

```python
def color_depth_from_env(env) -> str
```

Best-effort colour depth from COLORTERM / TERM (no query exists for this).

<a id="bittty.terminals.probe.parse_probe_replies"></a>

#### parse\_probe\_replies

```python
def parse_probe_replies(buf: str, env) -> TerminalCaps
```

Build TerminalCaps from a probe-reply buffer, unioned with env (probe wins).

<a id="bittty.terminals.probe.probe_caps"></a>

#### probe\_caps

```python
def probe_caps(stdin_fd,
               write,
               env=None,
               timeout: float = 0.5) -> TerminalCaps
```

Query the real terminal and return TerminalCaps; env-only on a non-tty/timeout.

`write` is a callable that writes a str to the outer terminal (and flushes).

<a id="bittty.terminals.base"></a>

# bittty.terminals.base

The Terminal abstract base: the chrome a human looks at.

A concrete terminal *is-a* Terminal and *has-a* Board (composition). It plugs
itself into the board's display port, pushes TerminalCaps up, and receives
discrete side-effects through present(), which dispatches each PresentEvent to
a typed hook. Every hook defaults to a no-op, so adding a new event type can
never break an existing terminal — it just grows the surface with another
optional override.

The board never imports this module: the boundary only ever runs
terminal -> board, never the reverse.

<a id="bittty.terminals.base.Terminal"></a>

## Terminal Objects

```python
class Terminal()
```

Abstract base for terminals (chrome). Compose a Board; override the hooks you need.

<a id="bittty.terminals.base.Terminal.attach"></a>

#### attach

```python
def attach() -> None
```

Plug this terminal into its board's display port.

<a id="bittty.terminals.base.Terminal.detach"></a>

#### detach

```python
def detach() -> None
```

Unplug from the board's display port.

<a id="bittty.terminals.base.Terminal.set_caps"></a>

#### set\_caps

```python
def set_caps(caps: TerminalCaps) -> None
```

Push the real terminal's capabilities down to the board.

<a id="bittty.terminals.base.Terminal.present"></a>

#### present

```python
def present(event: PresentEvent) -> None
```

Route a present event to its typed hook (unknown types are ignored).

<a id="bittty.terminals.stdio"></a>

# bittty.terminals.stdio

StdioTerminal: the reference terminal, whose venue is this process's stdio.

Composes a Board (never subclasses it) and drives the real outer terminal:
raw-mode stdin, ANSI rendering to stdout, resize handling, and mouse mirroring.
Discrete side-effects arrive through the Terminal hooks (on_bell/on_title/
on_mouse_mode).

<a id="bittty.terminals.stdio.HostInputSink"></a>

## HostInputSink Objects

```python
class HostInputSink()
```

Sink for the input-direction parser: host bytes in, board events out.

Every operation carries its raw bytes, so anything we don't intercept is
forwarded to the child verbatim and in order — arrow keys, control chars,
pastes, whole unknown sequences. Interception is by raw prefix, not
operation name: on the input direction CSI I is a focus report, never CHT.

<a id="bittty.terminals.stdio.StdioTerminal"></a>

## StdioTerminal Objects

```python
class StdioTerminal(Terminal)
```

Render a bittty Board to the real terminal this program is running in.

<a id="bittty.terminals.stdio.StdioTerminal.get_default_shell"></a>

#### get\_default\_shell

```python
def get_default_shell() -> str
```

Get the default shell command for the current platform.

<a id="bittty.terminals.stdio.StdioTerminal.on_bell"></a>

#### on\_bell

```python
def on_bell() -> None
```

Ring the outer terminal's bell.

<a id="bittty.terminals.stdio.StdioTerminal.on_title"></a>

#### on\_title

```python
def on_title(title: str, icon_title: str) -> None
```

Mirror the window title onto the outer terminal.

<a id="bittty.terminals.stdio.StdioTerminal.on_mouse_mode"></a>

#### on\_mouse\_mode

```python
def on_mouse_mode(mode: str, sgr: bool) -> None
```

Mirror the child's requested mouse-tracking mode onto the outer terminal.

<a id="bittty.terminals.stdio.StdioTerminal.disable_host_mouse"></a>

#### disable\_host\_mouse

```python
def disable_host_mouse() -> None
```

Turn off host-terminal mouse reporting.

<a id="bittty.terminals.stdio.StdioTerminal.setup_terminal"></a>

#### setup\_terminal

```python
def setup_terminal() -> None
```

Put the host terminal into raw mode, clear it, and ask for focus events.

<a id="bittty.terminals.stdio.StdioTerminal.restore_terminal"></a>

#### restore\_terminal

```python
def restore_terminal() -> None
```

Restore the host terminal to its original state.

<a id="bittty.terminals.stdio.StdioTerminal.probe_capabilities"></a>

#### probe\_capabilities

```python
def probe_capabilities() -> None
```

Ask the outer terminal what it can do and push TerminalCaps to the backend.

<a id="bittty.terminals.stdio.StdioTerminal.render_screen"></a>

#### render\_screen

```python
def render_screen() -> None
```

Render the current board state to stdout, then place the host's hardware cursor.

The cursor is the host terminal's own: position it and show it when the
child wants it visible (DECTCEM). The host hollows it on unfocus by
itself, exactly like a real terminal.

<a id="bittty.terminals.stdio.StdioTerminal.handle_pty_data"></a>

#### handle\_pty\_data

```python
def handle_pty_data(data: str) -> None
```

Feed child output into the emulator and mark the screen dirty.

Rendering happens on the run loop's tick, not per PTY chunk — a repaint
per chunk backpressures a flooding child (it blocks writing to the PTY
while we paint), turning a 66ms `find` into a 750ms one.

<a id="bittty.terminals.stdio.StdioTerminal.handle_sgr_mouse_sequence"></a>

#### handle\_sgr\_mouse\_sequence

```python
def handle_sgr_mouse_sequence(sequence: str) -> bool
```

Parse a host SGR mouse report and re-inject it through bittty.

<a id="bittty.terminals.stdio.StdioTerminal.handle_focus"></a>

#### handle\_focus

```python
def handle_focus(focused: bool) -> None
```

A host focus event: the backend owns the state; we just repaint.

<a id="bittty.terminals.stdio.StdioTerminal.handle_input"></a>

#### handle\_input

```python
def handle_input(data: str) -> None
```

Feed host input through the input-direction parser.

The parser reassembles sequences split across reads; HostInputSink
intercepts SGR mouse reports and focus events and forwards everything
else to the child verbatim.

<a id="bittty.terminals.stdio.StdioTerminal.flush_pending_input"></a>

#### flush\_pending\_input

```python
def flush_pending_input() -> None
```

Release a held incomplete sequence that never completed.

A lone ESC keypress looks like a sequence prefix, so the parser holds
it; when no follow-up arrives within an input-loop tick it was a real
ESC and must reach the child.

<a id="bittty.terminals.stdio.StdioTerminal.handle_resize"></a>

#### handle\_resize

```python
def handle_resize() -> None
```

Re-read the host size and resize the emulator (called from a SIGWINCH handler).

<a id="bittty.terminals.stdio.StdioTerminal.input_loop"></a>

#### input\_loop

```python
async def input_loop() -> None
```

Read host input and forward it.

<a id="bittty.terminals.stdio.StdioTerminal.run"></a>

#### run

```python
async def run() -> None
```

Main loop: start the shell, pump input, render until it exits.

<a id="bittty.terminals.stdio.StdioTerminal.cleanup"></a>

#### cleanup

```python
def cleanup() -> None
```

Tear down the child and restore the host terminal.

<a id="bittty.terminals"></a>

# bittty.terminals

Terminals: the chrome a human looks at, named by venue.

Kept in its own package so the board never imports terminal code —
the "board is never subclassed by a terminal" rule, enforced structurally.

<a id="bittty.video"></a>

# bittty.video

Video memory: the 2D cell grid the blitter writes and terminals render.

A Board has two pages of it (primary and alternate).

<a id="bittty.video.Video"></a>

## Video Objects

```python
class Video()
```

A 2D grid that stores terminal content.

<a id="bittty.video.Video.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int, height: int) -> None
```

Initialize buffer with given dimensions.

<a id="bittty.video.Video.observe"></a>

#### observe

```python
def observe() -> int
```

Snapshot for dirty tracking: close the current epoch, open a new one.

Returns the new epoch; rows stamped at or after it are dirty relative
to this observation. Each reader keeps its own returned value.

<a id="bittty.video.Video.dirty_rows"></a>

#### dirty\_rows

```python
def dirty_rows(seen: int) -> List[int]
```

Rows changed since `seen` (a value returned by observe()).

<a id="bittty.video.Video.set_line_attribute"></a>

#### set\_line\_attribute

```python
def set_line_attribute(y: int, attribute: str) -> None
```

Set a line's DECDHL/DECDWL/DECSWL attribute.

<a id="bittty.video.Video.get_line_attribute"></a>

#### get\_line\_attribute

```python
def get_line_attribute(y: int) -> str
```

Return a line's width/height attribute (single by default).

<a id="bittty.video.Video.reset_line_attributes"></a>

#### reset\_line\_attributes

```python
def reset_line_attributes() -> None
```

Return every line to single-width, single-height (RIS).

<a id="bittty.video.Video.get_content"></a>

#### get\_content

```python
def get_content() -> List[List[Cell]]
```

Get buffer content as a 2D grid.

<a id="bittty.video.Video.get_cell"></a>

#### get\_cell

```python
def get_cell(x: int, y: int) -> Cell
```

Get cell at position.

<a id="bittty.video.Video.set_cell"></a>

#### set\_cell

```python
def set_cell(x: int, y: int, char: str, style_or_ansi=None) -> None
```

Set a single cell at position.

**Arguments**:

  x, y: Position
- `char` - Character to store
- `style_or_ansi` - Either a Style object or ANSI string (for backward compatibility)

<a id="bittty.video.Video.set"></a>

#### set

```python
def set(x: int, y: int, text: str, style_or_ansi=None) -> None
```

Set text at position, overwriting existing content.

<a id="bittty.video.Video.insert"></a>

#### insert

```python
def insert(x: int, y: int, text: str, style_or_ansi=None) -> None
```

Insert text at position, shifting existing content right.

<a id="bittty.video.Video.delete"></a>

#### delete

```python
def delete(x: int, y: int, count: int = 1) -> None
```

Delete characters at position.

<a id="bittty.video.Video.clear_region"></a>

#### clear\_region

```python
def clear_region(x1: int,
                 y1: int,
                 x2: int,
                 y2: int,
                 style_or_ansi=None) -> None
```

Clear a rectangular region.

<a id="bittty.video.Video.clear_line"></a>

#### clear\_line

```python
def clear_line(y: int,
               mode: int = constants.ERASE_FROM_CURSOR_TO_END,
               cursor_x: int = 0,
               style_or_ansi=None) -> None
```

Clear line content.

<a id="bittty.video.Video.scroll_up"></a>

#### scroll\_up

```python
def scroll_up(count: int) -> None
```

Scroll content up, removing top lines and adding blank lines at bottom.

<a id="bittty.video.Video.scroll_down"></a>

#### scroll\_down

```python
def scroll_down(count: int) -> None
```

Scroll content down, removing bottom lines and adding blank lines at top.

<a id="bittty.video.Video.scroll_region_up"></a>

#### scroll\_region\_up

```python
def scroll_region_up(top: int, bottom: int, count: int) -> None
```

Scroll a specific region up by count lines. BLAZING FAST bulk operation!

<a id="bittty.video.Video.scroll_region_down"></a>

#### scroll\_region\_down

```python
def scroll_region_down(top: int, bottom: int, count: int) -> None
```

Scroll a specific region down by count lines. BLAZING FAST bulk operation!

<a id="bittty.video.Video.resize"></a>

#### resize

```python
def resize(width: int, height: int) -> None
```

Resize buffer to new dimensions.

<a id="bittty.video.Video.link_extent"></a>

#### link\_extent

```python
def link_extent(x: int, y: int) -> tuple | None
```

The contiguous same-link run containing (x, y) on its row.

Returns (uri, link_id, x0, x1) with an inclusive column span, or None
if the cell isn't a link. Segments split across rows share a link_id;
grouping those into one hover is the chrome's job.

<a id="bittty.video.Video.get_line_text"></a>

#### get\_line\_text

```python
def get_line_text(y: int) -> str
```

Get plain text content of a line (for debugging/testing).

<a id="bittty.video.Video.get_line"></a>

#### get\_line

```python
def get_line(y: int, width: int = None) -> str
```

Get full ANSI sequence for a line — a pure read of video memory.

No cursor or pointer is composited in; those are chrome concerns,
rendered by the terminal from the board's registers.

<a id="bittty.video.Video.get_line_tuple"></a>

#### get\_line\_tuple

```python
def get_line_tuple(y: int, width: int = None) -> tuple
```

Get line as a hashable tuple for caching — a pure read of video memory.

<a id="bittty.connections"></a>

# bittty.connections

Connections and the board-side ports they plug into.

A port is a jack on the board, and both are full-duplex. The host port carries
bytes both ways (a serial line: PTY, pipe, socket). The display port carries
typed events both ways: present events down to the terminal (chrome), input
events up from it.

<a id="bittty.connections.Connection"></a>

## Connection Objects

```python
@runtime_checkable
class Connection(Protocol)
```

A cable implementation (PTY, pipe, socket) that accepts terminal input/reply data.

<a id="bittty.connections.Connection.write"></a>

#### write

```python
def write(data: str)
```

Write data to the connected host.

<a id="bittty.connections.Presentable"></a>

## Presentable Objects

```python
@runtime_checkable
class Presentable(Protocol)
```

A terminal (chrome) that receives discrete present events from the board.

<a id="bittty.connections.Presentable.present"></a>

#### present

```python
def present(event: "PresentEvent") -> None
```

Handle one present event.

<a id="bittty.connections.HostPort"></a>

## HostPort Objects

```python
class HostPort()
```

The board's jack toward the child program; a Connection (PTY, pipe) plugs in.

Full duplex: write() is the transmit pin (replies and encoded input toward
the child); connect() starts the receive pump, feeding the child's output
into a sink — the board wires it to its parser.

<a id="bittty.connections.HostPort.attach"></a>

#### attach

```python
def attach(connection: Connection) -> None
```

Attach a connection to this host port (transmit side only).

<a id="bittty.connections.HostPort.detach"></a>

#### detach

```python
def detach() -> None
```

Detach the current connection.

<a id="bittty.connections.HostPort.connect"></a>

#### connect

```python
def connect(connection: Connection,
            on_data: Callable[[str], None],
            on_idle: Optional[Callable[[], bool]] = None,
            on_closed: Optional[Callable[[], None]] = None) -> None
```

Plug in a duplex connection and start pumping its receive side.

on_data receives each decoded chunk. on_idle fires when a read returns
nothing — return True to stop the pump (the board reaps its dead child
there). on_closed fires when the connection errors out.

<a id="bittty.connections.HostPort.disconnect"></a>

#### disconnect

```python
def disconnect() -> None
```

Stop the receive pump and unplug the connection.

<a id="bittty.connections.HostPort.connected"></a>

#### connected

```python
@property
def connected() -> bool
```

Whether a connection is attached.

<a id="bittty.connections.HostPort.write"></a>

#### write

```python
def write(data: str, flush: bool = False)
```

Write data to the attached connection.

<a id="bittty.connections.DisplayPort"></a>

## DisplayPort Objects

```python
class DisplayPort()
```

The board's jack toward the terminal (chrome); mirrors HostPort.

The name is the video-connector pun, kept on purpose: the one place
"display" survives in board vocabulary. Full duplex: the board pushes
discrete present events down; the terminal sends input events, focus
changes, and capability reports up. When no terminal is attached
present() is a no-op, so the board runs headless exactly as before.

<a id="bittty.connections.DisplayPort.attach"></a>

#### attach

```python
def attach(terminal: Presentable) -> None
```

Attach a terminal (chrome) to receive present events.

<a id="bittty.connections.DisplayPort.detach"></a>

#### detach

```python
def detach() -> None
```

Detach the current terminal.

<a id="bittty.connections.DisplayPort.connected"></a>

#### connected

```python
@property
def connected() -> bool
```

Whether a terminal (chrome) is attached.

<a id="bittty.connections.DisplayPort.present"></a>

#### present

```python
def present(event: "PresentEvent") -> None
```

Forward a present event to the attached terminal, if any.

<a id="bittty.connections.DisplayPort.input"></a>

#### input

```python
def input(data: str) -> None
```

Keystrokes from the terminal, translated per keyboard modes.

<a id="bittty.connections.DisplayPort.input_key"></a>

#### input\_key

```python
def input_key(char: str, modifier: int = constants.KEY_MOD_NONE) -> None
```

A key + modifier from the terminal.

<a id="bittty.connections.DisplayPort.input_fkey"></a>

#### input\_fkey

```python
def input_fkey(num: int, modifier: int = constants.KEY_MOD_NONE) -> None
```

A function key + modifier from the terminal.

<a id="bittty.connections.DisplayPort.input_numpad_key"></a>

#### input\_numpad\_key

```python
def input_numpad_key(key: str) -> None
```

A numpad key from the terminal.

<a id="bittty.connections.DisplayPort.input_mouse"></a>

#### input\_mouse

```python
def input_mouse(x: int, y: int, button: int, event_type: str,
                modifiers: set[str]) -> None
```

A mouse event from the terminal.

<a id="bittty.connections.DisplayPort.focus_in"></a>

#### focus\_in

```python
def focus_in() -> None
```

The box gained focus.

<a id="bittty.connections.DisplayPort.focus_out"></a>

#### focus\_out

```python
def focus_out() -> None
```

The box lost focus.

<a id="bittty.connections.DisplayPort.set_caps"></a>

#### set\_caps

```python
def set_caps(caps: "TerminalCaps") -> None
```

The terminal reports what its venue can do.

<a id="bittty.parser.dcs"></a>

# bittty.parser.dcs

DCS (Device Control String) operation parser.

<a id="bittty.parser.dcs.parse_dcs_operation"></a>

#### parse\_dcs\_operation

```python
def parse_dcs_operation(string_buffer: str, raw: str = "") -> Operation
```

Return an operation for a DCS sequence.

<a id="bittty.parser.csi"></a>

# bittty.parser.csi

CSI (Control Sequence Introducer) operation parser.

<a id="bittty.parser.csi.param"></a>

#### param

```python
def param(params, index=0, default=None)
```

Return params[index] when present and not None, else default.

<a id="bittty.parser.csi.parse_csi_params"></a>

#### parse\_csi\_params

```python
@lru_cache(maxsize=1000)
def parse_csi_params(data)
```

Parse CSI parameters when actually needed.

**Arguments**:

- `data` - Complete CSI sequence like '[1;2H' or '[?25h'
  

**Returns**:

- `tuple` - (params_list, intermediate_chars, final_char)

<a id="bittty.parser.csi.parse_csi_operation"></a>

#### parse\_csi\_operation

```python
@lru_cache(maxsize=4096)
def parse_csi_operation(raw_csi_data: str) -> Operation | None
```

Return a semantic operation for CSI sequences migrated to the operation layer.

Cached: real terminal traffic repeats a small CSI vocabulary (a full-screen
TUI session uses a few hundred distinct sequences), and Operation is frozen
with immutable args, so one instance per distinct sequence is safe to share.

<a id="bittty.parser.osc"></a>

# bittty.parser.osc

OSC (Operating System Command) operation parser.

<a id="bittty.parser.osc.parse_osc_operation"></a>

#### parse\_osc\_operation

```python
def parse_osc_operation(string_buffer: str, raw: str = "") -> Operation | None
```

Return a semantic operation for an OSC sequence.

<a id="bittty.parser.core"></a>

# bittty.parser.core

Core Parser class with state machine and sequence dispatching (fast state-specific scanners).

<a id="bittty.parser.core.parse_string_sequence"></a>

#### parse\_string\_sequence

```python
@lru_cache(maxsize=300)
def parse_string_sequence(data: str, sequence_type: str) -> str
```

Strip prefix and terminator for OSC/DCS/APC/PM/SOS.

<a id="bittty.parser.core.Parser"></a>

## Parser Objects

```python
class Parser()
```

State machine: GROUND → (CSI | STRING[osc|dcs|apc|pm|sos]) → GROUND
Uses small, state-specific scanners for speed.

<a id="bittty.parser.core.Parser.flush_trailing"></a>

#### flush\_trailing

```python
def flush_trailing() -> None
```

Emit any held incomplete sequence as plain text and reset to ground.

For an input-direction parser: a lone ESC (or a dangling introducer)
that never completed within the caller's patience was a keypress, not
a sequence prefix, and must reach the sink as-is. Never called on the
output direction, where waiting for the rest of the sequence is right.

<a id="bittty.parser.escape"></a>

# bittty.parser.escape

Simple escape sequence operation parser.

<a id="bittty.parser.escape.parse_escape_operation"></a>

#### parse\_escape\_operation

```python
def parse_escape_operation(data: str) -> Operation | None
```

Return a semantic operation for a simple ESC sequence.

<a id="bittty.parser.escape.parse_hash_operation"></a>

#### parse\_hash\_operation

```python
def parse_hash_operation(data: str) -> Operation | None
```

Return a semantic operation for an ESC # n line-size / alignment sequence.

<a id="bittty.parser.escape.parse_charset_operation"></a>

#### parse\_charset\_operation

```python
def parse_charset_operation(data: str) -> Operation | None
```

Return a semantic operation for a charset designation sequence.

<a id="bittty.parser"></a>

# bittty.parser

Parser module for terminal escape sequence processing.

This module provides a modular parser system that processes terminal escape sequences
through specialized handlers:

- CSI sequences (cursor movement, styling, modes)
- OSC sequences (window titles, colors)
- Simple escape sequences (cursor save/restore, etc.)
- DCS sequences (device control strings)

The main Parser class coordinates all these handlers and maintains the state machine.

<a id="bittty.operations"></a>

# bittty.operations

Parser operation model.

<a id="bittty.operations.Operation"></a>

## Operation Objects

```python
@dataclass(frozen=True)
class Operation()
```

A parsed terminal operation.

<a id="bittty.operations.OperationSink"></a>

## OperationSink Objects

```python
class OperationSink(Protocol)
```

Receives operations emitted by the parser.

<a id="bittty.operations.OperationSink.handle_operation"></a>

#### handle\_operation

```python
def handle_operation(operation: Operation) -> None
```

Handle one parsed operation.

<a id="bittty.operations.control_name"></a>

#### control\_name

```python
def control_name(ch: str) -> str
```

Return a stable operation name for a C0 control character.

<a id="bittty.keymap"></a>

# bittty.keymap

Keyboard encoding as model data.

Function keys are where real terminals diverge most: a VT100 has only PF1-PF4
and no keyboard-modifier encoding, while xterm sends F1-F12 and folds shift/alt/
ctrl into a ``;mod`` parameter. A `KeyMap` captures that difference as data.

<a id="bittty.keymap.KeyMap"></a>

## KeyMap Objects

```python
@dataclass(frozen=True)
class KeyMap()
```

How a terminal encodes its keys (and whether it encodes modifiers).

<a id="bittty.keymap.KeyMap.cursor_keys"></a>

#### cursor\_keys

"up"/"down"/"left"/"right" -> CSI/SS3 final byte

<a id="bittty.keymap.KeyMap.nav_keys"></a>

#### nav\_keys

"home"/"end"/... -> CSI body

<a id="bittty.keymap.KeyMap.modifiers"></a>

#### modifiers

whether shift/alt/ctrl are folded into the sequence

<a id="bittty.keymap.apply_modifier"></a>

#### apply\_modifier

```python
def apply_modifier(sequence: str, modifier: int) -> str
```

Fold an xterm-style modifier into a function-key sequence.

``ESC O X`` becomes ``ESC [ 1 ; mod X``; ``ESC [ n ~`` becomes ``ESC [ n ; mod ~``.

<a id="bittty.model"></a>

# bittty.model

Terminal models: the emulation profile as data.

A model captures the constants that distinguish one real terminal from
another — starting with the Device Attributes (DA) responses used to identify
the terminal to the host. Over time this grows to carry charset repertoire,
colour depth, and which capabilities a board assembles.

<a id="bittty.model.Model"></a>

## Model Objects

```python
@dataclass(frozen=True)
class Model()
```

A terminal type expressed as data.

<a id="bittty.model.Model.da1_response"></a>

#### da1\_response

Primary Device Attributes (answer to CSI c)

<a id="bittty.model.Model.da2_response"></a>

#### da2\_response

Secondary DA (CSI > c); None if unsupported

<a id="bittty.model.Model.da3_response"></a>

#### da3\_response

Tertiary DA (CSI = c); None if unsupported

<a id="bittty.model.get_model"></a>

#### get\_model

```python
def get_model(term_name: str | None, default: Model = DEFAULT) -> Model
```

Resolve a $TERM name to a model, falling back through shorter prefixes.

So "xterm-kitty" or "screen.xterm-256color" degrade gracefully to the nearest
known family, and an unknown or empty TERM yields the default (xterm).

<a id="bittty.pty.base"></a>

# bittty.pty.base

Base PTY interface for terminal emulation.

This module provides a concrete base class that works with file-like objects,
with platform-specific subclasses overriding only the byte-level I/O methods.

<a id="bittty.pty.base.PTY"></a>

## PTY Objects

```python
class PTY()
```

A generic PTY that lacks OS integration.

Uses StringIO if no file handles are provided, and subprocess to handle its
children.

If you use this then you'll have to

<a id="bittty.pty.base.PTY.__init__"></a>

#### \_\_init\_\_

```python
def __init__(from_process: Optional[BinaryIO] = None,
             to_process: Optional[BinaryIO] = None,
             rows: int = constants.DEFAULT_TERMINAL_HEIGHT,
             cols: int = constants.DEFAULT_TERMINAL_WIDTH)
```

Initialize PTY with file-like input/output sources.

**Arguments**:

- `from_process` - File-like object to read process output from (or None)
- `to_process` - File-like object to write user input to (or None)
- `rows` - Terminal height
- `cols` - Terminal width

<a id="bittty.pty.base.PTY.read_bytes"></a>

#### read\_bytes

```python
def read_bytes(size: int) -> bytes
```

Read raw bytes. Override in subclasses for platform-specific I/O.

<a id="bittty.pty.base.PTY.write_bytes"></a>

#### write\_bytes

```python
def write_bytes(data: bytes) -> int
```

Write raw bytes. Override in subclasses for platform-specific I/O.

<a id="bittty.pty.base.PTY.read"></a>

#### read

```python
def read(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Read data using the C incremental UTF-8 decoder (buffers split code points).

<a id="bittty.pty.base.PTY.write"></a>

#### write

```python
def write(data: str) -> int
```

Write string as UTF-8 bytes.

<a id="bittty.pty.base.PTY.resize"></a>

#### resize

```python
def resize(rows: int, cols: int) -> None
```

Resize the terminal (base implementation just updates dimensions).

<a id="bittty.pty.base.PTY.close"></a>

#### close

```python
def close() -> None
```

Close the PTY streams.

<a id="bittty.pty.base.PTY.closed"></a>

#### closed

```python
@property
def closed() -> bool
```

Check if PTY is closed.

<a id="bittty.pty.base.PTY.spawn_process"></a>

#### spawn\_process

```python
def spawn_process(command: str, env: dict[str, str] = ENV) -> subprocess.Popen
```

Spawn a process connected to PTY streams.

<a id="bittty.pty.base.PTY.read_async"></a>

#### read\_async

```python
async def read_async(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Async read using thread pool executor.

Uses loop.run_in_executor() as a generic cross-platform approach.
Unix PTY overrides this with more efficient file descriptor monitoring.
Windows and other platforms use this thread pool implementation.

<a id="bittty.pty.base.PTY.flush"></a>

#### flush

```python
def flush() -> None
```

Flush output.

<a id="bittty.pty.unix"></a>

# bittty.pty.unix

Unix/Linux/macOS PTY implementation.

<a id="bittty.pty.unix.UnixPTY"></a>

## UnixPTY Objects

```python
class UnixPTY(PTY)
```

Unix/Linux/macOS PTY implementation.

<a id="bittty.pty.unix.UnixPTY.resize"></a>

#### resize

```python
def resize(rows: int, cols: int) -> None
```

Resize the terminal using TIOCSWINSZ ioctl.

<a id="bittty.pty.unix.UnixPTY.close"></a>

#### close

```python
def close() -> None
```

Close the PTY file descriptors.

<a id="bittty.pty.unix.UnixPTY.spawn_process"></a>

#### spawn\_process

```python
def spawn_process(command: str,
                  env: dict[str, str] = UNIX_ENV) -> subprocess.Popen
```

Spawn a process attached to this PTY.

<a id="bittty.pty.unix.UnixPTY.flush"></a>

#### flush

```python
def flush() -> None
```

PTY master file descriptors don't support fsync - data flows immediately.

For Unix PTYs, data written to the master side appears immediately
on the slave side, so no explicit flushing is needed.

<a id="bittty.pty.unix.UnixPTY.read_async"></a>

#### read\_async

```python
async def read_async(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Async read from PTY using efficient file descriptor monitoring.

Uses loop.add_reader() with file descriptors for maximum efficiency on Unix.
This is the most performant approach since Unix supports select/poll on PTY fds.

<a id="bittty.pty.windows"></a>

# bittty.pty.windows

Windows PTY implementation using pywinpty.

<a id="bittty.pty.windows.WinptyFileWrapper"></a>

## WinptyFileWrapper Objects

```python
class WinptyFileWrapper()
```

File-like wrapper for winpty.PTY to work with base PTY class.

<a id="bittty.pty.windows.WinptyFileWrapper.read"></a>

#### read

```python
def read(size: int = -1) -> str
```

Read data as strings.

<a id="bittty.pty.windows.WinptyFileWrapper.write"></a>

#### write

```python
def write(data: str) -> int
```

Write string data.

<a id="bittty.pty.windows.WinptyFileWrapper.close"></a>

#### close

```python
def close() -> None
```

Close the PTY.

<a id="bittty.pty.windows.WinptyFileWrapper.closed"></a>

#### closed

```python
@property
def closed() -> bool
```

Check if closed.

<a id="bittty.pty.windows.WinptyFileWrapper.flush"></a>

#### flush

```python
def flush() -> None
```

Flush - no-op for winpty.

<a id="bittty.pty.windows.WinptyProcessWrapper"></a>

## WinptyProcessWrapper Objects

```python
class WinptyProcessWrapper()
```

Wrapper to provide subprocess.Popen-like interface for winpty PTY.

<a id="bittty.pty.windows.WinptyProcessWrapper.poll"></a>

#### poll

```python
def poll()
```

Check if process is still running.

<a id="bittty.pty.windows.WinptyProcessWrapper.wait"></a>

#### wait

```python
def wait()
```

Wait for process to complete.

<a id="bittty.pty.windows.WinptyProcessWrapper.returncode"></a>

#### returncode

```python
@property
def returncode()
```

Get the return code.

<a id="bittty.pty.windows.WinptyProcessWrapper.pid"></a>

#### pid

```python
@property
def pid()
```

Get the process ID.

<a id="bittty.pty.windows.WindowsPTY"></a>

## WindowsPTY Objects

```python
class WindowsPTY(PTY)
```

Windows PTY implementation using pywinpty.

Note: This PTY operates in text mode - winpty handles UTF-8 internally.
The read/write methods work directly with strings for performance,
with bytes conversion only when needed for compatibility.

<a id="bittty.pty.windows.WindowsPTY.read"></a>

#### read

```python
def read(size: int = constants.DEFAULT_PTY_BUFFER_SIZE) -> str
```

Read data directly from winpty (text mode, no UTF-8 splitting needed).

<a id="bittty.pty.windows.WindowsPTY.write"></a>

#### write

```python
def write(data: str) -> int
```

Write string data directly to winpty (text mode).

<a id="bittty.pty.windows.WindowsPTY.resize"></a>

#### resize

```python
def resize(rows: int, cols: int) -> None
```

Resize the terminal.

<a id="bittty.pty.windows.WindowsPTY.spawn_process"></a>

#### spawn\_process

```python
def spawn_process(command: str,
                  env: Optional[Dict[str, str]] = ENV) -> subprocess.Popen
```

Spawn a process attached to this PTY.

<a id="bittty.pty"></a>

# bittty.pty

PTY implementations for terminal emulation.

<a id="bittty.constants"></a>

# bittty.constants

Constants for the terminal parser and emulator.

This module contains constants used in the terminal parsing and emulation logic,
following standards like VT100, VT220, and xterm.

<a id="bittty.constants.ENQ"></a>

#### ENQ

Enquiry (triggers answerback)

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

<a id="bittty.constants.VT"></a>

#### VT

Vertical Tab

<a id="bittty.constants.FF"></a>

#### FF

Form Feed

<a id="bittty.constants.CR"></a>

#### CR

Carriage Return

<a id="bittty.constants.SO"></a>

#### SO

Shift Out (activate G1)

<a id="bittty.constants.SI"></a>

#### SI

Shift In (activate G0)

<a id="bittty.constants.ESC"></a>

#### ESC

Escape

<a id="bittty.constants.DEL"></a>

#### DEL

Delete

<a id="bittty.constants.LINE_SINGLE"></a>

#### LINE\_SINGLE

DECSWL — normal single-width, single-height

<a id="bittty.constants.LINE_DOUBLE_WIDTH"></a>

#### LINE\_DOUBLE\_WIDTH

DECDWL

<a id="bittty.constants.LINE_DOUBLE_TOP"></a>

#### LINE\_DOUBLE\_TOP

DECDHL top half

<a id="bittty.constants.LINE_DOUBLE_BOTTOM"></a>

#### LINE\_DOUBLE\_BOTTOM

DECDHL bottom half

<a id="bittty.constants.DECKBUM_KEYBOARD_USAGE"></a>

#### DECKBUM\_KEYBOARD\_USAGE

DECKBUM is mode 68; mode 69 is DECLRMM (left/right margins)

<a id="bittty.constants.DA1_132_COLUMNS"></a>

#### DA1\_132\_COLUMNS

132 column mode

<a id="bittty.constants.DA1_PRINTER_PORT"></a>

#### DA1\_PRINTER\_PORT

Printer port

<a id="bittty.constants.DA1_REGIS_GRAPHICS"></a>

#### DA1\_REGIS\_GRAPHICS

ReGIS graphics

<a id="bittty.constants.DA1_SIXEL_GRAPHICS"></a>

#### DA1\_SIXEL\_GRAPHICS

Sixel graphics

<a id="bittty.constants.DA1_SELECTIVE_ERASE"></a>

#### DA1\_SELECTIVE\_ERASE

Selective erase

<a id="bittty.constants.DA1_USER_DEFINED_KEYS"></a>

#### DA1\_USER\_DEFINED\_KEYS

User-defined keys (UDKs)

<a id="bittty.constants.DA1_NATIONAL_REPLACEMENT_CHARSETS"></a>

#### DA1\_NATIONAL\_REPLACEMENT\_CHARSETS

National replacement character sets

<a id="bittty.constants.DA1_TECH_CHARACTERS"></a>

#### DA1\_TECH\_CHARACTERS

Technical characters

<a id="bittty.constants.DA1_LOCATOR_PORT"></a>

#### DA1\_LOCATOR\_PORT

Locator port

<a id="bittty.constants.DA1_TERMINAL_STATE_INTERROGATION"></a>

#### DA1\_TERMINAL\_STATE\_INTERROGATION

Terminal state interrogation

<a id="bittty.constants.DA1_USER_WINDOWS"></a>

#### DA1\_USER\_WINDOWS

User windows

<a id="bittty.constants.DA1_DUAL_SESSIONS"></a>

#### DA1\_DUAL\_SESSIONS

Dual sessions

<a id="bittty.constants.DA1_HORIZONTAL_SCROLLING"></a>

#### DA1\_HORIZONTAL\_SCROLLING

Horizontal scrolling

<a id="bittty.constants.DA1_ANSI_COLOR"></a>

#### DA1\_ANSI\_COLOR

ANSI color

<a id="bittty.constants.DA1_GREEK_CHARSET"></a>

#### DA1\_GREEK\_CHARSET

Greek character set

<a id="bittty.constants.DA1_TURKISH_CHARSET"></a>

#### DA1\_TURKISH\_CHARSET

Turkish character set

<a id="bittty.constants.DA1_ISO_LATIN2_CHARSET"></a>

#### DA1\_ISO\_LATIN2\_CHARSET

ISO Latin-2 character set

<a id="bittty.constants.DA1_PC_TERM"></a>

#### DA1\_PC\_TERM

PC Term

<a id="bittty.constants.DA1_SOFT_KEY_MAP"></a>

#### DA1\_SOFT\_KEY\_MAP

Soft key map

<a id="bittty.constants.DA1_ASCII_EMULATION"></a>

#### DA1\_ASCII\_EMULATION

ASCII emulation

<a id="bittty.constants.EBADF"></a>

#### EBADF

Bad file descriptor

<a id="bittty.constants.EINVAL"></a>

#### EINVAL

Invalid argument

<a id="bittty.charsets"></a>

# bittty.charsets

Character set mappings for terminal emulation.

<a id="bittty.charsets.get_charset"></a>

#### get\_charset

```python
def get_charset(designator: str) -> dict
```

Get character set mapping for a designator.

<a id="bittty.devices.query"></a>

# bittty.devices.query

Query operation handler for the current board state.

<a id="bittty.devices.query.QueryDevice"></a>

## QueryDevice Objects

```python
class QueryDevice(Device)
```

Applies terminal query operations to the current board implementation.

<a id="bittty.devices.query.QueryDevice.handle_cwd"></a>

#### handle\_cwd

```python
def handle_cwd(operation: Operation) -> None
```

OSC 7 — record the reported working directory.

<a id="bittty.devices.query.QueryDevice.handle_notify"></a>

#### handle\_notify

```python
def handle_notify(operation: Operation) -> None
```

OSC 9 / 777 / 99 — a desktop notification.

<a id="bittty.devices.query.QueryDevice.handle_shell_mark"></a>

#### handle\_shell\_mark

```python
def handle_shell_mark(operation: Operation) -> None
```

OSC 133 — a shell-integration prompt/command mark.

<a id="bittty.devices.query.QueryDevice.handle_pointer_shape"></a>

#### handle\_pointer\_shape

```python
def handle_pointer_shape(operation: Operation) -> None
```

OSC 22 — the requested mouse-pointer shape.

<a id="bittty.devices.query.QueryDevice.handle_font"></a>

#### handle\_font

```python
def handle_font(operation: Operation) -> None
```

OSC 50 — set the font, or answer a query (data == '?') with the current one.

<a id="bittty.devices.query.QueryDevice.report_version"></a>

#### report\_version

```python
def report_version(operation: Operation) -> None
```

XTVERSION (CSI > q) — reply DCS > | name version ST.

<a id="bittty.devices.query.QueryDevice.report_status_string"></a>

#### report\_status\_string

```python
def report_status_string(operation: Operation) -> None
```

DECRQSS — answer a request for the current value of a setting.

<a id="bittty.devices.query.QueryDevice.handle_clipboard"></a>

#### handle\_clipboard

```python
def handle_clipboard(operation: Operation) -> None
```

OSC 52 — set the clipboard, or answer a query with its current contents.

<a id="bittty.devices.query.QueryDevice.handle_window_op"></a>

#### handle\_window\_op

```python
def handle_window_op(operation: Operation) -> None
```

XTWINOPS — window manipulation requests and reports; a terminal (chrome) actuates them.

<a id="bittty.devices.query.QueryDevice.set_conformance_level"></a>

#### set\_conformance\_level

```python
def set_conformance_level(operation: Operation) -> None
```

DECSCL — record the requested conformance level (behaviourally a no-op).

<a id="bittty.devices.query.QueryDevice.handle_setterm"></a>

#### handle\_setterm

```python
def handle_setterm(operation: Operation) -> None
```

linux `setterm` CSI...] — update the board's hardware registers.

<a id="bittty.devices.query.QueryDevice.request_checksum"></a>

#### request\_checksum

```python
def request_checksum(operation: Operation) -> None
```

DECRQCRA — reply DCS Pid ! ~ HHHH ST with a 16-bit checksum of a rectangle.

This is the DEC character-value form: the negated sum of the codepoints in
the area, masked to 16 bits. (xterm can fold SGR attributes in too; that is a
model detail we can add when a terminal needs it.)

<a id="bittty.devices.query.QueryDevice.request_termcap"></a>

#### request\_termcap

```python
def request_termcap(operation: Operation) -> None
```

XTGETTCAP — answer hex-encoded termcap/terminfo capability requests.

<a id="bittty.devices.board"></a>

# bittty.devices.board

The board: the whole terminal emulator machine.

Hosts the devices and registers, owns the child process and its PTY, and routes
parser operations to device handlers. A terminal (chrome) (bittty.terminals) plugs into
the display port; the child program is wired to the host port via a PTY.

<a id="bittty.devices.board.Board"></a>

## Board Objects

```python
class Board()
```

The terminal emulator: devices, registers, and process/PTY lifecycle.

<a id="bittty.devices.board.Board.get_pty_handler"></a>

#### get\_pty\_handler

```python
@staticmethod
def get_pty_handler(rows: int = constants.DEFAULT_TERMINAL_HEIGHT,
                    cols: int = constants.DEFAULT_TERMINAL_WIDTH,
                    stdin=None,
                    stdout=None)
```

Create a platform-appropriate PTY handler.

<a id="bittty.devices.board.Board.print_text"></a>

#### print\_text

```python
def print_text(text: str) -> None
```

Write printable text (the parser's fast path — no Operation wrapper).

<a id="bittty.devices.board.Board.resize"></a>

#### resize

```python
def resize(width: int, height: int) -> None
```

Resize the terminal, including buffers and the attached PTY.

<a id="bittty.devices.board.Board.bell"></a>

#### bell

```python
def bell() -> None
```

Ring the terminal bell: pushed to the terminal (chrome) as a present event.

<a id="bittty.devices.board.Board.present"></a>

#### present

```python
def present(event: PresentEvent) -> None
```

Push a discrete side-effect to the attached terminal (no-op if none).

<a id="bittty.devices.board.Board.set_caps"></a>

#### set\_caps

```python
def set_caps(caps: TerminalCaps) -> None
```

Record what the real terminal can do (a terminal (chrome) pushes this after probing).

<a id="bittty.devices.board.Board.set_focus"></a>

#### set\_focus

```python
def set_focus(focused: bool) -> None
```

Record the box's focus state and report it to the child (DECSET 1004).

<a id="bittty.devices.board.Board.reset"></a>

#### reset

```python
def reset(hard: bool = True) -> None
```

Reset the terminal. hard is RIS (full power-on); soft is DECSTR.

<a id="bittty.devices.board.Board.get_device"></a>

#### get\_device

```python
def get_device(name: str)
```

Return a plugged-in device by slot name.

<a id="bittty.devices.board.Board.get_content"></a>

#### get\_content

```python
def get_content()
```

Get current screen content as raw buffer data.

<a id="bittty.devices.board.Board.capture_pane"></a>

#### capture\_pane

```python
def capture_pane() -> str
```

Capture screen content: a pure pull of video memory as ANSI lines.

No cursor or pointer is composited in — the chrome renders those from
the board's registers (cursor.x/y, modes.cursor_visible, mouse.x/y).

<a id="bittty.devices.board.Board.link_at"></a>

#### link\_at

```python
def link_at(x: int, y: int) -> tuple | None
```

The hyperlink under a cell: (uri, link_id) or None.

The chrome pulls this for hover and click arbitration — link data is
model state; the hover effect and the click-through are chrome.

<a id="bittty.devices.board.Board.attach_display"></a>

#### attach\_display

```python
def attach_display(display) -> None
```

Attach a terminal (chrome) to receive present events (mirrors the host/PTY cable).

<a id="bittty.devices.board.Board.detach_display"></a>

#### detach\_display

```python
def detach_display() -> None
```

Detach the current terminal.

<a id="bittty.devices.board.Board.input_key"></a>

#### input\_key

```python
def input_key(char: str, modifier: int = constants.KEY_MOD_NONE) -> None
```

Convert key + modifier to standard control codes, then send to the host.

<a id="bittty.devices.board.Board.input_fkey"></a>

#### input\_fkey

```python
def input_fkey(num: int, modifier: int = constants.KEY_MOD_NONE) -> None
```

Convert function key + modifier to standard control codes, then send to the host.

<a id="bittty.devices.board.Board.input_numpad_key"></a>

#### input\_numpad\_key

```python
def input_numpad_key(key: str) -> None
```

Convert numpad key to appropriate sequence based on DECNKM mode.

<a id="bittty.devices.board.Board.input"></a>

#### input

```python
def input(data: str) -> None
```

Translate control codes based on terminal modes and send to the host.

<a id="bittty.devices.board.Board.input_mouse"></a>

#### input\_mouse

```python
def input_mouse(x: int, y: int, button: int, event_type: str,
                modifiers: set[str]) -> None
```

Handle mouse input, cache position, and send appropriate sequence to the host.

**Arguments**:

- `x` - 1-based mouse column.
- `y` - 1-based mouse row.
- `button` - The button that was pressed/released.
- `event_type` - "press", "release", or "move".
- `modifiers` - A set of active modifiers ("shift", "meta", "ctrl").

<a id="bittty.devices.board.Board.focus_in"></a>

#### focus\_in

```python
def focus_in() -> None
```

The box gained focus: record it and report to the child if DECSET 1004 is on.

<a id="bittty.devices.board.Board.focus_out"></a>

#### focus\_out

```python
def focus_out() -> None
```

The box lost focus: record it and report to the child if DECSET 1004 is on.

<a id="bittty.devices.board.Board.pty"></a>

#### pty

```python
@property
def pty() -> Optional[Any]
```

Attached PTY connection.

<a id="bittty.devices.board.Board.set_pty_data_callback"></a>

#### set\_pty\_data\_callback

```python
def set_pty_data_callback(callback: Callable[[str], None]) -> None
```

Swap the host port's receive sink (a terminal uses this to add render throttling).

<a id="bittty.devices.board.Board.start_process"></a>

#### start\_process

```python
async def start_process() -> None
```

Start the child process with PTY.

<a id="bittty.devices.board.Board.stop_process"></a>

#### stop\_process

```python
def stop_process() -> None
```

Stop the child process and clean up.

<a id="bittty.devices.charset"></a>

# bittty.devices.charset

Charset operation handler for the current board state.

<a id="bittty.devices.charset.CharsetDevice"></a>

## CharsetDevice Objects

```python
class CharsetDevice(Device)
```

Owns charset state and applies charset operations.

<a id="bittty.devices.charset.CharsetDevice.designate"></a>

#### designate

```python
def designate(index: int, designator: str) -> None
```

Apply an SCS G-set designation, ignoring charsets the terminal lacks.

<a id="bittty.devices.charset.CharsetDevice.translate"></a>

#### translate

```python
def translate(text: str) -> str
```

Translate text through the invoked G-sets: GL for 0x20-0x7F, GR for 0xA0-0xFF.

<a id="bittty.devices.charset.CharsetDevice.set_g0_charset"></a>

#### set\_g0\_charset

```python
def set_g0_charset(charset: str) -> None
```

Set the G0 character set.

<a id="bittty.devices.charset.CharsetDevice.set_g1_charset"></a>

#### set\_g1\_charset

```python
def set_g1_charset(charset: str) -> None
```

Set the G1 character set.

<a id="bittty.devices.charset.CharsetDevice.set_g2_charset"></a>

#### set\_g2\_charset

```python
def set_g2_charset(charset: str) -> None
```

Set the G2 character set.

<a id="bittty.devices.charset.CharsetDevice.set_g3_charset"></a>

#### set\_g3\_charset

```python
def set_g3_charset(charset: str) -> None
```

Set the G3 character set.

<a id="bittty.devices.charset.CharsetDevice.shift_in"></a>

#### shift\_in

```python
def shift_in() -> None
```

Shift In (SI / LS0) - invoke G0 into GL.

<a id="bittty.devices.charset.CharsetDevice.shift_out"></a>

#### shift\_out

```python
def shift_out() -> None
```

Shift Out (SO / LS1) - invoke G1 into GL.

<a id="bittty.devices.charset.CharsetDevice.locking_shift"></a>

#### locking\_shift

```python
def locking_shift(gset: int, right: bool = False) -> None
```

Persistently invoke a G-set: LS2/LS3 into GL, LS1R/LS2R/LS3R into GR.

<a id="bittty.devices.charset.CharsetDevice.single_shift_2"></a>

#### single\_shift\_2

```python
def single_shift_2() -> None
```

Single Shift 2 (SS2) - use G2 for next character only.

<a id="bittty.devices.charset.CharsetDevice.single_shift_3"></a>

#### single\_shift\_3

```python
def single_shift_3() -> None
```

Single Shift 3 (SS3) - use G3 for next character only.

<a id="bittty.devices.charset.CharsetDevice.reset"></a>

#### reset

```python
def reset() -> None
```

Reset charset selections to US ASCII.

<a id="bittty.devices.style"></a>

# bittty.devices.style

Style operation handler for the current board state.

<a id="bittty.devices.style.StyleDevice"></a>

## StyleDevice Objects

```python
class StyleDevice(Device)
```

Owns current style state and applies style operations.

<a id="bittty.devices.style.StyleDevice.pop_sgr"></a>

#### pop\_sgr

```python
def pop_sgr() -> None
```

XTPOPSGR — restore the SGR attributes saved by the matching XTPUSHSGR.

<a id="bittty.devices.style.StyleDevice.current_ansi_code"></a>

#### current\_ansi\_code

```python
@property
def current_ansi_code() -> str
```

The active style as an ANSI SGR string (boundary/compat accessor).

<a id="bittty.devices.style.StyleDevice.apply_sgr"></a>

#### apply\_sgr

```python
def apply_sgr(style: Style | None, reset: bool = False) -> None
```

Apply an SGR style update (API/testing surface over the hot handler).

<a id="bittty.devices.style.StyleDevice.set_default"></a>

#### set\_default

```python
def set_default() -> None
```

ESC [ 8 ] — make the current attributes the default (the SGR 0 target).

<a id="bittty.devices.style.StyleDevice.set_hyperlink"></a>

#### set\_hyperlink

```python
def set_hyperlink(uri: str, link_id: str = "") -> None
```

OSC 8 — start (non-empty URI) or end (empty) the active hyperlink.

The id= param groups link segments a layout has split (wrapped lines,
columns); the chrome uses it to hover them as one link.

<a id="bittty.devices.style.StyleDevice.set_protected"></a>

#### set\_protected

```python
def set_protected(mode: int) -> None
```

DECSCA — 1 protects subsequent characters from selective erase; 0/2 clears it.

<a id="bittty.devices.style.StyleDevice.reset"></a>

#### reset

```python
def reset() -> None
```

Reset to the default style (and clear the ESC[8] default register and SGR stack).

<a id="bittty.devices.style.StyleDevice.background_ansi"></a>

#### background\_ansi

```python
def background_ansi() -> str
```

Return the active background style as ANSI.

<a id="bittty.devices.base"></a>

# bittty.devices.base

Base class shared by board devices.

<a id="bittty.devices.base.Device"></a>

## Device Objects

```python
class Device()
```

A board device: dispatches an operation to its name -> handler table.

<a id="bittty.devices.blitter"></a>

# bittty.devices.blitter

The blitter: writes video memory. Screen and editing operation handlers.

<a id="bittty.devices.blitter.Blitter"></a>

## Blitter Objects

```python
class Blitter(Device)
```

Owns the video pages and applies screen/editing operations.

<a id="bittty.devices.blitter.Blitter.set_line_attribute"></a>

#### set\_line\_attribute

```python
def set_line_attribute(attribute: str) -> None
```

DECDHL/DECDWL/DECSWL — set the cursor line's width/height attribute.

<a id="bittty.devices.blitter.Blitter.write_text"></a>

#### write\_text

```python
def write_text(text: str, ansi_code: str = "") -> None
```

Write printable text at the cursor position, wrapping runs longer than the line.

A single PRINT run can be arbitrarily long (a shell line wider than the
screen arrives as one chunk), so write it line-sized piece by line-sized
piece; prepare_for_text_write supplies the wrap (or the clip, with
autowrap off) between pieces.

<a id="bittty.devices.blitter.Blitter.repeat_last_character"></a>

#### repeat\_last\_character

```python
def repeat_last_character(count: int) -> None
```

Repeat the last printed character count times.

<a id="bittty.devices.blitter.Blitter.resize"></a>

#### resize

```python
def resize(width: int, height: int) -> None
```

Resize terminal dimensions and screen buffers.

<a id="bittty.devices.blitter.Blitter.clear_screen"></a>

#### clear\_screen

```python
def clear_screen(mode: int = constants.ERASE_FROM_CURSOR_TO_END) -> None
```

Clear screen.

<a id="bittty.devices.blitter.Blitter.clear_line"></a>

#### clear\_line

```python
def clear_line(mode: int = constants.ERASE_FROM_CURSOR_TO_END) -> None
```

Clear line.

<a id="bittty.devices.blitter.Blitter.clear_rect"></a>

#### clear\_rect

```python
def clear_rect(x1: int,
               y1: int,
               x2: int,
               y2: int,
               ansi_code: str = "") -> None
```

Clear a rectangular region.

<a id="bittty.devices.blitter.Blitter.selective_erase_display"></a>

#### selective\_erase\_display

```python
def selective_erase_display(mode: int) -> None
```

DECSED — erase in display, leaving DECSCA-protected characters.

<a id="bittty.devices.blitter.Blitter.selective_erase_line"></a>

#### selective\_erase\_line

```python
def selective_erase_line(mode: int) -> None
```

DECSEL — erase in line, leaving DECSCA-protected characters.

<a id="bittty.devices.blitter.Blitter.fill_rectangle"></a>

#### fill\_rectangle

```python
def fill_rectangle(params) -> None
```

DECFRA — fill a rectangle with a character (Pch;Pt;Pl;Pb;Pr).

<a id="bittty.devices.blitter.Blitter.erase_rectangle"></a>

#### erase\_rectangle

```python
def erase_rectangle(params) -> None
```

DECERA — erase a rectangle (Pt;Pl;Pb;Pr).

<a id="bittty.devices.blitter.Blitter.selective_erase_rectangle"></a>

#### selective\_erase\_rectangle

```python
def selective_erase_rectangle(params) -> None
```

DECSERA — erase a rectangle, leaving DECSCA-protected characters.

<a id="bittty.devices.blitter.Blitter.copy_rectangle"></a>

#### copy\_rectangle

```python
def copy_rectangle(params) -> None
```

DECCRA — copy a rectangle to another origin (Pts;Pls;Pbs;Prs;Pps;Ptd;Pld;Ppd).

<a id="bittty.devices.blitter.Blitter.set_attr_change_extent"></a>

#### set\_attr\_change\_extent

```python
def set_attr_change_extent(ps: int) -> None
```

DECSACE — 1 = stream (wrapping run), else rectangle (default).

<a id="bittty.devices.blitter.Blitter.change_attributes_rectangle"></a>

#### change\_attributes\_rectangle

```python
def change_attributes_rectangle(params) -> None
```

DECCARA — merge SGR attributes into every cell of the area (rectangle or stream).

<a id="bittty.devices.blitter.Blitter.reverse_attributes_rectangle"></a>

#### reverse\_attributes\_rectangle

```python
def reverse_attributes_rectangle(params) -> None
```

DECRARA — toggle the given attributes (1/4/5/7) across the area (rectangle or stream).

<a id="bittty.devices.blitter.Blitter.switch_screen"></a>

#### switch\_screen

```python
def switch_screen(alt: bool) -> None
```

Switch between primary and alternate screen.

<a id="bittty.devices.blitter.Blitter.alignment_test"></a>

#### alignment\_test

```python
def alignment_test() -> None
```

Fill the screen with 'E' characters for alignment testing.

<a id="bittty.devices.blitter.Blitter.set_scroll_region"></a>

#### set\_scroll\_region

```python
def set_scroll_region(top: int, bottom: int) -> None
```

Set scroll region.

<a id="bittty.devices.blitter.Blitter.set_top_and_bottom_margins"></a>

#### set\_top\_and\_bottom\_margins

```python
def set_top_and_bottom_margins(top: int, bottom: int | None) -> None
```

DECSTBM — set the scroll region and home the cursor (origin-aware).

<a id="bittty.devices.blitter.Blitter.insert_lines"></a>

#### insert\_lines

```python
def insert_lines(count: int) -> None
```

Insert blank lines at cursor position.

<a id="bittty.devices.blitter.Blitter.delete_lines"></a>

#### delete\_lines

```python
def delete_lines(count: int) -> None
```

Delete lines at cursor position.

<a id="bittty.devices.blitter.Blitter.insert_characters"></a>

#### insert\_characters

```python
def insert_characters(count: int, ansi_code: str = "") -> None
```

Insert blank characters at cursor position.

<a id="bittty.devices.blitter.Blitter.delete_characters"></a>

#### delete\_characters

```python
def delete_characters(count: int) -> None
```

Delete characters at cursor position.

<a id="bittty.devices.blitter.Blitter.scroll"></a>

#### scroll

```python
def scroll(lines: int) -> None
```

Scroll content within the active scroll region.

<a id="bittty.devices.blitter.Blitter.pan"></a>

#### pan

```python
def pan(columns: int) -> None
```

SL/SR — pan the scroll-region rows horizontally within the left/right margins.

<a id="bittty.devices.blitter.Blitter.shift_columns"></a>

#### shift\_columns

```python
def shift_columns(count: int) -> None
```

DECIC (count > 0) / DECDC (count < 0) — insert/delete columns at the cursor.

Confined to the left/right margin box; a cursor outside it is a no-op.

<a id="bittty.devices.blitter.Blitter.set_left_right_margins"></a>

#### set\_left\_right\_margins

```python
def set_left_right_margins(left: int | None, right: int | None) -> None
```

DECSLRM — set the left/right margins (1-based; None/0 = extremes) and home the cursor.

<a id="bittty.devices.blitter.Blitter.reset_left_right_margins"></a>

#### reset\_left\_right\_margins

```python
def reset_left_right_margins() -> None
```

Restore the margins to the full screen width.

<a id="bittty.devices.blitter.Blitter.apply_left_right_margins"></a>

#### apply\_left\_right\_margins

```python
def apply_left_right_margins(operation: Operation) -> None
```

CSI Pl ; Pr s — DECSLRM when margin mode is on, else SCOSC (save cursor).

<a id="bittty.devices.blitter.Blitter.scroll_up"></a>

#### scroll\_up

```python
def scroll_up(count: int) -> None
```

Scroll content up within scroll region.

<a id="bittty.devices.blitter.Blitter.scroll_down"></a>

#### scroll\_down

```python
def scroll_down(count: int) -> None
```

Scroll content down within scroll region.

<a id="bittty.devices.blitter.Blitter.reset"></a>

#### reset

```python
def reset(hard: bool = True) -> None
```

Restore the full scroll region; a hard reset also clears both buffers to primary.

<a id="bittty.devices.blitter.Blitter.set_column_mode"></a>

#### set\_column\_mode

```python
def set_column_mode(columns: int) -> None
```

DECCOLM — switch 80/132 columns; always clears the screen and homes the cursor.

<a id="bittty.devices.blitter.Blitter.erase_characters"></a>

#### erase\_characters

```python
def erase_characters(count: int) -> None
```

Erase `count` characters from the cursor with the current style; the cursor stays (ECH).

<a id="bittty.devices.control"></a>

# bittty.devices.control

Control operation handler for the current board state.

<a id="bittty.devices.control.ControlDevice"></a>

## ControlDevice Objects

```python
class ControlDevice(Device)
```

Applies C0 and simple control operations to the current board implementation.

<a id="bittty.devices.control.ControlDevice.carriage_return_line_feed"></a>

#### carriage\_return\_line\_feed

```python
def carriage_return_line_feed() -> None
```

CR+LF as one fused token (the parser batches the pair).

<a id="bittty.devices.control.ControlDevice.next_line"></a>

#### next\_line

```python
def next_line() -> None
```

NEL — carriage return followed by line feed.

<a id="bittty.devices.control.ControlDevice.answerback"></a>

#### answerback

```python
def answerback() -> None
```

ENQ — transmit the programmed answerback string, if any is set.

<a id="bittty.devices.cursor"></a>

# bittty.devices.cursor

Cursor operation handler for the current board state.

<a id="bittty.devices.cursor.CursorDevice"></a>

## CursorDevice Objects

```python
class CursorDevice(Device)
```

Owns cursor state and applies cursor operations.

<a id="bittty.devices.cursor.CursorDevice.set_position"></a>

#### set\_position

```python
def set_position(x: int | None, y: int | None) -> None
```

Move cursor to an absolute, clamped terminal position.

<a id="bittty.devices.cursor.CursorDevice.move_to"></a>

#### move\_to

```python
def move_to(x: int | None, y: int | None) -> None
```

Apply a CUP/HVP/VPA move, honouring origin mode (DECOM).

Under origin mode the row is relative to the scroll region's top and the
column to the left margin, each clamped within its margins.

<a id="bittty.devices.cursor.CursorDevice.clamp_to_terminal"></a>

#### clamp\_to\_terminal

```python
def clamp_to_terminal() -> None
```

Clamp the current position after terminal dimensions change.

<a id="bittty.devices.cursor.CursorDevice.carriage_return"></a>

#### carriage\_return

```python
def carriage_return() -> None
```

Move cursor to the beginning of the current line.

<a id="bittty.devices.cursor.CursorDevice.line_feed"></a>

#### line\_feed

```python
def line_feed(is_wrapped: bool = False) -> None
```

Move down one line, scrolling the active scroll region if needed.

<a id="bittty.devices.cursor.CursorDevice.forward_index"></a>

#### forward\_index

```python
def forward_index() -> None
```

DECFI — move right; at the right margin, pan the margin box one column left.

<a id="bittty.devices.cursor.CursorDevice.back_index"></a>

#### back\_index

```python
def back_index() -> None
```

DECBI — move left; at the left margin, pan the margin box one column right.

<a id="bittty.devices.cursor.CursorDevice.reverse_index"></a>

#### reverse\_index

```python
def reverse_index() -> None
```

Move up one line, scrolling down at the top of the scroll region.

<a id="bittty.devices.cursor.CursorDevice.backspace"></a>

#### backspace

```python
def backspace() -> None
```

Move cursor back one position, wrapping to the previous line if needed.

<a id="bittty.devices.cursor.CursorDevice.set_tab_stop"></a>

#### set\_tab\_stop

```python
def set_tab_stop(x: int | None = None) -> None
```

Set a horizontal tab stop at the given column.

<a id="bittty.devices.cursor.CursorDevice.next_tab_stop"></a>

#### next\_tab\_stop

```python
def next_tab_stop() -> int
```

Return the next horizontal tab stop, clamped to the last column.

<a id="bittty.devices.cursor.CursorDevice.horizontal_tab"></a>

#### horizontal\_tab

```python
def horizontal_tab() -> None
```

Advance to the next horizontal tab stop.

<a id="bittty.devices.cursor.CursorDevice.previous_tab_stop"></a>

#### previous\_tab\_stop

```python
def previous_tab_stop() -> int
```

Return the nearest tab stop left of the cursor, or column 0.

<a id="bittty.devices.cursor.CursorDevice.forward_tab"></a>

#### forward\_tab

```python
def forward_tab(count: int) -> None
```

CHT — advance `count` tab stops.

<a id="bittty.devices.cursor.CursorDevice.backward_tab"></a>

#### backward\_tab

```python
def backward_tab(count: int) -> None
```

CBT — retreat `count` tab stops.

<a id="bittty.devices.cursor.CursorDevice.clear_tab_stop"></a>

#### clear\_tab\_stop

```python
def clear_tab_stop(mode: int) -> None
```

TBC — clear the tab stop at the cursor (0) or all tab stops (3).

<a id="bittty.devices.cursor.CursorDevice.tab_control"></a>

#### tab\_control

```python
def tab_control(mode: int) -> None
```

CTC — set (0) or clear (2) a tab stop at the cursor, or clear all (5).

<a id="bittty.devices.cursor.CursorDevice.reset_tab_stops"></a>

#### reset\_tab\_stops

```python
def reset_tab_stops() -> None
```

DECST8C — reset to a tab stop every 8 columns.

<a id="bittty.devices.cursor.CursorDevice.next_line"></a>

#### next\_line

```python
def next_line(count: int) -> None
```

CNL — move to the first column, `count` lines down (no scroll).

<a id="bittty.devices.cursor.CursorDevice.previous_line"></a>

#### previous\_line

```python
def previous_line(count: int) -> None
```

CPL — move to the first column, `count` lines up (no scroll).

<a id="bittty.devices.cursor.CursorDevice.set_cursor_style"></a>

#### set\_cursor\_style

```python
def set_cursor_style(style: int) -> None
```

DECSCUSR — set cursor shape and blink from the style parameter.

<a id="bittty.devices.cursor.CursorDevice.prepare_for_text_write"></a>

#### prepare\_for\_text\_write

```python
def prepare_for_text_write() -> None
```

Apply wrapping or clipping before writing at the cursor.

<a id="bittty.devices.cursor.CursorDevice.advance_after_text_write"></a>

#### advance\_after\_text\_write

```python
def advance_after_text_write(character_count: int) -> None
```

Advance after printable text, preserving existing autowrap behavior.

<a id="bittty.devices.cursor.CursorDevice.save"></a>

#### save

```python
def save() -> None
```

Save cursor position and attributes.

<a id="bittty.devices.cursor.CursorDevice.restore"></a>

#### restore

```python
def restore() -> None
```

Restore cursor position and attributes.

<a id="bittty.devices.cursor.CursorDevice.reset"></a>

#### reset

```python
def reset(hard: bool = True) -> None
```

Home the cursor and clear saved state; a hard reset restores default tab stops.

<a id="bittty.devices.palette"></a>

# bittty.devices.palette

Palette device: owns the live colour palette and the OSC colour surface.

<a id="bittty.devices.palette.PaletteDevice"></a>

## PaletteDevice Objects

```python
class PaletteDevice(Device)
```

Holds the current 256-colour table plus fg/bg/cursor, and applies OSC colour ops.

<a id="bittty.devices.palette.PaletteDevice.special_color"></a>

#### special\_color

```python
def special_color(operation: Operation) -> None
```

OSC 5 — set or (spec == '?') query a special colour (0=bold, 1=underline, …).

<a id="bittty.devices.palette.PaletteDevice.special_color_enable"></a>

#### special\_color\_enable

```python
def special_color_enable(operation: Operation) -> None
```

OSC 6 — enable or disable a special colour.

<a id="bittty.devices.palette.PaletteDevice.reset"></a>

#### reset

```python
def reset() -> None
```

Restore the model's default colours plus construction overrides (RIS).

<a id="bittty.devices.palette.PaletteDevice.dynamic_color"></a>

#### dynamic\_color

```python
def dynamic_color(operation: Operation, slot: str, cmd: int,
                  fallback: str) -> None
```

OSC 13/14/17/19 — set, or (data == '?') query a dynamic colour with a fg/bg fallback.

<a id="bittty.devices.palette.PaletteDevice.push_colors"></a>

#### push\_colors

```python
def push_colors() -> None
```

XTPUSHCOLORS — save the whole palette (256 entries plus fg/bg/cursor).

<a id="bittty.devices.palette.PaletteDevice.pop_colors"></a>

#### pop\_colors

```python
def pop_colors() -> None
```

XTPOPCOLORS — restore the palette saved by the matching XTPUSHCOLORS.

<a id="bittty.devices.palette.PaletteDevice.resolve"></a>

#### resolve

```python
def resolve(color) -> RGB | None
```

Resolve a Style colour to concrete RGB. None means "use the default fg/bg".

<a id="bittty.devices.palette.PaletteDevice.set_palette"></a>

#### set\_palette

```python
def set_palette(operation: Operation) -> None
```

OSC 4 ; n ; spec [; n ; spec ...] — set or (spec == '?') query palette entries.

<a id="bittty.devices.palette.PaletteDevice.set_or_query_special"></a>

#### set\_or\_query\_special

```python
def set_or_query_special(operation: Operation, slot: str, cmd: int) -> None
```

OSC 10/11/12 — set or (data == '?') query the fg/bg/cursor colour.

<a id="bittty.devices.palette.PaletteDevice.reset_palette"></a>

#### reset\_palette

```python
def reset_palette(operation: Operation) -> None
```

OSC 104 — reset all palette entries, or just the listed indices.

<a id="bittty.devices.palette.PaletteDevice.reset_special"></a>

#### reset\_special

```python
def reset_special(slot: str) -> None
```

OSC 110/111/112 — reset the fg/bg/cursor colour to the model default.

<a id="bittty.devices.palette.PaletteDevice.set_linux_palette"></a>

#### set\_linux\_palette

```python
def set_linux_palette(operation: Operation) -> None
```

ESC ] P nrrggbb — the linux console's own single-entry palette set.

<a id="bittty.devices.printer"></a>

# bittty.devices.printer

Printer device: the terminal's aux printer port (Media Copy / MC).

Historically a terminal had a printer hanging off its aux port; Media Copy
routed screen data to it. Here the printer is a board device with an
attachable *sink* — a callable taking a str, or any object with a write()
method (a file, an io.StringIO, a real printer driver). Unattached, printed
output is simply discarded, exactly like a terminal with no printer connected.

<a id="bittty.devices.printer.PrinterDevice"></a>

## PrinterDevice Objects

```python
class PrinterDevice(Device)
```

Owns printer state (controller/auto-print modes) and the output sink.

<a id="bittty.devices.printer.PrinterDevice.attach"></a>

#### attach

```python
def attach(sink) -> None
```

Attach a printer sink: a callable(str), or an object with a write(str) method.

<a id="bittty.devices.printer.PrinterDevice.emit"></a>

#### emit

```python
def emit(text: str) -> None
```

Send text to the attached sink, if any.

<a id="bittty.devices.printer.PrinterDevice.media_copy"></a>

#### media\_copy

```python
def media_copy(operation: Operation) -> None
```

MC (CSI Ps i) — ANSI media copy.

<a id="bittty.devices.printer.PrinterDevice.dec_media_copy"></a>

#### dec\_media\_copy

```python
def dec_media_copy(operation: Operation) -> None
```

DEC MC (CSI ? Ps i) — auto-print and DEC print variants.

<a id="bittty.devices.printer.PrinterDevice.print_screen"></a>

#### print\_screen

```python
def print_screen() -> None
```

Send the whole current screen to the printer, one line per row.

<a id="bittty.devices.printer.PrinterDevice.print_line"></a>

#### print\_line

```python
def print_line(y: int) -> None
```

Send a single row to the printer.

<a id="bittty.devices.printer.PrinterDevice.reset"></a>

#### reset

```python
def reset(hard: bool = True) -> None
```

Leave printer controller/auto-print modes; the attached sink is config, so it stays.

<a id="bittty.devices.mouse"></a>

# bittty.devices.mouse

Mouse input encoder: xterm mouse reports and the DEC locator protocol.

<a id="bittty.devices.mouse.MouseDevice"></a>

## MouseDevice Objects

```python
class MouseDevice(Device)
```

Owns mouse presentation state and emits mouse input reports.

<a id="bittty.devices.mouse.MouseDevice.enable_locator"></a>

#### enable\_locator

```python
def enable_locator(operation: Operation) -> None
```

DECELR — enable/disable locator reporting; ps2==1 selects pixel coordinates.

<a id="bittty.devices.mouse.MouseDevice.select_locator_events"></a>

#### select\_locator\_events

```python
def select_locator_events(operation: Operation) -> None
```

DECSLE — choose whether button presses/releases trigger reports.

<a id="bittty.devices.mouse.MouseDevice.set_filter_rectangle"></a>

#### set\_filter\_rectangle

```python
def set_filter_rectangle(operation: Operation) -> None
```

DECEFR — report once the locator leaves this rectangle.

<a id="bittty.devices.mouse.MouseDevice.request_locator_position"></a>

#### request\_locator\_position

```python
def request_locator_position(operation: Operation) -> None
```

DECRQLP — report the locator position now (or that it is unavailable).

<a id="bittty.devices.mouse.MouseDevice.input_mouse"></a>

#### input\_mouse

```python
def input_mouse(x: int, y: int, button: int, event_type: str,
                modifiers: set[str]) -> None
```

Handle mouse input, cache position, and send appropriate sequence to the host.

**Arguments**:

- `x` - 1-based mouse column.
- `y` - 1-based mouse row.
- `button` - The button that was pressed/released.
- `event_type` - "press", "release", or "move".
- `modifiers` - A set of active modifiers ("shift", "meta", "ctrl").

<a id="bittty.devices.keyboard"></a>

# bittty.devices.keyboard

Keyboard input encoder for terminal key events.

<a id="bittty.devices.keyboard.KeyboardDevice"></a>

## KeyboardDevice Objects

```python
class KeyboardDevice(Device)
```

Encodes keyboard input into terminal control sequences.

<a id="bittty.devices.keyboard.KeyboardDevice.set_user_keys"></a>

#### set\_user\_keys

```python
def set_user_keys(operation: Operation) -> None
```

DECUDK — install user-defined strings for function keys.

<a id="bittty.devices.keyboard.KeyboardDevice.set_modify_keys"></a>

#### set\_modify\_keys

```python
def set_modify_keys(operation: Operation) -> None
```

XTMODKEYS (CSI > Pp ; Pv m) — set a key-modifier resource; Pp 4 is modifyOtherKeys.

<a id="bittty.devices.keyboard.KeyboardDevice.kitty_push"></a>

#### kitty\_push

```python
def kitty_push(operation: Operation) -> None
```

CSI > flags u — save the current flags and adopt new ones.

<a id="bittty.devices.keyboard.KeyboardDevice.kitty_pop"></a>

#### kitty\_pop

```python
def kitty_pop(operation: Operation) -> None
```

CSI < n u — pop n saved flag-states off the stack.

<a id="bittty.devices.keyboard.KeyboardDevice.kitty_set"></a>

#### kitty\_set

```python
def kitty_set(operation: Operation) -> None
```

CSI = flags ; mode u — set (1), add (2) or remove (3) flag bits.

<a id="bittty.devices.keyboard.KeyboardDevice.kitty_query"></a>

#### kitty\_query

```python
def kitty_query(operation: Operation) -> None
```

CSI ? u — report the current Kitty flags as CSI ? flags u.

<a id="bittty.devices.keyboard.KeyboardDevice.report_focus"></a>

#### report\_focus

```python
def report_focus(focused: bool) -> None
```

Focus reporting (DECSET 1004) — send CSI I on focus in, CSI O on focus out.

<a id="bittty.devices.keyboard.KeyboardDevice.reset"></a>

#### reset

```python
def reset(hard: bool = True) -> None
```

RIS clears the modern-keyboard negotiation state.

<a id="bittty.devices.keyboard.KeyboardDevice.input_key"></a>

#### input\_key

```python
def input_key(char: str, modifier: int = constants.KEY_MOD_NONE) -> None
```

Convert key + modifier to standard control codes, then send to input().

<a id="bittty.devices.keyboard.KeyboardDevice.input_fkey"></a>

#### input\_fkey

```python
def input_fkey(num: int, modifier: int = constants.KEY_MOD_NONE) -> None
```

Encode a function key using any user-defined string, else the keymap.

<a id="bittty.devices.keyboard.KeyboardDevice.input_numpad_key"></a>

#### input\_numpad\_key

```python
def input_numpad_key(key: str) -> None
```

Convert numpad key to the sequence for the current keypad mode.

<a id="bittty.devices.keyboard.KeyboardDevice.input"></a>

#### input

```python
def input(data: str) -> None
```

Translate control codes based on terminal modes and send to the host.

<a id="bittty.devices.keyboard.KeyboardDevice.translate_application_cursor_keys"></a>

#### translate\_application\_cursor\_keys

```python
def translate_application_cursor_keys(data: str) -> str
```

Translate embedded normal cursor-key CSI sequences to application mode.

<a id="bittty.devices.modes"></a>

# bittty.devices.modes

Terminal modes as a declarative capability table.

Each mode is a small `Mode` capability that claims a number (ANSI or DEC
private), knows how to apply itself and how to report its DECRQM status, and
can be omitted by a model (so, e.g., a terminal that predates bracketed
paste simply does not recognise mode 2004). The boolean flags themselves stay
as attributes on the device: they are read widely across the emulator, and
several modes legitimately share one flag (mode 7 and 1000 both drive
`mouse_tracking`).

<a id="bittty.devices.modes.Mode"></a>

## Mode Objects

```python
@dataclass(frozen=True)
class Mode()
```

One terminal mode: which flag it backs and how it answers DECRQM.

<a id="bittty.devices.modes.Mode.attr"></a>

#### attr

device flag this mode drives, if any

<a id="bittty.devices.modes.Mode.invert"></a>

#### invert

"set" stores the negation (modes 12, 66)

<a id="bittty.devices.modes.Mode.queryable"></a>

#### queryable

DECRQM reports this mode's state

<a id="bittty.devices.modes.Mode.apply_fn"></a>

#### apply\_fn

side effect

<a id="bittty.devices.modes.Mode.status_fn"></a>

#### status\_fn

custom DECRQM status

<a id="bittty.devices.modes.Mode.peripheral"></a>

#### peripheral

"mouse"/"cursor"/"sync": emit a present event on change

<a id="bittty.devices.modes.Mode.status"></a>

#### status

```python
def status(device: ModeDevice) -> int
```

DECRQM status: 1 = set, 2 = reset, 0 = not recognised.

<a id="bittty.devices.modes.ModeDevice"></a>

## ModeDevice Objects

```python
class ModeDevice(Device)
```

Owns terminal mode state and applies mode operations via the mode table.

<a id="bittty.devices.modes.ModeDevice.reset"></a>

#### reset

```python
def reset(hard: bool = True) -> None
```

Reset modes. hard restores every flag (RIS); soft is the DECSTR subset.

<a id="bittty.devices.modes.ModeDevice.set_mode"></a>

#### set\_mode

```python
def set_mode(mode: int, value: bool = True, private: bool = False) -> None
```

Set a single terminal mode.

<a id="bittty.devices.modes.ModeDevice.clear_mode"></a>

#### clear\_mode

```python
def clear_mode(mode: int, private: bool = False) -> None
```

Clear a single terminal mode.

<a id="bittty.devices.title"></a>

# bittty.devices.title

Title operation handler for the current board state.

<a id="bittty.devices.title.TitleDevice"></a>

## TitleDevice Objects

```python
class TitleDevice(Device)
```

Owns terminal title state and applies title operations.

<a id="bittty.devices.title.TitleDevice.set_title"></a>

#### set\_title

```python
def set_title(title: str) -> None
```

Set terminal title.

<a id="bittty.devices.title.TitleDevice.set_icon_title"></a>

#### set\_icon\_title

```python
def set_icon_title(icon_title: str) -> None
```

Set terminal icon title.

<a id="bittty.devices.title.TitleDevice.set_both"></a>

#### set\_both

```python
def set_both(title: str) -> None
```

Set both the window title and the icon title.

<a id="bittty.devices.title.TitleDevice.push"></a>

#### push

```python
def push() -> None
```

XTWINOPS 22 — save the current window and icon titles.

<a id="bittty.devices.title.TitleDevice.pop"></a>

#### pop

```python
def pop() -> None
```

XTWINOPS 23 — restore the most recently saved titles.

<a id="bittty.devices"></a>

# bittty.devices

Device adapters for applying parser operations.

<a id="bittty.style"></a>

# bittty.style

<a id="bittty.style.CURSOR_CODE"></a>

#### CURSOR\_CODE

Reverse video for cursor display

<a id="bittty.style.RESET_CODE"></a>

#### RESET\_CODE

Reset all formatting

<a id="bittty.style.Style"></a>

## Style Objects

```python
class Style()
```

Immutable text style. The keyword surface matches the old dataclass field
per field (None = inherit); internally the tri-state attributes are packed
so merge/eq/hash cost a couple of int ops instead of a 20-field walk.

<a id="bittty.style.Style.merge"></a>

#### merge

```python
def merge(other: Style) -> Style
```

Merge another style into this one; the other's set attributes win.

<a id="bittty.style.Style.replace"></a>

#### replace

```python
def replace(**kwargs) -> Style
```

A new Style with the given fields replaced (None = back to inherit).

<a id="bittty.style.Style.diff"></a>

#### diff

```python
def diff(other: "Style") -> str
```

Generate minimal ANSI sequence to transition to another style.

<a id="bittty.style.parse_sgr_with_reset"></a>

#### parse\_sgr\_with\_reset

```python
@lru_cache(maxsize=10000)
def parse_sgr_with_reset(ansi: str) -> Tuple[Optional[Style], bool]
```

Parse an SGR sequence into (style, reset): reset means "clear, then apply style".

A reset token (0, 00, or an empty parameter) anywhere in the sequence discards
everything before it, so ESC[0;31m is "reset, then red" — not a red merge into
the current attributes. A pure reset returns (None, True) so the hot path can
skip the merge without comparing 20 Style fields.

<a id="bittty.style.interpret"></a>

#### interpret

```python
@lru_cache(maxsize=10000)
def interpret(tokens: Tuple[str, ...]) -> Style
```

Interpret SGR tokens into a Style, accumulating the packed masks directly.

<a id="bittty.style.get_background"></a>

#### get\_background

```python
@lru_cache(maxsize=10000)
def get_background(ansi: str) -> str
```

Extract just the background color as an ANSI sequence.

**Arguments**:

- `ansi` - ANSI escape sequence
  

**Returns**:

  ANSI sequence with just the background color, or empty string

<a id="bittty.style.merge_ansi_styles"></a>

#### merge\_ansi\_styles

```python
@lru_cache(maxsize=10000)
def merge_ansi_styles(base: str, new: str) -> str
```

Merge two ANSI style sequences, returning a new ANSI sequence.

**Arguments**:

- `base` - Base ANSI sequence
- `new` - New ANSI sequence to merge
  

**Returns**:

  Merged ANSI sequence

<a id="bittty.style.style_to_ansi"></a>

#### style\_to\_ansi

```python
@lru_cache(maxsize=10000)
def style_to_ansi(style: Style) -> str
```

Convert a Style object back to an ANSI escape sequence.

**Arguments**:

- `style` - Style object to convert
  

**Returns**:

  ANSI escape sequence string

<a id="bittty.caps"></a>

# bittty.caps

TerminalCaps: physical facts about the real terminal, pushed *up* by the chrome.

The backend answers the child's physical-fact queries (window/cell pixel size,
background colour) from these when a terminal (chrome) has supplied them. Every field
defaults to "unknown" (None / "unknown"), meaning "change nothing" — so a board
with no attached terminal behaves exactly as it does today.

Graphics-capability flags (sixel / kitty / iTerm images) are deliberately absent
until graphics modes are on the table; there is nothing to reconcile without them.

<a id="bittty.caps.TerminalCaps"></a>

## TerminalCaps Objects

```python
@dataclass(frozen=True)
class TerminalCaps()
```

What the real terminal can actually do (terminal -> board).

<a id="bittty.caps.TerminalCaps.color_depth"></a>

#### color\_depth

"monochrome" / "16" / "256" / "truecolor" / "unknown"

<a id="bittty.caps.TerminalCaps.cell_px"></a>

#### cell\_px

character cell size in pixels (CSI 16 t)

<a id="bittty.caps.TerminalCaps.window_px"></a>

#### window\_px

window size in pixels (CSI 14 t)

<a id="bittty.caps.TerminalCaps.background"></a>

#### background

actual background colour (OSC 11)

<a id="bittty.caps.TerminalCaps.unknown"></a>

#### unknown

```python
@classmethod
def unknown(cls) -> "TerminalCaps"
```

Caps that assert nothing — the backend keeps its current behaviour.

<a id="bittty.palette"></a>

# bittty.palette

Colour palettes: the index -> RGB mapping a terminal presents.

bittty stores colours symbolically (a `Style` holds an indexed or rgb `Color`);
the palette is the authoritative map an indexed colour resolves *through*. It is
seeded from the model, mutated by OSC colour sequences, and queried by
their `?` forms. Rendering to real pixels stays a terminal (chrome) concern — the
terminal calls `PaletteDevice.resolve()` when it wants RGB.

<a id="bittty.palette.build_256"></a>

#### build\_256

```python
def build_256(base16: tuple[RGB, ...]) -> list[RGB]
```

Build the full 256-colour table: 16 base + 216 colour cube + 24 greys.

<a id="bittty.palette.parse_color_spec"></a>

#### parse\_color\_spec

```python
def parse_color_spec(spec: str) -> RGB | None
```

Parse an X11 colour spec: ``rgb:R/G/B`` or ```RGB```/```RRGGBB```/... .

<a id="bittty.palette.format_rgb"></a>

#### format\_rgb

```python
def format_rgb(rgb: RGB) -> str
```

Format an RGB triple as an X11 ``rgb:rrrr/gggg/bbbb`` reply string.

<a id="bittty.palette.PaletteDefaults"></a>

## PaletteDefaults Objects

```python
@dataclass(frozen=True)
class PaletteDefaults()
```

A terminal's default colours: the 16 ANSI colours plus fg/bg/cursor.

<a id="bittty.present"></a>

# bittty.present

Present events: discrete side-effects the board pushes to the attached terminal (chrome).

Screen content stays *pull* (a terminal (chrome) reads capture_pane()/get_line on its own
cadence). Only these discrete events are *pushed*, through the board's DisplayPort.
Each is a plain frozen dataclass — pure data, no imports from board/devices — so
board.py can depend on this module without a cycle.

<a id="bittty.present.Bell"></a>

## Bell Objects

```python
@dataclass(frozen=True)
class Bell()
```

The terminal bell rang (C0 BEL).

<a id="bittty.present.TitleChanged"></a>

## TitleChanged Objects

```python
@dataclass(frozen=True)
class TitleChanged()
```

Window and/or icon title changed (OSC 0/1/2, XTWINOPS title stack).

<a id="bittty.present.Notification"></a>

## Notification Objects

```python
@dataclass(frozen=True)
class Notification()
```

A desktop notification was posted (OSC 9 / 777 / 99).

<a id="bittty.present.ClipboardChanged"></a>

## ClipboardChanged Objects

```python
@dataclass(frozen=True)
class ClipboardChanged()
```

A clipboard selection was set (OSC 52 write).

<a id="bittty.present.PromptMark"></a>

## PromptMark Objects

```python
@dataclass(frozen=True)
class PromptMark()
```

A shell-integration prompt/command mark (OSC 133).

<a id="bittty.present.PointerShapeChanged"></a>

## PointerShapeChanged Objects

```python
@dataclass(frozen=True)
class PointerShapeChanged()
```

The mouse-pointer shape was requested (OSC 22).

<a id="bittty.present.FontChanged"></a>

## FontChanged Objects

```python
@dataclass(frozen=True)
class FontChanged()
```

The font was set (OSC 50).

<a id="bittty.present.CwdChanged"></a>

## CwdChanged Objects

```python
@dataclass(frozen=True)
class CwdChanged()
```

The reported working directory changed (OSC 7).

<a id="bittty.present.WindowRequest"></a>

## WindowRequest Objects

```python
@dataclass(frozen=True)
class WindowRequest()
```

A window action was requested: "raise" / "lower" / "refresh" (XTWINOPS 5/6/7).

<a id="bittty.present.WindowStateChanged"></a>

## WindowStateChanged Objects

```python
@dataclass(frozen=True)
class WindowStateChanged()
```

Window iconify/maximize/fullscreen/position state changed (XTWINOPS).

<a id="bittty.present.ConsoleRequest"></a>

## ConsoleRequest Objects

```python
@dataclass(frozen=True)
class ConsoleRequest()
```

A virtual-console switch was requested (linux setterm 12/15).

<a id="bittty.present.ConsoleRequest.kind"></a>

#### kind

"switch" / "previous"

<a id="bittty.present.MouseModeChanged"></a>

## MouseModeChanged Objects

```python
@dataclass(frozen=True)
class MouseModeChanged()
```

The requested mouse-tracking mode changed (derived from modes 9/1000/1002/1003).

<a id="bittty.present.MouseModeChanged.mode"></a>

#### mode

"off" / "basic" / "button" / "any"

<a id="bittty.present.MouseModeChanged.sgr"></a>

#### sgr

SGR (1006) encoding requested

<a id="bittty.present.CursorVisibilityChanged"></a>

## CursorVisibilityChanged Objects

```python
@dataclass(frozen=True)
class CursorVisibilityChanged()
```

Text-cursor visibility changed (DECTCEM, mode 25).

<a id="bittty.present.SyncOutputChanged"></a>

## SyncOutputChanged Objects

```python
@dataclass(frozen=True)
class SyncOutputChanged()
```

Synchronized-output mode toggled (mode 2026); a terminal (chrome) gates repaint on it.

