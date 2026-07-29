# xfh

`xfh` is a pure-Python data-recovery library and command-line tool for
historical Amiga XPK files, including files written transparently through
DiskExpander.

## Install

```console
python -m pip install xfh
```

## Recover a file

Inspect and verify the stream before writing output:

```console
xfh info packed-file
xfh verify packed-file
xfh unpack packed-file recovered-file
```

Damaged streams can be handled with explicit salvage mode:

```console
xfh unpack damaged-file recovered-prefix --salvage --report recovery.json
```

See [codec support](codec-support.md), [format notes](format.md), and the
[original-code oracle](oracle-matrix.md) for technical details.
