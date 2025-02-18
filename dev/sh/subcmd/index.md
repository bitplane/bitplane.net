# 📺 subcmd.sh

A simple subcommand dispatcher. Like how `git commit` runs `git-commit`

## ▶️ Usage

In a file called `mycmd`

```sh
export HELP="Usage: mycmd [subcommand] ..."

. subcmd.sh
```

And if any functions, aliases or functions called `mycmd-*` exist, it'll
run them instead. If you call `mycmd --help`, it'll print the available
subcommands after the HELP you specified.

You can include it subcommands too.

## ⚖️ License

WTFPL with 1 additional clause: don't blame me.

## 🔗 Links

* [🏠 home](https://bitplane.net/dev/sh/subcmd)
* [🐱 github](https://github.com/bitplane/subcmd)

