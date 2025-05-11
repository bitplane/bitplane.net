# 🧊 blkcache

Userspace transparent block device cache.

## ⬇️ Deps

```
sudo apt install libndb-bin nbdkit-plugin-python nbdfuse fuse3
```

## ℹ️ Usage

```
uvx blkcache /dev/sr0 file.iso
```

Then point tools at `file.iso` instead of `/dev/sr0`.

## Why?

Copying some CDs and needed a way to do mount in FUSE, dump the filesystem, and
then `ddrescue /dev/sr0` to get the image if possible. This means it doesn't
read the disk twice, even if you have a ton of drives attached

## How?

It uses `nbdkit` to create a Network Block Storage device in Python, mounts it
using `fuse`, then creates a mmapped disk cache of sectors as they're read.

## 🔗 Links

* [🏠 home](https://bitplane.net/dev/python/blkcache)
* [🐱 github](https://github.com/bitplane/blkcache)
* [🐍 pypi](https://pypi.org/project/blkcache)
* [📖 pydoc](https://bitplane.net/dev/python/blkcache/pydoc)

## 🌍 Related

* [🪦 rip](https://github.com/bitplane/rip)
* [🕷️ scrapers](https://bitplane.net/python/scrapers)

