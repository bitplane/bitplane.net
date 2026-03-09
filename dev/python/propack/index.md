# PRO-PACK for Python

Based on [RNC ProPack Source](https://github.com/lab313ru/rnc_propack_source).

I wanted something I could install from pypi and I could import in Python
projects. So here it is.

Test data can be found in [this repo](https://github.com/bitplane/pro-pack-test-data)

## Install

```bash
pip install propack
```

## Usage

### Python API

```python
from propack import pack, unpack, parse_header

# Compress
raw = open('data.bin', 'rb').read()
packed = pack(raw, method=1)       # method 1 (Huffman+LZ77) or 2

# Decompress
original = unpack(packed)
assert original == raw

# Inspect header
header = parse_header(packed)
print(f'method={header.method} {header.packed_size} -> {header.unpacked_size} bytes')
```

### CLI

```bash
# Compress
propack pack data.bin                     # -> data.rnc1
propack pack data.bin -m 2                # -> data.rnc2
propack pack data.bin -m 1 output.rnc     # explicit output

# Decompress
propack unpack data.rnc1                  # -> data.bin
propack unpack data.rnc1 output.bin       # explicit output

# Inspect
propack info data.rnc1                    # show header fields

# Scan a file for embedded RNC data
propack scan rom.bin

# Extract all embedded RNC blocks
propack extract rom.bin -o output_dir/
```
