<a id="tvmux"></a>

# tvmux

<a id="tvmux.proc.bg"></a>

# tvmux.proc.bg

Background process management with automatic cleanup.

<a id="tvmux.proc.bg.spawn"></a>

#### spawn

```python
def spawn(cmd: List[str], **kwargs) -> subprocess.Popen
```

Run a subprocess in the background with automatic cleanup on exit.

**Arguments**:

- `cmd` - Command to run as list of strings
- `**kwargs` - Additional arguments passed to subprocess.Popen
  

**Returns**:

  The Popen process object

<a id="tvmux.proc.bg.terminate"></a>

#### terminate

```python
def terminate(pid: int) -> bool
```

Stop a tracked background process.

**Arguments**:

- `pid` - Process ID to stop
  

**Returns**:

  True if process was stopped, False if not found

<a id="tvmux.proc.bg.reap"></a>

#### reap

```python
def reap()
```

Remove PIDs of processes that have already exited.

<a id="tvmux.proc"></a>

# tvmux.proc

Process utilities.

<a id="tvmux.proc.run"></a>

#### run

```python
def run(cmd: List[str], **kwargs) -> subprocess.CompletedProcess
```

Run a subprocess synchronously with automatic logging.

**Arguments**:

- `cmd` - Command to run as list of strings
- `**kwargs` - Additional arguments passed to subprocess.run
  

**Returns**:

  CompletedProcess result

<a id="tvmux.proc.run_bg"></a>

#### run\_bg

```python
async def run_bg(cmd: List[str], **kwargs) -> subprocess.Popen
```

Run a subprocess in the background asynchronously.

**Arguments**:

- `cmd` - Command to run as list of strings
- `**kwargs` - Additional arguments passed to subprocess.Popen
  

**Returns**:

  The Popen process object

<a id="tvmux.models.remote"></a>

# tvmux.models.remote

Base model for objects that sync with a remote backend.

<a id="tvmux.models.remote.RemoteModel"></a>

## RemoteModel Objects

```python
class RemoteModel(BaseModel)
```

Base model that tracks changes and syncs with remote backend.

<a id="tvmux.models.remote.RemoteModel.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__()
```

Enter transaction mode - disable auto-sync.

<a id="tvmux.models.remote.RemoteModel.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(exc_type, exc_val, exc_tb)
```

Exit transaction mode - commit changes.

<a id="tvmux.models.remote.RemoteModel.from_remote"></a>

#### from\_remote

```python
@classmethod
def from_remote(cls, **data)
```

Create instance from remote data without syncing back.

<a id="tvmux.models.remote.RemoteModel.dirty_fields"></a>

#### dirty\_fields

```python
@property
def dirty_fields()
```

Get list of fields with pending changes.

<a id="tvmux.models.remote.RemoteModel.commit"></a>

#### commit

```python
def commit()
```

Commit pending changes to remote backend.

Subclasses must implement this method.

<a id="tvmux.models.session"></a>

# tvmux.models.session

Session model for tvmux.

<a id="tvmux.models.session.Session"></a>

## Session Objects

```python
class Session(BaseModel)
```

A tmux session.

<a id="tvmux.models.position"></a>

# tvmux.models.position

Position type for dimensions.

<a id="tvmux.models.position.Position"></a>

## Position Objects

```python
class Position(BaseModel)
```

A position or size as (x, y) coordinates.

<a id="tvmux.models.position.Position.from_string"></a>

#### from\_string

```python
@classmethod
def from_string(cls, value: str) -> "Position"
```

Parse from tmux format like '80x24'.

<a id="tvmux.models.position.Position.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Format as tmux string.

<a id="tvmux.models.position.Position.as_tuple"></a>

#### as\_tuple

```python
def as_tuple() -> Tuple[int, int]
```

Get as tuple.

<a id="tvmux.models.recording"></a>

# tvmux.models.recording

Recording model for tvmux.

<a id="tvmux.models.recording.Recording"></a>

## Recording Objects

```python
class Recording(BaseModel)
```

A tmux recording session.

<a id="tvmux.models.recording.Recording.start"></a>

#### start

```python
async def start(active_pane: str, output_dir: Path)
```

Start recording this window.

<a id="tvmux.models.recording.Recording.switch_pane"></a>

#### switch\_pane

```python
def switch_pane(new_pane_id: str)
```

Switch recording to a different pane in the window.

<a id="tvmux.models.recording.Recording.stop"></a>

#### stop

```python
def stop()
```

Stop recording.

<a id="tvmux.models"></a>

# tvmux.models

Models for tvmux.

<a id="tvmux.models.window"></a>

# tvmux.models.window

Window model for tvmux.

<a id="tvmux.models.window.Window"></a>

## Window Objects

```python
class Window(BaseModel)
```

A tmux window.

<a id="tvmux.models.pane"></a>

# tvmux.models.pane

Pane model for tvmux.

<a id="tvmux.models.pane.Pane"></a>

## Pane Objects

```python
class Pane(BaseModel)
```

A tmux pane.

<a id="tvmux.connection"></a>

# tvmux.connection

Connection to tvmux server.

<a id="tvmux.connection.Connection"></a>

## Connection Objects

```python
class Connection()
```

Manages connection to tvmux server.

<a id="tvmux.connection.Connection.server_pid"></a>

#### server\_pid

```python
@property
def server_pid() -> Optional[int]
```

Get server PID if running.

<a id="tvmux.connection.Connection.is_running"></a>

#### is\_running

```python
@property
def is_running() -> bool
```

Check if server is running.

<a id="tvmux.connection.Connection.api"></a>

#### api

```python
def api()
```

Get API client with typed methods matching the server routes.

<a id="tvmux.repair"></a>

# tvmux.repair

Asciinema cast file repair utilities.

Simple functions to detect and repair corrupted asciinema cast files.
Handles large files by streaming instead of loading into RAM.

<a id="tvmux.repair.validate_cast_file"></a>

#### validate\_cast\_file

```python
def validate_cast_file(cast_path: Path) -> bool
```

Validate that an asciinema cast file is properly formatted.
Only reads header and tail to avoid loading large files into RAM.

**Arguments**:

- `cast_path` - Path to the cast file
  

**Returns**:

  True if file is valid, False otherwise

<a id="tvmux.repair.repair_cast_file"></a>

#### repair\_cast\_file

```python
def repair_cast_file(cast_path: Path, backup: bool = True) -> bool
```

Repair a corrupted asciinema cast file.

Streams the file to avoid memory issues with large files.
Fixes incomplete JSON arrays due to asciinema termination during write.

**Arguments**:

- `cast_path` - Path to the cast file to repair
- `backup` - Whether to create a backup before repair
  

**Returns**:

  True if repair was successful or unnecessary, False on failure

<a id="tvmux.tui.app"></a>

# tvmux.tui.app

Main TUI application with CRT TV interface.

<a id="tvmux.tui.app.setup_client_logging"></a>

#### setup\_client\_logging

```python
def setup_client_logging()
```

Set up client-side logging.

<a id="tvmux.tui.app.ChannelTuner"></a>

## ChannelTuner Objects

```python
class ChannelTuner(Static)
```

TV channel tuner showing tmux windows as channels.

<a id="tvmux.tui.app.ChannelTuner.on_mount"></a>

#### on\_mount

```python
async def on_mount() -> None
```

Load channels when widget mounts.

<a id="tvmux.tui.app.ChannelTuner.refresh_channels"></a>

#### refresh\_channels

```python
async def refresh_channels() -> None
```

Refresh the list of available tmux windows/sessions.

<a id="tvmux.tui.app.ChannelTuner.render"></a>

#### render

```python
def render() -> str
```

Render the channel tuner.

<a id="tvmux.tui.app.ChannelTuner.action_select_next"></a>

#### action\_select\_next

```python
def action_select_next() -> None
```

Select next channel.

<a id="tvmux.tui.app.ChannelTuner.action_select_previous"></a>

#### action\_select\_previous

```python
def action_select_previous() -> None
```

Select previous channel.

<a id="tvmux.tui.app.ChannelTuner.get_selected_channel"></a>

#### get\_selected\_channel

```python
def get_selected_channel() -> Optional[dict]
```

Get the currently selected channel.

<a id="tvmux.tui.app.ChannelTuner.toggle_recording"></a>

#### toggle\_recording

```python
async def toggle_recording() -> None
```

Start or stop recording for the selected channel.

<a id="tvmux.tui.app.CRTPlayer"></a>

## CRTPlayer Objects

```python
class CRTPlayer(Static)
```

CRT-style video player widget.

<a id="tvmux.tui.app.CRTPlayer.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Compose the CRT player.

<a id="tvmux.tui.app.CRTPlayer.play_recording"></a>

#### play\_recording

```python
async def play_recording(recording_path: Path) -> None
```

Play a recording file.

<a id="tvmux.tui.app.CRTPlayer.show_blank"></a>

#### show\_blank

```python
async def show_blank() -> None
```

Show a blank/static screen for channels not recording.

<a id="tvmux.tui.app.TVMuxApp"></a>

## TVMuxApp Objects

```python
class TVMuxApp(App)
```

Main tvmux TUI application.

<a id="tvmux.tui.app.TVMuxApp.compose"></a>

#### compose

```python
def compose() -> ComposeResult
```

Compose the application layout.

<a id="tvmux.tui.app.TVMuxApp.on_mount"></a>

#### on\_mount

```python
async def on_mount() -> None
```

Initialize player when app starts.

<a id="tvmux.tui.app.TVMuxApp.action_refresh"></a>

#### action\_refresh

```python
async def action_refresh() -> None
```

Refresh channels list.

<a id="tvmux.tui.app.TVMuxApp.action_select_next"></a>

#### action\_select\_next

```python
def action_select_next() -> None
```

Select next channel.

<a id="tvmux.tui.app.TVMuxApp.action_select_previous"></a>

#### action\_select\_previous

```python
def action_select_previous() -> None
```

Select previous channel.

<a id="tvmux.tui.app.TVMuxApp.action_play_selected"></a>

#### action\_play\_selected

```python
async def action_play_selected() -> None
```

Tune to the selected channel.

<a id="tvmux.tui.app.TVMuxApp.action_toggle_playback"></a>

#### action\_toggle\_playback

```python
async def action_toggle_playback() -> None
```

Toggle recording for current channel.

<a id="tvmux.tui.app.TVMuxApp.schedule_channel_check"></a>

#### schedule\_channel\_check

```python
def schedule_channel_check() -> None
```

Schedule a channel check for auto-play.

<a id="tvmux.tui.app.TVMuxApp.tune_to_selected_channel"></a>

#### tune\_to\_selected\_channel

```python
async def tune_to_selected_channel() -> None
```

Auto-play the selected channel if it's recording.

<a id="tvmux.tui.app.run_tui"></a>

#### run\_tui

```python
def run_tui()
```

Run the tvmux TUI application.

<a id="tvmux.tui"></a>

# tvmux.tui

TUI components for tvmux.

<a id="tvmux.api_client"></a>

# tvmux.api\_client

Simple API client function for tvmux server.

<a id="tvmux.api_client.APIError"></a>

## APIError Objects

```python
class APIError(Exception)
```

API request failed.

<a id="tvmux.api_client.api_call"></a>

#### api\_call

```python
def api_call(base_url: str,
             method: str,
             path: str,
             data: Optional[BaseModel] = None,
             response_model: Optional[Type[T]] = None) -> Union[T, dict]
```

Make an API call with Pydantic support.

**Arguments**:

- `base_url` - Server base URL
- `method` - HTTP method
- `path` - API endpoint path
- `data` - Request body as Pydantic model
- `response_model` - Expected response model class
  

**Returns**:

  Instance of response_model or dict
  

**Raises**:

- `APIError` - If the request fails

<a id="tvmux.utils"></a>

# tvmux.utils

Utility functions for tvmux.

<a id="tvmux.utils.get_session_dir"></a>

#### get\_session\_dir

```python
def get_session_dir(hostname: str,
                    session_name: str,
                    tmux_var: str,
                    base_dir: str = "/run/tvmux") -> Path
```

Generate a filesystem-safe session directory name.

**Arguments**:

- `hostname` - The hostname where tmux is running
- `session_name` - The tmux session name
- `tmux_var` - The $TMUX environment variable value
- `base_dir` - Base directory for tvmux runtime data
  

**Returns**:

  Path to the session directory
  

**Example**:

  >>> get_session_dir("laptop", "my project", "/tmp/tmux-1000/default,3028,0")
  PosixPath('/run/tvmux/session_laptop_my_project_a1b2c3')

<a id="tvmux.utils.safe_filename"></a>

#### safe\_filename

```python
def safe_filename(name: str) -> str
```

Make a string safe for use as a filename.

<a id="tvmux.utils.file_has_readers"></a>

#### file\_has\_readers

```python
def file_has_readers(file_path: str) -> bool
```

Check if any process is set up to read from the file.

<a id="tvmux.config"></a>

# tvmux.config

Configuration management for tvmux.

<a id="tvmux.config.OutputConfig"></a>

## OutputConfig Objects

```python
class OutputConfig(BaseModel)
```

Output configuration.

<a id="tvmux.config.ServerConfig"></a>

## ServerConfig Objects

```python
class ServerConfig(BaseModel)
```

Server configuration.

<a id="tvmux.config.RecordingConfig"></a>

## RecordingConfig Objects

```python
class RecordingConfig(BaseModel)
```

Recording configuration.

<a id="tvmux.config.AnnotationConfig"></a>

## AnnotationConfig Objects

```python
class AnnotationConfig(BaseModel)
```

Annotation configuration.

<a id="tvmux.config.LoggingConfig"></a>

## LoggingConfig Objects

```python
class LoggingConfig(BaseModel)
```

Logging configuration.

<a id="tvmux.config.Config"></a>

## Config Objects

```python
class Config(BaseModel)
```

Main tvmux configuration.

<a id="tvmux.config.load_config"></a>

#### load\_config

```python
def load_config(config_file: Optional[str] = None) -> Config
```

Load configuration from file and environment variables.

Precedence (highest to lowest):
1. Environment variables
2. Specified config file
3. TVMUX_CONFIG_FILE environment variable
4. ~/.tvmux.conf
5. Built-in defaults

<a id="tvmux.config.generate_env_var_name"></a>

#### generate\_env\_var\_name

```python
def generate_env_var_name(section: str, field: str) -> str
```

Generate environment variable name for a config field.

Follows convention: TVMUX_{SECTION}_{FIELD}

<a id="tvmux.config.get_all_env_mappings"></a>

#### get\_all\_env\_mappings

```python
def get_all_env_mappings() -> Dict[str, tuple[str, str]]
```

Get all possible environment variable mappings.

Returns dict mapping env var name to (section, field) tuple.

<a id="tvmux.config.load_all_env_overrides"></a>

#### load\_all\_env\_overrides

```python
def load_all_env_overrides() -> Dict[str, Any]
```

Load all environment variable overrides programmatically.

<a id="tvmux.config.dump_config_toml"></a>

#### dump\_config\_toml

```python
def dump_config_toml(config: Config) -> str
```

Convert Config to TOML string.

<a id="tvmux.config.dump_config_env"></a>

#### dump\_config\_env

```python
def dump_config_env(config: Config) -> str
```

Convert Config to environment variable format.

<a id="tvmux.config.get_config"></a>

#### get\_config

```python
def get_config() -> Config
```

Get the global configuration instance.

<a id="tvmux.config.set_config"></a>

#### set\_config

```python
def set_config(config: Config) -> None
```

Set the global configuration instance.

<a id="tvmux.cli.main"></a>

# tvmux.cli.main

Main CLI entry point for tvmux.

<a id="tvmux.cli.main.print_version"></a>

#### print\_version

```python
def print_version(ctx, param, value)
```

Print version information for client and server.

<a id="tvmux.cli.main.cli"></a>

#### cli

```python
@click.group(invoke_without_command=True)
@click.option('--log-level',
              default='INFO',
              type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR']),
              help='Set logging level')
@click.option('--config-file',
              type=click.Path(exists=True),
              help='Path to configuration file')
@click.option('--version',
              is_flag=True,
              callback=print_version,
              expose_value=False,
              is_eager=True,
              help='Show version information')
@click.pass_context
def cli(ctx, log_level, config_file)
```

Per-window recorder for tmux.

<a id="tvmux.cli.record"></a>

# tvmux.cli.record

Recording management commands.

<a id="tvmux.cli.record.rec"></a>

#### rec

```python
@click.group(invoke_without_command=True)
@click.pass_context
def rec(ctx)
```

Manage window recordings.

<a id="tvmux.cli.record.start"></a>

#### start

```python
@rec.command("start")
def start()
```

Start recording the current tmux window.

<a id="tvmux.cli.record.ls"></a>

#### ls

```python
@rec.command("ls")
@click.option("-q",
              "--quiet",
              is_flag=True,
              help="Only output recording IDs (one per line)")
def ls(quiet)
```

List active recordings.

<a id="tvmux.cli.record.stop"></a>

#### stop

```python
@rec.command("stop")
@click.argument("recording_ids", nargs=-1)
def stop(recording_ids)
```

Stop recording(s). Stop all recordings if no IDs specified.

<a id="tvmux.cli.api_cli"></a>

# tvmux.cli.api\_cli

Better auto-generated CLI from FastAPI routes using introspection.

<a id="tvmux.cli.api_cli.pydantic_to_click_options"></a>

#### pydantic\_to\_click\_options

```python
def pydantic_to_click_options(model: type[BaseModel])
```

Convert Pydantic model fields to Click options.

<a id="tvmux.cli.api_cli.create_command_for_route"></a>

#### create\_command\_for\_route

```python
def create_command_for_route(route: APIRoute)
```

Create a Click command for a FastAPI route.

<a id="tvmux.cli.api_cli.api"></a>

#### api

```python
@click.group()
def api()
```

Direct API access for testing (auto-generated from routes).

<a id="tvmux.cli.api_cli.generate_cli"></a>

#### generate\_cli

```python
def generate_cli()
```

Generate CLI commands from FastAPI routes.

<a id="tvmux.cli"></a>

# tvmux.cli

CLI module for tvmux.

<a id="tvmux.cli.server"></a>

# tvmux.cli.server

Server management commands.

<a id="tvmux.cli.server.server"></a>

#### server

```python
@click.group()
def server()
```

Manage the tvmux server.

<a id="tvmux.cli.config"></a>

# tvmux.cli.config

Configuration management commands.

<a id="tvmux.cli.config.config"></a>

#### config

```python
@click.group()
def config()
```

Configuration management commands.

<a id="tvmux.cli.config.show"></a>

#### show

```python
@config.command()
@click.option('--format',
              'output_format',
              default='toml',
              type=click.Choice(['toml', 'env']),
              help='Output format (toml or env)')
def show(output_format)
```

Show current effective configuration.

<a id="tvmux.cli.config.defaults"></a>

#### defaults

```python
@config.command()
@click.option('--format',
              'output_format',
              default='toml',
              type=click.Choice(['toml', 'env']),
              help='Output format (toml or env)')
def defaults(output_format)
```

Show default configuration values.

<a id="tvmux.cli.tui"></a>

# tvmux.cli.tui

TUI command for tvmux.

<a id="tvmux.cli.tui.tui"></a>

#### tui

```python
@click.command()
def tui()
```

Launch the tvmux TUI interface.

<a id="tvmux.server.main"></a>

# tvmux.server.main

FastAPI server that manages tmux connections.

<a id="tvmux.server.main.setup_logging"></a>

#### setup\_logging

```python
def setup_logging()
```

Configure logging for the application.

<a id="tvmux.server.main.lifespan"></a>

#### lifespan

```python
@asynccontextmanager
async def lifespan(app: FastAPI)
```

Manage application lifespan.

<a id="tvmux.server.main.root"></a>

#### root

```python
@app.get("/")
async def root()
```

Server info.

<a id="tvmux.server.main.version"></a>

#### version

```python
@app.get("/version")
async def version()
```

Get server version.

<a id="tvmux.server.main.cleanup_and_exit"></a>

#### cleanup\_and\_exit

```python
def cleanup_and_exit(signum=None, frame=None)
```

Clean up and exit gracefully.

<a id="tvmux.server.main.run_server"></a>

#### run\_server

```python
def run_server()
```

Run the server on HTTP port.

<a id="tvmux.server.state"></a>

# tvmux.server.state

Global state management for tvmux server.

<a id="tvmux.server.state.SERVER_PORT"></a>

#### SERVER\_PORT

"TV" in ASCII

<a id="tvmux.server.window_monitor"></a>

# tvmux.server.window\_monitor

Monitor tmux windows to detect when they're closed.

<a id="tvmux.server.window_monitor.get_current_windows"></a>

#### get\_current\_windows

```python
def get_current_windows() -> Set[str]
```

Get the set of current window IDs as session:window_id keys.

<a id="tvmux.server.window_monitor.cleanup_closed_windows"></a>

#### cleanup\_closed\_windows

```python
def cleanup_closed_windows()
```

Check for closed windows and clean up their recordings.

<a id="tvmux.server"></a>

# tvmux.server

tvmux server package.

<a id="tvmux.server.routers.session"></a>

# tvmux.server.routers.session

Session router for tmux control.

<a id="tvmux.server.routers.session.SessionCreate"></a>

## SessionCreate Objects

```python
class SessionCreate(BaseModel)
```

Create session request.

<a id="tvmux.server.routers.session.SessionUpdate"></a>

## SessionUpdate Objects

```python
class SessionUpdate(BaseModel)
```

Update session request.

<a id="tvmux.server.routers.session.WindowReference"></a>

## WindowReference Objects

```python
class WindowReference(BaseModel)
```

Reference to a window in a session.

<a id="tvmux.server.routers.session.SessionWindows"></a>

## SessionWindows Objects

```python
class SessionWindows(BaseModel)
```

Session windows response.

<a id="tvmux.server.routers.session.update"></a>

#### update

```python
@router.patch("/{session_id}")
async def update(session_id: str, update: SessionUpdate)
```

Update a session (rename).

<a id="tvmux.server.routers.session.attach_session"></a>

#### attach\_session

```python
@router.post("/{session_id}/attach")
async def attach_session(session_id: str)
```

Attach to a session (returns attach command for client to execute).

<a id="tvmux.server.routers.session.detach_session"></a>

#### detach\_session

```python
@router.post("/{session_id}/detach")
async def detach_session(session_id: str)
```

Detach all clients from a session.

<a id="tvmux.server.routers.session.get_session_windows"></a>

#### get\_session\_windows

```python
@router.get("/{session_id}/windows", response_model=SessionWindows)
async def get_session_windows(session_id: str)
```

Get all window references for a session.

<a id="tvmux.server.routers.panes"></a>

# tvmux.server.routers.panes

Pane router for tmux control.

<a id="tvmux.server.routers.panes.PaneCreate"></a>

## PaneCreate Objects

```python
class PaneCreate(BaseModel)
```

Create pane request.

<a id="tvmux.server.routers.panes.PaneCreate.window_id"></a>

#### window\_id

Window to split

<a id="tvmux.server.routers.panes.PaneCreate.target_pane_id"></a>

#### target\_pane\_id

Specific pane to split (default: active)

<a id="tvmux.server.routers.panes.PaneCreate.horizontal"></a>

#### horizontal

False for vertical split, True for horizontal

<a id="tvmux.server.routers.panes.PaneCreate.size"></a>

#### size

Percentage or lines/columns

<a id="tvmux.server.routers.panes.PaneResize"></a>

## PaneResize Objects

```python
class PaneResize(BaseModel)
```

Resize pane request.

<a id="tvmux.server.routers.panes.PaneResize.direction"></a>

#### direction

U, D, L, or R

<a id="tvmux.server.routers.panes.PaneSendKeys"></a>

## PaneSendKeys Objects

```python
class PaneSendKeys(BaseModel)
```

Send keys request.

<a id="tvmux.server.routers.panes.list_panes"></a>

#### list\_panes

```python
@router.get("/", response_model=List[Pane])
async def list_panes(window_id: Optional[str] = Query(
    None, description="Filter by window ID"))
```

List all panes or panes in a specific window.

<a id="tvmux.server.routers.panes.create_pane"></a>

#### create\_pane

```python
@router.post("/", response_model=Pane)
async def create_pane(pane: PaneCreate)
```

Create a new pane by splitting a window.

<a id="tvmux.server.routers.panes.get_pane"></a>

#### get\_pane

```python
@router.get("/{pane_id}", response_model=Pane)
async def get_pane(pane_id: str)
```

Get a specific pane by ID.

<a id="tvmux.server.routers.panes.delete_pane"></a>

#### delete\_pane

```python
@router.delete("/{pane_id}")
async def delete_pane(pane_id: str)
```

Kill a pane.

<a id="tvmux.server.routers.panes.select_pane"></a>

#### select\_pane

```python
@router.post("/{pane_id}/select")
async def select_pane(pane_id: str)
```

Select/switch to a pane.

<a id="tvmux.server.routers.panes.resize_pane"></a>

#### resize\_pane

```python
@router.post("/{pane_id}/resize")
async def resize_pane(pane_id: str, resize: PaneResize)
```

Resize a pane.

<a id="tvmux.server.routers.panes.send_keys"></a>

#### send\_keys

```python
@router.post("/{pane_id}/send-keys")
async def send_keys(pane_id: str, send: PaneSendKeys)
```

Send keys to a pane.

<a id="tvmux.server.routers.panes.capture_pane"></a>

#### capture\_pane

```python
@router.get("/{pane_id}/capture")
async def capture_pane(pane_id: str,
                       start: Optional[int] = Query(None),
                       end: Optional[int] = Query(None))
```

Capture pane contents.

<a id="tvmux.server.routers.recording"></a>

# tvmux.server.routers.recording

Recording management endpoints.

<a id="tvmux.server.routers.recording.resolve_id"></a>

#### resolve\_id

```python
def resolve_id(session_id: str, window_name: str) -> str
```

Get window ID from window name/index/id.

**Arguments**:

- `session_id` - The session ID
- `window_name` - Window name, index, or ID
  

**Returns**:

  Window ID (e.g., "@1")

<a id="tvmux.server.routers.recording.display_name"></a>

#### display\_name

```python
def display_name(session_id: str, window_id: str) -> str
```

Get friendly display name for a window ID.

<a id="tvmux.server.routers.recording.RecordingCreate"></a>

## RecordingCreate Objects

```python
class RecordingCreate(BaseModel)
```

Request to start recording a window.

<a id="tvmux.server.routers.recording.RecordingCreate.window_id"></a>

#### window\_id

Window ID to record

<a id="tvmux.server.routers.recording.RecordingCreate.active_pane"></a>

#### active\_pane

If not provided, will detect active pane

<a id="tvmux.server.routers.recording.create_recording"></a>

#### create\_recording

```python
@router.post("/", response_model=Recording)
async def create_recording(request: RecordingCreate,
                           response: Response) -> Recording
```

Start a new recording.

<a id="tvmux.server.routers.recording.delete_recording"></a>

#### delete\_recording

```python
@router.delete("/{recording_id}")
async def delete_recording(recording_id: str) -> dict
```

Stop a recording.

<a id="tvmux.server.routers.recording.get_recording"></a>

#### get\_recording

```python
@router.get("/{recording_id}", response_model=Recording)
async def get_recording(recording_id: str) -> Recording
```

Get recording status.

<a id="tvmux.server.routers.recording.list_recordings"></a>

#### list\_recordings

```python
@router.get("/", response_model=list[Recording])
async def list_recordings() -> list[Recording]
```

List all active recordings.

<a id="tvmux.server.routers"></a>

# tvmux.server.routers

tvmux server routers.

<a id="tvmux.server.routers.hook"></a>

# tvmux.server.routers.hook

Single endpoint for receiving tmux hook events.

<a id="tvmux.server.routers.hook.HookEvent"></a>

## HookEvent Objects

```python
class HookEvent(BaseModel)
```

Event data from tmux hooks.

<a id="tvmux.server.routers.hook.receive_hook"></a>

#### receive\_hook

```python
@router.post("/")
async def receive_hook(event: HookEvent) -> Dict[str, str]
```

Receive and process a hook event from tmux.

<a id="tvmux.server.routers.window"></a>

# tvmux.server.routers.window

Window router for tmux control.

<a id="tvmux.server.routers.window.WindowCreate"></a>

## WindowCreate Objects

```python
class WindowCreate(BaseModel)
```

Create window request.

<a id="tvmux.server.routers.window.WindowCreate.session"></a>

#### session

Session to attach to (optional)

<a id="tvmux.server.routers.window.WindowUpdate"></a>

## WindowUpdate Objects

```python
class WindowUpdate(BaseModel)
```

Update window request.

<a id="tvmux.server.routers.window.update_window"></a>

#### update\_window

```python
@router.patch("/{window_id}")
async def update_window(window_id: str, update: WindowUpdate)
```

Update a window.

<a id="tvmux.server.routers.window.delete_window"></a>

#### delete\_window

```python
@router.delete("/{window_id}")
async def delete_window(window_id: str)
```

Kill a tmux window.

<a id="tvmux.server.routers.window.select_window"></a>

#### select\_window

```python
@router.post("/{window_id}/select")
async def select_window(window_id: str)
```

Select/switch to a window.

<a id="tvmux.server.routers.window.unlink_window"></a>

#### unlink\_window

```python
@router.post("/{window_id}/unlink")
async def unlink_window(window_id: str)
```

Unlink window from its session.

<a id="tvmux.server.routers.window.link_window"></a>

#### link\_window

```python
@router.post("/{window_id}/link")
async def link_window(window_id: str,
                      target_session: str,
                      target_index: Optional[int] = None)
```

Link window to a session.

<a id="tvmux.server.routers.window.get_window_panes"></a>

#### get\_window\_panes

```python
@router.get("/{window_id}/panes")
async def get_window_panes(window_id: str)
```

Get all panes in a window - redirects to panes endpoint.

<a id="tvmux.server.routers.callbacks"></a>

# tvmux.server.routers.callbacks

CRUD endpoints for managing tmux hooks.

<a id="tvmux.server.routers.callbacks.Hook"></a>

## Hook Objects

```python
class Hook(BaseModel)
```

Configuration for a tmux hook.

<a id="tvmux.server.routers.callbacks.Hook.command"></a>

#### command

If None, use default command

<a id="tvmux.server.routers.callbacks.HookCreate"></a>

## HookCreate Objects

```python
class HookCreate(BaseModel)
```

Request to create/install a hook.

<a id="tvmux.server.routers.callbacks.HookUpdate"></a>

## HookUpdate Objects

```python
class HookUpdate(BaseModel)
```

Request to update a hook.

<a id="tvmux.server.routers.callbacks.get_default_command"></a>

#### get\_default\_command

```python
def get_default_command(hook_name: str) -> str
```

Get the default command for a hook.

<a id="tvmux.server.routers.callbacks.install_hook"></a>

#### install\_hook

```python
def install_hook(hook: Hook) -> None
```

Install a tmux hook.

<a id="tvmux.server.routers.callbacks.uninstall_hook"></a>

#### uninstall\_hook

```python
def uninstall_hook(hook_name: str) -> None
```

Uninstall a tmux hook.

<a id="tvmux.server.routers.callbacks.list_hooks"></a>

#### list\_hooks

```python
@router.get("/")
async def list_hooks() -> List[Hook]
```

List all available hooks and their status.

<a id="tvmux.server.routers.callbacks.get_hook"></a>

#### get\_hook

```python
@router.get("/{hook_name}")
async def get_hook(hook_name: str) -> Hook
```

Get details about a specific hook.

<a id="tvmux.server.routers.callbacks.create_hook"></a>

#### create\_hook

```python
@router.post("/")
async def create_hook(hook_data: HookCreate) -> Hook
```

Create/install a new hook.

<a id="tvmux.server.routers.callbacks.update_hook"></a>

#### update\_hook

```python
@router.put("/{hook_name}")
async def update_hook(hook_name: str, update_data: HookUpdate) -> Hook
```

Update an existing hook.

<a id="tvmux.server.routers.callbacks.delete_hook"></a>

#### delete\_hook

```python
@router.delete("/{hook_name}")
async def delete_hook(hook_name: str) -> Dict[str, str]
```

Remove/uninstall a hook.

<a id="tvmux.server.routers.callbacks.setup_default_hooks"></a>

#### setup\_default\_hooks

```python
def setup_default_hooks()
```

Set up default tmux hooks for tvmux operation.

<a id="tvmux.server.routers.callbacks.remove_all_hooks"></a>

#### remove\_all\_hooks

```python
def remove_all_hooks()
```

Remove all installed tmux hooks.

