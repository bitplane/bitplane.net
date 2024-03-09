# office.md

A client-side office suite that is shell-friendly, using text files as
documents and the filesystem as the interface. The entire thing being a single
js file that you drop into a dir to make it a document repository, along with
an HTML stub to construct the editor.

## Common API

Develop the code in typescript and have interfaces for the API calls, which
get exposed in `openapi.json` format when built/minified. The APIs themselves
say which region they're for, so:

* They can be parsed into command line options and route to the right places,
  which also transparently works with --help.
* They're tagged with UI hints, so adding new document handling code is
  automatically added to the user interface.
* Have a REPL loop so editors or users can use the functionality in the js
  file without having to reload it each time they call a function. So `vim`
  or whatever can use it.
* They can be exposed as an HTTP API, using node, giving IoT devices and LLMs
  the ability to produce and consume documents via this one js file hosted
  elsewhere.

Pluggable and embedded editors can make use of the API and also provide their
own, where it makes sense.

## Filesystem as a source of truth

Use the filesystem and naming conventions to decide what files are what sort
of document. Avoid configuration wherever possible, but have a
`.office.md.json` at the root for places where it's unavoidable. Or `toml`
maybe, because let's face it `json` is deep and verbose and not readable
by humans while `yaml` is fragile and unwritable by humans.

### Documents and Web Pages

If a file is a .md file, it's a web page unless it contains page breaks then
it's a document. By page breaks we mean "in the rendered DOM, there's an
element that has `page-break-before=always` set"

If we add a page break all we do is insert a couple of blank lines with 
`<div style="page-break-before=always></div>"` in the middle, converting it
into a doc! And yes the "add page break" is an API that has keyboard shortcut,
menu position and command lines set.

Embed a WYSIWYG Markdown editor, but hard-wrap at 80 columns and be extra anal
about formatting it correctly, `black`-style. Why? Because it'll make it
easier to merge, easier to edit on the command line, and make the docs
beautiful by default.

#### Formatting

Have a `.css` file for styling from this dir downwards, or `dirname.css` in the
current dir to style files in a subdir, or `file.css` to style a document.

This keeps the whole thing in the filesystem. "Document templates" would be a
dir with a css file and a Markdown file.

#### Macros

Macros can be supported everywhere by running them in a `require('vm')` sandbox
so they don't have access to the filesystem like the main application does. Do
the same thing as with `.css` files, just load the ones in the path to the
document.

### Spreadsheets

If there are .tsv or .csv files in a dir then that dir can be interpreted as a
spreadsheet, with each file being a sheet.

Support Markdown in cells as well as HTML and plain text, but if it starts with
an `=` then it'll be parsed from Excel, GDocs and/or OO.o format(s) to
javascript functions. The spreadsheet part of the code exposes rows, columns
and sheets, and there's an API to list and call functions.

### Databases

Use sqlite exported `.sql` files as the raw database format, and `.json` files
as queryable graphs. Will need some performance considerations for merging
database, specially in realtime, but will work out of the box for a PoC.

If we add a remote data API provider that is p2p by default, we ought to be
able to make use of macros, databases and sheets to make more than just CRUD
applications.

### Vector Graphics

Use Mermaid embedded in Markdown for mind maps, UML and so on because it Just
Works; embed an editor for this and you've got a decent vector tool. Use
`.svg` for embedded vector graphics, and embed an editor for those too.

### Raster Graphics

Obviously there would need to be a simple JPEG / PNG crop and resize tool,
with local and remote file loading capabilities.

### Video and Audio

Use `.webm` for video and audio, allowing linked embeds, audio and video
recording and maybe even a video editor if there's one out there we can steal.

### Presentations

Interpret `.sozi.json` files as presentations, and embed Sozi too. So the thing
has presentations out of the box that are as good as Prezi!

Ideally we'd have a "play and record audio" which is missing from Sozi along
with present mode.

## Reading and Writing

Pluggable filesystem interface with local access or remote access, that is not
accessible to macros! Add plugins for cloud storage providers, GitHub, IPFS
and whatever else.

### Version Control

Use a `.git` dir at the document root and embed a javascript git client that
uses the filesystem API to read and write. While the user is editing, they
make a temporary branch that is periodically rebased on top of the source
branch, and is merged back in when the user saves. For example, making a branch
like `master/office.md/$sessionStartTimestamp` when the user opens the project
for editing, and then squash commits and rebase.

### Collaborative Editing

First we link repos together using the settings file. When you open it, it'll
add remotes and merge them in, and check for changes in remotes periodically.

Later on we could have a `peer.js` that streams branch commits from branches that
are forked from the same base.

Minimize merge conflicts by auto-formatting, and we'd need a merge conflict
resolution dialog (ew).

### Exporting

Obviously it'll need exporters for HTML at least, but screw docx and friends!
There's enough carrot here, but sometimes you need a stick too.

## What's missing?

* Email
* Calendar
* Task lists
* Maps
* 3D
* WebRTC calls during collaborative editing
* Publishing support via GitHub and GitLab actions etc
