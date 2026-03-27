# 🖼️ Adventures in netpbm

Continuing on a journey of computing archaeology, it's time to extend Pillow
with a plugin that can load images that are supported by
[netpbm](https://en.wikipedia.org/wiki/Netpbm).

The first step was a bridge for the `anyto*` applications, but it turned out it
wasn't so reliable - the tools rely on `file` and many ancient and obscure
formats lack proper libmagic detection, there's a lack of test data for them,
and being obscure they didn't get a lot of real world usage. So I ended up
having to write my own detection rules, which was a bit of a pig.

I grabbed a bit of test data for formats I really care about (like
[SEASCAPE.IFF](/log/2005/seascape)), created synthetic test data for as many as
I could using netpbm itself, pushed an alpha release to pypi and asked for it to
be added to Pillow's docs, so everyone in Pythonland can open the majority of
files with as little friction as possible.

This was the easy part.

* [🏠 project page](/dev/python/pillow-netpbm)
  * [📖 pydoc reference](/dev/python/pillow-netpbm/pydoc)
* [🐍 pypi package](https://pypi.org/project/pillow-netpbm)
* [🐱 github source](https://github.com/bitplane/pillow-netpbm)
* [🛏️ Pillow pull request](https://github.com/python-pillow/Pillow/pull/9482)

Then it was time to submit fixes for `file` detection rule issues, link in MIME
types wherever they're wrong around the web, open bug reports and pull requests
to steer various projects towards consistency, update wikidata where I could be
bothered, submit new types and amendments to PRONOM, collect more test data and
add more tests as I find bugs in my bridge. And of course document the research
and work here as I go, partly because I have a lack of interesting things to
write about, and a short memory, but also to link sources for future archivists,
and for the trophy cabinet 🏆.

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
* 🌍 IANA [submission](https://tools.iana.org/public-view/viewticket/1448324)
  [📨](https://mailarchive.ietf.org/arch/msg/media-types/5MUlMUJHMANhwVwAKLqAI0Z0NlA/)
* [🐛 MegaMimes PR](https://github.com/kobbyowen/MegaMimes/pull/4)
* [🌍 WikiData src links](https://www.wikidata.org/wiki/Q28049637)
* 🐛 PRONOM: TNA1774192312Q50

---

## FIASCO (Fractal Image And Sequence Codec)

![fiasco](fiasco.webp)

This novel fractal video format was created back in '94-'99 by Ullrich Hafner
as part of his
[PhD thesis](https://www.semanticscholar.org/paper/FIASCO%E2%80%94An-Open-Source-Fractal-Image-and-Sequence-Hafner/68d43f493618ab61503f20696bc442cd00799dee).
It uses Weighted Finite Automata to compress the data, and the results are
superb - it crushes other formats of the time at low bitrates, the above heavily
compressed image would be unrecognisable as a 3.7K JPEG.

There's actually two file types here that share a similar magic: one is the
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
[Linux Journal](https://www.linuxjournal.com/article/4367), that warrants both
detection rules and a PRONOM identifier. TBH the format really deserved
wide support back in the 2000s, I suspect it would have out-performed DivX
during the era of early swashbuckling video if compression was faster.

So, let's fix the omission:

* [🪄 libmagic rules](https://bugs.astron.com/view.php?id=743)
* 🗄️ PRONOM: TNA1774396137A87

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
the wild. It's unsupported by libmagic and unknown by PRONOM. But again has a
[Wikidata entry](https://www.wikidata.org/wiki/Q28206609) and an
[ArchiveTeam page](http://fileformats.archiveteam.org/wiki/MRF_(Monochrome_Recursive_Format)),
and of course Sembiance has
[more test data](https://sembiance.com/fileFormatSamples/image/monochromeRecursiveFormat/)
for us to play with.

So we'll pilfer his test data again and write a magic rule, and link this one in
to PRONOM like the others:

* [🪄 libmagic rules](https://bugs.astron.com/view.php?id=744)
* 🗄️ PRONOM: TNA1774653669Q59

---

## YBM Face File

![ybm](ybm.png)

Created by Bennet Yee at CMU around 1988 for his `face` and `xbm` programs -
small monochrome portraits in the early Unix tradition of user avatars. Jamie
Zawinski and Jef Poskanzer wrote the netpbm converters in 1991. The name
doesn't seem to be official — "YBM" appears to be a netpbm convention for
"Yee BitMap", to distinguish it from X BitMap (XBM).

The format is simple: a 6-byte header (`!!` magic, BE 16-bit width, BE
16-bit height), then 1bpp bitmap data packed into 16-bit BE words with reversed
bit order. It has a [Wikidata entry](https://www.wikidata.org/wiki/Q28207564)
and an [ArchiveTeam page](http://fileformats.archiveteam.org/wiki/YBM), but no
PRONOM identifier or MIME type. Sembiance has
[test data](https://sembiance.com/fileFormatSamples/image/ybm/), of course.

The 2-byte magic `!!` followed by two 16-bit big-endian ints is too generic for
a reliable libmagic rule, since it lacks a way to do bit-twiddling arithmetic to
make sure the file is the proper size. So rather than matching almost everything
starting with `!!` and positive matches being so rare, we'll skip submission to
libmagic. I did make a rule file anyway, and submitted the format details to
PRONOM for posterity.

* [🪄 magic rule file](https://github.com/bitplane/pillow-netpbm/blob/master/tests/data/ybm/ybm.magic)
* 🗄️ PRONOM: TNA1774654680B32

---

## NEO (Atari NEOchrome)

![neo](neo.png)

[NEOchrome](https://en.wikipedia.org/wiki/NEOchrome) was Atari Corporation's
own paint program, released in 1985 by Dave Staugas and Jim Eisenstein. Images
are planar 16 colour files very similar to Atari DEGAS but with extra header
data and a size of exactly 32128 bytes.

Unfortunately, the header partially overlaps with DEGAS files. This causes
false detection as DEGAS in libmagic and scrambles images in
[my own degas loader](/dev/python/pillow-degas). netpbm's anytopnm doesn't do
automatic detection of DEGAS or NEOchrome images, which is also worth flagging.

The format has an [ArchiveTeam entry](http://fileformats.archiveteam.org/wiki/NEOchrome)
but no PRONOM identifier. [Wikidata](https://www.wikidata.org/wiki/Q28049507)
lists both `image/x-neo` and `image/x-neochrome` as unregistered MIME types, but
I couldn't find evidence of the latter being used; dexvert and ksquirrel use
`image/x-neo`. Sembiance's dexvert test data contains
[14 test files](https://sembiance.com/fileFormatSamples/image/neochrome/) for us
to plunder, including the one above.

Let's fix some of this:

* [🛏️ release pillow-degas v0.2.0](https://pypi.org/project/pillow-degas/0.2.0/)
* [🪄 libmagic bug report](https://bugs.astron.com/view.php?id=746)
* 🗄️ PRONOM: TODO

---

## JBIG (Joint Bi-level Image experts Group)

![jbig/bie](bie.png)

[JBIG1](https://www.itu.int/rec/T-REC-T.82) is a black and white image
compression standard used for fax and scanned documents. The standalone file
format is called a BIE (Bi-level Image Entity). Files use `.jbg`, `.jbig`, or
`.bie` extensions - all the same format. The reference implementation is Markus
Kuhn's [jbigkit](https://www.cl.cam.ac.uk/~mgk25/jbigkit/).

`image/x-jbig` is the de-facto MIME used by both
[freedesktop](https://gitlab.freedesktop.org/xdg/shared-mime-info) and
[Apache Tika](https://github.com/apache/tika), it's in
[PRONOM](https://www.nationalarchives.gov.uk/pronom/fmt/399),a
[Wikidata](https://www.wikidata.org/wiki/Q747833), and
[ArchiveTeam's wiki](http://justsolve.archiveteam.org/wiki/JBIG).

So, it's well-known, but files are misidentified by `file` as `Targa image data`
because like Targa there's no magic string. I wrote a detection rule which is
too fragile for libmagic. Crappy file extension detection is all we have in
`pillow-netpbm` for now. Oh, and two of Sembiance's
[JBIG test files](https://sembiance.com/fileFormatSamples/image/jbig/) are
mislabelled JPEGs, so I guess I can help there at least.

* [🐛 dexvert data bug](https://github.com/Sembiance/dexvert/issues/41)
* [🪄 magic rule file](https://github.com/bitplane/pillow-netpbm/blob/master/tests/data/jbig/jbig.magic)

---

# WIP: research + notes from here on

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

