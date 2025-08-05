<a id="plansi"></a>

# plansi

plansi - Plays videos as differential ANSI in terminals.

<a id="plansi.player"></a>

# plansi.player

Main Player class that orchestrates video playback with differential rendering.

<a id="plansi.player.Player"></a>

## Player Objects

```python
class Player()
```

Video player that generates (timestamp, ansi_str) tuples.

<a id="plansi.player.Player.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int = 80,
             color_threshold: float = 5.0,
             fps: float = None,
             no_diff: bool = False,
             debug: bool = False,
             realtime: bool = True)
```

Initialize video player.

**Arguments**:

- `width` - Terminal width in characters
- `color_threshold` - RGB distance threshold for color changes (0.0-441.0)
- `fps` - Target playback FPS, None for original rate
- `no_diff` - Disable differential rendering
- `debug` - Enable debug output
- `realtime` - Skip frames to maintain real-time playback (True for console, False for cast files)

<a id="plansi.player.Player.play"></a>

#### play

```python
def play(video_path: str) -> Iterator[Tuple[float, str]]
```

Generate (timestamp, ansi_str) tuples for video playbook.

**Arguments**:

- `video_path` - Path to video file
  

**Yields**:

  Tuples of (timestamp_seconds, ansi_escape_sequences)

<a id="plansi.player.Player.frames"></a>

#### frames

```python
def frames(video_path: str) -> Iterator[Tuple[float, str]]
```

Generate raw frame data without timing delays.

**Arguments**:

- `video_path` - Path to video file
  

**Yields**:

  Tuples of (timestamp_seconds, ansi_escape_sequences)

<a id="plansi.player.Player.cast_entries"></a>

#### cast\_entries

```python
def cast_entries(video_path: str) -> Iterator[str]
```

Generate .cast file entries (JSON lines).

**Arguments**:

- `video_path` - Path to video file
  

**Yields**:

  JSON strings for .cast file format

<a id="plansi.core.video"></a>

# plansi.core.video

Video frame extraction using PyAV with scaling.

<a id="plansi.core.video.VideoExtractor"></a>

## VideoExtractor Objects

```python
class VideoExtractor()
```

Extracts and scales video frames using PyAV.

<a id="plansi.core.video.VideoExtractor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(video_path: str, width: int, fps: float = None)
```

Initialize video extractor.

**Arguments**:

- `video_path` - Path to video file
- `width` - Target width in characters (height auto-calculated)
- `fps` - Target FPS, None for original rate

<a id="plansi.core.video.VideoExtractor.frames"></a>

#### frames

```python
def frames() -> Iterator[Tuple[float, Image.Image]]
```

Generate (timestamp, PIL.Image) tuples.

<a id="plansi.core"></a>

# plansi.core

<a id="plansi.core.terminal_render"></a>

# plansi.core.terminal\_render

ANSI rendering using bittty terminal emulator with dual buffer approach.

<a id="plansi.core.terminal_render.TerminalRenderer"></a>

## TerminalRenderer Objects

```python
class TerminalRenderer()
```

Renders frames using bittty dual buffer approach.

- Main buffer: What we've sent to the real terminal
- Alt buffer: New frame rendered with chafa
- Diff the buffers and output only changed cells

<a id="plansi.core.terminal_render.TerminalRenderer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int,
             height: int,
             color_threshold: float = 5.0,
             debug: bool = False)
```

Initialize terminal renderer.

**Arguments**:

- `width` - Width in character cells
- `height` - Height in character cells
- `color_threshold` - RGB distance threshold for color changes (0.0-441.67)
- `debug` - Enable debug output

<a id="plansi.core.terminal_render.TerminalRenderer.render_differential"></a>

#### render\_differential

```python
def render_differential(
        image: Image.Image, changed_cells: Set[Tuple[int,
                                                     int]]) -> Tuple[str, int]
```

Render only changed cells using dual buffer approach.

**Arguments**:

- `image` - Current frame as PIL Image
- `changed_cells` - Set of (cell_x, cell_y) that have changed (IGNORED)
  

**Returns**:

  Tuple of (ANSI string with cursor movements and cell updates, number of changed cells)

<a id="plansi.core.terminal_render.TerminalRenderer.clear_cache"></a>

#### clear\_cache

```python
def clear_cache()
```

Clear both buffers to force full refresh.

<a id="plansi.__main__"></a>

# plansi.\_\_main\_\_

Command-line interface for plansi.

<a id="plansi.__main__.main"></a>

#### main

```python
def main()
```

Main CLI entry point.

<a id="plansi.__main__.play_to_console"></a>

#### play\_to\_console

```python
def play_to_console(player: Player, video_path: str)
```

Play video to console (timing handled by Player.play() with realtime flag).

<a id="plansi.__main__.write_cast_file"></a>

#### write\_cast\_file

```python
def write_cast_file(player: Player, video_path: str, output_path: str)
```

Write video to .cast file format.

