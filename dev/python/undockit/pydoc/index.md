<a id="undockit"></a>

# undockit

<a id="undockit.args"></a>

# undockit.args

Argument parsing for undockit CLI

<a id="undockit.args.add_install_parser"></a>

#### add\_install\_parser

```python
def add_install_parser(subparsers)
```

Add the install subcommand parser

<a id="undockit.args.add_build_parser"></a>

#### add\_build\_parser

```python
def add_build_parser(subparsers)
```

Add the build subcommand parser

<a id="undockit.args.add_run_parser"></a>

#### add\_run\_parser

```python
def add_run_parser(subparsers)
```

Add the run subcommand parser

<a id="undockit.args.get_parser"></a>

#### get\_parser

```python
def get_parser()
```

Create the argument parser for undockit

<a id="undockit.__version__"></a>

# undockit.\_\_version\_\_

<a id="undockit.__main__"></a>

# undockit.\_\_main\_\_

Main entry point when running undockit as a module

<a id="undockit.backend.base"></a>

# undockit.backend.base

Abstract base class for container backends

<a id="undockit.backend.base.Backend"></a>

## Backend Objects

```python
class Backend(ABC)
```

Abstract base class for container runtime backends

<a id="undockit.backend.base.Backend.build"></a>

#### build

```python
@abstractmethod
def build(dockerfile_path: Path, quiet: bool = False) -> str
```

Build image from dockerfile and return image ID

**Arguments**:

- `dockerfile_path` - Path to the dockerfile to build
- `quiet` - If True, suppress build output (default: False)
  

**Returns**:

  Image ID/hash that can be used to reference the built image
  

**Raises**:

- `RuntimeError` - If build fails

<a id="undockit.backend.base.Backend.command"></a>

#### command

```python
@abstractmethod
def command(image_id: str) -> list[str]
```

Extract default command from image

**Arguments**:

- `image_id` - Image ID returned from build()
  

**Returns**:

  List of command arguments (ENTRYPOINT + CMD combined)

<a id="undockit.backend.base.Backend.start"></a>

#### start

```python
@abstractmethod
def start(container_name: str, image_id: str, timeout: int = 600) -> None
```

Start a warm container

**Arguments**:

- `container_name` - Unique name for the container
- `image_id` - Image ID to run
- `timeout` - Seconds of inactivity before container shuts down

<a id="undockit.backend.base.Backend.stop"></a>

#### stop

```python
@abstractmethod
def stop(container_name: str) -> None
```

Stop and remove a container

**Arguments**:

- `container_name` - Name of container to stop

<a id="undockit.backend.base.Backend.is_running"></a>

#### is\_running

```python
@abstractmethod
def is_running(container_name: str) -> bool
```

Check if a container is currently running

**Arguments**:

- `container_name` - Name of container to check
  

**Returns**:

  True if container is running, False otherwise

<a id="undockit.backend.base.Backend.exec"></a>

#### exec

```python
@abstractmethod
def exec(container_name: str, argv: list[str]) -> int
```

Execute a command in the container

**Arguments**:

- `container_name` - Name of running container
- `argv` - Command and arguments to execute
  

**Returns**:

  Exit code from the executed command

<a id="undockit.backend.base.Backend.name"></a>

#### name

```python
@abstractmethod
def name(image_id: str) -> str
```

Get container name for an image ID

**Arguments**:

- `image_id` - Image ID returned from build()
  

**Returns**:

  Container name to use for this image

<a id="undockit.backend.podman"></a>

# undockit.backend.podman

Podman backend implementation

<a id="undockit.backend.podman.PodmanBackend"></a>

## PodmanBackend Objects

```python
class PodmanBackend(Backend)
```

<a id="undockit.backend.podman.PodmanBackend.build"></a>

#### build

```python
def build(dockerfile_path: Path, quiet: bool = False) -> str
```

Build image from dockerfile using podman build

<a id="undockit.backend.podman.PodmanBackend.command"></a>

#### command

```python
def command(image_id: str) -> list[str]
```

Extract default command from image using podman inspect

<a id="undockit.backend.podman.PodmanBackend.start"></a>

#### start

```python
def start(container_name: str, image_id: str, timeout: int = 600) -> None
```

Start a warm container with host integration and timeout management

<a id="undockit.backend.podman.PodmanBackend.stop"></a>

#### stop

```python
def stop(container_name: str) -> None
```

Stop and remove container

<a id="undockit.backend.podman.PodmanBackend.is_running"></a>

#### is\_running

```python
def is_running(container_name: str) -> bool
```

Check if container is currently running

<a id="undockit.backend.podman.PodmanBackend.exec"></a>

#### exec

```python
def exec(container_name: str, argv: list[str]) -> int
```

Execute command in container with proper workdir

<a id="undockit.backend.podman.PodmanBackend.name"></a>

#### name

```python
def name(image_id: str) -> str
```

Get container name for an image ID

<a id="undockit.backend"></a>

# undockit.backend

Backend system for undockit - manages container runtimes

<a id="undockit.backend.get_backend"></a>

#### get\_backend

```python
def get_backend() -> Backend
```

Auto-detect and return the best available backend

<a id="undockit.install"></a>

# undockit.install

Tool installation functionality for undockit

<a id="undockit.install.resolve_target_path"></a>

#### resolve\_target\_path

```python
def resolve_target_path(to: str,
                        env: Dict[str, str],
                        sys_prefix: str,
                        base_prefix: str,
                        prefix: Optional[Path] = None) -> Path
```

Return the directory where tool should be installed (pure logic)

<a id="undockit.install.extract_name"></a>

#### extract\_name

```python
def extract_name(image: str) -> str
```

Extract tool name from image string

<a id="undockit.install.make_dockerfile"></a>

#### make\_dockerfile

```python
def make_dockerfile(image: str, timeout: int = 600) -> str
```

Generate wrapper dockerfile with shebang

<a id="undockit.install.resolve_target"></a>

#### resolve\_target

```python
def resolve_target(to: str = "user", prefix: Optional[Path] = None) -> Path
```

Wrapper that calls resolve_target_path with actual system values

<a id="undockit.install.install"></a>

#### install

```python
def install(image: str,
            to: str = "user",
            name: Optional[str] = None,
            prefix: Optional[Path] = None,
            timeout: int = 600,
            no_undockit: bool = False) -> Path
```

Install tool to target directory

<a id="undockit.main"></a>

# undockit.main

Main entry point for undockit CLI

<a id="undockit.main.main"></a>

#### main

```python
def main()
```

Main entry point for undockit CLI

<a id="undockit.deploy"></a>

# undockit.deploy

Binary deployment for undockit - installs the undockit zipapp to target directory

<a id="undockit.deploy.get_installed_version"></a>

#### get\_installed\_version

```python
def get_installed_version(binary_path: Path) -> Optional[str]
```

Get version of installed undockit binary, or None if not installed

<a id="undockit.deploy.needs_update"></a>

#### needs\_update

```python
def needs_update(binary_path: Path, current_version: str) -> bool
```

Check if binary needs updating based on version

<a id="undockit.deploy.create_zipapp"></a>

#### create\_zipapp

```python
def create_zipapp(source_dir: Path,
                  output_path: Path,
                  main_module: str = "undockit.main:main",
                  python_shebang: str = "/usr/bin/env python3") -> None
```

Create a zipapp from source directory

**Arguments**:

- `source_dir` - Directory containing the package source
- `output_path` - Where to write the zipapp
- `main_module` - Entry point in module:function format
- `python_shebang` - Shebang line for the zipapp

<a id="undockit.deploy.find_package_source"></a>

#### find\_package\_source

```python
def find_package_source() -> Path
```

Find the source directory of the undockit package

<a id="undockit.deploy.ensure_binary"></a>

#### ensure\_binary

```python
def ensure_binary(target_dir: Path,
                  binary_name: str = "undockit",
                  force: bool = False) -> Optional[Path]
```

Ensure undockit binary is deployed to target directory

**Arguments**:

- `target_dir` - Directory to install binary to
- `binary_name` - Name for the binary (default: undockit)
- `force` - Force reinstall even if up to date
  

**Returns**:

  Path to installed binary, or None if skipped

