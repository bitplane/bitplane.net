# 🖼️ Snakes in a netpbm

Continuing on a journey of computing archaeology, it's time to extend Pillow
with a plugin that can load images that are supported by
[netpbm](https://en.wikipedia.org/wiki/Netpbm).

The first step here was to write a bridge for the `anyto*` applications, but it
turned out it wasn't so reliable - the tools rely on `file` and many ancient
and obscure formats lack proper libmagic detection, there's a lack of test data
for them, and being obscure they didn't get a lot of real world usage.

I grabbed a bit of test data for formats I really care about, created synthetic
test data for as many as I could using netpbm itself, pushed an alpha release to
pypi and asked for it to be added to Pillow's docs, so everyone in Pythonland
can open the majority of files with as little friction as possible.

This was the easy part.

* [🏠 project page](/dev/python/pillow-netpbm)
  * [📖 pydoc reference](/dev/python/pillow-netpbm/pydoc)
* [🐍 pypi package](https://pypi.org/project/pillow-netpbm)
* [🐱 github source](https://github.com/bitplane/pillow-netpbm)
* [🛏️ Pillow pull request](https://github.com/python-pillow/Pillow/pull/9482)

Then it's time to submit fixes for `file` detection rule issues, link in MIME
types wherever they're wrong around the web, open bug reports and pull requests
to steer various projects towards consistency, update wikidata, submit new types
and amendments to PRONOM, collect more test data and add more tests as I find
bugs in my bridge. And of course document the research and work here as I go,
partly because I have a lack of interesting things to write about, and a short
memory, but also to link sources for future archivists, and for the trophy
cabinet too 🏆.

---

## Andrew Toolkit Raster

![atk](andrew.png)

A nice simple file format to load, a properly registered MIME type - at least
for the data format itself (`application/andrew-inset`) - with test data
available in the [project's source](https://www.cs.cmu.edu/~AUIS/) since the
90's.

`netpbm` can load and save these, but `file` thinks all Andrew files are
LaTeX documents, and the example raster files are buried in the distro's source
tree.

Let's fix both of those things:

* [🖼️ test data repo](https://github.com/bitplane/atk-raster-test-data)
* [🐛 libmagic bug report](https://bugs.astron.com/view.php?id=740)

---

## AutoCAD Slide

![sld](sld.png)

AutoCAD slides are vector screen dumps of AutoCAD created by MSLIDE and viewed
with VSLIDE. While the specs have been removed from
[AutoDesk's website](https://web.archive.org/web/20191223211310/http://www.autodesk.com/techpubs/autocad/acadr14/dxf/slide_file_format_al_u05_b.htm),
[Martin Reddy](http://www.martinreddy.net/gfx/2d/SLD.txt) has a backup.

Most of my test files were taken from Robert Schultz's awesome
[test data collection](https://sembiance.com/fileFormatSamples/image/autoCADSlide/),
and were detected as `data` by `file` - which usually means no detection rule.
Its [PRONOM entry](https://www.nationalarchives.gov.uk/PRONOM/x-fmt/105) lists
3 different MIME types (`application/sld`, `application/x-sld` and
`image/x-sld`), and AutoDesk never actually registered an
`image/vnd.sld` with IANA. Unsurprising since other people registered their
other formats on their behalf. PRONOM's first entry has a weak collision with
`application/vnd.ogc.sld+xml`, and this ambiguity has bled through into
[Archive Team's wiki](http://justsolve.archiveteam.org/wiki/Ext:sld), and across
github
like in [MegaMimes](https://github.com/kobbyowen/MegaMimes) and
[Vitam](https://github.com/ProgrammeVitam/vitam-ui), presumably via
[DNSCore](https://github.com/da-nrw/DNSCore)'s seed data repo.

Fixing as much of this as possible, I contacted PRONOM, fixed the wiki, sent a
PR to MegaMimes, submitted a libmagic rules file, updated WikiData sources with
links to existing usage, started the IANA registration process for
`image/vnd.sld` to replace the `image/x-sld` I was lobbying for.

Once the IANA registration is complete and/or detection rules are in libmagic, 
[Apache Tika](https://issues.apache.org/jira/projects/TIKA) and
[freedesktop shared-mime-info](https://gitlab.freedesktop.org/xdg/shared-mime-info/-/issues)
will likely follow suit. If not, I'll give them a nudge.

* [🪄 libmagic rules](https://bugs.astron.com/view.php?id=742)
* [🌍 IANA submission](https://tools.iana.org/public-view/viewticket/1448324) 
* [🐛 MegaMimes PR](https://github.com/kobbyowen/MegaMimes/pull/4)
* [🌍 WikiData src links](https://www.wikidata.org/wiki/Q28049637)
* 🐛 PRONOM correction ref: TNA1774192312Q50

---

## Fractal Image And Sequence Codec (FIASCO)

![fiasco](fiasco.webp)

This novel fractal video format was created by Ullrich Hafner as part of his
[PhD thesis](https://www.semanticscholar.org/paper/FIASCO%E2%80%94An-Open-Source-Fractal-Image-and-Sequence-Hafner/68d43f493618ab61503f20696bc442cd00799dee)
back in '94-'99. It uses Weighted Finite Automata to compress the data, and the
results are superb - it crushes other formats of the time at low bitrates, the
above image would be unrecognisable as a 3.7K JPEG.

There's actually two file types that share a similar magic: one is the
compressed binary data containing an image or some video, the other is an ASCII
basis dictionary used during compression. Writing an image loader means I only
care about the first type, but detection rules deserve to support both. netpbm
uses the `.wfa` extension for compressed files, while the standalone
[FIASCO tools](https://github.com/l-tamas/Fiasco) use `.fco` for both types.
So we'll support both in `pillow-netpbm`.

The files detect as `data` as they lack a detection rule. There's also no PRONOM
identifier and no MIME type, but since it is known by both
[ArchiveTeam](http://fileformats.archiveteam.org/wiki/FIASCO) and
[Wikidata](https://www.wikidata.org/wiki/Q27979385), and was even mentioned in
[Linux Journal](https://www.linuxjournal.com/article/4367), it deserves
both detection rules and a PRONOM identifier. TBH the format really deserved
wide support back in the 2000s, I suspect it would have out-performed DivX
during the era of early swashbuckling video.

So, let's fix the omission:

* [🪄 libmagic rules](https://bugs.astron.com/view.php?id=743)
* 🗄️ PRONOM ref:TNA1774396137A87

---

## MRF (Monochrome Recursive Format)

![mrf](mrf.png)

Created by Russell Marks in 1997 for [zgv](https://en.wikipedia.org/wiki/Zgv),
this simple monochrome bitmap compression format uses quadtree decomposition -
images are divided into 64x64 tiles, each recursively subdivided until we end up
with a single colour. Brian Raiter liked it enough to create a colour extension
called
[PRF (Polychrome Recursive Format)](https://www.muppetlabs.com/~breadbox/software/prf.html),
which, unlike netpbm, is supported by both XnView and Konvertor.

MRF has no MIME type registered and nobody is using `image/x-mrf` anywhere in
the wild. It's unsupported by libmagic and unknown by PRONOM. But it does have
both a [Wikidata entry](https://www.wikidata.org/wiki/Q28206609) and an
[ArchiveTeam page](http://fileformats.archiveteam.org/wiki/MRF_(Monochrome_Recursive_Format),
and of course Sembiance has
[some test data](https://sembiance.com/fileFormatSamples/image/monochromeRecursiveFormat/)
for us to play with.

So we'll pinch his test data again and write a magic rule, and link this one in
to PRONOM like the others:

* [🪄 libmagic rules]
* 🗄️ PRONOM ref: 

---

# WIP: research + notes from here on

---

## YBM Face File

Only 2 bytes (`!!`), may need extra validation to avoid false positives. YBM
files are 2 bytes of magic, 2 bytes width (LE), 2 bytes height (LE), then
bitmap data.

TODO: research the format and loader

```magic
0       string  !!      YBM face image data
!:ext   ybm
```



## Misidentified formats

---

### Atari Neochrome → wrongly matched as DEGAS

File reports `Atari DEGAS Elite bitmap 320x200x16` for `.neo` files. Similar
Atari header layout but distinct format. Neochrome has a different structure
but no unique magic that distinguishes it within the first 16 bytes.

---

### JBIG → wrongly matched as Targa

Standalone JBIG/BIE files are misidentified as `Targa image data`. Targa
detection in libmagic is notoriously loose. JBIG rules only exist within TIFF
compression detection, not for standalone `.jbig`/`.bie` files.

---

### CompuServe RLE → "ASCII text with escape sequences"

ESC-based encoding, hard to detect without pattern matching on escape
sequences.

---

### FaceSaver → "ASCII text"

Text-based header format. Could match on `FirstName:` or `PicData:` strings.

---

### Sun Icon → "ASCII text"

Text-based C-style format. Could match on `/* Format_version=` string.

---

### SBIG ST-4 → "ISO-8859 text"

Raw scientific image data misread as text.

---

## Broken/incomplete rules

---

### Interleaf

Existing Magdir rule uses `\x88OPS` but netpbm's `leaftoppm` (and our test
file) expects `\x89OPS`. May be a format variant that needs adding to the
existing rule.

---

### GEM Raster

Rules exist in Magdir but compete with DEGAS detection. Our valid GEM file
comes back as "data" — the condition tree seems to exclude it.

---

### MacPaint

Rules exist but require `PNTGMPNT` at offset 65 (resource fork magic).
Headerless/data-fork-only MacPaint files are not detected.

---

### Group 3 Fax

Rules exist in Magdir's `modem` file but raw G3 detection is
fragile/conditional. Our test file comes back as "data".

