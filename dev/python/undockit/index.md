# undockit

Run docker containers like they're native commands.


## Setup

Deps:

1. nvidia drivers
2. nvidia-container-toolkit
3. `podman`

Now create a CDI config:

```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```

Then install `undockit` from pypi. You could use pipx or uv, it'll work all
the same:

```bash
pip install undockit
```

## Usage

To install a container as an executable, use the install command:

```bash
undockit install docker.io/bitplanenet/whisper
```

This will add an executable Dockerfile with the undockit runtime as the shebang
into your `~/.local/bin` dir or `$PREFIX`. You can override that location;
see `--help` for details

You can now run it:

```bash
whisper --help
```

## Links

* [🏠 home](https://bitplane.net/dev/python/undockit)
* [🐱 github](https://github.com/bitplane/undockit)
* [🐍 pypi](https://pypi.org/project/undockit)
* [📖 pydoc](https://bitplane.net/dev/python/undockit/pydoc)
