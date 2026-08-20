<a id="dockershit"></a>

# dockershit

<a id="dockershit.dockershit"></a>

# dockershit.dockershit

<a id="dockershit.dockershit.parse_args"></a>

#### parse\_args

```python
def parse_args(argv: list[str] = sys.argv[1:])
```

Nobody likes an argument, but sometimes you just have to parse them.

<a id="dockershit.dockershit.run"></a>

#### run

```python
def run(path: str,
        image: str,
        shell: str,
        tag: str,
        debug: bool,
        engine_name="auto")
```

The input loop.

<a id="dockershit.dockershit.main"></a>

#### main

```python
def main(argv: str = sys.argv[1:])
```

The main course.

<a id="dockershit.engine"></a>

# dockershit.engine

Container engines used to run commands and build images.

<a id="dockershit.engine.Engine"></a>

## Engine Objects

```python
class Engine(ABC)
```

The container operations dockershit needs.

<a id="dockershit.engine.Engine.build"></a>

#### build

```python
@abstractmethod
def build(dockerfile, tag, debug=False)
```

Build and tag an image from a Dockerfile.

<a id="dockershit.engine.Engine.run"></a>

#### run

```python
@abstractmethod
def run(workdir, tag, shell, command)
```

Run a command in a throwaway container.

<a id="dockershit.engine.Engine.is_top_layer_empty"></a>

#### is\_top\_layer\_empty

```python
@abstractmethod
def is_top_layer_empty(tag)
```

Return whether the newest image layer contains no filesystem changes.

<a id="dockershit.engine.CommandEngine"></a>

## CommandEngine Objects

```python
class CommandEngine(Engine)
```

Shared command-line behavior for Docker-compatible engines.

<a id="dockershit.engine.select_engine"></a>

#### select\_engine

```python
def select_engine(name="auto")
```

Select an installed engine, preferring Podman in auto mode.

<a id="dockershit.docker_file"></a>

# dockershit.docker\_file

For dealing with Dockerfiles

<a id="dockershit.docker_file.Dockerfile"></a>

## Dockerfile Objects

```python
class Dockerfile()
```

<a id="dockershit.docker_file.Dockerfile.parse_lines"></a>

#### parse\_lines

```python
def parse_lines(raw_lines: list[str]) -> list[str]
```

Parses multi-line commands into single lines

<a id="dockershit.docker_file.Dockerfile.exists"></a>

#### exists

```python
def exists() -> bool
```

Returns True if the file exists

<a id="dockershit.docker_file.Dockerfile.set_image"></a>

#### set\_image

```python
def set_image(image: str)
```

Sets the base image, in text. Example: "alpine:latest"

<a id="dockershit.docker_file.Dockerfile.cd"></a>

#### cd

```python
def cd(pwd: str)
```

Set the working directory for the Dockerfile

<a id="dockershit.docker_file.Dockerfile.resolve_workdir"></a>

#### resolve\_workdir

```python
def resolve_workdir(pwd: str)
```

Resolve a path relative to the current working directory.

<a id="dockershit.docker_file.Dockerfile.append_many"></a>

#### append\_many

```python
def append_many(lines)
```

Append logical lines with one atomic file replacement.

<a id="dockershit.docker_file.Dockerfile.append_comment"></a>

#### append\_comment

```python
def append_comment(line, reason)
```

Append a comment that is safe even when the input spans lines.

<a id="dockershit.docker_file.Dockerfile.snapshot"></a>

#### snapshot

```python
def snapshot()
```

Capture the exact file contents for transactional restoration.

<a id="dockershit.docker_file.Dockerfile.restore"></a>

#### restore

```python
def restore(snapshot: DockerfileSnapshot)
```

Restore an exact snapshot and recompute derived state.

<a id="dockershit.docker_file.Dockerfile.remove_last_command"></a>

#### remove\_last\_command

```python
def remove_last_command(reason: str = "removed")
```

Actually comment it out then reload the file

<a id="dockershit.docker_file.Dockerfile.save"></a>

#### save

```python
def save()
```

Write the thing to a file

<a id="dockershit.docker"></a>

# dockershit.docker

<a id="dockershit.docker.BrokenBaselineError"></a>

## BrokenBaselineError Objects

```python
class BrokenBaselineError(RuntimeError)
```

The Dockerfile still fails after the candidate change is restored.

<a id="dockershit.docker.Session"></a>

## Session Objects

```python
class Session()
```

<a id="dockershit.docker.Session.build"></a>

#### build

```python
def build()
```

Build the current Dockerfile without changing it on failure.

<a id="dockershit.docker.Session.apply"></a>

#### apply

```python
def apply(instruction, change, check_noop=False)
```

Apply and build one Dockerfile change as a transaction.

<a id="dockershit.docker.Session.run"></a>

#### run

```python
def run(cmd)
```

Run a command in a throwaway container.

<a id="dockershit.command"></a>

# dockershit.command

Helpers for dealing with commands

<a id="dockershit.command.split_command"></a>

#### split\_command

```python
def split_command(line: str) -> str
```

Get the command and args from a line

<a id="dockershit.command.is_dockerfile"></a>

#### is\_dockerfile

```python
def is_dockerfile(line: str) -> bool
```

Case sensitive to avoid shell mismatches

<a id="dockershit.command.is_simple"></a>

#### is\_simple

```python
def is_simple(line: str) -> bool
```

Just a command with params; no operators, subshells, pipes,
redirects or any of that fancy stuff.

<a id="dockershit.command.is_hidden"></a>

#### is\_hidden

```python
def is_hidden(line: str) -> bool
```

If this line should be hidden

<a id="dockershit.command.matters"></a>

#### matters

```python
def matters(line: str) -> bool
```

Does this line even do anything?

<a id="dockershit.command.flatten"></a>

#### flatten

```python
def flatten(lines: str) -> str
```

Flatten a multi-line command into a single line

<a id="dockershit.keyboard"></a>

# dockershit.keyboard

<a id="dockershit.keyboard.Keyboard"></a>

## Keyboard Objects

```python
class Keyboard()
```

<a id="dockershit.keyboard.Keyboard.input"></a>

#### input

```python
def input()
```

Get input from the user, with multi-line continuation via backslash.

