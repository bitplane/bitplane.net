# benpipe

I've been mucking about with the idea of P2P, self-seeding Docker images
[for a while now](../../../2022/12/ipfsos). The endgame being unprivileged
containers with encrypted IPFS mountpoints that are built from and self-host
P2P.

But that's quite a big project with a lot of moving parts, and
[getting mounts working](https://github.com/bitplane/dfused) is a big enough
job in itself.

A step in the right direction would be a tool that you just add to your
Dockerfile and add files via a magnet link, and in doing so they get hosted
while the container is running. So while trying to get that working, I found
myself digging around in the guts of .torrent files in ipython, wishing for a
tool that could dump them to something more readable and back again.

So I wrote one, and published it on pypi:

```bash
$ pip install benpipe
$ cat file.torrent | benpipe | benpipe > file2.torrent
```

* [source on Github](https://github.com/bitplane/benpipe)
