---
features: ["asciinema"]
---
# 🚻👀 `vwc`

Like `wc`, but with a live preview output to stderr if it's a tty.

![cast](https://bitplane.net/dev/python/vwc/vwc.cast.png)

It'll act like your own `wc`, whether that's busybox, gnu or bsd.

## ▶️ installing

```bash
$ pipx install vwc    # or uvx
$ echo "hey" | vwc -l
1
```

For faster counting of large streams, use the optional Numba scanner.

```bash
pipx install 'vwc[fast]'
```


## ⚖️License

WTFP with one additional clause:

- ⛔ Don't blame me

## Links

- [🏠 home](https://bitplane.net/dev/python/vwc)
- [🐱 github](https://github.com/bitplane/vwc)
- [🐍 pypi](https://pypi.org/project/vwc)
- [📖 pydoc](https://bitplane.net/dev/python/vwc/pydoc)
