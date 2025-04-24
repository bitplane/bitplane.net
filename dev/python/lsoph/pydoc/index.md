<a id="lsoph"></a>

# lsoph

<a id="lsoph.ui"></a>

# lsoph.ui

<a id="lsoph.ui.file_data_table"></a>

# lsoph.ui.file\_data\_table

A specialized DataTable widget using index-as-key for partial updates.
NOTE: This approach uses the visual index as the RowKey, which can lead
      to unexpected behavior if rows are added/removed in ways that disrupt
      the expected visual order compared to the underlying data sort order.

<a id="lsoph.ui.file_data_table.COLUMN_KEYS"></a>

#### COLUMN\_KEYS

Order must match TableRow

<a id="lsoph.ui.file_data_table.FileDataTable"></a>

## FileDataTable Objects

```python
class FileDataTable(DataTable)
```

A DataTable specialized for displaying and managing FileInfo.
Uses stringified index as RowKey and attempts partial updates.
Simplified error handling and logging.
Attempts to maintain relative cursor screen position during updates.

<a id="lsoph.ui.file_data_table.FileDataTable.RECENT_COL_WIDTH"></a>

#### RECENT\_COL\_WIDTH

Width for emoji history (e.g., 5 emojis + padding)

<a id="lsoph.ui.file_data_table.FileDataTable.AGE_COL_WIDTH"></a>

#### AGE\_COL\_WIDTH

width of the age column

<a id="lsoph.ui.file_data_table.FileDataTable.SCROLLBAR_WIDTH"></a>

#### SCROLLBAR\_WIDTH

just a guess 🤷

<a id="lsoph.ui.file_data_table.FileDataTable.COLUMN_PADDING"></a>

#### COLUMN\_PADDING

User's estimate for padding per column

<a id="lsoph.ui.file_data_table.FileDataTable.on_mount"></a>

#### on\_mount

```python
def on_mount() -> None
```

Set up columns on mount.

<a id="lsoph.ui.file_data_table.FileDataTable.selected_path"></a>

#### selected\_path

```python
@property
def selected_path() -> Optional[str]
```

Returns the path string of the data visually at the cursor row.

<a id="lsoph.ui.file_data_table.FileDataTable.on_resize"></a>

#### on\_resize

```python
def on_resize(event: events.Resize) -> None
```

Update path column width on resize.

<a id="lsoph.ui.file_data_table.FileDataTable.update_data"></a>

#### update\_data

```python
def update_data(infos: list[FileInfo]) -> None
```

Updates the table content using index as key and attempting partial updates.
Attempts to maintain relative cursor screen position.

<a id="lsoph.ui.app"></a>

# lsoph.ui.app

Main Textual application class for lsoph.

<a id="lsoph.ui.app.LsophApp"></a>

## LsophApp Objects

```python
class LsophApp(App[None])
```

Textual file monitor application for lsoph.

<a id="lsoph.ui.app.LsophApp.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Create child widgets for the main application screen.

<a id="lsoph.ui.app.LsophApp.start_backend_worker"></a>

#### start\_backend\_worker

```python
def start_backend_worker()
```

Starts the background worker to run the backend's async method.

<a id="lsoph.ui.app.LsophApp.cancel_backend_worker"></a>

#### cancel\_backend\_worker

```python
async def cancel_backend_worker()
```

Signals the backend instance to stop and cancels the Textual worker.

<a id="lsoph.ui.app.LsophApp.on_mount"></a>

#### on\_mount

```python
def on_mount() -> None
```

Called when the app screen is mounted.

<a id="lsoph.ui.app.LsophApp.on_unmount"></a>

#### on\_unmount

```python
async def on_unmount() -> None
```

Called when the app is unmounted (e.g., on quit).

<a id="lsoph.ui.app.LsophApp.watch_last_monitor_version"></a>

#### watch\_last\_monitor\_version

```python
def watch_last_monitor_version(old_version: int, new_version: int) -> None
```

Triggers table update when monitor version changes.

<a id="lsoph.ui.app.LsophApp.watch_status_text"></a>

#### watch\_status\_text

```python
def watch_status_text(old_text: str, new_text: str) -> None
```

Updates the status bar widget when status_text changes.

<a id="lsoph.ui.app.LsophApp.check_monitor_version"></a>

#### check\_monitor\_version

```python
def check_monitor_version()
```

Periodically checks the monitor's version and worker status.

<a id="lsoph.ui.app.LsophApp.update_status"></a>

#### update\_status

```python
def update_status(text: str)
```

Helper method to update the reactive status_text variable.

<a id="lsoph.ui.app.LsophApp.on_data_table_row_selected"></a>

#### on\_data\_table\_row\_selected

```python
def on_data_table_row_selected(event: DataTable.RowSelected) -> None
```

Handle row selection (Enter key) - show details.

<a id="lsoph.ui.app.LsophApp.on_data_table_row_activated"></a>

#### on\_data\_table\_row\_activated

```python
def on_data_table_row_activated(event: "DataTable.RowActivated") -> None
```

Handle row activation (Double Click) - show details.

<a id="lsoph.ui.app.LsophApp.action_quit"></a>

#### action\_quit

```python
async def action_quit() -> None
```

Action to quit the application.

<a id="lsoph.ui.app.LsophApp.action_ignore_selected"></a>

#### action\_ignore\_selected

```python
def action_ignore_selected() -> None
```

Action to ignore the currently selected file path.

<a id="lsoph.ui.app.LsophApp.action_ignore_all"></a>

#### action\_ignore\_all

```python
def action_ignore_all() -> None
```

Action to ignore all currently tracked files.

<a id="lsoph.ui.app.LsophApp.action_show_log"></a>

#### action\_show\_log

```python
def action_show_log() -> None
```

Action to show or hide the log screen.

<a id="lsoph.ui.app.LsophApp.action_show_detail"></a>

#### action\_show\_detail

```python
def action_show_detail() -> None
```

Shows the detail screen for the selected row (requires focus check).

<a id="lsoph.ui.app.LsophApp.action_scroll_home"></a>

#### action\_scroll\_home

```python
def action_scroll_home() -> None
```

Scrolls the file table to the top.

<a id="lsoph.ui.app.LsophApp.action_scroll_end"></a>

#### action\_scroll\_end

```python
def action_scroll_end() -> None
```

Scrolls the file table to the bottom.

<a id="lsoph.ui.app.LsophApp.action_dump_monitor"></a>

#### action\_dump\_monitor

```python
def action_dump_monitor() -> None
```

Debug action to dump monitor state to log.

<a id="lsoph.ui.emoji"></a>

# lsoph.ui.emoji

Generates emoji history strings for file activity.

<a id="lsoph.ui.emoji.get_emoji_history_string"></a>

#### get\_emoji\_history\_string

```python
def get_emoji_history_string(file_info: FileInfo, max_len: int = 5) -> str
```

Generates a string of emojis representing recent file activity history.

**Arguments**:

- `file_info` - The FileInfo object containing the event history.
- `max_len` - The maximum number of emojis to include in the string.
  

**Returns**:

  A string of emojis (most recent first), padded with spaces.

<a id="lsoph.ui.detail_screen"></a>

# lsoph.ui.detail\_screen

Screen to display file event history using a DataTable.

<a id="lsoph.ui.detail_screen.DetailScreen"></a>

## DetailScreen Objects

```python
class DetailScreen(Screen)
```

Screen to display event history and details for a specific file using DataTable.

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

Called when the screen is mounted. Populates the DataTable.

<a id="lsoph.ui.log_screen"></a>

# lsoph.ui.log\_screen

Full-screen display for application logs.

<a id="lsoph.ui.log_screen.LogScreen"></a>

## LogScreen Objects

```python
class LogScreen(Screen)
```

A full screen to display application logs using RichLog.

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

Called when the screen is mounted. Populates with existing logs and starts timer.

<a id="lsoph.ui.log_screen.LogScreen.on_unmount"></a>

#### on\_unmount

```python
def on_unmount() -> None
```

Called when the screen is unmounted. Stops the timer.

<a id="lsoph.ui.log_screen.LogScreen.action_clear_log"></a>

#### action\_clear\_log

```python
def action_clear_log() -> None
```

Action to clear the log display.

<a id="lsoph.backend"></a>

# lsoph.backend

LSOPH Backend Package.

<a id="lsoph.backend.log"></a>

#### log

Logger for this package

<a id="lsoph.backend.base"></a>

# lsoph.backend.base

Base definitions for asynchronous monitoring backends.

<a id="lsoph.backend.base.Backend"></a>

## Backend Objects

```python
class Backend(ABC)
```

Abstract Base Class for all monitoring backends.

<a id="lsoph.backend.base.Backend.backend_name"></a>

#### backend\_name

Default, should be overridden

<a id="lsoph.backend.base.Backend.__init__"></a>

#### \_\_init\_\_

```python
def __init__(monitor: Monitor)
```

Initialize the backend.

<a id="lsoph.backend.base.Backend.is_available"></a>

#### is\_available

```python
@staticmethod
@abstractmethod
def is_available() -> bool
```

Check if the backend's dependencies (e.g., executable) are met.
This MUST be implemented by subclasses.

<a id="lsoph.backend.base.Backend.attach"></a>

#### attach

```python
@abstractmethod
async def attach(pids: list[int])
```

Asynchronously attach to and monitor existing process IDs.
Should periodically check `self.should_stop`.

<a id="lsoph.backend.base.Backend.run_command"></a>

#### run\_command

```python
async def run_command(command: list[str])
```

Default implementation to run a command and monitor it using the backend's attach method.
Backends like strace should override this if they have a different run mechanism.

<a id="lsoph.backend.base.Backend.stop"></a>

#### stop

```python
async def stop()
```

Signals the backend's running task to stop and terminates the managed process if any.

<a id="lsoph.backend.base.Backend.should_stop"></a>

#### should\_stop

```python
@property
def should_stop() -> bool
```

Check if the stop event has been set.

<a id="lsoph.backend.strace.handlers"></a>

# lsoph.backend.strace.handlers

Syscall handlers and CWD update logic for the strace backend.

<a id="lsoph.backend.strace.handlers.update_cwd"></a>

#### update\_cwd

```python
def update_cwd(pid: int, cwd_map: dict[int, str], monitor: Monitor,
               event: Syscall)
```

Updates the CWD map based on chdir or fchdir syscalls.

<a id="lsoph.backend.strace.terminate"></a>

# lsoph.backend.strace.terminate

Contains logic for terminating the strace process.

<a id="lsoph.backend.strace.terminate.log"></a>

#### log

Use module-specific logger

<a id="lsoph.backend.strace.terminate.terminate_strace_process"></a>

#### terminate\_strace\_process

```python
async def terminate_strace_process(process: asyncio.subprocess.Process | None,
                                   pid: int)
```

Helper to terminate the strace process robustly.

<a id="lsoph.backend.strace"></a>

# lsoph.backend.strace

<a id="lsoph.backend.strace.backend"></a>

# lsoph.backend.strace.backend

Strace backend implementation using refactored components.

<a id="lsoph.backend.strace.backend.Strace"></a>

## Strace Objects

```python
class Strace(Backend)
```

Async backend implementation using strace (refactored).

<a id="lsoph.backend.strace.backend.Strace.is_available"></a>

#### is\_available

```python
@staticmethod
def is_available() -> bool
```

Check if the strace executable is available in the system PATH.

<a id="lsoph.backend.strace.backend.Strace.attach"></a>

#### attach

```python
async def attach(pids: list[int])
```

Implementation of the attach method.

<a id="lsoph.backend.strace.backend.Strace.run_command"></a>

#### run\_command

```python
async def run_command(command: list[str])
```

Implementation of the run_command method.

<a id="lsoph.backend.strace.backend.Strace.stop"></a>

#### stop

```python
async def stop()
```

Signals the backend's running task to stop and terminates the managed strace process.

<a id="lsoph.backend.strace.parse"></a>

# lsoph.backend.strace.parse

Parsing logic for strace output.

<a id="lsoph.backend.strace.parse.Syscall"></a>

## Syscall Objects

```python
@dataclass
class Syscall()
```

Represents a parsed strace syscall event.

<a id="lsoph.backend.strace.parse.Syscall.timestamp"></a>

#### timestamp

Timestamp when processed

<a id="lsoph.backend.strace.parse.Syscall.raw_line"></a>

#### raw\_line

Store original line for debugging

<a id="lsoph.backend.strace.parse.parse_strace_stream"></a>

#### parse\_strace\_stream

```python
async def parse_strace_stream(
        lines: AsyncIterator[str],
        monitor: Monitor,
        stop_event: asyncio.Event,
        syscalls: list[str] | None = None,
        attach_ids: list[int] | None = None) -> AsyncIterator[Syscall]
```

Asynchronously parses a stream of raw strace output lines into Syscall objects.

<a id="lsoph.backend.strace.helpers"></a>

# lsoph.backend.strace.helpers

General helper functions for the strace backend.

<a id="lsoph.backend.strace.helpers.parse_result_int"></a>

#### parse\_result\_int

```python
def parse_result_int(result_str: str) -> int | None
```

Safely parses an integer result string from strace.

<a id="lsoph.backend.strace.helpers.clean_path_arg"></a>

#### clean\_path\_arg

```python
def clean_path_arg(path_arg: Any) -> str | None
```

Cleans and decodes path arguments from strace, handling quotes and escapes.

<a id="lsoph.backend.strace.helpers.parse_dirfd"></a>

#### parse\_dirfd

```python
def parse_dirfd(dirfd_arg: str | None) -> int | str | None
```

Parses the dirfd argument, handling AT_FDCWD.

<a id="lsoph.backend.strace.helpers.resolve_path"></a>

#### resolve\_path

```python
def resolve_path(pid: int,
                 path: str | None,
                 cwd_map: dict[int, str],
                 monitor: Monitor,
                 dirfd: int | str | None = None) -> str | None
```

Resolves a path argument relative to CWD or dirfd if necessary.

<a id="lsoph.backend.lsof"></a>

# lsoph.backend.lsof

Lsof backend package for lsoph.

<a id="lsoph.backend.lsof.backend"></a>

# lsoph.backend.lsof.backend

Lsof backend implementation using polling and descendant tracking.

<a id="lsoph.backend.lsof.backend.log"></a>

#### log

Use specific logger

<a id="lsoph.backend.lsof.backend.Lsof"></a>

## Lsof Objects

```python
class Lsof(Backend)
```

Async backend implementation using periodic `lsof` command execution.

Monitors specified initial PIDs and automatically discovers and monitors
their descendants over time. Detects file open/close events by comparing
lsof output between poll cycles.

<a id="lsoph.backend.lsof.backend.Lsof.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        monitor: Monitor,
        poll_interval: float = DEFAULT_LSOF_POLL_INTERVAL,
        child_check_multiplier: int = DEFAULT_CHILD_CHECK_INTERVAL_MULTIPLIER)
```

Initializes the Lsof backend.

**Arguments**:

- `monitor` - The central Monitor instance.
- `poll_interval` - Time in seconds between lsof polls.
- `child_check_multiplier` - Check for new descendants every N polls.

<a id="lsoph.backend.lsof.backend.Lsof.is_available"></a>

#### is\_available

```python
@staticmethod
def is_available() -> bool
```

Check if the lsof executable is available in the system PATH.

<a id="lsoph.backend.lsof.backend.Lsof.attach"></a>

#### attach

```python
async def attach(pids: list[int])
```

Attaches to and monitors a list of initial PIDs and their descendants.

This method runs a continuous loop, polling with `lsof`, updating the
monitor state, and periodically checking for new child processes of the
initial PIDs.

**Arguments**:

- `pids` - A list of initial process IDs to monitor.

<a id="lsoph.backend.lsof.parse"></a>

# lsoph.backend.lsof.parse

Parsing functions for lsof -F output.

<a id="lsoph.backend.lsof.parse.log"></a>

#### log

Use specific logger

<a id="lsoph.backend.lsof.helpers"></a>

# lsoph.backend.lsof.helpers

Helper functions for the lsof backend.

<a id="lsoph.backend.lsof.helpers.log"></a>

#### log

Use specific logger

<a id="lsoph.backend.psutil"></a>

# lsoph.backend.psutil

Psutil backend package for lsoph.

<a id="lsoph.backend.psutil.backend"></a>

# lsoph.backend.psutil.backend

Psutil backend implementation using polling.

<a id="lsoph.backend.psutil.backend.log"></a>

#### log

Use specific logger

<a id="lsoph.backend.psutil.backend.Psutil"></a>

## Psutil Objects

```python
class Psutil(Backend)
```

Async backend implementation using psutil polling.

<a id="lsoph.backend.psutil.backend.Psutil.is_available"></a>

#### is\_available

```python
@staticmethod
def is_available() -> bool
```

Check if the psutil library is installed.

<a id="lsoph.backend.psutil.backend.Psutil.attach"></a>

#### attach

```python
async def attach(pids: list[int])
```

Implementation of the attach method.

<a id="lsoph.backend.psutil.helpers"></a>

# lsoph.backend.psutil.helpers

Helper functions for the psutil backend.

<a id="lsoph.backend.psutil.helpers.log"></a>

#### log

Use specific logger

<a id="lsoph.log"></a>

# lsoph.log

Logging setup for the lsoph application.

<a id="lsoph.log.LOG_QUEUE"></a>

#### LOG\_QUEUE

Max 1000 lines in memory

<a id="lsoph.log.TextualLogHandler"></a>

## TextualLogHandler Objects

```python
class TextualLogHandler(logging.Handler)
```

A logging handler that puts formatted messages into a deque for Textual.

<a id="lsoph.log.TextualLogHandler.emit"></a>

#### emit

```python
def emit(record: logging.LogRecord)
```

Formats the log record and adds it to the queue with Rich markup.

<a id="lsoph.log.setup_logging"></a>

#### setup\_logging

```python
def setup_logging(level_name: str = "INFO")
```

Configures the root logger to use the TextualLogHandler.

<a id="lsoph.cli"></a>

# lsoph.cli

<a id="lsoph.cli.parse_arguments"></a>

#### parse\_arguments

```python
def parse_arguments(available_backends: dict[str, Type[Backend]],
                    argv: list[str] | None = None) -> argparse.Namespace
```

Parses command-line arguments for lsoph.

<a id="lsoph.cli.main"></a>

#### main

```python
def main(argv: list[str] | None = None) -> int
```

Main entry point: Parses args, sets up logging, creates Monitor,
instantiates backend, creates the specific backend coroutine,
and launches the Textual UI.

<a id="lsoph.util"></a>

# lsoph.util

<a id="lsoph.util.pid"></a>

# lsoph.util.pid

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

Provides a base class and decorators for simple version tracking and
thread-safe access using locks. Useful for UI updates based on state changes.

<a id="lsoph.util.versioned.Versioned"></a>

## Versioned Objects

```python
class Versioned()
```

Base class for objects whose state changes should be trackable via a version number.
Includes a reentrant lock for thread safety when modifying or accessing state.

<a id="lsoph.util.versioned.Versioned.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initializes version to 0 and creates a reentrant lock.

<a id="lsoph.util.versioned.Versioned.change"></a>

#### change

```python
def change()
```

Manually increments the version number.
Acquires the lock to ensure atomic update.

<a id="lsoph.util.versioned.Versioned.version"></a>

#### version

```python
@property
def version() -> int
```

Returns the current version number of this object.
Acquires the lock for thread-safe read.

<a id="lsoph.util.versioned.Versioned.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Makes Versioned objects hashable based on identity and current version.
Useful for caching mechanisms that depend on object state.
Acquires the lock for thread-safe read of version.

<a id="lsoph.util.versioned.changes"></a>

#### changes

```python
def changes(method)
```

Decorator for methods that modify the state of a Versioned object.
Acquires the object's lock, executes the method, and then increments
the version number atomically.

<a id="lsoph.util.versioned.waits"></a>

#### waits

```python
def waits(method)
```

Decorator for methods that access the state of a Versioned object
but do not modify it.
Acquires the object's lock before executing the method to ensure
thread-safe reads, especially if accessing multiple attributes.

<a id="lsoph.util.short_path"></a>

# lsoph.util.short\_path

Utility function for shortening file paths.

<a id="lsoph.util.short_path.short_path"></a>

#### short\_path

```python
def short_path(path: str | os.PathLike,
               max_length: int,
               cwd: str = CWD) -> str
```

Shortens a file path string to fit max_length:
1. Tries to make path relative to CWD.
2. Prioritizes keeping the full filename visible.
3. If filename alone is too long, truncates filename from the left ("...name").
4. If path is still too long but filename fits, truncates directory in the middle ("dir...ory/name").

**Arguments**:

- `path` - The file path string or path-like object.
- `max_length` - The maximum allowed length for the output string.
- `cwd` - The current working directory to make the path relative to.
  

**Returns**:

  The shortened path string.

<a id="lsoph.monitor._fileinfo"></a>

# lsoph.monitor.\_fileinfo

Dataclass definition for storing information about a single tracked file.

<a id="lsoph.monitor._fileinfo.FileInfo"></a>

## FileInfo Objects

```python
@dataclass
class FileInfo()
```

Holds state information about a single tracked file.

<a id="lsoph.monitor._fileinfo.FileInfo.status"></a>

#### status

e.g., unknown, open, closed, active, deleted, error

<a id="lsoph.monitor._fileinfo.FileInfo.last_event_type"></a>

#### last\_event\_type

e.g., OPEN, CLOSE, READ, WRITE, STAT, DELETE, RENAME

<a id="lsoph.monitor._fileinfo.FileInfo.last_error_enoent"></a>

#### last\_error\_enoent

True if last relevant op failed with ENOENT

<a id="lsoph.monitor._fileinfo.FileInfo.is_open"></a>

#### is\_open

```python
@property
def is_open() -> bool
```

Checks if any process currently holds this file open according to state.

<a id="lsoph.monitor"></a>

# lsoph.monitor

lsoph Monitor Package.

This package provides the core state management for monitored file access.

<a id="lsoph.monitor._monitor"></a>

# lsoph.monitor.\_monitor

Contains the Monitor class responsible for managing file access state.

<a id="lsoph.monitor._monitor.log"></a>

#### log

Use the same logger name

<a id="lsoph.monitor._monitor.Monitor"></a>

## Monitor Objects

```python
class Monitor(Versioned)
```

Manages the state of files accessed by a monitored target (process group).
Inherits from Versioned for change tracking and thread safety via decorators.
Provides methods for backends to report file events (open, close, read, etc.).

<a id="lsoph.monitor._monitor.Monitor.ignore"></a>

#### ignore

```python
@changes
def ignore(path: str)
```

Adds a path to the ignore list and removes existing state for it.

<a id="lsoph.monitor._monitor.Monitor.ignore_all"></a>

#### ignore\_all

```python
@changes
def ignore_all()
```

Adds all currently tracked file paths to the ignore list.

<a id="lsoph.monitor._monitor.Monitor.open"></a>

#### open

```python
@changes
def open(pid: int, path: str, fd: int, success: bool, timestamp: float,
         **details)
```

Handles an 'open' or 'creat' event.

<a id="lsoph.monitor._monitor.Monitor.close"></a>

#### close

```python
@changes
def close(pid: int, fd: int, success: bool, timestamp: float, **details)
```

Handles a 'close' event.

<a id="lsoph.monitor._monitor.Monitor.read"></a>

#### read

```python
@changes
def read(pid: int, fd: int, path: str | None, success: bool, timestamp: float,
         **details)
```

Handles a 'read' (or similar) event.

<a id="lsoph.monitor._monitor.Monitor.write"></a>

#### write

```python
@changes
def write(pid: int, fd: int, path: str | None, success: bool, timestamp: float,
          **details)
```

Handles a 'write' (or similar) event.

<a id="lsoph.monitor._monitor.Monitor.stat"></a>

#### stat

```python
@changes
def stat(pid: int, path: str, success: bool, timestamp: float, **details)
```

Handles a 'stat', 'access', 'lstat' etc. event.

<a id="lsoph.monitor._monitor.Monitor.delete"></a>

#### delete

```python
@changes
def delete(pid: int, path: str, success: bool, timestamp: float, **details)
```

Handles an 'unlink', 'rmdir' event.

<a id="lsoph.monitor._monitor.Monitor.rename"></a>

#### rename

```python
@changes
def rename(pid: int, old_path: str, new_path: str, success: bool,
           timestamp: float, **details)
```

Handles a 'rename' event.

<a id="lsoph.monitor._monitor.Monitor.process_exit"></a>

#### process\_exit

```python
@changes
def process_exit(pid: int, timestamp: float)
```

Handles cleanup when a process exits.

<a id="lsoph.monitor._monitor.Monitor.get_path"></a>

#### get\_path

```python
@waits
def get_path(pid: int, fd: int) -> str | None
```

Retrieves the path for a PID/FD, handling standard streams.

