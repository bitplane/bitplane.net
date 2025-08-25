---
features: ["asciinema"]
---
# 🚻👀 `vwc`

Like `wc`, but with a live preview output to stderr if it's a tty.

![cast](https://bitplane.net/dev/python/vwc/vwc.cast.png)

## ▶️ installing

```bash
$ pipx install vwc    # or uvx
$ echo "hey" | vwc -l
1
```

## ✅ To Do

- [x] Detect platform and mirror it
- [ ] Integration tests
  - [x] Create runner
  - [ ] Containers
    - [x] GNU
    - [x] BusyBox
    - [ ] BSD
  - [ ] Coverage
    - [ ] Prove it:  merge `.coverage` from containers
    - [ ] Write more tests
- [ ] Performance tune
  - [ ] Evaluate options
    - [x] `numba`
      - fast on large files
      - slower on small ones, even with cache
      - bulky af
      - difficult to install
    - [ ] `Cython`
      - requires pre-built wheels
      - can we execute without compiler?
    - [ ] `pypy`
      - is this still as good as it used to be?
      - is it more available?
  - [ ] Implement one or more of them
  - [ ] Add to test suite
- [ ] Record `asciinema` video(s)

## 💣 Known bugs

- Needs to get text length from a proper API
- BusyBox closes stdin on first ctrl+d, gnu does not
- Performance is terrible since dropping Numba bloat

## ⚖️ License

WTFP with one additional clause:

- ⛔ Don't blame me

## Links

- [🏠 home](https://bitplane.net/dev/python/vwc)
- [🐱 github](https://github.com/bitplane/vwc)
- [🐍 pypi](https://pypi.org/project/vwc)
- [📖 pydoc](https://bitplane.net/dev/python/vwc/pydoc)
