# Format notes

## XPKF

`xfh` validates the 36-byte global header, optional extended header, short and
long chunk headers, header XORs, payload XORs, four-byte alignment, declared
sizes, and the terminal chunk before decoding. Integers are big-endian.

## DiskExpander 2.1 stream

The recovered files begin with `01 80 63 68 05 61 01 0a`, followed by the
unpacked size, a packed-length field (measured from byte 8), and an eight-byte
NUL-padded sublibrary name such as `xpkNUKE`. It is not a later `XPKF`
stream.

The second length is the absolute offset of a chunk-boundary table at the end
of the file. The table is a sequence of big-endian 32-bit offsets. It begins
with 24, ends with its own file offset, and therefore describes every chunk as
a pair of adjacent boundaries. Each chunk starts with a big-endian 16-bit
compressed-stream length followed by exactly that many codec bytes.
The length value `0xffff` is a raw-block sentinel; in that case exactly
10,000 uncompressed bytes follow.

DiskExpander's `Block 10` setting divides unpacked data into decimal 10,000-byte
chunks; the final chunk contains the remainder. Its bundled `xpkNUKE.library`
identifies itself as NUKE 1.0 and is byte-identical to the public XPK 2.4-era
library. Passing only the bytes after each two-byte chunk length to the NUKE
decoder recovers the known 130-byte `Cancel.gads` sample to its 204-byte
plaintext exactly.

The identification comes from the recovered startup command
`DiskExpander ... Compressor NUKE Block 10 Table 1000 ...`, the `$VER:
DiskExpander 2.1` strings in its executable and handlers, and matching wrapper
magic in those handlers. It is distinct from XFH and from the later `XPKF`
container.
