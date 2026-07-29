# Initial XFH / xpkNUKE recovery notes

## The job

`~/Documents/amiga/amiga.ddr.img` is a 3-partition Amiga drive image. Its
third partition, **dh2 `SHITE`**, ran **XFH** — the AmigaOS *xpk File
Handler*, a DOS handler that transparently compresses everything written to
a directory or partition via `xpkmaster.library`. **2,356 of its 5,276
files** are compressed with the **xpkNUKE** sublibrary and cannot currently
be read.

| partition | sector range | crunched | total |
|---|---|---|---|
| dh1 `WORKBENCH` | 1536 + 82944 | 1 | 4,459 |
| dh0 `WORK` | 84480 + 411648 | 0 | 7,433 |
| **dh2 `SHITE`** | **496128 + 217344** | **2,356** | **5,276** |

Goal: read them. The headline prize is `kaos/shit/` — 63 files of digitised
animation frames from 1991–1995 by Matt Benson, Dave Gary, James Benson and
John Hayes, including a claymation wombat with six arms, one of which falls
off mid-animation. But it is 2,356 files in total, across `Other`, `Games`,
`t`, `GadToolsBox`, `Legion`, `GMS` and more.

## Why it is XFH and not someone crunching files

- **252 crunched files in `t/`** — the temp directory. Nobody hand-crunches
  temp files.
- `.info` icons of ~300 bytes are crunched, where compression is pointless.
- It spans a dozen unrelated drawers, and is confined to one partition.

No `xpkmaster.library` and no XFH handler survive on the drive (only
`xfdmaster`, bundled with virus checkers, which is the unrelated *decrunch*
library). So the handler binary is not available to disassemble.

## The container, as far as it is decoded

Verified byte-exactly against `samples/matt1.info` (310 bytes on disk):

```
+0   01 80 63 68 05 61 01 0a   constant magic, identical in every file
+8   ULONG   unpacked length            (460 for matt1.info)
+12  ULONG   length of everything from +8 onward
                                        (302; and 302 + 8 = 310 = file size)
+16  "xpkNUKE\0"                8 bytes, NUL-padded
+24  compressed data
```

Sample sizes:

| file | on disk | unpacked (from +8) |
|---|---|---|
| `matt1.info` | 310 | 460 |
| `wombat1.pic` | 12,492 | 19,844 |
| `wombat` | 112,134 | 122,780 |
| `wombat2` | 190,746 | 206,006 |

**Unsolved:** for `wombat` the arithmetic leaves 560 bytes unaccounted for
(file − 8 − declared length). 560 = 35 × 16, and an XPK chunk header is 16
bytes, so the payload is probably chunked with per-chunk headers. The small
single-chunk files fit the simple layout; the large ones do not.

## What has been ruled out

**`ancient` (temisu, `apt install ancient`, installed) does NOT read these.**
It implements xpkNUKE correctly, but expects an `XPKF` *stream*. These are
XFH's container. Keep it installed anyway — it handles DMS and LhA, which
the corpus is full of.

`tools/try_xpkf.py` wraps the payload from +24 in a synthetic `XPKF` header
and brute-forces all 256 header-checksum values, looking for one `ancient`
will accept. It finds none, so the payload is not a bare XPK chunk stream —
or the assumed 36-byte `XPKF` header layout is wrong. Worth retrying with
other header lengths and with reconstructed chunk headers.

## The lever: known plaintext, in quantity

**382 filenames exist both crunched on dh2 and uncrunched on dh0/dh1.**
Pick one whose uncrunched size matches the crunched file's declared unpacked
length and you have a verified plaintext/ciphertext pair to develop and
check against. Reproduce with:

```bash
# tools/amigapeek.ts <image> <path-filter> <first-sector> <blocks>
# prints "size  path  <first 24 bytes as text>" per file
npx tsx tools/amigapeek.ts ~/Documents/amiga/amiga.ddr.img "" 496128 217344 > peek-dh2.txt
npx tsx tools/amigapeek.ts ~/Documents/amiga/amiga.ddr.img "" 84480 411648 > peek-dh0.txt
grep xpkNUKE peek-dh2.txt | awk '{print $2}' | awk -F/ '{print $NF}' | LC_ALL=C sort -u > c.txt
grep -v xpkNUKE peek-dh0.txt | awk '{print $2}' | awk -F/ '{print $NF}' | LC_ALL=C sort -u > u.txt
LC_ALL=C comm -12 c.txt u.txt
```

## Tools here

Run from `~/src/tmp/amos/amos-ts` (they import from its `src/`):

- `tools/amigaget.ts <img> <path> <out> [sector] [blocks]` — extract one file
- `tools/amigapeek.ts <img> <filter> [sector] [blocks]` — list files + first bytes
- `tools/amigadates.ts <img> [--sector N] [--blocks N]` — real AmigaDOS
  datestamps, tick precision
- `tools/abk2png.ts <file.abk> <prefix>` — render an AMOS sprite/icon bank
  (handles the `AmBs` multi-bank wrapper)
- `tools/try_xpkf.py <file>` — the failed XPKF-wrapping experiment

## Where this is written up

`~/src/tmp/amos/dating-amos-games.md`, section "Blocked: dh2 ran an XPK
filesystem packer".
