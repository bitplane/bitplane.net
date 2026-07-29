<a id="xfh"></a>

# xfh

Recover files compressed with historical Amiga XPK tools.

<a id="xfh.cli"></a>

# xfh.cli

Command-line interface.

<a id="xfh.cli.main"></a>

#### main

```python
def main(argv: list[str] | None = None) -> int
```

Run the CLI and return its process status.

<a id="xfh.limits"></a>

# xfh.limits

Resource limits applied before allocating decompressed output.

<a id="xfh.limits.Limits"></a>

## Limits Objects

```python
@dataclass(frozen=True, slots=True)
class Limits()
```

Limits used to bound work on untrusted compressed input.

<a id="xfh.__main__"></a>

# xfh.\_\_main\_\_

Module entry point for ``python -m xfh``.

<a id="xfh.models"></a>

# xfh.models

Immutable metadata returned by the public API.

<a id="xfh.models.FileFormat"></a>

## FileFormat Objects

```python
class FileFormat(str, Enum)
```

Known XPK stream container variants.

<a id="xfh.models.ChunkInfo"></a>

## ChunkInfo Objects

```python
@dataclass(frozen=True, slots=True)
class ChunkInfo()
```

Metadata for one encoded stream chunk.

<a id="xfh.models.FileInfo"></a>

## FileInfo Objects

```python
@dataclass(frozen=True, slots=True)
class FileInfo()
```

Parsed stream metadata.

<a id="xfh.models.RecoveryIssue"></a>

## RecoveryIssue Objects

```python
@dataclass(frozen=True, slots=True)
class RecoveryIssue()
```

One reason why salvage output is incomplete.

<a id="xfh.models.RecoveryResult"></a>

## RecoveryResult Objects

```python
@dataclass(frozen=True, slots=True)
class RecoveryResult()
```

Partial or complete output from explicit salvage mode.

<a id="xfh.codecs.ilzr"></a>

# xfh.codecs.ilzr

XPK ILZR decompression.

Derived from Ancient's ILZRDecompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.ilzr.decompress_ilzr"></a>

#### decompress\_ilzr

```python
@register("ILZR")
def decompress_ilzr(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode incremental Lempel-Ziv-Renau data.

<a id="xfh.codecs.fast"></a>

# xfh.codecs.fast

XPK FAST decompression.

<a id="xfh.codecs.fast.decompress_fast"></a>

#### decompress\_fast

```python
@register("FAST")
def decompress_fast(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one FAST chunk.

<a id="xfh.codecs.lzw_variants"></a>

# xfh.codecs.lzw\_variants

CyberYAFA XPK LZW2, LZW3, LZW4, and LZW5 decompression.

Despite their names, these formats are control-bit LZ variants rather than
dictionary-based LZW streams.

Derived from Ancient's LZW2Decompressor, LZW4Decompressor, and
LZW5Decompressor, Copyright (c) 2017-2025 Teemu Suutari, under the BSD
2-Clause License.

<a id="xfh.codecs.lzw_variants.decompress_lzw2"></a>

#### decompress\_lzw2

```python
@register("LZW2")
def decompress_lzw2(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an LZW2 stream.

<a id="xfh.codecs.lzw_variants.decompress_lzw3"></a>

#### decompress\_lzw3

```python
@register("LZW3")
def decompress_lzw3(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an LZW3 stream, whose packed representation matches LZW2.

<a id="xfh.codecs.lzw_variants.decompress_lzw4"></a>

#### decompress\_lzw4

```python
@register("LZW4")
def decompress_lzw4(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an LZW4 stream.

<a id="xfh.codecs.lzw_variants.decompress_lzw5"></a>

#### decompress\_lzw5

```python
@register("LZW5")
def decompress_lzw5(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an LZW5 stream.

<a id="xfh.codecs.rdcn"></a>

# xfh.codecs.rdcn

XPK RDCN decompression.

Derived from Ancient's RDCNDecompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.rdcn.decompress_rdcn"></a>

#### decompress\_rdcn

```python
@register("RDCN")
def decompress_rdcn(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode Ross Data Compression chunks.

<a id="xfh.codecs._range"></a>

# xfh.codecs.\_range

Shared 16-bit arithmetic range decoder.

<a id="xfh.codecs._range.RangeDecoder"></a>

## RangeDecoder Objects

```python
class RangeDecoder()
```

Decode integer ranges using the historical XPK 16-bit coder.

<a id="xfh.codecs.standard"></a>

# xfh.codecs.standard

XPK wrappers around standardized compression streams.

<a id="xfh.codecs.standard.decompress_bzp2"></a>

#### decompress\_bzp2

```python
@register("BZP2")
def decompress_bzp2(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an XPK-wrapped bzip2 stream.

<a id="xfh.codecs.standard.decompress_gzip"></a>

#### decompress\_gzip

```python
@register("GZIP")
def decompress_gzip(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode GZIP's zlib-format payload.

<a id="xfh.codecs.zeno"></a>

# xfh.codecs.zeno

XPK ZENO decompression.

Derived from Ancient's ZENODecompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.zeno.decompress_zeno"></a>

#### decompress\_zeno

```python
@register("ZENO")
def decompress_zeno(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode ZENO's variable-width dictionary stream.

<a id="xfh.codecs.impl"></a>

# xfh.codecs.impl

XPK File Imploder decompression.

<a id="xfh.codecs.impl.decompress_impl"></a>

#### decompress\_impl

```python
@register("IMPL")
def decompress_impl(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an XPK-wrapped File Imploder stream.

<a id="xfh.codecs.sqsh"></a>

# xfh.codecs.sqsh

XPK SQSH decompression.

<a id="xfh.codecs.sqsh.decompress_sqsh"></a>

#### decompress\_sqsh

```python
@register("SQSH")
def decompress_sqsh(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an SQSH sample-prediction and LZ stream.

<a id="xfh.codecs.pwpk"></a>

# xfh.codecs.pwpk

XPK PowerPacker (PWPK) decompression.

<a id="xfh.codecs.pwpk.decompress_pwpk"></a>

#### decompress\_pwpk

```python
@register("PWPK")
def decompress_pwpk(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode a PowerPacker chunk.

<a id="xfh.codecs.ppmq"></a>

# xfh.codecs.ppmq

XPK PPMQ decompression.

Derived from Ancient's PPMQDecompressor, Copyright (c) 2017-2026
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.ppmq.decompress_ppmq"></a>

#### decompress\_ppmq

```python
@register("PPMQ")
def decompress_ppmq(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one PPMQ prediction-by-partial-matching chunk.

<a id="xfh.codecs.smpl"></a>

# xfh.codecs.smpl

XPK SMPL decompression.

<a id="xfh.codecs.smpl.decompress_smpl"></a>

#### decompress\_smpl

```python
@register("SMPL")
def decompress_smpl(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode a static Huffman stream followed by byte delta prediction.

<a id="xfh.codecs._prefix"></a>

# xfh.codecs.\_prefix

Small prefix-code helpers shared by XPK codecs.

<a id="xfh.codecs._prefix.PrefixDecoder"></a>

## PrefixDecoder Objects

```python
class PrefixDecoder()
```

Decode explicit most-significant-bit-first prefix codes.

<a id="xfh.codecs._prefix.PrefixDecoder.decode"></a>

#### decode

```python
def decode(bits: object) -> int
```

Decode one value from an object exposing ``read(count)``.

<a id="xfh.codecs._prefix.variable_length"></a>

#### variable\_length

```python
def variable_length(bits: object, specifications: tuple[int, ...],
                    index: int) -> int
```

Decode an indexed variable-length integer with cumulative bases.

<a id="xfh.codecs._streams"></a>

# xfh.codecs.\_streams

Bounded byte and bit streams used by historical XPK codecs.

The stream behavior is derived from Ancient, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs._streams.CoupledInput"></a>

## CoupledInput Objects

```python
class CoupledInput()
```

Forward word reads and backward byte reads sharing one payload.

<a id="xfh.codecs._streams.ByteInput"></a>

## ByteInput Objects

```python
class ByteInput()
```

A bounded forward byte stream.

<a id="xfh.codecs._streams.BitReader"></a>

## BitReader Objects

```python
class BitReader()
```

Read most- or least-significant bits from fixed-width words.

<a id="xfh.codecs._streams.copy_forward"></a>

#### copy\_forward

```python
def copy_forward(output: bytearray, distance: int, count: int,
                 output_size: int) -> None
```

Copy an overlapping LZ match within a bounded output buffer.

<a id="xfh.codecs.crm"></a>

# xfh.codecs.crm

Crunch-Mania XPK codecs.

<a id="xfh.codecs.dlta"></a>

# xfh.codecs.dlta

XPK DLTA decompression.

<a id="xfh.codecs.dlta.decompress_dlta"></a>

#### decompress\_dlta

```python
@register("DLTA")
def decompress_dlta(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode DLTA's byte-delta transform.

<a id="xfh.codecs.mash"></a>

# xfh.codecs.mash

XPK MASH decompression.

<a id="xfh.codecs.mash.decompress_mash"></a>

#### decompress\_mash

```python
@register("MASH")
def decompress_mash(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode a MASH mixed literal and LZ stream.

<a id="xfh.codecs.wrappers"></a>

# xfh.codecs.wrappers

Nested and transform XPK codecs.

Derived from Ancient's CYB2Decoder and SDHCDecompressor,
Copyright (c) 2017-2025 Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.wrappers.decompress_cyb2"></a>

#### decompress\_cyb2

```python
@register("CYB2")
def decompress_cyb2(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode a CYB2 wrapper around another XPK codec payload.

<a id="xfh.codecs.wrappers.decompress_sdhc"></a>

#### decompress\_sdhc

```python
@register("SDHC")
def decompress_sdhc(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode SDHC's optional nested stream and sample delta transform.

<a id="xfh.codecs.nuke"></a>

# xfh.codecs.nuke

XPK NUKE decompression.

Derived from Ancient's NUKEDecompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.nuke.decompress_nuke"></a>

#### decompress\_nuke

```python
@register("NUKE")
def decompress_nuke(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one NUKE chunk.

<a id="xfh.codecs.nuke.decompress_duke"></a>

#### decompress\_duke

```python
@register("DUKE")
def decompress_duke(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode NUKE data followed by DUKE's byte-delta transform.

<a id="xfh.codecs.shri"></a>

# xfh.codecs.shri

XPK SHRI decompression.

Derived from Ancient's SHRXDecompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.shri.ShriState"></a>

## ShriState Objects

```python
@dataclass(slots=True)
class ShriState()
```

Adaptive model carried by SHRI version 2 continuation chunks.

<a id="xfh.codecs.shri.decompress_shri_chunk"></a>

#### decompress\_shri\_chunk

```python
def decompress_shri_chunk(payload: bytes,
                          output_size: int,
                          previous: bytes,
                          state: ShriState | None,
                          *,
                          shr3: bool = False) -> tuple[bytes, ShriState]
```

Decode one SHRI chunk and return its continuation model.

<a id="xfh.codecs.shri.decompress_shri"></a>

#### decompress\_shri

```python
@register("SHRI")
def decompress_shri(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one independently initialized SHRI chunk.

<a id="xfh.codecs.shri.decompress_shr3"></a>

#### decompress\_shr3

```python
@register("SHR3")
def decompress_shr3(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one independently initialized SHR3 chunk.

<a id="xfh.codecs.rle"></a>

# xfh.codecs.rle

XPK byte-run codecs.

Derived from Ancient's CBR0, FRLE, and RLEN decompressors,
Copyright (c) 2017-2025 Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.rle.decompress_cbr0"></a>

#### decompress\_cbr0

```python
@register("CBR1")
@register("CBR0")
def decompress_cbr0(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode Commodore ByteRun-style CBR0/CBR1 data.

<a id="xfh.codecs.rle.decompress_rlen"></a>

#### decompress\_rlen

```python
@register("RLEN")
def decompress_rlen(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode XPK RLEN data.

<a id="xfh.codecs.rle.decompress_frle"></a>

#### decompress\_frle

```python
@register("FRLE")
def decompress_frle(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode cache-oriented XPK FRLE data.

<a id="xfh.codecs.artm"></a>

# xfh.codecs.artm

XPK ARTM arithmetic decompression.

Derived from Ancient's ARTMDecompressor and RangeDecoder,
Copyright (c) 2017-2025 Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.artm.decompress_artm"></a>

#### decompress\_artm

```python
@register("ARTM")
def decompress_artm(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode ARTM's adaptive arithmetic stream.

<a id="xfh.codecs.rake"></a>

# xfh.codecs.rake

XPK RAKE decompression.

Derived from Ancient's RAKEDecompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.rake.decompress_rake"></a>

#### decompress\_rake

```python
@register("FRHT")
@register("RAKE")
def decompress_rake(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one RAKE/FRHT chunk.

<a id="xfh.codecs.fbr2"></a>

# xfh.codecs.fbr2

XPK FBR2 decompression.

Derived from Ancient's FBR2Decompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.fbr2.decompress_fbr2"></a>

#### decompress\_fbr2

```python
@register("FBR2")
def decompress_fbr2(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode CyberYAFA FBR2 byte runs.

<a id="xfh.codecs.none"></a>

# xfh.codecs.none

The XPK NONE storage codec.

<a id="xfh.codecs.none.decompress_none"></a>

#### decompress\_none

```python
@register("NONE")
def decompress_none(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Return a raw NONE chunk after validating its declared size.

<a id="xfh.codecs.lz_small"></a>

# xfh.codecs.lz\_small

Small historical XPK LZ codecs.

Derived from Ancient's LZBSDecompressor, SLZ3Decompressor, and
TDCSDecompressor, Copyright (c) 2017-2025 Teemu Suutari, under the BSD
2-Clause License.

<a id="xfh.codecs.lz_small.decompress_lzbs"></a>

#### decompress\_lzbs

```python
@register("LZBS")
def decompress_lzbs(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode the CyberYAFA LZBS format.

<a id="xfh.codecs.lz_small.decompress_slz3"></a>

#### decompress\_slz3

```python
@register("SLZ3")
def decompress_slz3(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode the CyberYAFA SLZ3 format.

<a id="xfh.codecs.lz_small.decompress_tdcs"></a>

#### decompress\_tdcs

```python
@register("TDCS")
def decompress_tdcs(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode TDCS LZ77 data.

<a id="xfh.codecs.lhlb"></a>

# xfh.codecs.lhlb

XPK LHLB decompression.

Derived from Ancient's LHDecompressor and DynamicHuffmanDecoder,
Copyright (c) 2017-2025 Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.lhlb.decompress_lhlb"></a>

#### decompress\_lhlb

```python
@register("LHLB")
def decompress_lhlb(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode the lh.library-compatible LHLB format.

<a id="xfh.codecs.acca"></a>

# xfh.codecs.acca

XPK ACCA decompression.

Derived from Ancient's ACCADecompressor, Copyright (c) 2017-2025
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.acca.decompress_acca"></a>

#### decompress\_acca

```python
@register("ACCA")
def decompress_acca(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode Andre's code compression algorithm.

<a id="xfh.codecs.lzx_wrappers"></a>

# xfh.codecs.lzx\_wrappers

XPK wrappers around the classic Amiga LZX archiver.

<a id="xfh.codecs.lzx_wrappers.decompress_elzx"></a>

#### decompress\_elzx

```python
@register("ELZX")
def decompress_elzx(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an Amiga LZX archive embedded by xpkELZX.

<a id="xfh.codecs.lzx_wrappers.decompress_slzx"></a>

#### decompress\_slzx

```python
@register("SLZX")
def decompress_slzx(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode xpkSLZX's Amiga LZX member and cumulative-byte transform.

<a id="xfh.codecs.lzcb"></a>

# xfh.codecs.lzcb

XPK LZCB decompression.

Derived from Ancient's LZCBDecompressor and RangeDecoder,
Copyright (c) 2017-2026 Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.lzcb.decompress_lzcb"></a>

#### decompress\_lzcb

```python
@register("LZCB")
def decompress_lzcb(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one LZCB range-coded LZ chunk.

<a id="xfh.codecs.amiga_lzx"></a>

# xfh.codecs.amiga\_lzx

Pure-Python decoder for the classic Amiga LZX archive format.

This is the Amiga archiver format, not the unrelated Microsoft LZX format.
The implementation follows the independently documented decoder in
``amiga-lzx`` and is intentionally limited to the single-entry archives
embedded by the ELZX and SLZX XPK libraries.

<a id="xfh.codecs.amiga_lzx.decompress_archive"></a>

#### decompress\_archive

```python
def decompress_archive(data: bytes, output_size: int) -> bytes
```

Decode the single-entry Amiga LZX archive embedded in an XPK chunk.

<a id="xfh.codecs.hfmn"></a>

# xfh.codecs.hfmn

XPK HFMN decompression.

<a id="xfh.codecs.hfmn.decompress_hfmn"></a>

#### decompress\_hfmn

```python
@register("HFMN")
def decompress_hfmn(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode an HFMN dynamic Huffman stream.

<a id="xfh.codecs.blzw"></a>

# xfh.codecs.blzw

XPK BLZW decompression.

Derived from Ancient's BLZWDecompressor and LZWDecoder,
Copyright (c) 2017-2025 Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.blzw.decompress_blzw"></a>

#### decompress\_blzw

```python
@register("BLZW")
def decompress_blzw(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode Bryan Ford's XPK BLZW format.

<a id="xfh.codecs.huff"></a>

# xfh.codecs.huff

XPK HUFF decompression.

<a id="xfh.codecs.huff.decompress_huff"></a>

#### decompress\_huff

```python
@register("HUFF")
def decompress_huff(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one HUFF chunk.

<a id="xfh.codecs"></a>

# xfh.codecs

XPK codec registry.

<a id="xfh.codecs.register"></a>

#### register

```python
def register(codec: str) -> Callable[[Decoder], Decoder]
```

Register a decoder by its four-character XPK identifier.

<a id="xfh.codecs.decode"></a>

#### decode

```python
def decode(codec: str,
           payload: bytes,
           output_size: int,
           previous: bytes = b"") -> bytes
```

Decode one packed XPK chunk.

<a id="xfh.codecs.supported_codecs"></a>

#### supported\_codecs

```python
def supported_codecs() -> frozenset[str]
```

Return codec identifiers implemented by this build.

<a id="xfh.codecs.sxsc"></a>

# xfh.codecs.sxsc

XPK SASC and SHSC decompression.

Derived from Ancient's SXSCDecompressor, Copyright (c) 2017-2026
Teemu Suutari, under the BSD 2-Clause License.

<a id="xfh.codecs.sxsc.decompress_sasc"></a>

#### decompress\_sasc

```python
@register("SASC")
def decompress_sasc(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one SASC arithmetic-LZ chunk.

<a id="xfh.codecs.sxsc.decompress_shsc"></a>

#### decompress\_shsc

```python
@register("SHSC")
def decompress_shsc(payload: bytes,
                    output_size: int,
                    previous: bytes = b"") -> bytes
```

Decode one SHSC finite-context arithmetic chunk.

<a id="xfh.errors"></a>

# xfh.errors

Public exception hierarchy.

<a id="xfh.errors.XfhError"></a>

## XfhError Objects

```python
class XfhError(Exception)
```

Base class for expected recovery failures.

<a id="xfh.errors.InvalidFormatError"></a>

## InvalidFormatError Objects

```python
class InvalidFormatError(XfhError)
```

The input is not a recognized XPK stream.

<a id="xfh.errors.CorruptDataError"></a>

## CorruptDataError Objects

```python
class CorruptDataError(XfhError)
```

The stream is recognized but fails structural or checksum validation.

<a id="xfh.errors.UnsupportedCodecError"></a>

## UnsupportedCodecError Objects

```python
class UnsupportedCodecError(XfhError)
```

The stream uses a codec or mode which is not implemented.

<a id="xfh.errors.PasswordRequiredError"></a>

## PasswordRequiredError Objects

```python
class PasswordRequiredError(XfhError)
```

The input is encrypted and needs a password.

<a id="xfh.errors.ResourceLimitError"></a>

## ResourceLimitError Objects

```python
class ResourceLimitError(XfhError)
```

The stream exceeds a configured recovery safety limit.

<a id="xfh.api"></a>

# xfh.api

Public recovery API.

<a id="xfh.api.detect"></a>

#### detect

```python
def detect(data: bytes | bytearray | memoryview) -> FileFormat
```

Detect an XPK container variant.

<a id="xfh.api.inspect"></a>

#### inspect

```python
def inspect(data: bytes | bytearray | memoryview,
            *,
            limits: Limits = DEFAULT_LIMITS) -> FileInfo
```

Parse and validate stream metadata without decompressing it.

<a id="xfh.api.decompress"></a>

#### decompress

```python
def decompress(data: bytes | bytearray | memoryview,
               *,
               password: str | bytes | None = None,
               limits: Limits = DEFAULT_LIMITS) -> bytes
```

Strictly decompress one complete stream.

<a id="xfh.api.salvage"></a>

#### salvage

```python
def salvage(data: bytes | bytearray | memoryview,
            *,
            limits: Limits = DEFAULT_LIMITS) -> RecoveryResult
```

Recover verified chunks until the first decoding failure.

<a id="xfh.api.decompress_file"></a>

#### decompress\_file

```python
def decompress_file(source: str | os.PathLike[str],
                    destination: str | os.PathLike[str],
                    *,
                    overwrite: bool = False,
                    password: str | bytes | None = None,
                    limits: Limits = DEFAULT_LIMITS) -> FileInfo
```

Decompress to an atomic destination path.

<a id="xfh.container"></a>

# xfh.container

Strict parsers for historical XPK stream containers.

<a id="xfh.container.ParsedChunk"></a>

## ParsedChunk Objects

```python
@dataclass(frozen=True, slots=True)
class ParsedChunk()
```

Internal chunk metadata and its encoded bytes.

<a id="xfh.container.ParsedFile"></a>

## ParsedFile Objects

```python
@dataclass(frozen=True, slots=True)
class ParsedFile()
```

Internal parsed stream.

<a id="xfh.container.detect_format"></a>

#### detect\_format

```python
def detect_format(data: bytes) -> FileFormat
```

Detect a supported container without parsing it.

<a id="xfh.container.parse"></a>

#### parse

```python
def parse(data: bytes, limits: Limits) -> ParsedFile
```

Parse and validate one complete stream.

