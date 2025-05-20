# 📺 `tvmux`

So I want to capture my dev work in tmux so I can train models on how to program
and actually use a computer. More data is good.

This is my current tmux setup, including my `tmux.conf`.

## `0.3.1`

This shell script records a session following the active pane. After some turd
polish and more testing, I plan to expand it to work with one window per
project, quantizing recordings, asciinema streaming etc etc

## Links

* [🏠 home](https://bitplane.net/dev/sh/tvmux)
* [🐱 github](https://github.com/bitplane/tvmux)

## To-do

### General

- [ ] get the monitor panel working so I don't need to manually create it each
      reboot.
- [x] Write a `./configure` script that checks all the things we need.
- [x] `make build` and `make install` to `$PREFIX`, defaulting to `~/.local/`

### `0.4`

- [ ] Record everything and selectively switch between buffers
  - [ ] timestamp logs with an awk script
- [ ] Get alternative buffers working
- [x] Break stuff into a library + pack it
- [ ] quantize because spinners are a menace
  - thought: set a cps limit and send full buffers if exceeded

### `__future__`

- [ ] Command line args / flags / config
  - [ ] Consider a generic settings approach that works with config file, args
        and env vars as first class citizens.
- [ ] Move deployment/install code into the script itself
  - [ ] Put markers in so it can unpack itself to source 😎
  - [ ] Think about how to pack docs, unpacking full source with makefile and
        `README.md`? 🤯
