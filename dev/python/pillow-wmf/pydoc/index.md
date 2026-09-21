<a id="pillow_wmf"></a>

# pillow\_wmf

WMF codec, GDI recording and Pillow loading with an RGB raster backend.

<a id="pillow_wmf.environment_codepages"></a>

# pillow\_wmf.environment\_codepages

Native Windows OEM/Mac mapping additions to Python codecs.

Byte tables preserve vendor/private-use values without normalization.
The three full upper-half tables cover pages without a matching Python codec.
Regressions fingerprint every byte against the native NLS probe.

<a id="pillow_wmf.environment_codepages.decode_environment"></a>

#### decode\_environment

```python
def decode_environment(data, codepage)
```

Decode a verified, single-byte legacy environment page.

<a id="pillow_wmf.wingdings"></a>

# pillow\_wmf.wingdings

Wingdings bytes mapped to Unicode character identities, not matching outlines.

Source: Unicode/WG2 N4363, mapping appendix:
https://www.unicode.org/wg2/docs/n4363.pdf
Rows start at byte 0x20. Zero marks an undefined/unencoded character; notably
0xFF is the Windows logo, not a Unicode symbol. Space is preserved separately
from the reference's printable-symbol repertoire.

<a id="pillow_wmf.wingdings.decode_wingdings"></a>

#### decode\_wingdings

```python
def decode_wingdings(data)
```

Preserve one character per byte, including supplementary-plane symbols.

<a id="pillow_wmf.stroke"></a>

# pillow\_wmf.stroke

Solid GDI strokes: realized polygonal pens and cosmetic grid lines.

The pen is realized once from the mapping. Every wide segment then uses the
same support-vertex sweep, independent of its slope or the mapping scale.

<a id="pillow_wmf.stroke.realize_pen"></a>

#### realize\_pen

```python
def realize_pen(width: int,
                scale_x=1,
                scale_y=1,
                *,
                geometric=False) -> PenGeometry
```

Realize CreatePen width in device space, including the hairline rule.

<a id="pillow_wmf.stroke.frame_footprint"></a>

#### frame\_footprint

```python
def frame_footprint(width, height, scale_x, scale_y)
```

Rectangular frame support realized through GDI's geometric pen.

<a id="pillow_wmf.stroke.widen_segment"></a>

#### widen\_segment

```python
def widen_segment(segment: StrokeSegment,
                  pen: PenGeometry,
                  *,
                  cap_start=True,
                  cap_end=True,
                  miter=False) -> Polygon
```

Construct a stroke body and requested endpoint caps in 28.4 units.

<a id="pillow_wmf.stroke.join_outline"></a>

#### join\_outline

```python
def join_outline(first: StrokeSegment,
                 second: StrokeSegment,
                 pen: PenGeometry,
                 *,
                 miter=False) -> Polygon
```

Cover the exterior turn between two incident stroke bodies.

<a id="pillow_wmf.stroke.line_outline"></a>

#### line\_outline

```python
def line_outline(start: Point, end: Point, width: int, scale_x,
                 scale_y) -> Polygon
```

Device-integer convenience entry point for diagnostic path probes.

<a id="pillow_wmf.stroke.cosmetic_span"></a>

#### cosmetic\_span

```python
def cosmetic_span(start: Point, end: Point) -> range
```

Unclipped, directed major-axis pixel span, in constant time.

Only endpoint diamonds can shorten the span; interior grid intersections
each own a pixel. This counts style steps even when the whole line is off
screen, without enumerating arbitrarily distant coordinates.

<a id="pillow_wmf.stroke.cosmetic_line"></a>

#### cosmetic\_line

```python
def cosmetic_line(start: Point, end: Point, width: int, height: int)
```

GIQ coverage for a 28.4 segment, including fractional curve vertices.

Choose the closest minor-coordinate pixel at each major grid intersection
(ties to the smaller coordinate). A pixel is emitted when the segment exits
its half-pixel diamond. Endpoint ownership uses the legacy GIQ boundary
rules (including slope +/-1 edges), not a blanket start/end convention.
Bounds restrict grid enumeration without changing the original line.

<a id="pillow_wmf.text"></a>

# pillow\_wmf.text

Explicit font inputs, glyph masks and compatible-mode GDI text layout.

Font files, aliases and missing-glyph policy are supplied by the caller, not by
a WMF. There is no host-font discovery or registry-based font substitution.

<a id="pillow_wmf.text.text_rotation"></a>

#### text\_rotation

```python
def text_rotation(escapement)
```

Share the font scaler's 16.16 rotation with baseline placement.

<a id="pillow_wmf.text.decode_single_byte"></a>

#### decode\_single\_byte

```python
def decode_single_byte(data, codepage)
```

Decode using Windows NLS mappings, including undefined/vendor bytes.

<a id="pillow_wmf.text.decode_codepage"></a>

#### decode\_codepage

```python
def decode_codepage(data, codepage)
```

Decode characters and their source spans through one code-page policy.

<a id="pillow_wmf.text.RasterFont"></a>

## RasterFont Objects

```python
@dataclass
class RasterFont()
```

Glyph generation is independent of GDI alignment and DC state.

<a id="pillow_wmf.text.RasterFont.glyph_index"></a>

#### glyph\_index

```python
def glyph_index(index, max_pixels)
```

Realize a physical glyph without character mapping or font linking.

<a id="pillow_wmf.text.FontFace"></a>

## FontFace Objects

```python
class FontFace()
```

A pinned TrueType face with its Windows metrics, not Pillow's metrics.

<a id="pillow_wmf.text.FontFace.bundled_wingdings"></a>

#### bundled\_wingdings

```python
@classmethod
def bundled_wingdings(cls)
```

Load the prebuilt Unicode Wingdings fallback; selection stays explicit.

<a id="pillow_wmf.text.FontFace.bundled_symbol"></a>

#### bundled\_symbol

```python
@classmethod
def bundled_symbol(cls)
```

Wine's unmodified Symbol face, retaining its legacy symbol cmap.

<a id="pillow_wmf.text.FontFace.realize"></a>

#### realize

```python
def realize(request, scale, *, missing_glyph="error")
```

Classic compatible-mode realization; natural width follows height.

<a id="pillow_wmf.text.FontCollection"></a>

## FontCollection Objects

```python
class FontCollection()
```

Supplied faces and explicit aliases; never discover or silently replace.

<a id="pillow_wmf.text.FontCollection.layout_font"></a>

#### layout\_font

```python
def layout_font(request, face, scale, *, characters=None)
```

Prepare a run; controlled fonts never depend on host discovery.

<a id="pillow_wmf.text.FontRun"></a>

## FontRun Objects

```python
@dataclass(frozen=True)
class FontRun()
```

Use base line metrics, selecting supplied fallback faces only for holes.

<a id="pillow_wmf.text.FontRun.shape"></a>

#### shape

```python
def shape(characters, max_pixels, *, raw=False)
```

Shape SBCS control runs before choosing masks and advances.

A control run containing an unshapable character falls back to raw
character output. Its formerly invisible controls then participate in
font linking too. Separators terminate runs; they are not tab stops or
multiline layout commands. Paired advances request raw glyph output,
bypassing the control-run shaper without disabling font linking.

<a id="pillow_wmf.text.layout_text"></a>

#### layout\_text

```python
def layout_text(font,
                text,
                x,
                y,
                alignment,
                advances,
                *,
                opaque,
                max_pixels,
                scale=1,
                extra=0,
                justification=(0, 0),
                characters=None,
                escapement=0,
                glyph_indices=None,
                vertical_advances=(),
                vertical_scale=1,
                mirrored_layout=False,
                precise_origin=None,
                byte_lengths=(),
                byte_indexed_advances=True)
```

Place independently realized glyphs; explicit advances replace metrics.

<a id="pillow_wmf.text.paired_background"></a>

#### paired\_background

```python
def paired_background(glyphs, offsets, vertical_offsets, origin_x, baseline,
                      cell, x, y, escapement)
```

Bound positioned glyph cells in font space, then realize their corners.

<a id="pillow_wmf.plugin"></a>

# pillow\_wmf.plugin

Pillow's WMF entry point; EMF remains with Pillow's existing handler.

<a id="pillow_wmf.plugin.WmfImageFile"></a>

## WmfImageFile Objects

```python
class WmfImageFile(ImageFile.ImageFile)
```

<a id="pillow_wmf.plugin.WmfImageFile.load"></a>

#### load

```python
def load(*, size=None, dpi=None, fonts=None)
```

Rasterize once; choose size or placeable DPI before the first load.

Plain WMFs have no physical size. Invalid placeable bounds fall back
to the same 128-square canvas. Records can override the initial mapping.
Unsupported drawing raises OSError rather than returning partial art.
Invalid caller options raise ValueError.

<a id="pillow_wmf.flood"></a>

# pillow\_wmf.flood

Four-connected scanline discovery, independent of brush realization.

<a id="pillow_wmf.flood.flood_spans"></a>

#### flood\_spans

```python
def flood_spans(width, height, seed, eligible)
```

Return disjoint (y, left, right) spans; right is exclusive.

Mark whole runs when discovered, then search their vertical neighbours.
No recursion and no dependence on whether painting changes a pixel.
``eligible`` must describe the unchanged source surface and clip.

<a id="pillow_wmf.constants"></a>

# pillow\_wmf.constants

GDI values used by the emulator, independent of WMF record opcodes.

<a id="pillow_wmf.halftone"></a>

# pillow\_wmf.halftone

Native RGB HALFTONE: 13-bit area weights, sharpening and tent expansion.

Includes the native colour census and fast replication-run enlargement filter.

<a id="pillow_wmf.halftone.replication_candidate"></a>

#### replication\_candidate

```python
def replication_candidate(sw, sh, width, height)
```

ComputeAABBP's integer eligibility test, before image classification.

The +500 is literal: it is not half of the source dimension. A decrease
in total pixel area overrides the small-image replication decision.

<a id="pillow_wmf.halftone.fixup_candidate"></a>

#### fixup\_candidate

```python
def fixup_candidate(sw, sh, width, height)
```

Eligibility for the colour census and its buffered source reader.

<a id="pillow_wmf.halftone.classify_content"></a>

#### classify\_content

```python
def classify_content(bitmap, x, y, width, height, *, depth=24)
```

CheckBMPNeedFixup's bounded colour census of the source rectangle.

Small images bypass the census. Medium images discount rows introducing
no new colours; large images sample every sixth row with a 20-colour cap.
The native key coarsens channels when red equals blue (not just greys).

<a id="pillow_wmf.halftone.halftone_bitmap"></a>

#### halftone\_bitmap

```python
def halftone_bitmap(bitmap, x, y, sw, sh, width, height, *, content=None)
```

Return a filtered view, no-op, or explicit request for scan replication.

A view with valid=False means no output, never replication.

<a id="pillow_wmf.halftone.ExpansionAxis"></a>

## ExpansionAxis Objects

```python
class ExpansionAxis()
```

Integrate a power-adjusted discrete tent over source pixel cells.

<a id="pillow_wmf.halftone.RunExpansionAxis"></a>

## RunExpansionAxis Objects

```python
class RunExpansionAxis()
```

Native FastExpAA's five replication-run stencils, in units of 1/32.

<a id="pillow_wmf.halftone.HalftoneExpansion"></a>

## HalftoneExpansion Objects

```python
class HalftoneExpansion()
```

Source Laplacian, then horizontal and vertical fixed-point expansion.

<a id="pillow_wmf.halftone.area_weights"></a>

#### area\_weights

```python
def area_weights(source_length, destination_length, index)
```

Integrate source cells using quantized *cumulative* boundaries.

Taking differences after quantization carries the division remainder across
contributions. Rounding independently computed overlap weights does not.
Coordinates use the common integer grid: source cells are D units wide,
destination cells S units wide. Each output's weights sum to exactly 8192.

<a id="pillow_wmf.halftone.HalftoneReduction"></a>

## HalftoneReduction Objects

```python
class HalftoneReduction()
```

Lazy bitmap view; destination clipping does not change filtering phase.

Bounded per-transfer caches avoid allocating the destination or a potentially
large source-height intermediate image. Output pixels remain ordinary RGB
samples consumed by the shared transfer compositor.

<a id="pillow_wmf._values"></a>

# pillow\_wmf.\_values

Snapshot sequence inputs so recorded commands cannot change underneath us.

<a id="pillow_wmf.system_fonts"></a>

# pillow\_wmf.system\_fonts

Opt-in host font discovery, separate from controlled-font rendering.

<a id="pillow_wmf.system_fonts.font_paths"></a>

#### font\_paths

```python
def font_paths()
```

Use Fontconfig's configured inventory, or conventional system directories.

<a id="pillow_wmf.system_fonts.SystemFontCollection"></a>

## SystemFontCollection Objects

```python
class SystemFontCollection(FontCollection)
```

Best-effort installed fonts; construct one collection per rendering job.

Discovery is lazy. Pass paths to use a bounded application font inventory
instead of the host. Unsupported outline formats are ignored. Missing glyphs
use .notdef after installed Unicode fallbacks have been exhausted.
Immutable catalogues are shared across jobs, including host discovery.
Call clear_cache() after installing, removing or replacing fonts, then
construct a new collection. Existing jobs retain their inventory snapshot.

<a id="pillow_wmf.system_fonts.SystemFontCollection.clear_cache"></a>

#### clear\_cache

```python
@staticmethod
def clear_cache()
```

Refresh discovery/catalogues for future jobs; live jobs stay unchanged.

Loaded FreeType faces and substitution reports are never shared.
Changes to files at existing paths also require this explicit refresh.

<a id="pillow_wmf.paint"></a>

# pillow\_wmf.paint

Boolean raster operations for RGB pattern, source and destination pixels.

<a id="pillow_wmf.paint.rop3"></a>

#### rop3

```python
def rop3(rop: int, pattern: RGB, source: RGB, destination: RGB) -> RGB
```

Evaluate the eight-entry P,S,D table in bits 16..23 of a GDI ROP.

Split on P: each half is an S,D binary table. This covers all 256
functions without a catalogue of named raster-operation exceptions.

<a id="pillow_wmf.paint.pattern_rop2"></a>

#### pattern\_rop2

```python
def pattern_rop2(rop: int) -> int | None
```

Reduce a source-independent ROP3 to ROP2; otherwise return None.

<a id="pillow_wmf.paint.rop2"></a>

#### rop2

```python
def rop2(mode: int, source: RGB, destination: RGB) -> RGB
```

Apply the four-entry P,D truth table encoded by a WMF ROP2 value.

The entries are ordered (P,D) = 00, 01, 10, 11. Windows numbers the
sixteen possible tables from 1 through 16, so the table bits are mode-1.

<a id="pillow_wmf.dbcs"></a>

# pillow\_wmf.dbcs

Decoded text retains byte spans for ANSI GDI's byte-indexed advances.

<a id="pillow_wmf.dbcs.collapse_advances"></a>

#### collapse\_advances

```python
def collapse_advances(advances, byte_lengths, *, byte_indexed=True)
```

Map ANSI advances to characters, including signed x or y offsets.

GDI collapses byte entries only for CP932/936/949/950. Johab and Mac pages
keep the first character-count entries; trailing byte entries are unused.
The WMF array must still supply an entry for every source byte.

<a id="pillow_wmf.dbcs.decode_cp932"></a>

#### decode\_cp932

```python
def decode_cp932(data)
```

Decode Windows Japanese text with source-byte spans.

<a id="pillow_wmf.dbcs.decode_dbcs"></a>

#### decode\_dbcs

```python
def decode_dbcs(data, codepage)
```

Decode Windows DBCS text, preserving NLS replacement boundaries.

A malformed pair consumes both bytes and becomes the page's replacement
character: KATAKANA MIDDLE DOT for Japanese pages, question mark for others.
NUL is the exception: it is retained as a separate character. A dangling
lead byte also becomes the replacement. Python codecs provide the base
mappings; explicit Windows extensions preserve vendor and Jamo mappings.

<a id="pillow_wmf.numeric"></a>

# pillow\_wmf.numeric

Storage precision shared by GDI arithmetic, not a universal rounding rule.

<a id="pillow_wmf.numeric.float32"></a>

#### float32

```python
def float32(value: float) -> float
```

Round one arithmetic result to IEEE-754 binary32.

<a id="pillow_wmf.geometry"></a>

# pillow\_wmf.geometry

Device paths in 28.4 fixed point, retained through scan conversion.

<a id="pillow_wmf.geometry.DevicePath"></a>

## DevicePath Objects

```python
@dataclass(frozen=True)
class DevicePath()
```

Connected line/cubic commands, retained until the stroke is realized.

<a id="pillow_wmf.geometry.DevicePath.rectangle"></a>

#### rectangle

```python
@classmethod
def rectangle(cls, left: int, top: int, right: int, bottom: int)
```

A closed rectangle in fixed device coordinates, starting top-right.

<a id="pillow_wmf.geometry._CurveAxis"></a>

## \_CurveAxis Objects

```python
@dataclass
class _CurveAxis()
```

One axis of an adaptive forward-difference cubic.

Curvature terms describe the end and start of the current interval.
Keeping them alongside position and advance lets us walk the curve or
change interval size without repeatedly evaluating its polynomial.

<a id="pillow_wmf.geometry._CurveAxis.controls"></a>

#### controls

```python
def controls() -> tuple[int, int, int, int]
```

Recover rounded controls for one coarse interval of a large curve.

<a id="pillow_wmf.geometry.flatten_cubic"></a>

#### flatten\_cubic

```python
def flatten_cubic(control: Cubic) -> Polygon
```

Flatten using GDI's integer adaptive curve walk; see gdi-curves.md.

Arithmetic shifts during step changes are observable. Exact recursive
subdivision can choose identical sample parameters but different vertices.

<a id="pillow_wmf.geometry.contains"></a>

#### contains

```python
def contains(polygons: tuple[Polygon, ...],
             x: int,
             y: int,
             *,
             fill_mode: int = 1) -> bool
```

Evaluate alternate or winding coverage at a device-pixel coordinate.

<a id="pillow_wmf.wmf.records"></a>

# pillow\_wmf.wmf.records

Record envelopes and the explicit typed-record registry.

Unknown records stay opaque. Known records retain their original function word
and any uninterpreted trailing bytes independently of their decoded fields.

<a id="pillow_wmf.wmf.objects"></a>

# pillow\_wmf.wmf.objects

Wire-level graphics structures. Bitmap pixels are deliberately undecoded.

<a id="pillow_wmf.wmf.objects.BitmapData"></a>

## BitmapData Objects

```python
@dataclass(frozen=True)
class BitmapData()
```

An encoded Bitmap16 or DIB, not decoded or certified as renderable.

Keeping this explicit prevents opaque preservation from being mistaken for
bitmap codec support. The separate bitmap module decodes a bounded subset;
constructing this envelope alone does not validate its header or pixels.

<a id="pillow_wmf.wmf.constants"></a>

# pillow\_wmf.wmf.constants

WMF record function values, MS-WMF 2.1.1.1.

<a id="pillow_wmf.wmf.player"></a>

# pillow\_wmf.wmf.player

Translate WMF records to backend calls without rasterizing or decoding text.

<a id="pillow_wmf.wmf.player.PlaybackError"></a>

## PlaybackError Objects

```python
class PlaybackError(ValueError)
```

A stream's handle references or backend results are invalid.

<a id="pillow_wmf.wmf.player.play"></a>

#### play

```python
def play(metafile: Metafile,
         backend: GDI,
         *,
         strict: bool = False,
         limits: Limits | None = None) -> tuple[Omission, ...]
```

Play into a supplied context; return diagnostics for unsupported work.

The caller owns the backend and its initial state. No implicit drawing-state
reset, object deletion, or source-byte rewrite is inserted into the trace.
Unsupported creations occupy their WMF slots to prevent handle aliasing.

<a id="pillow_wmf.wmf.variable"></a>

# pillow\_wmf.wmf.variable

Variable-length vector, text, object and escape records.

<a id="pillow_wmf.wmf.bindings"></a>

# pillow\_wmf.wmf.bindings

Explicit WMF/GDI bindings. File handle indexes never cross into a backend.

<a id="pillow_wmf.wmf.file"></a>

# pillow\_wmf.wmf.file

WMF file framing and preserving/canonical serialization.

<a id="pillow_wmf.wmf.file.Metafile"></a>

## Metafile Objects

```python
@dataclass(frozen=True)
class Metafile()
```

<a id="pillow_wmf.wmf.file.Metafile.build"></a>

#### build

```python
@classmethod
def build(cls,
          records,
          *,
          placeable: PlaceableHeader | None = None,
          version: int = 0x0300)
```

Build a new stream, inserting EOF and calculating header accounting.

Direct records may intentionally contain semantically invalid handle
references for test fixtures. Use Recorder for checked handle lifetimes.

<a id="pillow_wmf.wmf.file.Metafile.to_bytes"></a>

#### to\_bytes

```python
def to_bytes(*, canonical: bool = False) -> bytes
```

Preserve metadata by default; canonical=True recomputes file sizes.

Trailing file bytes are retained but excluded from canonical stream size.
Reserved/padding bytes in records remain explicit data in either mode.

<a id="pillow_wmf.wmf.recorder"></a>

# pillow\_wmf.wmf.recorder

Record GDI commands into WMF with deterministic file-handle allocation.

<a id="pillow_wmf.wmf.recorder.Recorder"></a>

## Recorder Objects

```python
class Recorder(TraceContext)
```

A checked command recorder, not a rendering device-context emulator.

Use direct Record construction for reserved fields, unknown opcodes and
intentionally invalid test cases. Public calls use logical backend handles.

<a id="pillow_wmf.wmf.binary"></a>

# pillow\_wmf.wmf.binary

Bounded little-endian reads shared by WMF records and nested objects.

<a id="pillow_wmf.wmf.binary.FormatError"></a>

## FormatError Objects

```python
class FormatError(ValueError)
```

The input cannot be interpreted safely as a WMF structure.

<a id="pillow_wmf.wmf.binary.ResourceLimitError"></a>

## ResourceLimitError Objects

```python
class ResourceLimitError(FormatError)
```

A configured safety limit was exceeded; never a recoverable omission.

<a id="pillow_wmf.wmf.binary.Limits"></a>

## Limits Objects

```python
@dataclass(frozen=True)
class Limits()
```

Allocation/work limits; these are policy, not WMF format limits.

<a id="pillow_wmf.wmf.fixed"></a>

# pillow\_wmf.wmf.fixed

Fixed-field records. Field order follows MS-WMF, not the GDI argument order.

<a id="pillow_wmf.wmf"></a>

# pillow\_wmf.wmf

WMF reader/writer. Import record classes from fixed, variable and bitmaps.

<a id="pillow_wmf.wmf.bitmaps"></a>

# pillow\_wmf.wmf.bitmaps

Bitmap transfer envelopes; BitmapData explicitly preserves opaque pixels.

<a id="pillow_wmf.render"></a>

# pillow\_wmf.render

Complete WMF rendering; use ``play`` when collecting omissions is required.

<a id="pillow_wmf.render.render"></a>

#### render

```python
def render(data: bytes,
           size: tuple[int, int],
           *,
           fonts: FontCollection | None = None,
           background=(255, 255, 255),
           limits: Limits | None = None,
           max_bitmap_pixels: int = DEFAULT_MAX_BITMAP_PIXELS) -> Image.Image
```

Render to an RGB image, raising if any record cannot be rendered.

Size is the output canvas in pixels. Playback uses the WMF's mapping calls;
neither placeable bounds nor drawing bounds implicitly fit the image.
Fonts are supplied explicitly. For partial rendering with diagnostics, use
``play(metafile, context, strict=False)`` and inspect its omissions instead.

<a id="pillow_wmf.clip"></a>

# pillow\_wmf.clip

Immutable region algebra and application clipping.

The bitmap bounds are applied when pixels are written. They must not trim an
application clip: a later OffsetClipRgn can move an off-surface clip into view.

<a id="pillow_wmf.clip.RegionMask"></a>

## RegionMask Objects

```python
@dataclass(frozen=True)
class RegionMask()
```

Finite union of half-open rectangles, indexed as disjoint y bands.

<a id="pillow_wmf.clip.RegionMask.spans"></a>

#### spans

```python
def spans(y)
```

Disjoint half-open intervals on a scan line.

<a id="pillow_wmf.clip.RegionMask.difference"></a>

#### difference

```python
def difference(other)
```

Subtract bands without introducing pixel-sized storage.

<a id="pillow_wmf.clip.RegionMask.frame"></a>

#### frame

```python
def frame(width, height, *, point=None)
```

Inner rectangular border: subtract the rectangular erosion.

Dilating the complement includes holes and concave corners, without
exposing the artificial boundaries between a region's scan bands.
Half-integral device thickness represents an odd full footprint;
the extra pixel belongs to the left/top side of the inner border.

<a id="pillow_wmf.clip.ClipRegion"></a>

## ClipRegion Objects

```python
@dataclass(frozen=True)
class ClipRegion()
```

<a id="pillow_wmf.clip.ClipRegion.within"></a>

#### within

```python
def within(bounds: Rectangle) -> RegionMask
```

Resolve the application clip inside finite device bounds.

<a id="pillow_wmf.halftone_fixup"></a>

# pillow\_wmf.halftone\_fixup

Native source scan fixup, before HALFTONE resampling.

FixupColorScan detects alternating 2x2 cells. Extended checker runs collapse to
their rounded mean; otherwise the brighter diagonal is blended with its four
surrounding samples. Decisions use original scans, writes accumulate in scan
order. Border lookahead reflects the adjacent row/pixel, not the edge itself.

<a id="pillow_wmf.trace"></a>

# pillow\_wmf.trace

A non-rendering GDI backend with checked handle and save-stack bookkeeping.

This records requested operations. It does not emulate mapping, selected-object
deletion quirks, clipping, palette realization or any pixel effects.

<a id="pillow_wmf.symbol"></a>

# pillow\_wmf.symbol

Defined byte positions in Windows Symbol's legacy encoding.

The other positions select the missing glyph, including 0xA0 (not Euro) and
0xF0 (not the Apple glyph found in some PostScript-compatible Symbol fonts).
This repertoire is verified through WMF playback and native glyph lookup.
Glyph identities and outlines come from the selected Symbol font's cmap.

<a id="pillow_wmf.gdi_math"></a>

# pillow\_wmf.gdi\_math

Table-based angular arithmetic used by the native GDI Arc constructor.

These are mathematical lookup tables, not drawing-specific correction data.
Angular arithmetic rounds each stage to binary32 before device-coordinate conversion.

<a id="pillow_wmf.gdi_math.circle_control"></a>

#### circle\_control

```python
def circle_control(radius: int, *, upward: bool) -> int
```

GDI's signed 0.32 circle-inset multiply, expressed as a handle length.

The complement of the usual cubic circle coefficient is stored as
0x729d7775, not recomputed from sqrt(2). Arithmetic shifts preserve the
oriented rounding used by ellipse, rounded-rectangle and pen constructors.

<a id="pillow_wmf.gdi_math.atan2_degrees"></a>

#### atan2\_degrees

```python
def atan2_degrees(y: float, x: float) -> float
```

Reduce to the arctangent table's [0, 1] ratio interval.

<a id="pillow_wmf.gdi_math.sincos_degrees"></a>

#### sincos\_degrees

```python
def sincos_degrees(angle: float, *, accurate=False) -> tuple[float, float]
```

Return (sine, cosine), with quadrant signs and FLOAT results.

<a id="pillow_wmf.gdi_math.arc_control_normals"></a>

#### arc\_control\_normals

```python
def arc_control_normals(first: float, last: float, start, end)
```

Intersect endpoint tangents and blend their FLOAT control normals.

<a id="pillow_wmf.bitmap16"></a>

# pillow\_wmf.bitmap16

Legacy device-dependent bitmap storage, independent of DIB headers.

<a id="pillow_wmf.bitmap16.encode_bitmap16"></a>

#### encode\_bitmap16

```python
def encode_bitmap16(width,
                    height,
                    samples,
                    *,
                    depth=1,
                    pattern=False,
                    native_pattern=False)
```

Write WORD rows without a colour table.

``pattern=True`` writes the documented 32-byte Pattern Object header.
Add ``native_pattern=True`` for Windows' 36-byte playback layout.

<a id="pillow_wmf.palette"></a>

# pillow\_wmf.palette

Logical palette objects for the RGB reference device.

DC snapshots retain an object reference, not a copy of its mutable entries.
There is no display-wide hardware palette to animate on this device.

<a id="pillow_wmf.raster"></a>

# pillow\_wmf.raster

WMF rasterization into a Pillow RGB image.

<a id="pillow_wmf.raster.PreparedEffect"></a>

## PreparedEffect Objects

```python
@dataclass(frozen=True)
class PreparedEffect()
```

Decoded inputs shared by validation and application, never DC state.

<a id="pillow_wmf.raster.TextState"></a>

## TextState Objects

```python
@dataclass(frozen=True)
class TextState()
```

Logical font, alignment and spacing retained by SaveDC/RestoreDC.

<a id="pillow_wmf.raster.TextState.font"></a>

#### font

None uses the caller's configured default, if any.

<a id="pillow_wmf.raster.SavedDC"></a>

## SavedDC Objects

```python
@dataclass(frozen=True)
class SavedDC()
```

Saved drawing state; selected objects retain their identity.

Mapping is copied at save time. The image and handle allocation table are
not part of a snapshot, and palette mutations remain visible after restore.

<a id="pillow_wmf.raster.RasterContext"></a>

## RasterContext Objects

```python
class RasterContext(TraceContext)
```

Draw the currently supported GDI calls into an RGB Pillow image.

Unsupported modes and primitives raise rather than silently draw an
approximate image. Playback with ``strict=True`` exposes that boundary.

<a id="pillow_wmf.halftone_scan"></a>

# pillow\_wmf.halftone\_scan

HALFTONE source addressing, separate from filter weights and arithmetic.

These are random-access descriptions of the native scan readers: evaluating a
destination pixel out of order must not change the reader's history. None is an
unfilled buffer slot, not a black pixel fetched from the source bitmap.

<a id="pillow_wmf.halftone_scan.has_source"></a>

#### has\_source

```python
def has_source(bitmap, x, y, width, height)
```

Physical intersection, independent of filter output's closing cells.

<a id="pillow_wmf.dib_rle"></a>

# pillow\_wmf.dib\_rle

Bounded RLE4/RLE8 command decoding in bottom-up storage coordinates.

<a id="pillow_wmf.dib_rle.decode_rle"></a>

#### decode\_rle

```python
def decode_rle(data, width, height, depth, *, clip_spans=None)
```

Decode storage rows, optionally clipped during the native scan transfer.

``clip_spans(y)`` supplies disjoint half-open intervals in storage coordinates.
Encoded RLE4 runs restart at their high nibble after left clipping; absolute
runs retain their source phase. Clipping an already decoded bitmap differs.

<a id="pillow_wmf.mac_dbcs"></a>

# pillow\_wmf.mac\_dbcs

Windows Macintosh DBCS mappings, distinct from the similarly named ANSI pages.

<a id="pillow_wmf.blit"></a>

# pillow\_wmf.blit

Integer source-transfer geometry and scan selection.

<a id="pillow_wmf.blit.StretchAxis"></a>

## StretchAxis Objects

```python
@dataclass(frozen=True)
class StretchAxis()
```

<a id="pillow_wmf.blit.StretchAxis.samples"></a>

#### samples

```python
def samples(coordinate, mode)
```

Centre-phase DDA; reduction modes accumulate through each chosen scan.

<a id="pillow_wmf.dbcs_tables"></a>

# pillow\_wmf.dbcs\_tables

Windows NLS additions to Python's DBCS codecs.

These are encoding mappings, not font substitutions. User-defined character
areas retain their private-use code points even without a matching EUDC font.
Rows are traversed in lead-byte, then trail-byte order. GBK hole-range endpoints
below are inclusive.

<a id="pillow_wmf.ellipse"></a>

# pillow\_wmf.ellipse

Construct the exclusive-bound ellipse as a fixed-point device path.

<a id="pillow_wmf.ellipse.box_corners"></a>

#### box\_corners

```python
def box_corners(bounds)
```

Native box traversal: retain the upper edge, reflect about its centre.

<a id="pillow_wmf.ellipse.box_axes"></a>

#### box\_axes

```python
def box_axes(bounds)
```

Quantize the box's half-edge vectors before angular/corner scaling.

<a id="pillow_wmf.ellipse.ellipse_cubics"></a>

#### ellipse\_cubics

```python
def ellipse_cubics(
        left: int,
        top: int,
        right: int,
        bottom: int,
        *,
        null_pen=False,
        drawing_bounds=None,
        clockwise=False) -> tuple[tuple[Point, Point, Point, Point], ...]
```

Four GDI-style cubics, with orientation applied before quantization.

<a id="pillow_wmf.ellipse.round_rect_figure"></a>

#### round\_rect\_figure

```python
def round_rect_figure(left,
                      top,
                      right,
                      bottom,
                      ellipse_width,
                      ellipse_height,
                      *,
                      null_pen=False,
                      drawing_bounds=None,
                      clockwise=False) -> DevicePath
```

Place canonical ellipse quarters at four centres and connect the edges.

<a id="pillow_wmf.ellipse.ellipse_path"></a>

#### ellipse\_path

```python
def ellipse_path(left: int, top: int, right: int, bottom: int) -> Polygon
```

Flatten the four GDI-style cubic arcs of an exclusive-bound ellipse.

<a id="pillow_wmf.ellipse.arc_cubics"></a>

#### arc\_cubics

```python
def arc_cubics(
        left: int,
        top: int,
        right: int,
        bottom: int,
        start: tuple[int, int],
        end: tuple[int, int],
        *,
        null_pen=False,
        drawing_bounds=None,
        radial_bounds=None,
        clockwise=False) -> tuple[tuple[Point, Point, Point, Point], ...]
```

Cut an exclusive-bound ellipse at two radial directions.

Normalize radials in the inclusive device box, then construct cubics in
the exclusive-bound drawing box. WMF stores points on the radials, not
points required to lie on the ellipse.

<a id="pillow_wmf.ellipse.arc_figure"></a>

#### arc\_figure

```python
def arc_figure(left: int,
               top: int,
               right: int,
               bottom: int,
               start: Point,
               end: Point,
               *,
               closure: Literal["open", "chord", "pie"] = "open",
               null_pen=False,
               drawing_bounds=None,
               radial_bounds=None,
               clockwise=False) -> DevicePath
```

Retain one arc figure, optionally closed directly or through its centre.

<a id="pillow_wmf.halftone_power"></a>

# pillow\_wmf.halftone\_power

Six-decimal GDI tent-weight powers, using reproducible logarithm samples.

The native packed tables encode rounded log10 samples at 0.001 intervals on
[1, 10]. Generate those mathematical values, not copies of proprietary tables.
Only table construction uses Decimal; interpolation and powers use integers.

<a id="pillow_wmf.halftone_power.round_ratio"></a>

#### round\_ratio

```python
def round_ratio(numerator, denominator)
```

Round a signed ratio to nearest, with ties away from zero.

<a id="pillow_wmf.halftone_power.tent_power"></a>

#### tent\_power

```python
def tent_power(value)
```

Native asymmetric power curve; the exact half-weight bypasses power.

<a id="pillow_wmf.bitmap"></a>

# pillow\_wmf.bitmap

Packed DIB codecs, separate from WMF record framing and brush sampling.

<a id="pillow_wmf.bitmap.RGBBitmap"></a>

## RGBBitmap Objects

```python
@dataclass(frozen=True)
class RGBBitmap()
```

Immutable, top-down RGB pixels; storage orientation is a codec concern.

<a id="pillow_wmf.bitmap.RGBBitmap.monochrome"></a>

#### monochrome

```python
def monochrome(background: tuple[int, int,
                                 int] = (255, 255, 255)) -> "RGBBitmap"
```

Realize RGB-to-mono colour-key conversion, not a brightness filter.

<a id="pillow_wmf.bitmap.encode_dib24"></a>

#### encode\_dib24

```python
def encode_dib24(bitmap: RGBBitmap, *, top_down: bool = False) -> BitmapData
```

Build a 40-byte BITMAPINFOHEADER and DWORD-aligned BGR scanlines.

<a id="pillow_wmf.bitmap.encode_dib"></a>

#### encode\_dib

```python
def encode_dib(width,
               height,
               samples,
               *,
               depth,
               colors=(),
               masks=None,
               header_size=40,
               top_down=False,
               rle=False,
               color_usage=0)
```

Record exact integer pixels, without quantization or palette selection.

Indexed samples are table indexes; direct-colour samples are packed words
in the requested RGB/mask layout. Samples are supplied top-to-bottom.
For DIB_PAL_COLORS, colors contains WORD logical-palette indexes instead
of RGB triples. DIB_PAL_INDICES has no table.

<a id="pillow_wmf.bitmap.DIBLayout"></a>

## DIBLayout Objects

```python
@dataclass(frozen=True)
class DIBLayout()
```

Validated packed layout, before choosing full-image or scan-band decoding.

<a id="pillow_wmf.bitmap.DIBLayout.complete"></a>

#### complete

```python
@property
def complete() -> bool
```

Whether the packed object contains the entire declared image.

<a id="pillow_wmf.bitmap.DIBLayout.decode"></a>

#### decode

```python
def decode(rows: int | None = None,
           *,
           replicate_channels=True,
           preserve_gaps=False,
           palette=None,
           clip_spans=None,
           gap_color=None) -> RGBBitmap
```

Decode rows from the beginning of the pixel buffer, not a row offset.

For direct RLE scans, ``clip_spans`` provides top-down clip intervals.
``gap_color`` selects a realized background instead of palette index 0;
``preserve_gaps`` retains coverage so unwritten pixels can be skipped.

<a id="pillow_wmf.bitmap.DIBLayout.index"></a>

#### index

```python
def index(x, y, *, rows=None)
```

Read an uncompressed indexed sample in top-down coordinates.

<a id="pillow_wmf.bitmap.read_dib"></a>

#### read\_dib

```python
def read_dib(bitmap: BitmapData,
             *,
             color_usage: int = 0,
             max_pixels: int = DEFAULT_MAX_BITMAP_PIXELS) -> DIBLayout
```

Validate the supported packed DIB layout without allocating pixels.

Core/Info/V4/V5, RGB tables, direct RGB, bitfields and RLE4/RLE8.
Logical-palette references remain unresolved until decoding.
The decoder checks the required pixel extent; bands may omit other rows.

<a id="pillow_wmf.bitmap.decode_dib"></a>

#### decode\_dib

```python
def decode_dib(bitmap: BitmapData,
               *,
               color_usage: int = 0,
               max_pixels: int = DEFAULT_MAX_BITMAP_PIXELS,
               palette=None) -> RGBBitmap
```

Decode a complete packed DIB into immutable top-down RGB pixels.

<a id="pillow_wmf.mapping"></a>

# pillow\_wmf.mapping

Logical-to-device coordinate state for the Windows reference bitmap profile.

<a id="pillow_wmf.mapping.fixed"></a>

#### fixed

```python
def fixed(value: float) -> int
```

Convert to signed 28.4; exact half-unit ties go away from zero.

<a id="pillow_wmf.mapping.Mapping"></a>

## Mapping Objects

```python
@dataclass
class Mapping()
```

<a id="pillow_wmf.mapping.Mapping.linear_scale"></a>

#### linear\_scale

```python
@property
def linear_scale()
```

Signed linear transform for pen support and logical directions.

Point mapping separately preserves native product/translation rounding.

<a id="pillow_wmf.mapping.Mapping.translation_only"></a>

#### translation\_only

```python
@property
def translation_only() -> bool
```

Whether the realized FLOAT transform leaves both axes unchanged.

<a id="pillow_wmf.mapping.Mapping.clip_point"></a>

#### clip\_point

```python
def clip_point(x: int, y: int) -> tuple[int, int]
```

Rectangular clip edges use the driver's fixed-point transform.

<a id="pillow_wmf.mapping.Mapping.edge_point"></a>

#### edge\_point

```python
def edge_point(x: int, y: int) -> tuple[int, int]
```

Map half-open device edges, rather than inclusive pixel centres.

<a id="pillow_wmf.mapping.Mapping.device_point"></a>

#### device\_point

```python
def device_point(x: int, y: int) -> tuple[int, int]
```

Driver coordinates: quantize translation and product to 28.4.

The translation is realized separately, not reassociated with the
logical coordinate as (value - window_origin) * scale. Both stages
precede pixel rounding, which matters near half-pixel boundaries.
Driver scale coefficients and products are single precision before
fixed-point conversion; retaining Python doubles can miss a tie.
``point`` retains the separate LPtoDP-style integer conversion.

<a id="pillow_wmf.mapping.Mapping.fixed_point"></a>

#### fixed\_point

```python
def fixed_point(x, y)
```

Map a point without discarding its device-space sixteenths.

<a id="pillow_wmf.mapping.Mapping.clip_displacement"></a>

#### clip\_displacement

```python
def clip_displacement(x: int, y: int) -> tuple[int, int]
```

OffsetClipRgn rounds transformed distances symmetrically at ties.

<a id="pillow_wmf.gdi"></a>

# pillow\_wmf.gdi

GDI command interface used by recorders, trace sinks and future raster devices.

The interface retains primitive identity and logical coordinates. It does not
claim to implement rasterization or the complete Windows device-context state.

<a id="pillow_wmf.gdi.UnsupportedOperation"></a>

## UnsupportedOperation Objects

```python
class UnsupportedOperation(NotImplementedError)
```

A backend does not implement this operation.

<a id="pillow_wmf.gdi.InvalidOperation"></a>

## InvalidOperation Objects

```python
class InvalidOperation(ValueError)
```

Invalid call data rejected before the backend changes drawing state.

<a id="pillow_wmf.gdi.GDI"></a>

## GDI Objects

```python
class GDI()
```

Override invoke to implement a backend. Arguments are immutable values.

<a id="pillow_wmf.gdi.GDI.is_null_object"></a>

#### is\_null\_object

```python
def is_null_object(handle: Handle) -> bool
```

Whether a creation produced a native null object rather than a resource.

Logical handles still represent failed creations for subsequent calls;
emulating backends may share a typed null handle across failures.
WMF playback uses this result to preserve native file-slot allocation.
Non-emulating backends may retain the default successful-creation model.

<a id="pillow_wmf.gdi.GDI.set_dib_to_device"></a>

#### set\_dib\_to\_device

```python
def set_dib_to_device(x: int, y: int, width: int, height: int, src_x: int,
                      src_y: int, start_scan: int, scan_count: int,
                      color_usage: int, source: BitmapData) -> None
```

Transfer a band from a complete packed DIB (the WMF buffer contract).

