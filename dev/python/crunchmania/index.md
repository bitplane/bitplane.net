# 📦 crunchmania

![pic](https://bitplane.net/dev/python/crunchmania/crunch-mania.png)

A Python decompressor for [Crunch-Mania](https://amiga.resource.cx/exp/crunchmania)
files from the Amiga era.

* [🏠 home](https://bitplane.net/dev/python/crunchmania)
  * [📖 pydoc](https://bitplane.net/dev/python/crunchmania/pydoc)
* [🐍 pypi](https://pypi.org/project/crunchmania/)
* [🐱 github](https://github.com/bitplane/crunchmania)
* [📦 test data](https://github.com/bitplane/crunch-mania-test-data)

## The format

Crunch-Mania was a file cruncher for the Commodore Amiga, written by Thomas
Schwarz and released between 1989 and 1994. It was designed for in-place
decompression: the compressed data is read backward and the output is written
backward, so a file can be decompressed into the same memory it occupies.

There are four format variants, identified by a 4-byte magic at offset 0:

| Magic  | Mode     | Delta | Description                |
|--------|----------|-------|----------------------------|
| `CrM!` | Standard | No    | Fixed Huffman + VLC        |
| `CrM2` | LZH      | No    | Dynamic Huffman per block  |
| `Crm!` | Standard | Yes   | Standard + delta encoding  |
| `Crm2` | LZH      | Yes   | LZH + delta encoding       |

The lowercase `m` variants apply a cumulative byte delta as a post-processing
step, used for sample data where adjacent bytes tend to have similar values.

Several Amiga demos and games used obfuscated copies of the format with
different magic bytes (`Iron`, `DCS!`, `MSS!`, etc). These are detected and
handled transparently.

The 14-byte header is followed by the packed data stream, which is read from
the end toward the start using an LSB-first bit reader initialized from the
last 6 bytes of the packed block.

## Installation

```
pip install crunchmania
```

## CLI usage

```bash
# Show file info
crunchmania info packed_file.crm

# Decompress a file
crunchmania unpack packed_file.crm output_file

# Scan a file for embedded CrM blocks
crunchmania scan amiga_disk.adf
```

## Library usage

```python
from crunchmania import unpack, parse_header

data = open("packed_file.crm", "rb").read()

# Inspect the header
header = parse_header(data)
print(f"{header.magic!r}, {header.packed_size} -> {header.unpacked_size}")

# Decompress
output = unpack(data)
```

## License

WTFPL
