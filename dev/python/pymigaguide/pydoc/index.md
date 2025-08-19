<a id="pymigaguide"></a>

# pymigaguide

<a id="pymigaguide.markdown"></a>

# pymigaguide.markdown

<a id="pymigaguide.model"></a>

# pymigaguide.model

<a id="pymigaguide.model.GuideMetadata"></a>

## GuideMetadata Objects

```python
class GuideMetadata(BaseModel)
```

<a id="pymigaguide.model.GuideMetadata.database"></a>

#### database

@DATABASE

<a id="pymigaguide.model.GuideMetadata.author"></a>

#### author

@AUTHOR

<a id="pymigaguide.model.GuideMetadata.version"></a>

#### version

@$VER: ...

<a id="pymigaguide.model.GuideMetadata.copyright"></a>

#### copyright

@(c) ...

<a id="pymigaguide.model.GuideMetadata.index_node"></a>

#### index\_node

@INDEX  (global)

<a id="pymigaguide.model.GuideMetadata.help_node"></a>

#### help\_node

@HELP   (global)

<a id="pymigaguide.model.GuideMetadata.font_name"></a>

#### font\_name

@FONT name size (global)

<a id="pymigaguide.model.GuideMetadata.wordwrap"></a>

#### wordwrap

@WORDWRAP

<a id="pymigaguide.model.GuideMetadata.smartwrap"></a>

#### smartwrap

@SMARTWRAP

<a id="pymigaguide.model.GuideMetadata.tab_width"></a>

#### tab\_width

@TAB n

<a id="pymigaguide.model.GuideMetadata.width_hint"></a>

#### width\_hint

@WIDTH

<a id="pymigaguide.model.GuideMetadata.height_hint"></a>

#### height\_hint

@HEIGHT

<a id="pymigaguide.model.GuideMetadata.onopen_script"></a>

#### onopen\_script

@ONOPEN (global)

<a id="pymigaguide.model.GuideMetadata.onclose_script"></a>

#### onclose\_script

@ONCLOSE (global)

<a id="pymigaguide.model.GuideMetadata.macros"></a>

#### macros

@MACRO name expansion (global)

<a id="pymigaguide.model.NodeAttributes"></a>

## NodeAttributes Objects

```python
class NodeAttributes(BaseModel)
```

<a id="pymigaguide.model.NodeAttributes.title"></a>

#### title

@TITLE or @NODE "title"

<a id="pymigaguide.model.NodeAttributes.toc"></a>

#### toc

@TOC

<a id="pymigaguide.model.NodeAttributes.next"></a>

#### next

@NEXT

<a id="pymigaguide.model.NodeAttributes.prev"></a>

#### prev

@PREV

<a id="pymigaguide.model.NodeAttributes.index"></a>

#### index

@INDEX (node-local)

<a id="pymigaguide.model.NodeAttributes.help"></a>

#### help

@HELP  (node-local)

<a id="pymigaguide.model.NodeAttributes.font_name"></a>

#### font\_name

@FONT (node-local)

<a id="pymigaguide.model.NodeAttributes.proportional"></a>

#### proportional

@PROPORTIONAL

<a id="pymigaguide.model.NodeAttributes.wordwrap"></a>

#### wordwrap

@WORDWRAP

<a id="pymigaguide.model.NodeAttributes.smartwrap"></a>

#### smartwrap

@SMARTWRAP

<a id="pymigaguide.model.NodeAttributes.tab_width"></a>

#### tab\_width

@TAB

<a id="pymigaguide.model.NodeAttributes.onopen_script"></a>

#### onopen\_script

@ONOPEN (node-local)

<a id="pymigaguide.model.NodeAttributes.onclose_script"></a>

#### onclose\_script

@ONCLOSE (node-local)

<a id="pymigaguide.model.NodeAttributes.keywords"></a>

#### keywords

@KEYWORDS

<a id="pymigaguide.model.NodeAttributes.macros"></a>

#### macros

@MACRO (node-local)

<a id="pymigaguide.model.NodeAttributes.embeds"></a>

#### embeds

@EMBED path(s)

<a id="pymigaguide.model.NodeAttributes.extras"></a>

#### extras

stash unknowns

<a id="pymigaguide.model.GuideNode"></a>

## GuideNode Objects

```python
class GuideNode(BaseModel)
```

<a id="pymigaguide.model.GuideNode.content"></a>

#### content

Flattened inline stream

<a id="pymigaguide.model.Link"></a>

## Link Objects

```python
class Link(BaseModel)
```

<a id="pymigaguide.model.Link.target_file"></a>

#### target\_file

"file.guide" or other file (e.g., image)

<a id="pymigaguide.model.Link.target_node"></a>

#### target\_node

"NODE" or dummy "main" when linking to non-guide

<a id="pymigaguide.model.Link.line"></a>

#### line

optional line number

<a id="pymigaguide.model.Action"></a>

## Action Objects

```python
class Action(BaseModel)
```

<a id="pymigaguide.model.Action.kind"></a>

#### kind

"SYSTEM", "RX", "RXS", "BEEP", "CLOSE", "QUIT"

<a id="pymigaguide.model.Action.value"></a>

#### value

command/script, or None for BEEP/CLOSE/QUIT

<a id="pymigaguide.model.StyleToggle"></a>

## StyleToggle Objects

```python
class StyleToggle(BaseModel)
```

<a id="pymigaguide.model.StyleToggle.style"></a>

#### style

"bold", "italic", "underline", "code"

<a id="pymigaguide.model.ColorChange"></a>

## ColorChange Objects

```python
class ColorChange(BaseModel)
```

<a id="pymigaguide.model.ColorChange.fg"></a>

#### fg

named color, or "APEN:<n>"

<a id="pymigaguide.model.ColorChange.bg"></a>

#### bg

named color, or "BPEN:<n>"

<a id="pymigaguide.model.AlignChange"></a>

## AlignChange Objects

```python
class AlignChange(BaseModel)
```

<a id="pymigaguide.model.AlignChange.align"></a>

#### align

"left", "center", "right"

<a id="pymigaguide.model.IndentChange"></a>

## IndentChange Objects

```python
class IndentChange(BaseModel)
```

<a id="pymigaguide.model.IndentChange.lindent"></a>

#### lindent

set left indent (spaces)

<a id="pymigaguide.model.IndentChange.pari"></a>

#### pari

set paragraph initial indent

<a id="pymigaguide.model.IndentChange.pard"></a>

#### pard

reset paragraph settings

<a id="pymigaguide.model.TabsChange"></a>

## TabsChange Objects

```python
class TabsChange(BaseModel)
```

<a id="pymigaguide.model.TabsChange.tab"></a>

#### tab

literal tab insertion

<a id="pymigaguide.model.Break"></a>

## Break Objects

```python
class Break(BaseModel)
```

<a id="pymigaguide.model.Break.kind"></a>

#### kind

"line" or "paragraph"

<a id="pymigaguide.model.UnknownInline"></a>

## UnknownInline Objects

```python
class UnknownInline(BaseModel)
```

<a id="pymigaguide.model.UnknownInline.raw"></a>

#### raw

raw command text inside @{ ... }

<a id="pymigaguide.cli"></a>

# pymigaguide.cli

<a id="pymigaguide.cli.detect_and_decode"></a>

#### detect\_and\_decode

```python
def detect_and_decode(data: bytes) -> tuple[str, str]
```

Detect encoding with chardet and decode to a Python str (UTF-8 internally).
Returns (text, detected_encoding).

<a id="pymigaguide.writer.markdown"></a>

# pymigaguide.writer.markdown

<a id="pymigaguide.writer.markdown.fence_backticks"></a>

#### fence\_backticks

```python
def fence_backticks(s: str) -> str
```

Wrap s in a backtick fence that doesn't conflict with backticks inside s.
Uses inline-style by default (not code blocks).

<a id="pymigaguide.writer.markdown.MarkdownOptions"></a>

## MarkdownOptions Objects

```python
@dataclass
class MarkdownOptions()
```

<a id="pymigaguide.writer.markdown.MarkdownOptions.heading_level"></a>

#### heading\_level

__heading per node__


<a id="pymigaguide.writer.markdown.MarkdownOptions.file_suffix"></a>

#### file\_suffix

links to other guides

<a id="pymigaguide.writer.markdown.MarkdownOptions.tab_spaces"></a>

#### tab\_spaces

how many spaces for @{TAB}

<a id="pymigaguide.writer.markdown.MarkdownOptions.paragraph_blank_lines"></a>

#### paragraph\_blank\_lines

blank lines for PAR

<a id="pymigaguide.writer.markdown.MarkdownOptions.line_break"></a>

#### line\_break

soft line break (we just use newline)

<a id="pymigaguide.writer.markdown.MarkdownOptions.underline_html"></a>

#### underline\_html

use <u> for underline

<a id="pymigaguide.writer.markdown.MarkdownOptions.include_node_title"></a>

#### include\_node\_title

emit H1/H2... title at top of node

<a id="pymigaguide.writer.markdown.MarkdownRenderer"></a>

## MarkdownRenderer Objects

```python
class MarkdownRenderer()
```

<a id="pymigaguide.writer.markdown.MarkdownRenderer.render_document"></a>

#### render\_document

```python
def render_document(doc: GuideDocument) -> Dict[str, str]
```

Returns a dict: { node_name: markdown }

<a id="pymigaguide.writer.html"></a>

# pymigaguide.writer.html

<a id="pymigaguide.writer.html.HtmlRenderer"></a>

## HtmlRenderer Objects

```python
class HtmlRenderer()
```

<a id="pymigaguide.writer.html.HtmlRenderer.render_document"></a>

#### render\_document

```python
def render_document(doc: GuideDocument) -> Dict[str, str]
```

Returns a dict: { node_name: html }

<a id="pymigaguide.writer.json"></a>

# pymigaguide.writer.json

<a id="pymigaguide.writer.json.dump_json"></a>

#### dump\_json

```python
def dump_json(doc: GuideDocument) -> str
```

Pydantic v2 uses model_dump_json; v1 uses .json().
Support both without caring which is installed.

<a id="pymigaguide.writer.txt"></a>

# pymigaguide.writer.txt

<a id="pymigaguide.writer.txt.TxtRenderer"></a>

## TxtRenderer Objects

```python
class TxtRenderer()
```

<a id="pymigaguide.writer.txt.TxtRenderer.render_document"></a>

#### render\_document

```python
def render_document(doc: GuideDocument) -> Dict[str, str]
```

Returns a dict: { node_name: text }

<a id="pymigaguide.parser"></a>

# pymigaguide.parser

<a id="pymigaguide.parser.AmigaGuideParser"></a>

## AmigaGuideParser Objects

```python
class AmigaGuideParser()
```

Pragmatic AmigaGuide parser:
  - Parses global directives, nodes, and inline @{...} commands.
  - Preserves unknown inline commands as UnknownInline.
  - Does not execute macros; it records global/node macro definitions.

<a id="pymigaguide.regex"></a>

# pymigaguide.regex

<a id="pymigaguide.regex.ESCAPED_AT_RE"></a>

#### ESCAPED\_AT\_RE

\@ => literal @

<a id="pymigaguide.regex.ESCAPED_BS_RE"></a>

#### ESCAPED\_BS\_RE

\\ => literal \

<a id="pymigaguide.app"></a>

# pymigaguide.app

<a id="pymigaguide.widgets.flowtext"></a>

# pymigaguide.widgets.flowtext

<a id="pymigaguide.widgets.flowtext.FlowOptions"></a>

## FlowOptions Objects

```python
@dataclass
class FlowOptions()
```

<a id="pymigaguide.widgets.flowtext.FlowOptions.word_wrap"></a>

#### word\_wrap

AmigaGuide WORDWRAP (soft wrap at width)

<a id="pymigaguide.widgets.flowtext.FlowOptions.smart_wrap"></a>

#### smart\_wrap

SMARTWRAP (single \n treated as space)

<a id="pymigaguide.widgets.flowtext.FlowOptions.default_tab"></a>

#### default\_tab

@TAB n default

<a id="pymigaguide.widgets.flowtext.FlowOptions.underline_html"></a>

#### underline\_html

honor underline (as underline style)

<a id="pymigaguide.widgets.flowtext.FlowOptions.show_unknown_inline"></a>

#### show\_unknown\_inline

render unknowns visibly (debug)

<a id="pymigaguide.widgets.flowtext.LinkActivated"></a>

## LinkActivated Objects

```python
class LinkActivated(Message)
```

Posted by FlowText when a link is clicked.

<a id="pymigaguide.widgets.flowtext.FlowText"></a>

## FlowText Objects

```python
class FlowText(Widget)
```

Render AmigaGuide Inline items faithfully enough for TUI:
- Styles: bold/italic/underline
- Colors: FG/BG by name; APEN/BPEN best-effort
- Breaks: LINE, PAR
- Tabs: @{TAB} with default/custom tab stops
- Links: clickable labels (emit LinkActivated)
- Actions: rendered as plain labels (no execution)

**Notes**:

  - Alignment (JLEFT/JCENTER/JRIGHT) is applied per paragraph.
  - CODE mode as a strict "no wrap" inline is not supported per-run in Rich;
  we treat it as a style toggle (monospace effect is up to your theme) and
- `TODO` - we can segment paragraphs to no-wrap blocks later.
  
  - SMARTWRAP: single newlines turn into spaces unless an explicit @{LINE}
  or paragraph boundary is encountered.

<a id="pymigaguide.widgets.guidetoolbar"></a>

# pymigaguide.widgets.guidetoolbar

<a id="pymigaguide.widgets.guidetoolbar.GuideToolbar"></a>

## GuideToolbar Objects

```python
class GuideToolbar(Horizontal)
```

Top navigation bar for AmigaGuide docs.

<a id="pymigaguide.widgets.guidetoolbar.GuideToolbar.NavRequested"></a>

## NavRequested Objects

```python
class NavRequested(Message)
```

Emitted when a toolbar button requests navigation.

<a id="pymigaguide.widgets"></a>

# pymigaguide.widgets

<a id="pymigaguide.widgets.guideview"></a>

# pymigaguide.widgets.guideview

<a id="pymigaguide.widgets.guideview.GuideView"></a>

## GuideView Objects

```python
class GuideView(Container)
```

High-level viewer: holds a Markdown widget, manages navigation/history,
and resolves links between nodes (and across files later).

<a id="pymigaguide.widgets.guideview.GuideView.goto"></a>

#### goto

```python
def goto(file: Optional[str], node: Optional[str],
         line: Optional[int]) -> None
```

Navigate to (file,node). If file is None or .guide is current, use current doc.
node may be a slug; map to actual node name if possible.

<a id="pymigaguide.widgets.guideview.GuideView.on_guide_toolbar_nav_requested"></a>

#### on\_guide\_toolbar\_nav\_requested

```python
def on_guide_toolbar_nav_requested(message: GuideToolbar.NavRequested) -> None
```

Handle navigation requests from the toolbar.

<a id="pymigaguide.widgets.guideview.GuideView.on_markdown_link_clicked"></a>

#### on\_markdown\_link\_clicked

```python
def on_markdown_link_clicked(event: Markdown.LinkClicked) -> None
```

Intercept Markdown links and navigate within guides.

