# Original-code oracle matrix

The isolated oracle uses FS-UAE 3.2.35, Workbench 3.1, xpkmaster 4.16
(21-Aug-1997), and recovered compressor libraries. ROMs, Amiga binaries,
private files, logs, and the complete workspace are not distributed.

`xQuery` reported these mode ranges:

| Codec | Default | Ranges |
| --- | ---: | --- |
| NONE | 50 | 0–100 |
| NUKE | 50 | 0–100 |
| FAST | 50 | 0–79, 80–100 |
| RAKE | 100 | 0–25, 26–50, 51–75, 76–100 |
| HUFF | 50 | 0–100 |
| SHRI | 100 | 0–14, 15–28, 29–42, 43–56, 57–70, 71–84, 85–100 |
| DLTA | 100 | 0–100 |
| SMPL | 50 | 0–100 |
| HFMN | 0 | 0–100 |
| MASH | 100 | 0–100 |
| SQSH | 100 | 0–100 |
| LZBS | 100 | 0, 1–10, 11–20, 21–30, 31–40, 41–50, 51–60, 61–70, 71–80, 81–90, 91–100 |
| SLZ3 | 100 | 0–100 |
| SDHC | 50 | 0–7, 8–15, 16–23, 24–31, 32–39, 40–47, 48–55, 56–63, 64–71, 72–79, 80–87, 88–100 |
| LHLB | 100 | 0–100 |
| BZP2 | 40 | 0–19, 20–29, 30–39, 40–49, 50–59, 60–69, 70–79, 80–89, 90–100 |
| GZIP | 65 | 0–9, 10–19, 20–29, 30–39, 40–49, 50–59, 60–69, 70–79, 80–89, 90–100 |
| IMPL | 100 | 0–10, 11–30, 31–50, 51–75, 76–98, 99–100 |

The matrix exercised every numeric mode on a canonical text vector and every
range boundary/default on deterministic pattern and size vectors:

- 990 byte-exact pack/unpack successes;
- 36 empty-input cases exposing an original-tool defect: a 36-byte XPKF header
  is emitted, then rejected by the same master library;
- one HUFF case which hangs after reporting successful compression, followed
  by 11 deliberately unrun HUFF cases;
- zero round-trip mismatches among completed non-empty cases.

All 1,026 emitted containers begin with `XPKF`. Small representative fixtures
for all six codecs are committed as reviewable hexadecimal files and validate
the current pure-Python implementations.

A second isolated run added `CBR0`, `RLEN`, `FRLE`, `RDCN`, `BLZW`, and
`DUKE`. Across the completed non-empty cases, all 372 original packed/plain
artifacts decode byte-exactly in Python. Compact acceptance containers for
each codec are committed as hexadecimal fixtures. The historical packers are
run in separate or short-lived emulator sessions because repeated use can
crash the original Amiga process; this is an oracle limitation rather than an
accepted decoder failure.

A third set covers `DLTA`, `SMPL`, `HFMN`, `MASH`, and `SQSH`. Short isolated
runs produced 35 byte-exact original pack/unpack artifacts across modes 0,
default, and 100. Python directly decoded all 20 generated compressed DLTA,
HFMN, MASH, and SQSH containers. The SMPL packer selected raw XPK chunks for
all 15 vectors, so its decoder additionally has a source-derived synthetic
prefix-code test rather than claiming compressed oracle coverage. DLTA hangs
on a one-byte input and HFMN hangs on one broad byte-pattern input; those
original-packer defects are excluded from the safe fixture stage.

Every compact committed acceptance container is recorded in the public
manifest with its input, output, size, and SHA-256 hashes. Known hanging
packer/vector pairs are machine-readable exclusions and are never emitted
into a guest stage. `oracle.py verify-python` performs the direct comparison
and records its results as JSON.

The CyberYAFA `LZW2`–`LZW5` variants are now backed by preserved original
libraries and headless UAE fixtures across every reported mode boundary.
`SHR3` remains source-derived because no corresponding original library has
been located; it is additionally tested by converting both packed chunks from
the 64 KiB SHRI continuation fixture to its headerless chunk representation.

Preserved original `ACCA`, `FBR2`, `ILZR`, and `ZENO` libraries were also
located and exercised under UAE. Together with the LZW family, 157 generated
artifacts round-trip in the original master library and decode byte-exactly in
Python. Compact fixtures, private library hashes, and the preservation archive
hash are linked in the public manifest; the binaries themselves are not
redistributed. `ARTM` remains source-derived because its original library has
not been located. Compact source-derived XPK containers for these codecs were
also independently compared byte-for-byte with Ancient 2.3.0 where Ancient
supports the emitted variant.

The next batch adds `LZBS`, `SLZ3`, `TDCS`, `LHLB`, `SDHC`, and `CYB2`.
Preserved `LZBS`, `SLZ3`, and `SDHC` packers produced 83 completed artifacts
across every reported mode boundary; Python decoded all of them byte-exactly.
Low-mode LZBS output also confirmed that its original depacker stops a final
literal run at the declared output size even when the packer rounds that run
up. Representative original-Amiga fixtures for all three codecs are committed.

`LHLB` initially appeared unpack-only because its required `lh.library` was
missing. Installing the original Aminet dependency exposes its 0–100 packing
range; a mode-100 artifact now round-trips in the Amiga master library and
decodes byte-exactly in Python. The dependency hash is recorded in the public
manifest, but the binary is not redistributed.

`CYB2` still reports no packing modes. Its preserved library also requires
`xpkcybhandle.library`; with that dependency and its `CYB1` companion installed,
the original library continues to reject source-constructed CYB2 containers
before unpacking. Consequently CYB2 remains source-derived rather than being
mislabelled as original-Amiga verified. `TDCS` has no library in the
preservation archive. Both retain synthetic success and malformed-stream
coverage.

Preserved BZP2, GZIP, and IMPL packers generated representative compressed
fixtures that round-trip under headless UAE and decode byte-exactly in Python.
The complete boundary/default matrix now contains 36 BZP2, 42 GZIP, 24 IMPL,
and six LHLB byte-exact successes with no Python mismatches.

PWPK, CRM2, and CRMS expose no packing modes in the preserved XPK libraries.
An original Amiga PPMC utility generated the positive PowerPacker stream used
by the PWPK fixture, which was also checked with Ancient. CRM2 and CRMS use
positive streams generated and decoded by an independent Crunch-Mania
implementation. Their XPK envelopes remain source-derived and are labelled
accordingly.

FS-UAE runs behind Xvfb with Mesa software rendering, so oracle generation
does not map a window onto the host desktop.

The recovered private wrapper beginning `01 80 63 68 05 61 01 0a` was not
recognized as packed data by the original master library. That result rules
out using generated XPKF files to infer its outer framing.
