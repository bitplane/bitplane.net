# Codec support and evidence

`xfh` currently recognizes 41 XPK identifiers. “Amiga pack” means at least one
fixture was created and unpacked by the original Amiga libraries under
headless UAE, then decoded byte-exactly by Python. “Derived” means the decoder
is covered by source-derived or transformed fixtures but an original packer
artifact is not yet available.

| Evidence | Codecs |
| --- | --- |
| Original Amiga pack/unpack | ACCA, BLZW, BZP2, CBR0, DLTA, DUKE, FAST, FBR2, FRLE, GZIP, HFMN, HUFF, ILZR, IMPL, LHLB, LZBS, LZW2, LZW3, LZW4, LZW5, MASH, NONE, NUKE, RAKE, RDCN, RLEN, SDHC, SHRI, SLZ3, SQSH, ZENO |
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

The preservation archive contains further codecs that are not implemented
yet. Wrapper/backend formats are being prioritized before encryption,
authentication, and preference-system formats.
