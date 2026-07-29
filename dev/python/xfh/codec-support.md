# Codec support

`xfh` decodes 53 XPK codec identifiers in pure Python.

| Evidence | Codecs |
| --- | --- |
| Original Amiga fixture | ACCA, BLFH, BLZW, BZP2, CBR0, DLTA, DUKE, ELZX, ENCO, FAST, FBR2, FEAL, FRLE, GZIP, HFMN, HUFF, IDEA, ILZR, IMPL, LHLB, LZBS, LZCB, LZW2, LZW3, LZW4, LZW5, MASH, NONE, NUID, NUKE, PPMQ, RAKE, RDCN, RLEN, SASC, SDHC, SHID, SHRI, SHSC, SLZ3, SLZX, SQSH, ZENO |
| Exact historical alias | CBR1, FRHT |
| Independent or source-derived fixture | ARTM, CRM2, CRMS, CYB2, PWPK, SHR3, SMPL, TDCS |

Original fixtures were packed and unpacked by preserved Amiga software under
headless UAE, then decoded byte-exactly by `xfh`. The fixture manifest records
their provenance, sizes, and hashes.

`BLFH`, `ENCO`, `FEAL`, `IDEA`, `NUID`, and `SHID` require a password. BLFH
supports packed and unpacked ECB, OFB, CFB, and CBC streams across modes 0–100.
These obsolete ciphers are provided only for data recovery.

## Evidence gaps

- `ARTM` and `SHR3`: no original library is available.
- `CYB2`: its preserved library does not expose a usable packing path.
- `TDCS`: no original library or packed sample is available.
- `SMPL`: the original packer emitted raw chunks for all tested inputs.
- `CRM2` and `CRMS`: verified with an independent Crunch-Mania implementation.
- `PWPK`: verified with the original PPMC utility and Ancient, but wrapped in a
  source-built XPK container.

## Unsupported preserved codecs

`CYB1`, `DHUF`, and `DMCB` are not implemented. Their preserved packers cannot
produce a compressed fixture suitable for safe decoder development:

- `CYB1` is decrunch-only.
- `DHUF` copies input instead of emitting compressed chunks.
- `DMCB` emits raw chunks for small inputs and hangs on larger probes.

Historical packed samples would allow these decoders to be completed.
