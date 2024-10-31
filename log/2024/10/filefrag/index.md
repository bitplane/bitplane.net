# filefrag for python

Spent last night making this, added some turd polish today and added it to pypi.

## 🤷 what?

I wanted to get file fragmentation info so I can punch holes in files, aligned
with memory pages. But I really didn't want to parse `filefrag`'s outputs, so I
wrote a python version with a friendly API and a command line that can produce
json.

It only works on Linux as it depends on the FIE interface, but pull requests
welcome.

## ⚒️ how?

See [the video](https://asciinema.org/a/681791) for a demo including installing
from source, but you can install with pip:

```python
pip install filefrag
```

Then run `pyfilefrag` on the command line. See `--help` for details. It has
`--verbose`, and `--json` outputs for your parsing pleasure.

To use the library, just call `filefrag.FileMap('/path/whatever')` to build a
map of the extents in the file using ioctl's interface. Then you can poke about
in the guts of a file:

* ⛓️‍💥 inspect fragmentation
* 🔍 find out where data is on your physical drive
* 🟰 compare extents between paths
* 📔 use them as dict keys
* 🕳️ check files for holes, like before and after hole punching
* ✅ verify your XFS deduplication strategy, write your own stats tool
* 💩 dump file layouts to json (`print(f"{filemap:j}"`)
* ⚠️ break your disk because you believed the outputs of this 0.0.1 release!

Comes with a Device class to do comparisons, so it ought to work with fragments
in files on different mountpoints, bind mounts and so on (unfortunately not
snap's FUSE mounts; they're far too abstract and piped in via a socket)

## 🌍 where?

* 📺 [asciinema](https://asciinema.org/a/681791) -
  video of install and use
* 🧑‍💻 [github](https://github.com/bitplane/pyfilefrag) -
  wtfpl licensed of course
* 📦 [pypi](https://pypi.org/project/filefrag/) -
  current version is 0.0.1
