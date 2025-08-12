<a id="vldmcp"></a>

# vldmcp

vldmcp - A distributed (FoaF) MCP server using veilid and podman.

<a id="vldmcp.docker"></a>

# vldmcp.docker

<a id="vldmcp.cli"></a>

# vldmcp.cli

Command line interface for vldmcp.

<a id="vldmcp.cli.cli"></a>

#### cli

```python
@click.group()
@click.version_option(version=__version__, prog_name="vldmcp")
@click.pass_context
def cli(ctx)
```

vldmcp - A distributed (FoaF) MCP server using veilid and podman.

<a id="vldmcp.cli.deploy"></a>

#### deploy

```python
@cli.command()
@click.option(
    "--prefix",
    default=os.path.expanduser("~/.local"),
    help="Installation prefix (default: ~/.local)",
    type=click.Path(),
)
def deploy(prefix)
```

Deploy the Docker base image and setup installation method.

