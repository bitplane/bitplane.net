# A simple 9p server

A smallish (<1MB) 9p server that can be static linked in busybox images.

Built for [qemount](https://github.com/bitplane/qemount)

Uses [libixp](https://github.com/0intro/libixp)

## Status

This was cobbled together in a few hours for a proof of concept. It has no test
coverage, and the only reason it actually works is because libixp is battle
tested.

Probably safe for read access in non-critical situations, but if you're gonna
use this in a way that risks anything you care about, then pay someone to write
a full battery of tests and do a security review.

## License

WTFPL with one additional clause:

* Don't blame me.

Do whatever the fuck you want with it, but if it goes wrong it's on you.
