<a id="propack"></a>

# propack

<a id="propack.cli"></a>

# propack.cli

<a id="propack.lz"></a>

# propack.lz

LZ77 match finding for RNC ProPack compression.

Works directly on the input data array. Match offsets are distances
back from the current position (1 = previous byte).

<a id="propack.lz.scan_block"></a>

#### scan\_block

```python
def scan_block(data,
               offset,
               size,
               block_size=PACK_BLOCK_SIZE,
               max_matches=MAX_MATCHES,
               max_offset=0xFFFF,
               raw_freq=None,
               pos_freq=None,
               len_freq=None)
```

Scan data for LZ77 matches, return match records.

Each record is (data_length, match_count_minus2, match_offset_minus1).

If freq lists are provided, frequency counts are accumulated
for Huffman table building (method 1).

Returns list of tuples and the number of bytes consumed.

<a id="propack.header"></a>

# propack.header

<a id="propack.bitreader"></a>

# propack.bitreader

<a id="propack.bitreader.BitReader"></a>

## BitReader Objects

```python
class BitReader()
```

Reads bits from a byte buffer, used by both method 1 and method 2.

<a id="propack.bitreader.BitReader.read_bits_m1"></a>

#### read\_bits\_m1

```python
def read_bits_m1(count: int) -> int
```

Read bits in method 1 style (LSB first, 16-bit token, lookahead).

<a id="propack.bitreader.BitReader.read_bits_m2"></a>

#### read\_bits\_m2

```python
def read_bits_m2(count: int) -> int
```

Read bits in method 2 style (MSB first, 8-bit token).

<a id="propack.unpack"></a>

# propack.unpack

<a id="propack.unpack.unpack"></a>

#### unpack

```python
def unpack(data: bytes | bytearray, key: int = 0) -> bytes
```

Decompress RNC ProPack compressed data.

**Arguments**:

- `data` - raw file data starting with RNC header
- `key` - encryption key (0 for unencrypted files)
  

**Returns**:

  decompressed data as bytes
  

**Raises**:

- `ValueError` - on invalid header, CRC mismatch, or corrupt data

<a id="propack.crc"></a>

# propack.crc

<a id="propack.pack"></a>

# propack.pack

RNC ProPack compression.

<a id="propack.pack.pack"></a>

#### pack

```python
def pack(data: bytes | bytearray, method: int = 1, key: int = 0) -> bytes
```

Compress data using RNC ProPack.

**Arguments**:

- `data` - raw uncompressed data
- `method` - compression method (1 or 2)
- `key` - encryption key (0 for no encryption)
  

**Returns**:

  compressed data with RNC header as bytes
  

**Raises**:

- `ValueError` - if method is not 1 or 2, or data is empty

<a id="propack.bits"></a>

# propack.bits

Shared bit manipulation utilities.

<a id="propack.bits.ror16"></a>

#### ror16

```python
def ror16(key)
```

Rotate right 16-bit value by 1.

<a id="propack.bits.inverse_bits"></a>

#### inverse\_bits

```python
def inverse_bits(value, count)
```

Reverse the bit order of value over count bits.

<a id="propack.constants"></a>

# propack.constants

<a id="propack.bitwriter"></a>

# propack.bitwriter

<a id="propack.bitwriter.BitWriterM2"></a>

## BitWriterM2 Objects

```python
class BitWriterM2()
```

Write bits MSB-first into 8-bit tokens, with interleaved byte queue.

<a id="propack.bitwriter.BitWriterM2.flush_pending"></a>

#### flush\_pending

```python
def flush_pending()
```

Flush pending bytes directly if no bits are buffered.

<a id="propack.bitwriter.BitWriterM1"></a>

## BitWriterM1 Objects

```python
class BitWriterM1()
```

Write bits LSB-first into 16-bit tokens, with interleaved byte queue.

