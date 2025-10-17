<a id="sh2mp4"></a>

# sh2mp4

sh2mp4 - Records shell commands to MP4 videos

<a id="sh2mp4.check_deps"></a>

# sh2mp4.check\_deps

Check dependencies for sh2mp4

<a id="sh2mp4.check_deps.check_command"></a>

#### check\_command

```python
def check_command(cmd: str) -> bool
```

Check if a command is available in PATH

<a id="sh2mp4.check_deps.check_locale"></a>

#### check\_locale

```python
def check_locale() -> bool
```

Check if en_US.UTF-8 locale is available

<a id="sh2mp4.check_deps.check_monospace_fonts"></a>

#### check\_monospace\_fonts

```python
def check_monospace_fonts() -> bool
```

Check if monospace fonts are available

<a id="sh2mp4.check_deps.get_required_commands"></a>

#### get\_required\_commands

```python
def get_required_commands(cast_file_mode: bool = False) -> list[str]
```

Get list of required commands based on mode

<a id="sh2mp4.check_deps.check_runtime_dependencies"></a>

#### check\_runtime\_dependencies

```python
def check_runtime_dependencies(cast_file_mode: bool = False) -> list[str]
```

Check runtime dependencies and return list of missing commands

<a id="sh2mp4.check_deps.main"></a>

#### main

```python
def main() -> int
```

Check all dependencies and report status

<a id="sh2mp4.xserver"></a>

# sh2mp4.xserver

X server management utilities

<a id="sh2mp4.xserver.XServerInfo"></a>

## XServerInfo Objects

```python
class XServerInfo()
```

Information about an X server

<a id="sh2mp4.xserver.find_available_display"></a>

#### find\_available\_display

```python
async def find_available_display() -> int
```

Find the next available X display number

<a id="sh2mp4.xserver.is_display_in_use"></a>

#### is\_display\_in\_use

```python
async def is_display_in_use(display_num: int) -> bool
```

Check if a display number is already in use

<a id="sh2mp4.xserver.list_running_xservers"></a>

#### list\_running\_xservers

```python
async def list_running_xservers() -> List[XServerInfo]
```

List all currently running X servers

<a id="sh2mp4.xserver.get_newest_xserver"></a>

#### get\_newest\_xserver

```python
async def get_newest_xserver() -> Optional[XServerInfo]
```

Get the most recently started X server

<a id="sh2mp4.xserver.test_display_connection"></a>

#### test\_display\_connection

```python
async def test_display_connection(display_name: str) -> bool
```

Test if we can connect to a display

<a id="sh2mp4.themes"></a>

# sh2mp4.themes

Terminal color themes for sh2mp4

<a id="sh2mp4.themes.Theme"></a>

## Theme Objects

```python
@dataclass
class Theme()
```

Represents a terminal color theme

<a id="sh2mp4.themes.Theme.colors"></a>

#### colors

Colors 0-15

<a id="sh2mp4.themes.Theme.xterm_args"></a>

#### xterm\_args

```python
@property
def xterm_args() -> list[str]
```

Generate xterm arguments for this theme

<a id="sh2mp4.themes.get_theme"></a>

#### get\_theme

```python
def get_theme(name: str) -> Theme
```

Get a theme by name, falling back to default

<a id="sh2mp4.themes.list_themes"></a>

#### list\_themes

```python
def list_themes() -> list[str]
```

List available theme names

<a id="sh2mp4.measure_fonts"></a>

# sh2mp4.measure\_fonts

Font measurement utility for sh2mp4

<a id="sh2mp4.measure_fonts.main"></a>

#### main

```python
def main() -> int
```

Main entry point for measure-fonts command

<a id="sh2mp4.args"></a>

# sh2mp4.args

Argument parsing for sh2mp4

<a id="sh2mp4.args.parse_args"></a>

#### parse\_args

```python
def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace
```

Parse command line arguments - simple and straightforward

<a id="sh2mp4.args.parse_and_validate_args"></a>

#### parse\_and\_validate\_args

```python
def parse_and_validate_args(
        argv: Optional[list[str]] = None) -> argparse.Namespace
```

Legacy wrapper - just parse args normally

<a id="sh2mp4.recorder"></a>

# sh2mp4.recorder

Screen recording using ffmpeg

<a id="sh2mp4.recorder.Recorder"></a>

## Recorder Objects

```python
class Recorder()
```

Handles screen recording with ffmpeg

<a id="sh2mp4.recorder.Recorder.start"></a>

#### start

```python
async def start() -> None
```

Start recording the display

<a id="sh2mp4.recorder.Recorder.stop"></a>

#### stop

```python
async def stop() -> int
```

Stop recording and return exit code

<a id="sh2mp4.recorder.Recorder.is_running"></a>

#### is\_running

```python
async def is_running() -> bool
```

Check if recording is active

<a id="sh2mp4.display"></a>

# sh2mp4.display

Virtual display management using Xvfb

<a id="sh2mp4.display.DisplayManager"></a>

## DisplayManager Objects

```python
class DisplayManager()
```

Manages a virtual X display using Xvfb

<a id="sh2mp4.display.DisplayManager.start"></a>

#### start

```python
async def start(width: int, height: int) -> None
```

Start the virtual display and window manager

<a id="sh2mp4.display.DisplayManager.stop"></a>

#### stop

```python
async def stop() -> None
```

Stop the display and clean up

<a id="sh2mp4.display.DisplayManager.is_ready"></a>

#### is\_ready

```python
async def is_ready() -> bool
```

Check if the display is ready for use

<a id="sh2mp4.__main__"></a>

# sh2mp4.\_\_main\_\_

Main entry point for sh2mp4

<a id="sh2mp4.__main__.record_command"></a>

#### record\_command

```python
async def record_command(args) -> int
```

Main recording function

<a id="sh2mp4.__main__.main"></a>

#### main

```python
def main() -> int
```

Main entry point

<a id="sh2mp4.asciicast"></a>

# sh2mp4.asciicast

Asciinema cast file handling and optimization

<a id="sh2mp4.asciicast.CastConfig"></a>

## CastConfig Objects

```python
class CastConfig(NamedTuple)
```

Configuration for recording a cast file

<a id="sh2mp4.asciicast.get_cast_dimensions"></a>

#### get\_cast\_dimensions

```python
def get_cast_dimensions(cast_file: Path) -> tuple[int, int]
```

Get optimal dimensions for cast file recording

<a id="sh2mp4.asciicast.get_cast_command"></a>

#### get\_cast\_command

```python
def get_cast_command(cast_file: Path, playback_speed: float = 1.0) -> str
```

Get the command to play back a cast file

<a id="sh2mp4.asciicast.get_cast_config"></a>

#### get\_cast\_config

```python
def get_cast_config(cast_file: Path,
                    playback_speed: float = 1.0,
                    base_fps: int = 30) -> CastConfig
```

Get complete configuration for recording a cast file

<a id="sh2mp4.ascii_preview"></a>

# sh2mp4.ascii\_preview

Simple ASCII art preview for terminal display

<a id="sh2mp4.ascii_preview.image_to_ascii"></a>

#### image\_to\_ascii

```python
def image_to_ascii(image_path: Path,
                   width: int = 80,
                   height: int = 24) -> Optional[str]
```

Convert an image to ASCII art for terminal display

<a id="sh2mp4.ascii_preview.colored_blocks_preview"></a>

#### colored\_blocks\_preview

```python
def colored_blocks_preview(image_path: Path,
                           width: int = 80,
                           height: int = 24) -> Optional[str]
```

Convert image to colored Unicode block characters

<a id="sh2mp4.terminal"></a>

# sh2mp4.terminal

Terminal (xterm) management for command execution

<a id="sh2mp4.terminal.TerminalManager"></a>

## TerminalManager Objects

```python
class TerminalManager()
```

Manages an xterm instance for command execution

<a id="sh2mp4.terminal.TerminalManager.start"></a>

#### start

```python
async def start(command: str) -> None
```

Start xterm and execute the command

<a id="sh2mp4.terminal.TerminalManager.signal_recorder_ready"></a>

#### signal\_recorder\_ready

```python
def signal_recorder_ready() -> None
```

Signal that the recorder is ready and command can proceed

<a id="sh2mp4.terminal.TerminalManager.wait_for_completion"></a>

#### wait\_for\_completion

```python
async def wait_for_completion() -> int
```

Wait for the terminal/command to complete and return exit code

<a id="sh2mp4.terminal.TerminalManager.is_running"></a>

#### is\_running

```python
async def is_running() -> bool
```

Check if the terminal is still running

<a id="sh2mp4.terminal.TerminalManager.stop"></a>

#### stop

```python
async def stop() -> None
```

Stop the terminal and clean up

<a id="sh2mp4.peep"></a>

# sh2mp4.peep

Live preview of X displays for debugging recordings

<a id="sh2mp4.peep.list_displays"></a>

#### list\_displays

```python
async def list_displays() -> int
```

List all available X displays

<a id="sh2mp4.peep.peep_display"></a>

#### peep\_display

```python
async def peep_display(display_name: str, interval: float = 0.1) -> int
```

Monitor an X display and show live preview using chafa

<a id="sh2mp4.peep.create_parser"></a>

#### create\_parser

```python
def create_parser() -> argparse.ArgumentParser
```

Create argument parser for peep command

<a id="sh2mp4.peep.main_async"></a>

#### main\_async

```python
async def main_async(args) -> int
```

Async main function

<a id="sh2mp4.peep.main"></a>

#### main

```python
def main() -> int
```

Main entry point for peep command

<a id="sh2mp4.fonts"></a>

# sh2mp4.fonts

Font handling and character dimension calculation

<a id="sh2mp4.fonts.FontMetrics"></a>

## FontMetrics Objects

```python
@dataclass
class FontMetrics()
```

Character dimensions for a specific font and size

<a id="sh2mp4.fonts.get_font_metrics"></a>

#### get\_font\_metrics

```python
def get_font_metrics(font_name: str, font_size: int) -> FontMetrics
```

Get character dimensions for a font and size.
Falls back to pre-measured values for DejaVu Sans Mono.

<a id="sh2mp4.fonts.measure_font"></a>

#### measure\_font

```python
def measure_font(font_name: str, font_size: int) -> FontMetrics
```

Dynamically measure font character dimensions using tkinter

<a id="sh2mp4.fonts.measure_all_fonts"></a>

#### measure\_all\_fonts

```python
def measure_all_fonts() -> Dict[str, Dict[int, FontMetrics]]
```

Measure all common monospace fonts at various sizes

<a id="sh2mp4.fonts.calculate_window_dimensions"></a>

#### calculate\_window\_dimensions

```python
def calculate_window_dimensions(cols: int, lines: int, font_name: str,
                                font_size: int) -> Tuple[int, int]
```

Calculate pixel dimensions for terminal window with padding for xterm margins

