# Codec support and evidence

`xfh` currently recognizes 47 XPK identifiers. “Amiga pack” means at least one
fixture was created and unpacked by the original Amiga libraries under
headless UAE, then decoded byte-exactly by Python. “Derived” means the decoder
is covered by source-derived or transformed fixtures but an original packer
artifact is not yet available.

| Evidence | Codecs |
| --- | --- |
| Original Amiga pack/unpack | ACCA, BLZW, BZP2, CBR0, DLTA, DUKE, ELZX, FAST, FBR2, FRLE, GZIP, HFMN, HUFF, ILZR, IMPL, LHLB, LZBS, LZCB, LZW2, LZW3, LZW4, LZW5, MASH, NONE, NUKE, PPMQ, RAKE, RDCN, RLEN, SASC, SDHC, SHRI, SHSC, SLZ3, SLZX, SQSH, ZENO |
| Exact historical aliases | CBR1, FRHT |
| Derived or transformed | ARTM, CRM2, CRMS, CYB2, PWPK, SHR3, SMPL, TDCS |

The important remaining evidence gaps are:

- CYB2 needs a genuine file created through XpkCybPrefs; its standalone
  library does not expose packing modes and rejects hand-built containers.
- TDCS needs an original library or authentic packed sample.
- ARTM and SHR3 need preserved original libraries.
- SMPL’s original packer selected raw chunks for every tested vector, so its
  compressed-stream test remains source-derived.

PWPK has a positive stream produced by the original Amiga PPMC tool and
cross-checked with Ancient. CRM2 and CRMS have positive streams generated and
decoded by an independent Crunch-Mania implementation. They remain in the
derived row because the committed XPK envelopes were constructed outside the
original XPK master library.

ELZX and SLZX were packed and unpacked through their original libraries using
LZX 1.21R under headless UAE, then decoded byte-exactly by Python. Modes 0, 20,
21, 40, 41, 60, 61, 80, and 81 all succeeded. Both original wrappers hang when
mode 100 is passed to their external LZX command, so the oracle excludes that
exact mode while retaining it as preservation metadata.

## Preserved but not implemented

The preservation inventory contains nine additional XPK identifiers. The
original libraries were identified by filename, embedded version strings, and
an `xQuery` run under the isolated headless-UAE oracle.

| Class | Codecs | Notes |
| --- | --- | --- |
| Standalone compression | CYB1, DHUF, DMCB | Require authentic compressed samples |
| Encryption | BLFH, ENCO, FEAL, IDEA | Require password and encryption API design |
| Composite | NUID, SHID | Combine NUKE or SHRI with IDEA |

The embedded versions and original-library packing modes are:

| Codec | Version | Default | Ranges |
| --- | --- | ---: | --- |
| BLFH | 2.1 | 66 | 0–13 ECB, 14–25 ECB+pack, 26–38 OFB, 39–50 OFB+pack, 51–68 CFB, 69–75 CFB+pack, 76–88 CBC, 89–100 CBC+pack |
| CYB1 | 1.0 | 100 | 0–100 |
| DHUF | 0.58 | 50 | 0–100 |
| DMCB | 0.8 | 100 | 0–100 |
| ENCO | 1.3 | — | — |
| FEAL | 1.5 | — | — |
| IDEA | 1.3 | — | — |
| LZCB | 1.0 | 50 | 0–10, 11–90, 91–100 |
| NUID | 1.0 | 100 | 0–100 |
| PPMQ | 1.0 | 50 | 0–100 |
| SASC | 1.3 | 0 | 0–33 normal, 34–66 delta, 67–100 best |
| SHID | 1.0 | 100 | 0–14, 15–28, 29–42, 43–56, 57–70, 71–84, 85–100 |
| SHSC | 1.3 | 0 | 0–33 normal, 34–66 delta, 67–100 best |

ENCO, FEAL, and IDEA identify themselves to `xQuery` but do not expose normal
packing-mode metadata. They are deliberately deferred with BLFH, NUID, and
SHID until password handling is designed.

The seven standalone identifiers are not equally reproducible. The preserved
CYB1 1.0 library is decrunch-only: attempts to pack through the original XPK
master return “feature not implemented.” DHUF 0.58 reports a crunch capability,
but its crunch entry only copies the input; headless-UAE runs at modes 0, 50,
and 100 produced raw XPK chunks even for highly skewed input. Neither codec can
therefore yield a genuine compressed oracle fixture from the preserved
libraries alone. They remain recovery targets, but require a historical packed
sample or independently reconstructed encoder before implementation can be
verified safely.

DMCB 0.8 also fails the original-library fixture gate. It stores the short text
probe as a raw chunk, while both the ascending-byte and zero-filled 256-byte
probes hang the original compressor past the oracle's 120-second limit.
Without a historical compressed sample, implementing its arithmetic Markov
decoder would not be verifiable.

LZCB, PPMQ, SASC, and SHSC are implemented from their adaptive range-coded
streams. Every reported mode boundary was verified under headless UAE; SASC
and SHSC additionally cover both normal and delta preprocessing. CYB1, DHUF,
and DMCB are the remaining standalone preservation gaps described above.
