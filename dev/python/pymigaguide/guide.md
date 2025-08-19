# AmigaGuide Format Reference

This document summarises the **AmigaGuide** hypertext file format as implemented in our parser.
Use it as a working reference when extending parsing, rendering, or Markdown output.

---

## 1. Overview

An AmigaGuide file is a plain text hypertext database used on classic AmigaOS (2.1+).
It contains:

* **Global commands** before/between nodes.
* **One or more named nodes** (`@NODE ...` / `@ENDNODE ...`) containing text.
* **Inline commands** inside text, delimited by `@{ ... }`.

The first non-empty line is normally `@DATABASE <name>`.

---

## 2. Node Structure

A `.guide` file contains one or more **nodes**:

```text
@DATABASE MyGuide
@NODE MAIN "Welcome"
This is the main node.
@ENDNODE

@NODE Other
See @{ "Main page" LINK "MAIN" }.
@ENDNODE
```

* **Node name**: identifier without spaces, tabs, `:` or `/`.
* **Node title**: quoted string (optional if given in `@NODE` line).

The first node (`MAIN` by convention) is shown on open.

---

## 3. Global Commands

Global commands start at column 0 and appear outside any node:

| Command          | Args                  | Purpose                               |
| ---------------- | --------------------- | ------------------------------------- |
| `@DATABASE`      | name                  | Identify the guide file.              |
| `@$VER:`         | string                | Version string (AmigaDOS convention). |
| `@(c)`           | string                | Copyright notice.                     |
| `@AUTHOR`        | name                  | Author metadata.                      |
| `@INDEX`         | node or `"file/node"` | Default Index button target.          |
| `@HELP`          | node or `"file/node"` | Default Help button target.           |
| `@FONT`          | name size             | Default font.                         |
| `@WORDWRAP`      |                       | Enable word-wrap mode.                |
| `@SMARTWRAP`     |                       | Enable smart-wrap mode.               |
| `@TAB`           | n                     | Tab width in spaces.                  |
| `@WIDTH`         | cols                  | Width hint.                           |
| `@HEIGHT`        | rows                  | Height hint.                          |
| `@ONOPEN`        | script                | Run script on open.                   |
| `@ONCLOSE`       | script                | Run script on close.                  |
| `@MACRO`         | name expansion        | Define global macro.                  |
| `@AMIGAGUIDE`    |                       | Insert “AmigaGuide®” in bold.         |
| `@REM`/`@REMARK` | comment               | Comment (ignored).                    |

---

## 4. Node Commands

Node-local commands start at column 0, inside a node:

| Command         | Args           | Purpose                               |
| --------------- | -------------- | ------------------------------------- |
| `@TITLE`        | string         | Node title.                           |
| `@TOC`          | node           | Contents button target for this node. |
| `@NEXT`         | node           | Next button target.                   |
| `@PREV`         | node           | Previous button target.               |
| `@INDEX`        | node           | Index target (local override).        |
| `@HELP`         | node           | Help target (local override).         |
| `@FONT`         | name size      | Font override.                        |
| `@PROPORTIONAL` |                | Use proportional font.                |
| `@WORDWRAP`     |                | Word-wrap (local).                    |
| `@SMARTWRAP`    |                | Smart-wrap (local).                   |
| `@TAB`          | n              | Tab width.                            |
| `@KEYWORDS`     | words          | Keywords for this node.               |
| `@ONOPEN`       | script         | Script on node open.                  |
| `@ONCLOSE`      | script         | Script on node close.                 |
| `@MACRO`        | name expansion | Local macro.                          |
| `@EMBED`        | path           | Insert file contents here.            |

---

## 5. Inline Commands

Inline commands appear **anywhere inside text** between `@{` and `}`.
Common categories:

### 5.1 Links & Actions

```text
@{ "Label" LINK "TargetNode" }
@{ "Label" ALINK "TargetNode" }
@{ "Label" GUIDE "file.guide/Node" }
@{ "Label" SYSTEM "command" }
@{ "Label" RX "script.rexx" }
@{ "Label" RXS "inline-rexx-command" }
@{ "Label" BEEP }
@{ "Label" CLOSE }
@{ "Label" QUIT }
```

### 5.2 Styles

```
@{B} / @{UB}      bold on/off
@{I} / @{UI}      italic on/off
@{U} / @{UU}      underline on/off
@{CODE}           toggle code mode (no wrapping)
@{PLAIN}          reset styles
```

### 5.3 Colours

```
@{FG name}        foreground colour
@{BG name}        background colour
@{APEN n}         foreground pen index
@{BPEN n}         background pen index
```

### 5.4 Layout & Breaks

```
@{JLEFT} / @{JCENTER} / @{JRIGHT}    alignment
@{LINDENT n}                         left indent
@{PARI n}                            paragraph indent
@{PARD}                              reset paragraph formatting
@{TAB}                               insert tab
@{SETTABS n1 n2 ...}                 set custom tab stops
@{CLEARTABS}                         reset tab stops
@{LINE}                              line break
@{PAR}                               paragraph break
```

---

## 6. Escaping

* `\@` → literal `@`
* `\\` → literal backslash

---

## 7. Encoding

* Typically ASCII or ISO-8859-1 (Latin-1).
* May use other 8-bit Amiga charsets for localisation.
* No encoding metadata — detect with `chardet` or similar.
* Convert to UTF-8 for processing.

---

## 8. Notes & Quirks

* Commands are case-insensitive.
* Multiple commands can be on one line if each starts with `@`.
* `ALINK` now behaves like `LINK` in modern viewers.
* MultiView (AmigaOS 3.x+) supports linking to non-guide files via datatypes.
* `SMARTWRAP` mode: single newlines treated as spaces, double newlines = paragraph.
* Macro expansion is not handled by this parser (stored as-is).
