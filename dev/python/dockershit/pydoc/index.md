<a id="dockershit"></a>

# dockershit

<a id="dockershit.docker"></a>

# dockershit.docker

<a id="dockershit.docker.Docker"></a>

## Docker Objects

```python
class Docker()
```

<a id="dockershit.docker.Docker.run"></a>

#### run

```python
def run(cmd)
```

Run a command in the Docker container

<a id="dockershit.docker.Docker.is_top_layer_empty"></a>

#### is\_top\_layer\_empty

```python
def is_top_layer_empty()
```

Check if top layer of Docker image is empty (0B)

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
def run(path: str, image: str, shell: str, tag: str, debug: bool)
```

The input loop.

<a id="dockershit.dockershit.main"></a>

#### main

```python
def main(argv: str = sys.argv[1:])
```

The main course.

