<a id="lsoph"></a>

# lsoph

<a id="lsoph.ui"></a>

# lsoph.ui

<a id="lsoph.ui.app"></a>

# lsoph.ui.app

Main Textual application class for lsoph.

<a id="lsoph.ui.app.FileApp"></a>

## FileApp Objects

```python
class FileApp(App[None])
```

Textual file monitor application.

<a id="lsoph.ui.app.FileApp.__init__"></a>

#### \_\_init\_\_

```python
def __init__(monitor: Monitor, log_queue: deque, backend_func: BackendFuncType,
             backend_args: BackendArgsType,
             backend_worker_func: BackendWorkerFuncType)
```

Initialize the FileApp.

<a id="lsoph.ui.app.FileApp.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Create child widgets for the main application screen.

<a id="lsoph.ui.app.FileApp.on_mount"></a>

#### on\_mount

```python
def on_mount() -> None
```

Called when the app screen is mounted.

<a id="lsoph.ui.app.FileApp.update_status"></a>

#### update\_status

```python
def update_status(text: str)
```

Helper to update the status bar widget safely.

<a id="lsoph.ui.app.FileApp.update_table"></a>

#### update\_table

```python
def update_table() -> None
```

Updates the DataTable with the latest file information.

<a id="lsoph.ui.app.FileApp.on_data_table_row_selected"></a>

#### on\_data\_table\_row\_selected

```python
def on_data_table_row_selected(event: DataTable.RowSelected) -> None
```

Called when the user presses Enter on a DataTable row.

<a id="lsoph.ui.app.FileApp.action_quit"></a>

#### action\_quit

```python
def action_quit() -> None
```

Action to quit the application.

<a id="lsoph.ui.app.FileApp.action_ignore_selected"></a>

#### action\_ignore\_selected

```python
def action_ignore_selected() -> None
```

Action to ignore the currently selected file path.

<a id="lsoph.ui.app.FileApp.action_ignore_all"></a>

#### action\_ignore\_all

```python
def action_ignore_all() -> None
```

Action to ignore all currently tracked files.

<a id="lsoph.ui.app.FileApp.action_show_log"></a>

#### action\_show\_log

```python
def action_show_log() -> None
```

Action to show or hide the log screen.

<a id="lsoph.ui.app.FileApp.action_dump_monitor"></a>

#### action\_dump\_monitor

```python
def action_dump_monitor() -> None
```

Debug action to dump monitor state to log.

<a id="lsoph.ui.detail_screen"></a>

# lsoph.ui.detail\_screen

Modal screen for displaying file event history.

<a id="lsoph.ui.detail_screen.DetailScreen"></a>

## DetailScreen Objects

```python
class DetailScreen(ModalScreen[None])
```

Screen to display event history for a specific file.

<a id="lsoph.ui.detail_screen.DetailScreen.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Create child widgets for the detail screen.

<a id="lsoph.ui.detail_screen.DetailScreen.on_mount"></a>

#### on\_mount

```python
def on_mount() -> None
```

Called when the screen is mounted. Populates the log.

<a id="lsoph.ui.log_screen"></a>

# lsoph.ui.log\_screen

Modal screen for displaying application logs.

<a id="lsoph.ui.log_screen.LogScreen"></a>

## LogScreen Objects

```python
class LogScreen(ModalScreen[None])
```

A modal screen to display application logs using RichLog.

<a id="lsoph.ui.log_screen.LogScreen.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Create child widgets for the log screen.

<a id="lsoph.ui.log_screen.LogScreen.on_mount"></a>

#### on\_mount

```python
def on_mount() -> None
```

Called when the screen is mounted.

<a id="lsoph.ui.log_screen.LogScreen.on_unmount"></a>

#### on\_unmount

```python
def on_unmount() -> None
```

Called when the screen is unmounted.

<a id="lsoph.ui.log_screen.LogScreen.action_clear_log"></a>

#### action\_clear\_log

```python
def action_clear_log() -> None
```

Action to clear the log display.

<a id="lsoph.backend.strace"></a>

# lsoph.backend.strace

<a id="lsoph.backend.strace.attach"></a>

#### attach

```python
def attach(pids_or_tids: list[int],
           monitor: Monitor,
           syscalls: list[str] = DEFAULT_SYSCALLS)
```

Attaches strace to existing PIDs/TIDs and processes events.

<a id="lsoph.backend.strace.run"></a>

#### run

```python
def run(command: list[str],
        monitor: Monitor,
        syscalls: list[str] = DEFAULT_SYSCALLS)
```

Launches a command via strace and processes events.

<a id="lsoph.backend.strace.main"></a>

#### main

```python
def main(argv: list[str] | None = None) -> int
```

Command-line entry point for testing strace adapter.

<a id="lsoph.backend"></a>

# lsoph.backend

<a id="lsoph.backend.lsof"></a>

# lsoph.backend.lsof

<a id="lsoph.backend.lsof.log"></a>

#### log

Use package-aware logger name

<a id="lsoph.backend.lsof.attach"></a>

#### attach

```python
def attach(pids: List[int], monitor: Monitor) -> None
```

Standard attach function which monitors the specified PIDs without tracking descendants.
For command execution with descendants tracking, use _attach_with_descendants.

<a id="lsoph.backend.lsof.run"></a>

#### run

```python
def run(command: List[str], monitor: Monitor) -> None
```

Run a command and monitor its open files using lsof.

<a id="lsoph.backend.psutil"></a>

# lsoph.backend.psutil

<a id="lsoph.backend.psutil.PsutilBackend"></a>

## PsutilBackend Objects

```python
class PsutilBackend()
```

Backend implementation that uses psutil to monitor file activities.

<a id="lsoph.backend.psutil.PsutilBackend.attach"></a>

#### attach

```python
def attach(pids: List[int], monitor: Monitor) -> None
```

Attach to existing processes.

<a id="lsoph.backend.psutil.PsutilBackend.run"></a>

#### run

```python
def run(command: List[str], monitor: Monitor) -> None
```

Run a command and monitor its file activity.

<a id="lsoph.backend.psutil.attach"></a>

#### attach

```python
def attach(pids: List[int], monitor: Monitor) -> None
```

Attach to existing processes.

<a id="lsoph.backend.psutil.run"></a>

#### run

```python
def run(command: List[str], monitor: Monitor) -> None
```

Run a command and monitor its file activity.

<a id="lsoph.backend.strace_cmd"></a>

# lsoph.backend.strace\_cmd

<a id="lsoph.backend.strace_cmd.stream_strace_output"></a>

#### stream\_strace\_output

```python
def stream_strace_output(
        monitor: Monitor,
        target_command: list[str] | None = None,
        attach_ids: list[int] | None = None,
        syscalls: list[str] = DEFAULT_SYSCALLS) -> Iterator[str]
```

Runs strace, yields output lines, stores strace PID in monitor.

<a id="lsoph.backend.strace_cmd.parse_strace_stream"></a>

#### parse\_strace\_stream

```python
def parse_strace_stream(
        monitor: Monitor,
        target_command: list[str] | None = None,
        attach_ids: list[int] | None = None,
        syscalls: list[str] = DEFAULT_SYSCALLS) -> Iterator[Syscall]
```

Runs strace via stream_strace_output, parses lines into Syscall objects.

<a id="lsoph.monitor"></a>

# lsoph.monitor

<a id="lsoph.monitor.log"></a>

#### log

Use package-aware logger name

<a id="lsoph.monitor.FileInfo"></a>

## FileInfo Objects

```python
@dataclass
class FileInfo()
```

Holds state information about a single tracked file.

<a id="lsoph.monitor.FileInfo.open_by_pids"></a>

#### open\_by\_pids

Key: pid, Value: set[fd]

<a id="lsoph.monitor.FileInfo.is_open"></a>

#### is\_open

```python
@property
def is_open() -> bool
```

Checks if any process currently holds this file open according to state.

<a id="lsoph.monitor.Monitor"></a>

## Monitor Objects

```python
class Monitor(Versioned)
```

Manages the state of files accessed by a monitored target (process group).
Inherits from Versioned for change tracking and thread safety.
Provides direct iteration and dictionary-style access.

<a id="lsoph.monitor.Monitor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(identifier: str)
```

Initialize the Monitor.

**Arguments**:

- `identifier` - A string identifying the monitoring session (e.g., command or PIDs).

<a id="lsoph.monitor.Monitor.ignore"></a>

#### ignore

```python
@changes
def ignore(path: str)
```

Adds a path to the ignore list (in-memory only).

<a id="lsoph.monitor.Monitor.ignore_all"></a>

#### ignore\_all

```python
@changes
def ignore_all()
```

Adds all currently tracked file paths to the ignore list (in-memory only).

<a id="lsoph.monitor.Monitor.process_exit"></a>

#### process\_exit

```python
@changes
def process_exit(pid: int, timestamp: float)
```

Handles cleanup when a process exits (e.g., receives exit_group).

<a id="lsoph.cli"></a>

# lsoph.cli

<a id="lsoph.cli.TextualLogHandler"></a>

## TextualLogHandler Objects

```python
class TextualLogHandler(logging.Handler)
```

A logging handler that puts messages into a deque for Textual.

<a id="lsoph.cli.TextualLogHandler.emit"></a>

#### emit

```python
def emit(record: logging.LogRecord)
```

Emit a record, formatting it as a string with Rich markup.

<a id="lsoph.cli.run_backend_worker"></a>

#### run\_backend\_worker

```python
def run_backend_worker(backend_func: BackendFuncType,
                       monitor_instance: Monitor,
                       target_args: BackendArgsType)
```

Target function to run the selected backend in a background worker/thread.

<a id="lsoph.cli.main"></a>

#### main

```python
def main(argv: list[str] | None = None) -> int
```

Parses command line arguments, sets up logging and monitor,
and launches the UI, passing backend details for later execution.

<a id="lsoph.util"></a>

# lsoph.util

<a id="lsoph.util.pid"></a>

# lsoph.util.pid

<a id="lsoph.util.pid.log"></a>

#### log

Get logger instance

<a id="lsoph.util.pid.get_descendants"></a>

#### get\_descendants

```python
def get_descendants(parent_pid: int) -> list[int]
```

Retrieves a list of all descendant process IDs (PIDs) for a given parent PID.

<a id="lsoph.util.pid.get_cwd"></a>

#### get\_cwd

```python
def get_cwd(pid: int) -> str | None
```

Retrieves the Current Working Directory (CWD) for a given PID.

Uses psutil for cross-platform compatibility where possible, falling
back to /proc/<pid>/cwd on Linux if needed (though psutil usually handles this).

**Arguments**:

- `pid` - The Process ID.
  

**Returns**:

  The absolute path string of the CWD, or None if the process doesn't exist,
  access is denied, or the CWD cannot be determined.

<a id="lsoph.util.pid.main"></a>

#### main

```python
def main(argv: list[str] | None = None) -> int
```

Command-line entry point for testing pid functions.

<a id="lsoph.util.versioned"></a>

# lsoph.util.versioned

<a id="lsoph.util.versioned.Versioned"></a>

## Versioned Objects

```python
class Versioned()
```

Inherit this class to store a version number on each change.

<a id="lsoph.util.versioned.Versioned.change"></a>

#### change

```python
def change()
```

Call this if you changed something and need to blow caches

<a id="lsoph.util.versioned.Versioned.version"></a>

#### version

```python
@property
def version()
```

Return the version number of this object.

<a id="lsoph.util.versioned.Versioned.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Versionable objects are cacheable ones

<a id="lsoph.util.versioned.changes"></a>

#### changes

```python
def changes(method)
```

Decorate methods with this if they make changes to the object

<a id="lsoph.util.versioned.waits"></a>

#### waits

```python
def waits(method)
```

Decorate methods with this if they need to wait for changes

<a id="lsoph.util.short_path"></a>

# lsoph.util.short\_path

Utility functions for lsoph.

<a id="lsoph.util.short_path.short_path"></a>

#### short\_path

```python
def short_path(path: str | os.PathLike,
               max_length: int,
               cwd: str = CWD) -> str
```

Shortens a file path string to fit max_length:
1. Tries to make path relative to CWD.
2. Prioritizes filename.
3. If filename too long, truncate filename from left "...name".
4. If path too long but filename fits, truncate directory in middle "dir...ectory/name".

**Arguments**:

- `path` - The file path string or path-like object.
- `max_length` - The maximum allowed length for the output string.
  

**Returns**:

  The shortened path string.

