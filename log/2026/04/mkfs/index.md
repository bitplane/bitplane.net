# 💾 mkfs.\*

I've been building obscure filesystems test images for
[qemount](/dev/rust/qemount) using custom `mkfs` programs written in C. But
having started playing with Rust, why not port them over? They'll be safer that
way.

So I dropped the following crates:

* [🦀 SCO Boot File System](https://crates.io/crates/mkfs-bfs)
* [🦀 Linux EXT (1)](https://crates.io/crates/mkfs-ext)
* [🦀 GEMDOS](https://crates.io/crates/mkfs-gemdos)
* [🦀 Mac File System](https://crates.io/crates/mkfs-mfs)
* [🦀 System V UNIX](https://crates.io/crates/mkfs-sysv)
* [🦀 Xiafs](https://crates.io/crates/mkfs-xiafs)

And extracted a working mkfs for Tux3 from `linux-tux3`:

* [🐱 mkfs-tux3](https://github.com/bitplane/mkfs-tux3)

All confirmed mountable, but haven't been properly stress tested so we'll have
to see how they hold up over time.
