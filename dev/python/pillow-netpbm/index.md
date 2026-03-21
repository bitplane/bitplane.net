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
| Atari Compressed Spectrum | `spctoppm` | .spc | ext | no |
| Atari Degas | `pi1toppm` | .pi1 | ext | yes |
| Atari Degas Elite | `pc1toppm` | .pc1 | magic | yes |
| Atari Degas Low-Res | `pi3topbm` | .pi3 | ext | yes |
| Atari Neochrome | `neotoppm` | .neo | ext | yes |
| Atari Uncompressed Spectrum | `sputoppm` | .spu | ext | yes |
| AutoCAD Slide | `sldtoppm` | .sld | magic | yes |
| AVS X Image | `avstopam` | .avs | ext | yes |
| CMU Window Manager Bitmap | `cmuwmtopbm` | | magic | yes |
| CompuServe RLE | `cistopbm` | .cis | ext | yes |
| Fiasco Wavelet | `fiascotopnm` | .wfa | magic | yes |
| FITS | `fitstopnm` | .fits .fit .fts | magic | yes |
| Garmin SRF | `srftopam` | .srf | magic | yes |
| GEM Raster | `gemtopnm` | .gem | ext | yes |
| Gould Scanner | `gouldtoppm` | .gould | ext | no |
| Group 3 Fax | `g3topbm` | .g3 | ext | yes |
| HIPS | `hipstopgm` | .hips | ext | no |
| HP PaintJet | `pjtoppm` | .pj | ext | yes |
| Img-whatnot | `imgtoppm` | .img | ext | no |
| Interleaf | `leaftoppm` | .leaf | magic | yes |
| JBIG | `jbigtopnm` | .jbig .jbg .bie | ext | yes |
| Kodak Photo CD | `hpcdtoppm` | .pcd | ext | no |
| Lisp Machine Bitmap | `lispmtopgm` | | magic | yes |
| MacPaint | `macptopbm` | .macp | ext | yes |
| MGR Bitmap | `mgrtopbm` | .mgr | match | yes |
| Microdesign | `mdatopbm` | .mda | match | yes |
| MRF | `mrftopbm` | .mrf | magic | yes |
| MTV Ray Tracer | `mtvtoppm` | .mtv | ext | no |
| Palm DB Image | `pdbimgtopam` | .pdb | ext | yes |
| PostScript Image Data | `psidtopgm` | .psid | ext | no |
| QRT Ray Tracer | `qrttoppm` | .qrt | ext | no |
| SBIG CCD Camera | `sbigtopgm` | .sbig | ext | yes |
| SBIG ST-4 CCD Camera | `st4topgm` | .st4 | ext | yes |
| Solitaire | `sirtopnm` | .sir | magic | yes |
| Sony Mavica 411 | `411toppm` | .411 | ext | no |
| SPOT Satellite | `spottopgm` | .spot | ext | no |
| Sun Icon | `sunicontopnm` | .icon | ext | yes |
| SVG | `svgtopam` | .svg | ext | yes |
| TeX PK Font Bitmap | `pktopbm` | .pk | magic | no |
| Usenix FaceSaver | `fstopgm` | .fs | ext | yes |
| Utah RLE | `rletopnm` | .rle | magic | yes |
| Wavefront RLA | `rlatopam` | .rla | ext | no |
| Wireless Bitmap | `wbmptopbm` | .wbmp | ext | yes |
| X IMage | `ximtoppm` | .xim | ext | no |
| X Window Dump | `xwdtopnm` | .xwd | match | yes |
| XV Thumbnail | `xvminitoppm` | | magic | yes |
| Xerox Doodle Brush | `brushtopbm` | .brush | ext | no |
| YBM Face File | `ybmtopbm` | .ybm | magic | yes |
| Zeiss Confocal | `zeisstopnm` | .lsm | ext | no |

## Excluded formats

The following netpbm converters are not supported by this plugin:

| Converter | Format | Reason |
|-----------|--------|--------|
| `cameratopam` | Camera RAW (NEF, CR2) | Segfaults on NEF files, "File seek failed" on CR2 |
| `ddbugtopbm` | Diddle/DiddleBug sketch DB | Reads stdin only, writes multiple `.pbm` files to CWD |
| `pcdovtoppm` | Kodak Photo CD Overview | Shell script pipeline, not a single-binary converter |
| `bioradtopgm` | Bio-Rad Confocal | Magic at byte offset 54, beyond Pillow's 16-byte prefix limit; no known extension |
| `escp2topbm` | Epson ESC/P2 raster | No fixed header magic, no known file extension |
| `thinkjettopbm` | HP ThinkJet | No fixed header magic, no known file extension |
| `eyuvtoppm` | Encoder YUV | Headerless format, dimensions not in file |
| `yuvtoppm` | YUV 4:1:1 | Headerless format, dimensions not in file |
| `yuy2topam` | YUY2 Video Frame | Headerless format, dimensions not in file |
