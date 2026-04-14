<a id="crunchmania"></a>

# crunchmania

<a id="crunchmania.pack"></a>

# crunchmania.pack

<a id="crunchmania.pack.pack"></a>

#### pack

```python
def pack(data: bytes | bytearray, sampled: bool = False) -> bytes
```

Compress data using Crunch-Mania standard mode (CrM!/Crm!).

<a id="crunchmania.header"></a>

# crunchmania.header

<a id="crunchmania.bitreader"></a>

# crunchmania.bitreader

<a id="crunchmania.bitreader.BackwardBitReader"></a>

## BackwardBitReader Objects

```python
class BackwardBitReader()
```

LSB-first bit reader that reads bytes backward through packed data.

<a id="crunchmania.bitreader.BackwardBitReader.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data: bytes | bytearray, start: int, end: int)
```

**Arguments**:

- `data` - full file data
- `start` - first byte of packed data (after header)
- `end` - offset to last 6 bytes of packed data (header_size + packed_size - 6)

<a id="crunchmania.constants"></a>

# crunchmania.constants

<a id="crunchmania.unpack"></a>

# crunchmania.unpack

<a id="crunchmania.unpack.unpack"></a>

#### unpack

```python
def unpack(data: bytes | bytearray) -> bytes
```

Decompress Crunch-Mania compressed data.

**Arguments**:

- `data` - raw file data starting with CrM header
  

**Returns**:

  decompressed data as bytes
  

**Raises**:

- `ValueError` - on invalid header or corrupt data

<a id="crunchmania.cli"></a>

# crunchmania.cli

