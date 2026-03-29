# pillow-netpbm

A Pillow plugin that bridges netpbm converter binaries, adding read support for
dozens of legacy/obscure image formats.

## Supported formats

Each format is registered as a Pillow image plugin when its converter binary is
installed. Formats with magic bytes or match functions are detected by content;
the rest fall back to file extension matching.

| Format | Converter | Extensions | Detection | Tested |
|--------|-----------|------------|-----------|--------|
| Amiga IFF ILBM | `ilbmtoppm` | .iff .ilbm .lbm | match | yes |
| Amiga Info Icon | `infotopam` | .info | magic | yes |
| ATK Raster | `atktopbm` | .raster | magic | yes |
| Atari Compressed Spectrum | `spctoppm` | .spc | ext | yes |
| Atari Degas | `pi1toppm` | .pi1 | ext | yes |
| Atari Degas Elite | `pc1toppm` | .pc1 | magic | yes |
| Atari Degas Low-Res | `pi3topbm` | .pi3 | ext | yes |
| Atari Neochrome | `neotoppm` | .neo | ext | yes |
| Atari Uncompressed Spectrum | `sputoppm` | .spu | ext | yes |
| AutoCAD Slide | `sldtoppm` | .sld | magic | yes |
| AVS X Image | `avstopam` | .avs | ext | yes |
| CMU Window Manager Bitmap | `cmuwmtopbm` | | magic | yes |
| CompuServe RLE | `cistopbm` | .cis | ext | yes |
| Fiasco Wavelet | `fiascotopnm` | .wfa .fco | magic | yes |
| FITS | `fitstopnm` | .fits .fit .fts | magic | yes |
| Garmin SRF | `srftopam` | .srf | magic | yes |
| GEM Raster | `gemtopnm` | .gem | ext | yes |
| Gould Scanner | `gouldtoppm` | .gould | ext | no |
| Group 3 Fax | `g3topbm` | .g3 | ext | yes |
| HIPS | `hipstopgm` | .hips | ext | no |
| HP PaintJet | `pjtoppm` | .pj | ext | yes |
| Interleaf | `leaftoppm` | .leaf | magic | yes |
| JBIG | `jbigtopnm` | .jbig .jbg .bie | ext | yes |
| Lisp Machine Bitmap | `lispmtopgm` | | magic | yes |
| MacPaint | `macptopbm` | .macp | ext | yes |
| MGR Bitmap | `mgrtopbm` | .mgr | match | yes |
| Microdesign | `mdatopbm` | .mda | match | yes |
| MRF | `mrftopbm` | .mrf | magic | yes |
| MTV Ray Tracer | `mtvtoppm` | .mtv | ext | yes |
| Palm DB Image | `pdbimgtopam` | .pdb | ext | yes |
| QRT Ray Tracer | `qrttoppm` | .qrt .dis | ext | yes |
| SBIG CCD Camera | `sbigtopgm` | .sbig | ext | yes |
| SBIG ST-4 CCD Camera | `st4topgm` | .st4 | ext | yes |
| Solitaire | `sirtopnm` | .sir | magic | yes |
| Sony Mavica 411 | `411toppm` | .411 | ext | yes |
| SPOT Satellite | `spottopgm` | .spot | ext | no |
| Sun Icon | `sunicontopnm` | .icon | ext | yes |
| SVG | `svgtopam` | .svg | ext | yes |
| Usenix FaceSaver | `fstopgm` | .fs | ext | yes |
| Utah RLE | `rletopnm` | .rle | magic | yes |
| Wireless Bitmap | `wbmptopbm` | .wbmp | ext | yes |
| X IMage | `ximtoppm` | .xim | ext | yes |
| X Window Dump | `xwdtopnm` | .xwd | match | yes |
| XV Thumbnail | `xvminitoppm` | | magic | yes |
| Xerox Doodle Brush | `brushtopbm` | .brush | ext | no |
| YBM Face File | `ybmtopbm` | .ybm | magic | yes |

## Known issues

- **FIASCO multi-frame sequences**: FIASCO supports video (multiple frames in
  one file). The bridge currently only handles single-frame images because
  `fiascotopnm` can't output multi-frame sequences to stdout. Video files will
  fail to open.

## Excluded formats

The following netpbm converters are not supported by this plugin:

| Converter | Format | Reason |
|-----------|--------|--------|
| `hpcdtoppm` | Kodak Photo CD | Pillow handles PCD natively |
| `cameratopam` | Camera RAW (NEF, CR2) | Segfaults on NEF files, "File seek failed" on CR2 |
| `ddbugtopbm` | Diddle/DiddleBug sketch DB | Reads stdin only, writes multiple `.pbm` files to CWD |
| `pcdovtoppm` | Kodak Photo CD Overview | Shell script pipeline, not a single-binary converter |
| `bioradtopgm` | Bio-Rad Confocal | Magic at byte offset 54, beyond Pillow's 16-byte prefix limit; no known extension |
| `escp2topbm` | Epson ESC/P2 raster | No fixed header magic, no known file extension |
| `thinkjettopbm` | HP ThinkJet | No fixed header magic, no known file extension |
| `eyuvtoppm` | Encoder YUV | Headerless format, dimensions not in file |
| `yuvtoppm` | YUV 4:1:1 | Headerless format, dimensions not in file |
| `yuy2topam` | YUY2 Video Frame | Headerless format, dimensions not in file |
| `psidtopgm` | PostScript Image Data | Requires manual width/height/bps args, not a standalone file format |
| `imgtoppm` | Img-whatnot | `.img` extension clashes with many formats; no test data, origin server defunct |
| `pktopbm` | TeX PK Font Bitmap | Writes multiple PBM files (one per glyph), not a single-image converter |
| `rlatopam` | Wavefront RLA | Broken on 64-bit: `sizeof(long)` misaligns header read, `numChan` never assigned |
| `zeisstopnm` | Zeiss Confocal (LSM) | TIFF-based format, Pillow handles it natively |
