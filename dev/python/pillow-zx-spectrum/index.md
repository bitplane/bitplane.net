# `pillow_zx_spectrum`

<table>
<tr>
<td><img src="https://bitplane.net/dev/python/pillow-zx-spectrum/jetpac.png" alt="Jetpac"></td>
<td><img src="https://bitplane.net/dev/python/pillow-zx-spectrum/dizzy.png" alt="Treasure Island Dizzy"></td>
<td><img src="https://bitplane.net/dev/python/pillow-zx-spectrum/decathlon.png" alt="Daley Thompson's Decathlon"></td>
<td><img src="https://bitplane.net/dev/python/pillow-zx-spectrum/willy.png" alt="Jet Set Willy II"></td>
</tr>
</table>

Pillow loaders for ZX Spectrum loading screens, extracted from tape, disk
and snapshot files in the wild.

Open a tape, disk image, or snapshot with `Image.open(...)` and Pillow
gives you a 256×192 RGB image with the original Spectrum colours. Files
that contain multiple screens (multi-load games, multi-side disks)
expose them as Pillow frames via `seek()` / `n_frames`.

## Install

```bash
pip install pillow_zx_spectrum
```

## Usage

```python
from PIL import Image
import pillow_zx_spectrum  # registers the plugins on import

img = Image.open("Glug Glug (1984)(CRL).tap")
img.save("loading-screen.png")
print(img.size)                   # (256, 192)
print(img.info["pixel_aspect_ratio"])  # (1, 1)
```

Multi-screen containers (disks, multi-load tapes) expose every screen
they hold. Iterate with the stock Pillow helper:

```python
from PIL import ImageSequence

img = Image.open("Moonwalker (Erbe).dsk")
print(img.n_frames)  # e.g. 2
for i, frame in enumerate(ImageSequence.Iterator(img)):
    frame.save(f"moonwalker.{i}.png")
```

## Supported formats

### Tape

| Ext    | Format          | Notes |
| ------ | --------------- | ----- |
| `.tap` | TAP             | Plain ROM-loader block stream |
| `.tzx` | TZX             | Versioned tape with timing/meta blocks; we extract from standard (0x10) and turbo-speed (0x11) data blocks. Custom-loader pure-data blocks (SpeedLock / BleepLoad / Alkatraz, block 0x14) are skipped — they need per-protection decoders. |
| `.scr` | SCREEN$         | Raw 6912-byte screen dump |

### Disk

| Ext    | Format          | Notes |
| ------ | --------------- | ----- |
| `.dsk` | CPC DSK         | Spectrum +3 / Amstrad CPC, both standard and "Extended" variants. CP/M file system parsed (handles fragmented allocation). Auto-detects single/double-sided and various reserved-track conventions. |
| `.scl` | TR-DOS packed   | "SINCLAIR" magic, compact distribution format used in Russian-speaking scene |
| `.trd` | TR-DOS raw      | Sector-by-sector TR-DOS floppy dump; tolerant of truncated images |
| `.mgt` | DISCiPLE / +D   | Side-interleaved 80-track disk for the MGT DISCiPLE & +D interfaces. CODE/SCREEN$ files reassembled by following the per-sector chain. |
| `.d40`, `.d80` | Didaktik MDOS | Czechoslovak Didaktik D40/D80 floppy. MDOS file system with non-standard FAT12 packing (the 12-bit entries' high nibbles are byte-swapped relative to MS FAT12). Auto-detects geometry from the boot sector "SDOS" marker. Most TOSEC Czech games use packed loaders so plain SCREEN$ extraction is rare. |

### Microdrive

| Ext    | Format          | Notes |
| ------ | --------------- | ----- |
| `.mdr` | Microdrive cart | Sector-by-sector dump of a Spectrum Microdrive cartridge (543-byte sectors with mod-255 checksums). Files reconstructed by gathering all records belonging to a filename and stripping the inline 9-byte header. PRINT# files are not handled. |

### Snapshot

| Ext    | Format          | Notes |
| ------ | --------------- | ----- |
| `.sna` | SNA             | Classic 48K (49179 bytes) / 128K (131103 bytes) snapshot |
| `.z80` | Z80             | Gerton Lunter format (v1, v2, v3); 48K and 128K with bank decompression |
| `.szx` | SZX / ZX-State  | Spectaculator's modern chunked snapshot, with zlib-compressed RAM pages |
| `.slt` | SLT             | "Super Level Loader" — a Z80 snapshot with a table of additional screens (each becomes a frame) |

For 128K snapshots the shadow screen (bank 7) is exposed as an extra
frame when it's distinct from the main screen.

## How it works

Every container is reduced to a sequence of **load events** —
`(addr, body, name, kind)` tuples — and walked into a 64K Spectrum RAM
image. After each write the pipeline harvests two kinds of candidate:

1. **Direct** — if the event's body is exactly 6912 bytes (the SCREEN$
   shape), it might *be* a screen, regardless of its load address.
2. **RAM snapshot** — slice `$4000-$5AFF` after the write and emit it if
   the screen area now contains a new picture (catches screens loaded as
   part of larger CODE blocks, screens overwritten by later loads, etc.)

Candidates are then ranked by filename hint (`SCR` / `PIC` / `TITL` /
`LOAD` / `INTRO`...) → canonical `$4000` address → other; bodies that
clearly aren't screens (random attribute distribution, all-FLASH cells)
are dropped. The same pipeline runs for every format.

## What we don't load

- **Sampled-audio tapes** (`.csw`, `.wav`, `.mp3`) — these encode the
  loader's pulse train, decoding requires a Z80 emulator running the
  Spectrum ROM
- **Copy-protected disks** (`.ipf`) — needs the CAPS/SPS library
- **Custom-loader tapes** (SpeedLock 7, Alkatraz, BleepLoad, ...) —
  non-standard timing; the screen lives inside TZX 0x14 pure-data blocks
  that we skip rather than implement per-protection decoders for
- **16K Spectrum games** — no SCREEN$ saved before the program
- **BASIC-only programs** that draw their screen at runtime

These cases produce `UnidentifiedImageError` ("recognised the format,
nothing to extract") rather than a misleading blank frame.

## License

WTFPL with one additional clause:

1. Don't blame me.

Do what you like, but you're to blame.
