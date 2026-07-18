<a id="winhlp"></a>

# winhlp

winhlp - Windows HLP file library for Python

A pure Python library for parsing Windows Help (.HLP) files.
Based on helpdeco by Manfred Winterhoff, Ben Collver + Paul Wise.

<a id="winhlp.__main__"></a>

# winhlp.\_\_main\_\_

<a id="winhlp.__main__.strip_raw_data"></a>

#### strip\_raw\_data

```python
def strip_raw_data(obj)
```

Recursively drop 'raw_data' keys so the default JSON is readable.

Every parsed structure stores a raw_data blob (the source bytes plus a copy
of the parsed fields), which duplicates the model 2-3x and dominates the
output. --raw keeps it for byte-level fidelity; by default we remove it.

<a id="winhlp.lib.btree"></a>

# winhlp.lib.btree

Generic B+ tree implementation for HLP files.

<a id="winhlp.lib.btree.BTreeHeader"></a>

## BTreeHeader Objects

```python
class BTreeHeader(BaseModel)
```

A B+ tree starts with a BTREEHEADER.
From `helpdeco.h`: BTREEHEADER

<a id="winhlp.lib.btree.BTreeNodeHeader"></a>

## BTreeNodeHeader Objects

```python
class BTreeNodeHeader(BaseModel)
```

B+ tree leaf-page header.
From `helpdeco.h`: BTREENODEHEADER

<a id="winhlp.lib.btree.BTreeIndexHeader"></a>

## BTreeIndexHeader Objects

```python
class BTreeIndexHeader(BaseModel)
```

B+ tree index-page header.
From `helpdeco.h`: BTREEINDEXHEADER

<a id="winhlp.lib.btree.BTreeBuffer"></a>

## BTreeBuffer Objects

```python
class BTreeBuffer(BaseModel)
```

State management for B+ tree iteration.
Based on helpdeco's BUFFER struct used with GetFirstPage/GetNextPage.

From `helpdeco.h`:
typedef struct
{
    int32_t FirstLeaf;
    uint16_t PageSize;
    int16_t NextPage;
}
BUFFER;

<a id="winhlp.lib.btree.BTree"></a>

## BTree Objects

```python
class BTree(BaseModel)
```

A B+ tree is made from leaf-pages and index-pages of fixed size, one of which
is the root-page. All entries are contained in leaf-pages. If more entries
are required than fit into a single leaf-page, index-pages are used to locate
the leaf-page which contains the required entry.

<a id="winhlp.lib.btree.BTree.get_first_page"></a>

#### get\_first\_page

```python
def get_first_page() -> Tuple[int, BTreeBuffer]
```

Finds the first leaf page in the B+ tree and returns its entry count.
Based on helpdeco's GetFirstPage function.

**Returns**:

  Tuple of (number of entries, buffer state for iteration)

<a id="winhlp.lib.btree.BTree.get_next_page"></a>

#### get\_next\_page

```python
def get_next_page(buffer: BTreeBuffer) -> int
```

Gets the next leaf page in the B+ tree.
Based on helpdeco's GetNextPage function.

**Arguments**:

- `buffer` - State from previous get_first_page or get_next_page call
  

**Returns**:

  Number of entries in the page (0 if no more pages)

<a id="winhlp.lib.btree.BTree.iterate_leaf_pages"></a>

#### iterate\_leaf\_pages

```python
def iterate_leaf_pages() -> Iterator[Tuple[bytes, int]]
```

Iterates through all leaf pages using the GetFirstPage/GetNextPage approach.

**Yields**:

  Tuple of (page data, number of entries)

<a id="winhlp.lib.btree.BTree.iterate_leaf_entries_with_parser"></a>

#### iterate\_leaf\_entries\_with\_parser

```python
def iterate_leaf_entries_with_parser(parse_entry_func)
```

Iterates through all entries in B+ tree leaf pages with a custom parser function.

This method provides a higher-level iterator that abstracts away the page-by-page
iteration and header skipping, allowing callers to focus on their specific
entry parsing logic.

Based on the C reference's GetFirstPage/GetNextPage pattern but provides
a cleaner, more Pythonic interface.

**Arguments**:

- `parse_entry_func` - Function that takes (page_data, offset) and returns
  (parsed_entry, new_offset). Should return (None, offset)
  to skip invalid entries.
  

**Yields**:

  Parsed entries from parse_entry_func (excluding None results)

<a id="winhlp.lib.hlp"></a>

# winhlp.lib.hlp

Main HLP file reader class.

<a id="winhlp.lib.hlp.HLPHeader"></a>

## HLPHeader Objects

```python
class HLPHeader(BaseModel)
```

A help file starts with a header, the only structure at a fixed place.
From `helpdeco.h`: HELPHEADER

<a id="winhlp.lib.hlp.HelpFile"></a>

## HelpFile Objects

```python
class HelpFile(BaseModel)
```

The main class for reading and parsing a HLP file.

This class represents a HLP file and provides methods to parse its contents.
It loads the entire file into memory for parsing.

<a id="winhlp.lib.hlp.HelpFile.keyword_search_files"></a>

#### keyword\_search\_files

Maps 'A' -> {'btree': XWBTreeFile, 'data': XWDataFile, 'map': XWMapFile}

<a id="winhlp.lib.hlp.HelpFile.keyword_index_files"></a>

#### keyword\_index\_files

Maps 'A' -> {'btree': XWBTreeFile, 'data': XWDataFile, 'map': XWMapFile} for |xKWBTREE files

<a id="winhlp.lib.hlp.HelpFile.config_files"></a>

#### config\_files

Maps config number -> CFnFile

<a id="winhlp.lib.hlp.HelpFile.grp_files"></a>

#### grp\_files

Maps filename -> GRPFile for .GRP files

<a id="winhlp.lib.hlp.HelpFile.chartab_files"></a>

#### chartab\_files

Maps filename -> ChartabFile for .tbl files

<a id="winhlp.lib.hlp.HelpFile.is_gid_file"></a>

#### is\_gid\_file

True if this is a GID file created by WinHlp32

<a id="winhlp.lib.hlp.HelpFile.get_topics"></a>

#### get\_topics

```python
def get_topics() -> List[ParsedTopic]
```

Get all parsed topics with structured content.

<a id="winhlp.lib.hlp.HelpFile.get_topic_by_number"></a>

#### get\_topic\_by\_number

```python
def get_topic_by_number(topic_number: int) -> Optional[ParsedTopic]
```

Get a specific topic by its number.

<a id="winhlp.lib.hlp.HelpFile.get_topic_by_context_name"></a>

#### get\_topic\_by\_context\_name

```python
def get_topic_by_context_name(context_name: str) -> Optional[ParsedTopic]
```

Get a topic by its context name using hash lookup.

<a id="winhlp.lib.hlp.HelpFile.extract_bitmap"></a>

#### extract\_bitmap

```python
def extract_bitmap(bitmap_name: str) -> Optional[bytes]
```

Extract a bitmap as BMP file data.

<a id="winhlp.lib.hlp.HelpFile.get_topic_with_resolved_images"></a>

#### get\_topic\_with\_resolved\_images

```python
def get_topic_with_resolved_images(topic_number: int) -> Optional[dict]
```

Get a topic with all embedded images resolved to bitmap data.

<a id="winhlp.lib.hlp.HelpFile.get_all_hotspots"></a>

#### get\_all\_hotspots

```python
def get_all_hotspots() -> Dict[str, List]
```

Get all hotspots from all bitmaps with their context names.

<a id="winhlp.lib.hlp.HelpFile.extract_all_text"></a>

#### extract\_all\_text

```python
def extract_all_text() -> str
```

Extract all text content as plain text.

<a id="winhlp.lib.hlp.HelpFile.get_topic_count"></a>

#### get\_topic\_count

```python
def get_topic_count() -> int
```

Get the total number of topics in the help file.

<a id="winhlp.lib.hlp.HelpFile.parse"></a>

#### parse

```python
def parse()
```

Parses the HLP file from the loaded data.

<a id="winhlp.lib.hlp.HelpFile.search_keywords"></a>

#### search\_keywords

```python
def search_keywords(char: str, keyword: str) -> List[int]
```

Search for topic offsets associated with a keyword.

**Arguments**:

- `char` - The character identifier (A-Z, a-z) for the keyword type
- `keyword` - The keyword to search for
  

**Returns**:

  List of topic offsets where the keyword appears

<a id="winhlp.lib.hlp.HelpFile.get_all_keywords"></a>

#### get\_all\_keywords

```python
def get_all_keywords(char: str) -> List[str]
```

Get all keywords for a specific character type.

**Arguments**:

- `char` - The character identifier (A-Z, a-z) for the keyword type
  

**Returns**:

  List of all keywords for the character type

<a id="winhlp.lib.hlp.HelpFile.get_keyword_search_statistics"></a>

#### get\_keyword\_search\_statistics

```python
def get_keyword_search_statistics() -> Dict[str, Any]
```

Get statistics about all keyword search files.

**Returns**:

  Dictionary with keyword search statistics

<a id="winhlp.lib.hlp.HelpFile.get_config_macros"></a>

#### get\_config\_macros

```python
def get_config_macros(config_number: int) -> List[str]
```

Get all macros for a specific configuration number.

**Arguments**:

- `config_number` - The configuration number (0, 1, 2, etc.)
  

**Returns**:

  List of macro strings for the configuration

<a id="winhlp.lib.hlp.HelpFile.get_all_config_numbers"></a>

#### get\_all\_config\_numbers

```python
def get_all_config_numbers() -> List[int]
```

Get all available configuration numbers.

**Returns**:

  List of configuration numbers that have associated files

<a id="winhlp.lib.hlp.HelpFile.get_config_statistics"></a>

#### get\_config\_statistics

```python
def get_config_statistics() -> Dict[str, Any]
```

Get statistics about all configuration files.

**Returns**:

  Dictionary with configuration file statistics

<a id="winhlp.lib.hlp.HelpFile.search_keyword_indices"></a>

#### search\_keyword\_indices

```python
def search_keyword_indices(char: str, keyword: str) -> List[int]
```

Search for topic offsets associated with a keyword in keyword index files.

**Arguments**:

- `char` - The character identifier (A-Z, a-z) for the keyword index type
- `keyword` - The keyword to search for
  

**Returns**:

  List of topic offsets where the keyword appears

<a id="winhlp.lib.hlp.HelpFile.get_all_keyword_indices"></a>

#### get\_all\_keyword\_indices

```python
def get_all_keyword_indices(char: str) -> List[str]
```

Get all keywords for a specific keyword index character type.

**Arguments**:

- `char` - The character identifier (A-Z, a-z) for the keyword index type
  

**Returns**:

  List of all keywords for the character type

<a id="winhlp.lib.hlp.HelpFile.get_keyword_index_statistics"></a>

#### get\_keyword\_index\_statistics

```python
def get_keyword_index_statistics() -> Dict[str, Any]
```

Get statistics about all keyword index files.

**Returns**:

  Dictionary with keyword index statistics

<a id="winhlp.lib.hlp.HelpFile.get_macro_by_hash"></a>

#### get\_macro\_by\_hash

```python
def get_macro_by_hash(keyword_hash: int) -> Optional[str]
```

Get a macro string by its keyword hash from the |Rose file.

**Arguments**:

- `keyword_hash` - The keyword hash to look up
  

**Returns**:

  Macro string, or None if not found or no Rose file

<a id="winhlp.lib.hlp.HelpFile.get_all_macro_definitions"></a>

#### get\_all\_macro\_definitions

```python
def get_all_macro_definitions() -> List[tuple]
```

Get all macro definitions from the |Rose file.

**Returns**:

  List of (keyword_hash, macro, topic_title) tuples

<a id="winhlp.lib.hlp.HelpFile.find_macros_by_pattern"></a>

#### find\_macros\_by\_pattern

```python
def find_macros_by_pattern(pattern: str) -> List[tuple]
```

Find macro definitions containing a pattern.

**Arguments**:

- `pattern` - String pattern to search for in macro strings
  

**Returns**:

  List of (keyword_hash, macro, topic_title) tuples matching the pattern

<a id="winhlp.lib.hlp.HelpFile.get_rose_statistics"></a>

#### get\_rose\_statistics

```python
def get_rose_statistics() -> Dict[str, Any]
```

Get statistics about the Rose file.

**Returns**:

  Dictionary with Rose file statistics, or empty dict if no Rose file

<a id="winhlp.lib.hlp.HelpFile.get_character_mapping"></a>

#### get\_character\_mapping

```python
def get_character_mapping(filename: str, char_code: int) -> Optional[dict]
```

Get character mapping information for a specific character code from a CHARTAB file.

**Arguments**:

- `filename` - The CHARTAB filename (e.g., "ANSI.TBL")
- `char_code` - The character code to look up
  

**Returns**:

  Dictionary with character mapping information, or None if not found

<a id="winhlp.lib.hlp.HelpFile.get_all_character_mappings"></a>

#### get\_all\_character\_mappings

```python
def get_all_character_mappings(filename: str) -> Dict[int, dict]
```

Get all character mappings from a CHARTAB file.

**Arguments**:

- `filename` - The CHARTAB filename (e.g., "ANSI.TBL")
  

**Returns**:

  Dictionary mapping character codes to mapping information

<a id="winhlp.lib.hlp.HelpFile.get_chartab_statistics"></a>

#### get\_chartab\_statistics

```python
def get_chartab_statistics() -> Dict[str, Any]
```

Get statistics about all CHARTAB files.

**Returns**:

  Dictionary with CHARTAB file statistics

<a id="winhlp.lib.hlp.HelpFile.get_available_chartab_files"></a>

#### get\_available\_chartab\_files

```python
def get_available_chartab_files() -> List[str]
```

Get list of available CHARTAB filenames.

**Returns**:

  List of CHARTAB filenames

<a id="winhlp.lib.text_utils"></a>

# winhlp.lib.text\_utils

Text decoding utilities for Windows Help files.

This module provides centralized text decoding functionality with encoding
fallbacks to handle international character sets correctly across different
Windows Help file parsers.

<a id="winhlp.lib.text_utils.decode_help_text"></a>

#### decode\_help\_text

```python
def decode_help_text(data: bytes,
                     primary_encoding: Optional[str] = None) -> str
```

Decode byte string to text using Windows Help file appropriate encodings.

This function provides a centralized implementation of the text decoding
logic that was previously duplicated across multiple parser classes
(RoseFile, GMacrosFile, TopicIdFile, TTLBTreeFile, PhraseFile, etc.).

**Arguments**:

- `data` - Byte data to decode
- `primary_encoding` - Optional primary encoding to try first (e.g., from |SYSTEM file)
  If None, uses cp1252 as primary
  

**Returns**:

  Decoded string, with fallback handling to prevent decode errors

<a id="winhlp.lib.text_utils.decode_help_text_with_system"></a>

#### decode\_help\_text\_with\_system

```python
def decode_help_text_with_system(data: bytes, system_file=None) -> str
```

Decode byte string using encoding information from |SYSTEM file.

Convenience wrapper around decode_help_text that extracts encoding
from the system file if available.

**Arguments**:

- `data` - Byte data to decode
- `system_file` - SystemFile instance with encoding information
  

**Returns**:

  Decoded string

<a id="winhlp.lib.html"></a>

# winhlp.lib.html

Render a parsed HelpFile to a single self-contained HTML document.

The whole help file becomes one HTML page: a table of contents followed by every
topic as an anchored ``<section>``. Internal jumps/popups resolve to in-page
```anchor``` links (via each topic's TOPICOFFSET), character formatting comes from
the |FONT descriptors as CSS classes, and images are either embedded as data
URIs (self-contained) or written to a folder and referenced by ``<img src>``.

<a id="winhlp.lib.html.HtmlExporter"></a>

## HtmlExporter Objects

```python
class HtmlExporter()
```

<a id="winhlp.lib.html.HtmlExporter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(helpfile, images: str = "embed", image_dir: Optional[str] = None)
```

images: "embed" (data URIs) or "extract" (write files to image_dir).

<a id="winhlp.lib.html.export_html"></a>

#### export\_html

```python
def export_html(helpfile,
                images: str = "embed",
                image_dir: Optional[str] = None) -> str
```

Render a HelpFile to a single HTML document string.

<a id="winhlp.lib.exceptions"></a>

# winhlp.lib.exceptions

Custom exceptions for the HLP file reader library.

<a id="winhlp.lib.exceptions.HLPError"></a>

## HLPError Objects

```python
class HLPError(Exception)
```

Base class for exceptions in this module.

<a id="winhlp.lib.exceptions.InvalidHLPFileError"></a>

## InvalidHLPFileError Objects

```python
class InvalidHLPFileError(HLPError)
```

Raised when the file is not a valid HLP file.

<a id="winhlp.lib.exceptions.BTreeError"></a>

## BTreeError Objects

```python
class BTreeError(HLPError)
```

Raised for errors related to B-Tree parsing.

<a id="winhlp.lib.picture"></a>

# winhlp.lib.picture

Decoder for the internal lP/SHG/MRB picture format.

Pictures embedded in |bmN files and MediaView named bitmap resources are stored
in the SHG/MRB "lP"/"lp" container (doc/helpfile.md:1266-1323): a magic + a table
of picture offsets, each pointing at a DDB/DIB bitmap or a metafile whose
dimension header is written as *compressed* integers and whose pixels are packed
with RunLen and/or LZ77. This module decodes the first picture into a ready-to-
serve Windows .bmp (bitmaps) or raw metafile (.wmf).

<a id="winhlp.lib.picture.LP_MAGIC"></a>

#### LP\_MAGIC

"lP" (SHG) / "lp" (MRB)

<a id="winhlp.lib.picture.decode_picture"></a>

#### decode\_picture

```python
def decode_picture(raw: bytes) -> Optional[Tuple[str, bytes]]
```

Decode the first picture in an lP/SHG/MRB blob into (extension, bytes).

<a id="winhlp.lib.internal_files.topicid"></a>

# winhlp.lib.internal\_files.topicid

Parser for the |TopicId internal file.

<a id="winhlp.lib.internal_files.topicid.TopicIdIndexEntry"></a>

## TopicIdIndexEntry Objects

```python
class TopicIdIndexEntry(BaseModel)
```

Structure for |TopicId index-page entries.
From helpfile.md: TopicIdINDEXENTRY

<a id="winhlp.lib.internal_files.topicid.TopicIdLeafEntry"></a>

## TopicIdLeafEntry Objects

```python
class TopicIdLeafEntry(BaseModel)
```

Structure for |TopicId leaf-page entries.
From helpfile.md: TopicIdLEAFENTRY

<a id="winhlp.lib.internal_files.topicid.TopicIdFile"></a>

## TopicIdFile Objects

```python
class TopicIdFile(InternalFile)
```

Parses the |TopicId file, which contains context name mappings.

From helpfile.md:
The |TopicId internal file lists the ContextName assigned to a specific topic
offset if the help file was created using the /a option of HCRTF and is built
using a B+ tree.

Structure of |TopicId index-page entries:
struct {
    TOPICOFFSET TopicOffset
    short PageNumber
} TopicIdINDEXENTRY[NEntries]

Structure of |TopicId leaf-page entries:
struct {
    TOPICOFFSET TopicOffset
    STRINGZ ContextName
} TopicIdLEAFENTRY[NEntries]

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.topic_context_map"></a>

#### topic\_context\_map

topic_offset -> context_name

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.context_topic_map"></a>

#### context\_topic\_map

context_name -> topic_offset

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.get_context_name_for_topic"></a>

#### get\_context\_name\_for\_topic

```python
def get_context_name_for_topic(topic_offset: int) -> Optional[str]
```

Gets the context name for a given topic offset.

**Arguments**:

- `topic_offset` - The topic offset to look up
  

**Returns**:

  Context name string, or None if not found

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.get_topic_offset_for_context"></a>

#### get\_topic\_offset\_for\_context

```python
def get_topic_offset_for_context(context_name: str) -> Optional[int]
```

Gets the topic offset for a given context name.

**Arguments**:

- `context_name` - The context name to look up
  

**Returns**:

  Topic offset, or None if not found

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.get_all_context_names"></a>

#### get\_all\_context\_names

```python
def get_all_context_names() -> List[str]
```

Returns a list of all context names in the file.

**Returns**:

  List of context name strings

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.get_all_topic_offsets"></a>

#### get\_all\_topic\_offsets

```python
def get_all_topic_offsets() -> List[int]
```

Returns a list of all topic offsets in the file.

**Returns**:

  List of topic offsets

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.get_entry_count"></a>

#### get\_entry\_count

```python
def get_entry_count() -> int
```

Returns the total number of TopicId entries.

**Returns**:

  Number of entries

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.find_contexts_by_pattern"></a>

#### find\_contexts\_by\_pattern

```python
def find_contexts_by_pattern(pattern: str) -> List[tuple]
```

Find context names matching a pattern (case insensitive).

**Arguments**:

- `pattern` - String pattern to search for
  

**Returns**:

  List of (context_name, topic_offset) tuples matching the pattern

<a id="winhlp.lib.internal_files.topicid.TopicIdFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the TopicId data.

**Returns**:

  Dictionary with TopicId statistics

<a id="winhlp.lib.internal_files.phrase"></a>

# winhlp.lib.internal\_files.phrase

Parser for the |Phrases internal file.

<a id="winhlp.lib.internal_files.phrase.PhraseFile"></a>

## PhraseFile Objects

```python
class PhraseFile(InternalFile)
```

Parses the |Phrases file, which contains phrase compression tables.

Based on helldeco.c PhraseLoad function:
- Read PhraseCount as WORD
- Check for special VC4.0 format (PhraseCount == 0x0800)
- Read magic number (must be 0x0100)
- Read phrase offsets as WORDs
- Decompress phrase data using LZ77 (WinHelp 3.1+) or uncompressed (WinHelp 3.0)

<a id="winhlp.lib.internal_files.phrase.PhraseFile.is_new_format"></a>

#### is\_new\_format

VC4.0 MSDEV format

<a id="winhlp.lib.internal_files.phrase.PhraseFile.get_phrase"></a>

#### get\_phrase

```python
def get_phrase(phrase_number: int) -> Optional[str]
```

Gets a phrase by its number.

<a id="winhlp.lib.internal_files.petra"></a>

# winhlp.lib.internal\_files.petra

|Petra file parser for Windows HLP files.

The |Petra file maps topic offsets to original RTF source filenames.
It's created when using HCRTF /a option and follows a B+ tree structure
similar to |CONTEXT files.

Based on the helpdeco C reference implementation and documentation.

<a id="winhlp.lib.internal_files.petra.PetraEntry"></a>

## PetraEntry Objects

```python
class PetraEntry(BaseModel)
```

A single entry in the Petra mapping table.

<a id="winhlp.lib.internal_files.petra.PetraFile"></a>

## PetraFile Objects

```python
class PetraFile(InternalFile)
```

Parses the |Petra internal file which maps topic offsets to RTF source filenames.

The |Petra file is created when help files are compiled with HCRTF /a option.
It contains a B+ tree structure that maps TopicOffset -> RTFSourceFileName.

Structure:
- Uses B+ tree for efficient lookup
- Each leaf node contains topic offset to filename mappings
- Similar structure to |CONTEXT but with different data payload

<a id="winhlp.lib.internal_files.petra.PetraFile.entries"></a>

#### entries

topic_offset -> rtf_filename

<a id="winhlp.lib.internal_files.petra.PetraFile.get_rtf_filename"></a>

#### get\_rtf\_filename

```python
def get_rtf_filename(topic_offset: int) -> Optional[str]
```

Get the RTF source filename for a given topic offset.

<a id="winhlp.lib.internal_files.petra.PetraFile.get_all_mappings"></a>

#### get\_all\_mappings

```python
def get_all_mappings() -> Dict[int, str]
```

Get all topic offset to RTF filename mappings.

<a id="winhlp.lib.internal_files.petra.PetraFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Get statistics about the Petra file.

<a id="winhlp.lib.internal_files.tomap"></a>

# winhlp.lib.internal\_files.tomap

Parser for the |TOMAP internal file.

<a id="winhlp.lib.internal_files.tomap.TopicPosition"></a>

## TopicPosition Objects

```python
class TopicPosition(BaseModel)
```

Structure for a single topic position entry.
From helpfile.md: TOPICPOS entries in |TOMAP file.

<a id="winhlp.lib.internal_files.tomap.ToMapFile"></a>

## ToMapFile Objects

```python
class ToMapFile(InternalFile)
```

Parses the |TOMAP file, which contains topic position mappings for Windows 3.0 help files.

From helpfile.md:
Windows 3.0 (HC30) uses topic numbers that start at 16 for the first topic
to identify topics. To retrieve the location of the TOPICLINK for the TOPIC-
HEADER of a certain topic (in |TOPIC explained later), use the |TOMAP file.
It contains an array of topic positions. Index with TopicNumber (do not
subtract 16). TopicPos[0] points to the topic specified as INDEX in the help
project.

Structure: TOPICPOS TopicPos[UsedSpace/4]

<a id="winhlp.lib.internal_files.tomap.ToMapFile.topic_positions"></a>

#### topic\_positions

Array of TOPICPOS values

<a id="winhlp.lib.internal_files.tomap.ToMapFile.topic_map"></a>

#### topic\_map

topic_number -> topic_position mapping

<a id="winhlp.lib.internal_files.tomap.ToMapFile.get_topic_position"></a>

#### get\_topic\_position

```python
def get_topic_position(topic_number: int) -> Optional[int]
```

Get the topic position for a given topic number.

**Arguments**:

- `topic_number` - Topic number (starts at 16 for first topic)
  

**Returns**:

  Topic position or None if not found

<a id="winhlp.lib.internal_files.tomap.ToMapFile.get_index_topic_position"></a>

#### get\_index\_topic\_position

```python
def get_index_topic_position() -> Optional[int]
```

Get the position of the INDEX topic.

From helpfile.md: TopicPos[0] points to the topic specified as INDEX
in the help project.

**Returns**:

  Position of INDEX topic or None if no topics

<a id="winhlp.lib.internal_files.tomap.ToMapFile.get_topic_count"></a>

#### get\_topic\_count

```python
def get_topic_count() -> int
```

Get the total number of topics in the |TOMAP file.

<a id="winhlp.lib.internal_files.context"></a>

# winhlp.lib.internal\_files.context

Parser for the |CONTEXT internal file.

<a id="winhlp.lib.internal_files.context.ContextIndexEntry"></a>

## ContextIndexEntry Objects

```python
class ContextIndexEntry(BaseModel)
```

Structure for |CONTEXT index-page entries.
From `helpfile.md`: CONTEXTINDEXENTRY

<a id="winhlp.lib.internal_files.context.ContextLeafEntry"></a>

## ContextLeafEntry Objects

```python
class ContextLeafEntry(BaseModel)
```

Structure for |CONTEXT leaf-page entries.
From `helpfile.md`: CONTEXTLEAFENTRY

<a id="winhlp.lib.internal_files.context.ContextFile"></a>

## ContextFile Objects

```python
class ContextFile(InternalFile)
```

Parses the |CONTEXT file, which contains context name hash values
and their associated topic offsets. Used in WinHelp 3.1+.

From helpfile.md:
Windows 3.1 (HC31) uses hash values of context names to identify topics.
To get the location of the topic, search the B+ tree of the internal file |CONTEXT.

<a id="winhlp.lib.internal_files.context.ContextFile.context_map"></a>

#### context\_map

hash_value -> topic_offset

<a id="winhlp.lib.internal_files.context.ContextFile.get_topic_offset_for_hash"></a>

#### get\_topic\_offset\_for\_hash

```python
def get_topic_offset_for_hash(hash_value: int) -> Optional[int]
```

Gets the topic offset for a given context name hash value.

<a id="winhlp.lib.internal_files.context.ContextFile.calculate_hash"></a>

#### calculate\_hash

```python
@staticmethod
def calculate_hash(context_name: str) -> int
```

Calculates the hash value for a context name using the algorithm from helpfile.md.

From helpfile.md:
The hash value for an empty string is 1.
Only 0-9, A-Z, a-z, _ and . are legal characters for context ids in Win 3.1 (HC31).

Note: The hash table contains signed byte values. Values > 0x7F are negative.

<a id="winhlp.lib.internal_files.context.ContextFile.reverse_hash"></a>

#### reverse\_hash

```python
@staticmethod
def reverse_hash(hash_value: int) -> str
```

Attempts to reverse a hash value back to a context name.

Based on the unhash() function from helpdeco.c.
This generates a context ID that produces the given hash value.

<a id="winhlp.lib.internal_files.context.ContextFile.derive_from_title"></a>

#### derive\_from\_title

```python
@staticmethod
def derive_from_title(title: str,
                      desired_hash: int,
                      win95: bool = False) -> Optional[str]
```

Attempts to derive a context ID from a topic title that matches the desired hash.

Based on the Derive() function from helpdeco.c.
Many authoring systems create context IDs from topic titles by:
- Replacing illegal characters with _ or . or leaving them out
- Using only part of the topic title
- Prefixing with idh_ or helpid_

**Arguments**:

- `title` - The topic title to derive from
- `desired_hash` - The hash value we're trying to match
- `win95` - Whether to use Win95 character rules (allows more chars)
  

**Returns**:

  A context ID that hashes to desired_hash, or None if not found

<a id="winhlp.lib.internal_files.base"></a>

# winhlp.lib.internal\_files.base

Base class for internal file parsers.

<a id="winhlp.lib.internal_files.base.InternalFile"></a>

## InternalFile Objects

```python
class InternalFile(BaseModel)
```

Base class for all internal file parsers.

<a id="winhlp.lib.internal_files.gid"></a>

# winhlp.lib.internal\_files.gid

Parsers for GID-specific internal files.

Based on helpfile.md documentation, GID files created by WinHlp32 contain
several specific internal files that are not present in regular HLP files.

<a id="winhlp.lib.internal_files.gid.WinPosFile"></a>

## WinPosFile Objects

```python
class WinPosFile(InternalFile)
```

Parser for |WinPos internal file found in GID files.

From helpfile.md:
"This file has been seen in WinHlp32 GID files, but always contained an empty
Btree (with an unknown 'a' in the BTREEHEADER structure)."

<a id="winhlp.lib.internal_files.gid.PeteFile"></a>

## PeteFile Objects

```python
class PeteFile(InternalFile)
```

Parser for |Pete internal file found in GID files.

From helpfile.md:
"This file has been seen in WinHlp32 GID files but is currently not understood."

<a id="winhlp.lib.internal_files.gid.FlagsFile"></a>

## FlagsFile Objects

```python
class FlagsFile(InternalFile)
```

Parser for |Flags internal file found in GID files.

From helpfile.md:
"This file has been seen in WinHlp32 GID files but is currently not understood."

<a id="winhlp.lib.internal_files.gid.CntJumpFile"></a>

## CntJumpFile Objects

```python
class CntJumpFile(InternalFile)
```

Parser for |CntJump internal file found in GID files.

From helpfile.md:
"This B+ tree stored in WinHlp32 GID files contains the jump references of
the *.CNT file."

<a id="winhlp.lib.internal_files.gid.CntTextFile"></a>

## CntTextFile Objects

```python
class CntTextFile(InternalFile)
```

Parser for |CntText internal file found in GID files.

From helpfile.md:
"This B+ tree stored in WinHlp32 GID files contains the topic titles of the
jumps from the *.CNT file."

<a id="winhlp.lib.internal_files.cfn"></a>

# winhlp.lib.internal\_files.cfn

Parser for the |CFn internal file.

<a id="winhlp.lib.internal_files.cfn.CFnFile"></a>

## CFnFile Objects

```python
class CFnFile(InternalFile)
```

Parses the |CFn file, which contains configuration macros.

From helpfile.md:
The |CFn (where n is integer) internal file lists the macros defined in
[CONFIG:n] sections of the help project file (HCW 4.00). The file contains as
many macro strings as were specified one after another:

STRINGZ Macro[]

This is a simple sequential format where macros are stored as null-terminated
strings one after another.

<a id="winhlp.lib.internal_files.cfn.CFnFile.get_macros"></a>

#### get\_macros

```python
def get_macros() -> List[str]
```

Returns all macros in the configuration file.

**Returns**:

  List of macro strings

<a id="winhlp.lib.internal_files.cfn.CFnFile.get_macro_count"></a>

#### get\_macro\_count

```python
def get_macro_count() -> int
```

Returns the number of macros in the configuration file.

**Returns**:

  Number of macros

<a id="winhlp.lib.internal_files.cfn.CFnFile.get_config_number"></a>

#### get\_config\_number

```python
def get_config_number() -> int
```

Returns the configuration number extracted from the filename.

**Returns**:

  Configuration number (0 if not determinable)

<a id="winhlp.lib.internal_files.cfn.CFnFile.get_macro_by_index"></a>

#### get\_macro\_by\_index

```python
def get_macro_by_index(index: int) -> str
```

Gets a macro by its index.

**Arguments**:

- `index` - Zero-based index of the macro
  

**Returns**:

  Macro string, or empty string if index is out of range

<a id="winhlp.lib.internal_files.cfn.CFnFile.find_macros_by_pattern"></a>

#### find\_macros\_by\_pattern

```python
def find_macros_by_pattern(pattern: str) -> List[tuple]
```

Find macros containing a pattern (case insensitive).

**Arguments**:

- `pattern` - String pattern to search for
  

**Returns**:

  List of (index, macro) tuples matching the pattern

<a id="winhlp.lib.internal_files.cfn.CFnFile.get_macros_sorted"></a>

#### get\_macros\_sorted

```python
def get_macros_sorted() -> List[str]
```

Get all macros sorted alphabetically.

**Returns**:

  List of macro strings sorted alphabetically

<a id="winhlp.lib.internal_files.cfn.CFnFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the CFn data.

**Returns**:

  Dictionary with CFn statistics

<a id="winhlp.lib.internal_files.phrindex"></a>

# winhlp.lib.internal\_files.phrindex

Parser for the |PhrIndex internal file.

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader"></a>

## PhrIndexHeader Objects

```python
class PhrIndexHeader(BaseModel)
```

Header for the |PhrIndex file.
From `helpdeco.h`: PHRINDEXHDR

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.always_4a01"></a>

#### always\_4a01

Sometimes 0x0001, usually 0x4A01

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.entries"></a>

#### entries

Number of phrases

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.compressed_size"></a>

#### compressed\_size

Size of PhrIndex file

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.phr_image_size"></a>

#### phr\_image\_size

Size of decompressed PhrImage file

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.phr_image_compressed_size"></a>

#### phr\_image\_compressed\_size

Size of PhrImage file

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.always_0"></a>

#### always\_0

Should be 0

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.bits"></a>

#### bits

4-bit field

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.unknown"></a>

#### unknown

12-bit field

<a id="winhlp.lib.internal_files.phrindex.PhrIndexHeader.always_4a00"></a>

#### always\_4a00

Sometimes 0x4A01, 0x4A02, usually 0x4A00

<a id="winhlp.lib.internal_files.phrindex.PhrIndexFile"></a>

## PhrIndexFile Objects

```python
class PhrIndexFile(InternalFile)
```

Parses the |PhrIndex file, which contains phrase compression index.

The PhrIndex file is used for phrase compression in WinHelp 3.1+.
It contains an index of phrases that can be referenced to save space
in the actual help content.

From `helpdeco.h` PHRINDEXHDR structure:
- always4A01 (4 bytes): Magic number, sometimes 0x0001
- entries (4 bytes): Number of phrases
- compressedsize (4 bytes): Size of PhrIndex file
- phrimagesize (4 bytes): Size of decompressed PhrImage file
- phrimagecompressedsize (4 bytes): Size of PhrImage file
- always0 (4 bytes): Should be 0
- Combined 16-bit field with bits (4 bits) and unknown (12 bits)
- always4A00 (2 bytes): Magic number, sometimes 0x4A01, 0x4A02

<a id="winhlp.lib.internal_files.phrindex.PhrIndexFile.complete_phrase_parsing"></a>

#### complete\_phrase\_parsing

```python
def complete_phrase_parsing(phrimage_file=None)
```

Complete phrase parsing after PhrImage file is available.

**Arguments**:

- `phrimage_file` - The PhrImageFile object containing decompressed phrase data

<a id="winhlp.lib.internal_files.topic"></a>

# winhlp.lib.internal\_files.topic

Parser for the |TOPIC internal file.

<a id="winhlp.lib.internal_files.topic.safe_unpack_from"></a>

#### safe\_unpack\_from

```python
def safe_unpack_from(format_str: str,
                     data: bytes,
                     offset: int,
                     default_value=None)
```

Safely unpack struct data with bounds checking.

**Arguments**:

- `format_str` - struct format string (e.g., "<H", "<L")
- `data` - bytes to unpack from
- `offset` - offset in data to start from
- `default_value` - value to return if unpacking fails (None means raise exception)
  

**Returns**:

- `tuple` - unpacked values or default_value on error
  

**Raises**:

- `struct.error` - if bounds check fails and no default_value provided

<a id="winhlp.lib.internal_files.topic.safe_unpack_single"></a>

#### safe\_unpack\_single

```python
def safe_unpack_single(format_str: str,
                       data: bytes,
                       offset: int,
                       default_value=None)
```

Safely unpack a single value with bounds checking.

**Arguments**:

- `format_str` - struct format string (e.g., "<H", "<L")
- `data` - bytes to unpack from
- `offset` - offset in data to start from
- `default_value` - value to return if unpacking fails (None means raise exception)
  

**Returns**:

  single value or default_value on error
  

**Raises**:

- `struct.error` - if bounds check fails and no default_value provided

<a id="winhlp.lib.internal_files.topic.TopicBlockHeader"></a>

## TopicBlockHeader Objects

```python
class TopicBlockHeader(BaseModel)
```

Header for each block in the |TOPIC file.
From `helpdeco.h`: TOPICBLOCKHEADER

<a id="winhlp.lib.internal_files.topic.TopicLink"></a>

## TopicLink Objects

```python
class TopicLink(BaseModel)
```

A link to a topic, found within a topic block.
From `helpdeco.h`: TOPICLINK

<a id="winhlp.lib.internal_files.topic.TopicHeader"></a>

## TopicHeader Objects

```python
class TopicHeader(BaseModel)
```

Topic header for WinHelp 3.1+ files.
From `helpdeco.h`: TOPICHEADER

<a id="winhlp.lib.internal_files.topic.TopicHeader30"></a>

## TopicHeader30 Objects

```python
class TopicHeader30(BaseModel)
```

Topic header for WinHelp 3.0 files.
From `helpdeco.h`: TOPICHEADER30

<a id="winhlp.lib.internal_files.topic.ParagraphInfoBits"></a>

## ParagraphInfoBits Objects

```python
class ParagraphInfoBits(BaseModel)
```

Bit-packed field within ParagraphInfo.
From `helpfile.md`.

<a id="winhlp.lib.internal_files.topic.BorderInfo"></a>

## BorderInfo Objects

```python
class BorderInfo(BaseModel)
```

Structure describing paragraph borders.
From `helpfile.md`.

<a id="winhlp.lib.internal_files.topic.Tab"></a>

## Tab Objects

```python
class Tab(BaseModel)
```

Structure for a single tab stop.
From `helpfile.md`.

<a id="winhlp.lib.internal_files.topic.TabInfo"></a>

## TabInfo Objects

```python
class TabInfo(BaseModel)
```

Structure for defining tab stops.
From `helpfile.md`.

<a id="winhlp.lib.internal_files.topic.ParagraphInfo"></a>

## ParagraphInfo Objects

```python
class ParagraphInfo(BaseModel)
```

Variable-length structure describing paragraph formatting.
From `helpfile.md`.

<a id="winhlp.lib.internal_files.topic.VfldCommand"></a>

## VfldCommand Objects

```python
class VfldCommand(BaseModel)
```

0x20 - {vfld n} command for MVB files

<a id="winhlp.lib.internal_files.topic.VfldCommand.to_rtf"></a>

#### to\_rtf

```python
def to_rtf() -> str
```

Generate RTF output following C reference implementation.

<a id="winhlp.lib.internal_files.topic.DtypeCommand"></a>

## DtypeCommand Objects

```python
class DtypeCommand(BaseModel)
```

0x21 - {dtype n} command for MVB files

<a id="winhlp.lib.internal_files.topic.DtypeCommand.to_rtf"></a>

#### to\_rtf

```python
def to_rtf() -> str
```

Generate RTF output following C reference implementation.

<a id="winhlp.lib.internal_files.topic.FontChangeCommand"></a>

## FontChangeCommand Objects

```python
class FontChangeCommand(BaseModel)
```

0x80 - Font change command

<a id="winhlp.lib.internal_files.topic.LineBreakCommand"></a>

## LineBreakCommand Objects

```python
class LineBreakCommand(BaseModel)
```

0x81 - Line break command

<a id="winhlp.lib.internal_files.topic.ParagraphBreakCommand"></a>

## ParagraphBreakCommand Objects

```python
class ParagraphBreakCommand(BaseModel)
```

0x82 - Paragraph break command

<a id="winhlp.lib.internal_files.topic.TabCommand"></a>

## TabCommand Objects

```python
class TabCommand(BaseModel)
```

0x83 - Tab command

<a id="winhlp.lib.internal_files.topic.BitmapCommand"></a>

## BitmapCommand Objects

```python
class BitmapCommand(BaseModel)
```

0x86/0x87/0x88 - Bitmap commands (left/center/right aligned)

<a id="winhlp.lib.internal_files.topic.BitmapCommand.alignment"></a>

#### alignment

0x86=center, 0x87=left, 0x88=right

<a id="winhlp.lib.internal_files.topic.HotspotEndCommand"></a>

## HotspotEndCommand Objects

```python
class HotspotEndCommand(BaseModel)
```

0x89 - End of hotspot command

<a id="winhlp.lib.internal_files.topic.NonBreakSpaceCommand"></a>

## NonBreakSpaceCommand Objects

```python
class NonBreakSpaceCommand(BaseModel)
```

0x8B - Non-breaking space command

<a id="winhlp.lib.internal_files.topic.NonBreakHyphenCommand"></a>

## NonBreakHyphenCommand Objects

```python
class NonBreakHyphenCommand(BaseModel)
```

0x8C - Non-breaking hyphen command

<a id="winhlp.lib.internal_files.topic.MacroHotspotCommand"></a>

## MacroHotspotCommand Objects

```python
class MacroHotspotCommand(BaseModel)
```

0xC8 - Macro hotspot command

<a id="winhlp.lib.internal_files.topic.MacroNoFontCommand"></a>

## MacroNoFontCommand Objects

```python
class MacroNoFontCommand(BaseModel)
```

0xCC - Macro without font change command

<a id="winhlp.lib.internal_files.topic.PopupJumpHC30Command"></a>

## PopupJumpHC30Command Objects

```python
class PopupJumpHC30Command(BaseModel)
```

0xE0 - Popup jump (HC30)

<a id="winhlp.lib.internal_files.topic.TopicJumpHC30Command"></a>

## TopicJumpHC30Command Objects

```python
class TopicJumpHC30Command(BaseModel)
```

0xE1 - Topic jump (HC30)

<a id="winhlp.lib.internal_files.topic.PopupJumpHC31Command"></a>

## PopupJumpHC31Command Objects

```python
class PopupJumpHC31Command(BaseModel)
```

0xE2 - Popup jump (HC31)

<a id="winhlp.lib.internal_files.topic.TopicJumpHC31Command"></a>

## TopicJumpHC31Command Objects

```python
class TopicJumpHC31Command(BaseModel)
```

0xE3 - Topic jump (HC31)

<a id="winhlp.lib.internal_files.topic.PopupJumpNoFontCommand"></a>

## PopupJumpNoFontCommand Objects

```python
class PopupJumpNoFontCommand(BaseModel)
```

0xE6 - Popup jump without font change

<a id="winhlp.lib.internal_files.topic.TopicJumpNoFontCommand"></a>

## TopicJumpNoFontCommand Objects

```python
class TopicJumpNoFontCommand(BaseModel)
```

0xE7 - Topic jump without font change

<a id="winhlp.lib.internal_files.topic.ExternalPopupJumpCommand"></a>

## ExternalPopupJumpCommand Objects

```python
class ExternalPopupJumpCommand(BaseModel)
```

0xEA/0xEE - Popup jump into external file

<a id="winhlp.lib.internal_files.topic.ExternalPopupJumpCommand.type_field"></a>

#### type\_field

0, 1, 4 or 6

<a id="winhlp.lib.internal_files.topic.ExternalPopupJumpCommand.window_number"></a>

#### window\_number

only if Type = 1

<a id="winhlp.lib.internal_files.topic.ExternalPopupJumpCommand.external_file"></a>

#### external\_file

only if Type = 4 or 6

<a id="winhlp.lib.internal_files.topic.ExternalPopupJumpCommand.window_name"></a>

#### window\_name

only if Type = 6

<a id="winhlp.lib.internal_files.topic.ExternalTopicJumpCommand"></a>

## ExternalTopicJumpCommand Objects

```python
class ExternalTopicJumpCommand(BaseModel)
```

0xEB/0xEF - Topic jump into external file / secondary window

<a id="winhlp.lib.internal_files.topic.ExternalTopicJumpCommand.type_field"></a>

#### type\_field

0, 1, 4 or 6

<a id="winhlp.lib.internal_files.topic.ExternalTopicJumpCommand.window_number"></a>

#### window\_number

only if Type = 1

<a id="winhlp.lib.internal_files.topic.ExternalTopicJumpCommand.external_file"></a>

#### external\_file

only if Type = 4 or 6

<a id="winhlp.lib.internal_files.topic.ExternalTopicJumpCommand.window_name"></a>

#### window\_name

only if Type = 6

<a id="winhlp.lib.internal_files.topic.TextSpan"></a>

## TextSpan Objects

```python
class TextSpan(BaseModel)
```

A span of text with associated formatting.

<a id="winhlp.lib.internal_files.topic.TableCell"></a>

## TableCell Objects

```python
class TableCell(BaseModel)
```

A single cell in a table with its content and formatting.

<a id="winhlp.lib.internal_files.topic.TableCell.alignment"></a>

#### alignment

"left", "center", "right"

<a id="winhlp.lib.internal_files.topic.TableCell.get_plain_text"></a>

#### get\_plain\_text

```python
def get_plain_text() -> str
```

Extract plain text from this cell.

<a id="winhlp.lib.internal_files.topic.TableRow"></a>

## TableRow Objects

```python
class TableRow(BaseModel)
```

A row in a table containing multiple cells.

<a id="winhlp.lib.internal_files.topic.Table"></a>

## Table Objects

```python
class Table(BaseModel)
```

A complete table structure with rows and metadata.

<a id="winhlp.lib.internal_files.topic.Table.get_plain_text"></a>

#### get\_plain\_text

```python
def get_plain_text() -> str
```

Extract plain text representation of the table.

<a id="winhlp.lib.internal_files.topic.HotspotMapping"></a>

## HotspotMapping Objects

```python
class HotspotMapping(BaseModel)
```

Maps text spans to their interactive hotspot targets.

<a id="winhlp.lib.internal_files.topic.HotspotMapping.hotspot_type"></a>

#### hotspot\_type

"jump", "popup", "macro", "external"

<a id="winhlp.lib.internal_files.topic.HotspotMapping.target"></a>

#### target

topic offset, macro command, external file, etc.

<a id="winhlp.lib.internal_files.topic.HotspotMapping.start_position"></a>

#### start\_position

Character position in full text

<a id="winhlp.lib.internal_files.topic.ParsedTopic"></a>

## ParsedTopic Objects

```python
class ParsedTopic(BaseModel)
```

A fully parsed topic with structured content.

<a id="winhlp.lib.internal_files.topic.ParsedTopic.topic_offset"></a>

#### topic\_offset

this topic's TOPICOFFSET

<a id="winhlp.lib.internal_files.topic.ParsedTopic.non_scroll_offset"></a>

#### non\_scroll\_offset

start of scrolling region, or None

<a id="winhlp.lib.internal_files.topic.ParsedTopic.entry_macros"></a>

#### entry\_macros

macros run on entry (! footnotes)

<a id="winhlp.lib.internal_files.topic.ParsedTopic.context_names"></a>

#### context\_names

context ids resolving to this topic

<a id="winhlp.lib.internal_files.topic.ParsedTopic.keywords"></a>

#### keywords

K/A keywords attached to this topic

<a id="winhlp.lib.internal_files.topic.ParsedTopic.annotations"></a>

#### annotations

user annotation text (from a sibling .ANN file)

<a id="winhlp.lib.internal_files.topic.ParsedTopic.browse_prev_topic"></a>

#### browse\_prev\_topic

resolved browse-sequence neighbours

<a id="winhlp.lib.internal_files.topic.ParsedTopic.get_plain_text"></a>

#### get\_plain\_text

```python
def get_plain_text() -> str
```

Extract plain text content without formatting.

<a id="winhlp.lib.internal_files.topic.ParsedTopic.get_rtf_content"></a>

#### get\_rtf\_content

```python
def get_rtf_content() -> str
```

Generate RTF-formatted content with rich formatting support including tables.

<a id="winhlp.lib.internal_files.topic.ParsedTopic.get_hotspots_by_type"></a>

#### get\_hotspots\_by\_type

```python
def get_hotspots_by_type(hotspot_type: str) -> List[HotspotMapping]
```

Get all hotspots of a specific type (jump, popup, macro, external).

<a id="winhlp.lib.internal_files.topic.ParsedTopic.get_clickable_regions"></a>

#### get\_clickable\_regions

```python
def get_clickable_regions() -> List[dict]
```

Get all clickable regions with their text and targets for UI rendering.

<a id="winhlp.lib.internal_files.topic.ParsedTopic.get_hyperlinks"></a>

#### get\_hyperlinks

```python
def get_hyperlinks() -> List[str]
```

Get all hyperlink targets from this topic.

<a id="winhlp.lib.internal_files.topic.ParsedTopic.get_embedded_images"></a>

#### get\_embedded\_images

```python
def get_embedded_images() -> List[dict]
```

Get all embedded image references from this topic.

<a id="winhlp.lib.internal_files.topic.ParsedTopic.resolve_embedded_images"></a>

#### resolve\_embedded\_images

```python
def resolve_embedded_images(hlp_file) -> List[dict]
```

Resolve embedded image references to actual bitmap data.

**Arguments**:

- `hlp_file` - The HelpFile instance containing bitmap data
  

**Returns**:

  List of dictionaries with resolved image data

<a id="winhlp.lib.internal_files.topic.TopicFile"></a>

## TopicFile Objects

```python
class TopicFile(InternalFile)
```

Parses the |TOPIC file, which holds the actual help content,
including text, formatting, and links.

<a id="winhlp.lib.internal_files.topic.TopicFile.system_file"></a>

#### system\_file

To be replaced with SystemFile object

<a id="winhlp.lib.internal_files.topic.TopicFile.topic_offset"></a>

#### topic\_offset

Track TOPICOFFSET for hyperlink resolution

<a id="winhlp.lib.internal_files.topic.TopicFile.remaining_linkdata1"></a>

#### remaining\_linkdata1

LinkData1 remaining after ParagraphInfo parsing

<a id="winhlp.lib.internal_files.topic.TopicFile.scan_word"></a>

#### scan\_word

```python
@staticmethod
def scan_word(data: bytes, offset: int) -> Tuple[int, int]
```

Scan a compressed unsigned 16-bit integer.

From helpdec1.c:
If LSB is 0: value is in one byte (shift right by 1)
If LSB is 1: value is in two bytes (shift right by 1)

Returns: (value, new_offset)

<a id="winhlp.lib.internal_files.topic.TopicFile.scan_int"></a>

#### scan\_int

```python
@staticmethod
def scan_int(data: bytes, offset: int) -> Tuple[int, int]
```

Scan a compressed signed 16-bit integer.

From helpdec1.c:
If LSB is 0: value is in one byte (shift right by 1, subtract 0x40)
If LSB is 1: value is in two bytes (shift right by 1, subtract 0x4000)

Returns: (value, new_offset)

<a id="winhlp.lib.internal_files.topic.TopicFile.scan_long"></a>

#### scan\_long

```python
@staticmethod
def scan_long(data: bytes, offset: int) -> Tuple[int, int]
```

Scan a compressed 32-bit integer.

From helpdec1.c:
If LSB is 0: value is in two bytes (shift right by 1, subtract 0x4000)
If LSB is 1: value is in four bytes (shift right by 1, subtract 0x40000000)

Returns: (value, new_offset)

<a id="winhlp.lib.internal_files.topic.TopicFile.get_topic_by_number"></a>

#### get\_topic\_by\_number

```python
def get_topic_by_number(topic_number: int) -> Optional[ParsedTopic]
```

Get a parsed topic by its topic number.

<a id="winhlp.lib.internal_files.topic.TopicFile.get_all_topics"></a>

#### get\_all\_topics

```python
def get_all_topics() -> List[ParsedTopic]
```

Get all parsed topics.

<a id="winhlp.lib.internal_files.topic.TopicFile.extract_all_text"></a>

#### extract\_all\_text

```python
def extract_all_text() -> str
```

Extract all text content from all topics as plain text.

<a id="winhlp.lib.internal_files.font"></a>

# winhlp.lib.internal\_files.font

Parser for the |FONT internal file.

<a id="winhlp.lib.internal_files.font.FontHeader"></a>

## FontHeader Objects

```python
class FontHeader(BaseModel)
```

Structure at the beginning of the |FONT file.
From `helpdeco.h`: FONTHEADER

<a id="winhlp.lib.internal_files.font.OldFont"></a>

## OldFont Objects

```python
class OldFont(BaseModel)
```

Font descriptor for older HLP files.
From `helpdeco.h`: OLDFONT

<a id="winhlp.lib.internal_files.font.MVBFont"></a>

## MVBFont Objects

```python
class MVBFont(BaseModel)
```

Font descriptor for MultiMedia Viewer (MVP) files.
From `helpdeco.h`: MVBFONT

<a id="winhlp.lib.internal_files.font.MVBFont.font_name"></a>

#### font\_name

int16_t FontName

<a id="winhlp.lib.internal_files.font.MVBFont.expndtw"></a>

#### expndtw

int16_t expndtw

<a id="winhlp.lib.internal_files.font.MVBFont.style"></a>

#### style

uint16_t style

<a id="winhlp.lib.internal_files.font.MVBFont.fg_rgb"></a>

#### fg\_rgb

unsigned char FGRGB[3]

<a id="winhlp.lib.internal_files.font.MVBFont.bg_rgb"></a>

#### bg\_rgb

unsigned char BGRGB[3]

<a id="winhlp.lib.internal_files.font.MVBFont.height"></a>

#### height

int32_t Height

<a id="winhlp.lib.internal_files.font.MVBFont.mostly_zero"></a>

#### mostly\_zero

unsigned char mostlyzero[12]

<a id="winhlp.lib.internal_files.font.MVBFont.weight"></a>

#### weight

int16_t Weight

<a id="winhlp.lib.internal_files.font.MVBFont.unknown10"></a>

#### unknown10

unsigned char unknown10

<a id="winhlp.lib.internal_files.font.MVBFont.unknown11"></a>

#### unknown11

unsigned char unknown11

<a id="winhlp.lib.internal_files.font.MVBFont.italic"></a>

#### italic

unsigned char Italic

<a id="winhlp.lib.internal_files.font.MVBFont.underline"></a>

#### underline

unsigned char Underline

<a id="winhlp.lib.internal_files.font.MVBFont.strike_out"></a>

#### strike\_out

unsigned char StrikeOut

<a id="winhlp.lib.internal_files.font.MVBFont.double_underline"></a>

#### double\_underline

unsigned char DoubleUnderline

<a id="winhlp.lib.internal_files.font.MVBFont.small_caps"></a>

#### small\_caps

unsigned char SmallCaps

<a id="winhlp.lib.internal_files.font.MVBFont.unknown17"></a>

#### unknown17

unsigned char unknown17

<a id="winhlp.lib.internal_files.font.MVBFont.unknown18"></a>

#### unknown18

unsigned char unknown18

<a id="winhlp.lib.internal_files.font.MVBFont.pitch_and_family"></a>

#### pitch\_and\_family

unsigned char PitchAndFamily

<a id="winhlp.lib.internal_files.font.MVBFont.unknown20"></a>

#### unknown20

unsigned char unknown20

<a id="winhlp.lib.internal_files.font.MVBFont.charset"></a>

#### charset

unsigned char Charset

<a id="winhlp.lib.internal_files.font.MVBFont.unknown22"></a>

#### unknown22

unsigned char unknown22

<a id="winhlp.lib.internal_files.font.MVBFont.unknown23"></a>

#### unknown23

unsigned char unknown23

<a id="winhlp.lib.internal_files.font.MVBFont.unknown24"></a>

#### unknown24

unsigned char unknown24

<a id="winhlp.lib.internal_files.font.MVBFont.up"></a>

#### up

signed char up

<a id="winhlp.lib.internal_files.font.NewFont"></a>

## NewFont Objects

```python
class NewFont(BaseModel)
```

Font descriptor for newer HLP files.
From `helpdeco.h`: NEWFONT

<a id="winhlp.lib.internal_files.font.MVBStyle"></a>

## MVBStyle Objects

```python
class MVBStyle(BaseModel)
```

Character style for MultiMedia Viewer (MVP) files.
From `helpdeco.h`: MVBSTYLE

<a id="winhlp.lib.internal_files.font.MVBStyle.wStyleNum"></a>

#### wStyleNum

uint16_t StyleNum

<a id="winhlp.lib.internal_files.font.MVBStyle.wBasedOn"></a>

#### wBasedOn

uint16_t BasedOn

<a id="winhlp.lib.internal_files.font.MVBStyle.nf"></a>

#### nf

MVBFONT font

<a id="winhlp.lib.internal_files.font.MVBStyle.bReserved"></a>

#### bReserved

char unknown[35]

<a id="winhlp.lib.internal_files.font.MVBStyle.bStyleName"></a>

#### bStyleName

char StyleName[65]

<a id="winhlp.lib.internal_files.font.NewStyle"></a>

## NewStyle Objects

```python
class NewStyle(BaseModel)
```

Character style for newer HLP files.
From `helpdeco.h`: NEWSTYLE

<a id="winhlp.lib.internal_files.font.CharMapHeader"></a>

## CharMapHeader Objects

```python
class CharMapHeader(BaseModel)
```

Header for a character mapping table (*.tbl file).
From `helpdeco.h`: CHARMAPHEADER

<a id="winhlp.lib.internal_files.font.CharMapEntry"></a>

## CharMapEntry Objects

```python
class CharMapEntry(BaseModel)
```

Entry in a character mapping table.
From `helpfile.md`.

<a id="winhlp.lib.internal_files.font.FontFile"></a>

## FontFile Objects

```python
class FontFile(InternalFile)
```

Parses the |FONT file and manages the font descriptors.

<a id="winhlp.lib.internal_files.font.FontFile.get_font_attributes"></a>

#### get\_font\_attributes

```python
def get_font_attributes(font_index: Optional[int]) -> dict
```

Resolve a font-descriptor index into normalized character attributes.

Mirrors helpdeco's FontLoad (helpdeco.c:2160-2234): OLDFONT stores
bold/italic/underline/etc. as bits in a single Attributes byte and a
HalfPoints size, whereas NEWFONT/MVBFONT store each flag in its own byte,
derive bold from Weight > 500, and a size of -2 * Height.
Returns {} for an out-of-range or missing index.

<a id="winhlp.lib.internal_files.xwbtree"></a>

# winhlp.lib.internal\_files.xwbtree

Parser for the |xWBTREE internal file.

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeIndexEntry"></a>

## XWBTreeIndexEntry Objects

```python
class XWBTreeIndexEntry(BaseModel)
```

Structure for |xWBTREE index-page entries.
From helpfile.md: xWBTREEINDEXENTRY

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeLeafEntry"></a>

## XWBTreeLeafEntry Objects

```python
class XWBTreeLeafEntry(BaseModel)
```

Structure for |xWBTREE leaf-page entries.
From helpfile.md: xWBTREELEAFENTRY

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeGIDLeafEntry"></a>

## XWBTreeGIDLeafEntry Objects

```python
class XWBTreeGIDLeafEntry(BaseModel)
```

Structure for |xWBTREE leaf-page entries in Win95 GID files.
From helpfile.md: Different structure for GID files

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeGIDLeafEntry.records"></a>

#### records

List of {'file_number': int, 'topic_offset': int}

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile"></a>

## XWBTreeFile Objects

```python
class XWBTreeFile(InternalFile)
```

Parses the |xWBTREE file, which contains keyword search index.

From helpfile.md:
To locate a keyword assigned using a x-footnote (x may be A-Z, a-z), use the
|xWDATA, |xWBTREE and |xWMAP internal files. |xWBTREE tells you how often a
certain Keyword is defined in the help file.

Structure of |xWBTREE index page entries:
struct {
    STRINGZ Keyword
    short PageNumber
} xWBTREEINDEXENTRY[NEntries]

Structure of |xWBTREE leaf page entries:
struct {
    STRINGZ Keyword
    short Count             number of times keyword is referenced
    long KWDataOffset       this is the offset into |xWDATA
} xWBTREELEAFENTRY[NEntries]

For Win95 GID files, the structure is different:
struct {
    STRINGZ Keyword
    long Size               size of following record
    struct {
        long FileNumber     ?
        long TopicOffset    this is the offset into |xWDATA
    } record[Size/8]
} xWBTREELEAFENTRY[NEntries]

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile.get_keyword_info"></a>

#### get\_keyword\_info

```python
def get_keyword_info(
        keyword: str
) -> Optional[Union[XWBTreeLeafEntry, XWBTreeGIDLeafEntry]]
```

Gets keyword information by keyword string.

**Arguments**:

- `keyword` - The keyword to look up
  

**Returns**:

  Keyword entry, or None if not found

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile.get_all_keywords"></a>

#### get\_all\_keywords

```python
def get_all_keywords() -> List[str]
```

Returns a list of all keywords in the file.

**Returns**:

  List of keyword strings

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile.get_keyword_count"></a>

#### get\_keyword\_count

```python
def get_keyword_count() -> int
```

Returns the total number of keywords.

**Returns**:

  Number of keywords

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile.find_keywords_by_pattern"></a>

#### find\_keywords\_by\_pattern

```python
def find_keywords_by_pattern(pattern: str) -> List[str]
```

Find keywords matching a pattern (case insensitive).

**Arguments**:

- `pattern` - String pattern to search for
  

**Returns**:

  List of matching keyword strings

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile.get_keywords_sorted"></a>

#### get\_keywords\_sorted

```python
def get_keywords_sorted() -> List[str]
```

Get all keywords sorted alphabetically.

**Returns**:

  List of keyword strings sorted alphabetically

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile.get_topic_offsets_for_keyword"></a>

#### get\_topic\_offsets\_for\_keyword

```python
def get_topic_offsets_for_keyword(keyword: str) -> List[int]
```

Get topic offsets for a keyword (requires |xWDATA for standard format).
For GID format, returns topic offsets directly.

**Arguments**:

- `keyword` - The keyword to look up
  

**Returns**:

  List of topic offsets, empty if not found or requires |xWDATA

<a id="winhlp.lib.internal_files.xwbtree.XWBTreeFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the xWBTREE data.

**Returns**:

  Dictionary with xWBTREE statistics

<a id="winhlp.lib.internal_files.ctxomap"></a>

# winhlp.lib.internal\_files.ctxomap

Parser for the |CTXOMAP internal file.

<a id="winhlp.lib.internal_files.ctxomap.CtxoMapEntry"></a>

## CtxoMapEntry Objects

```python
class CtxoMapEntry(BaseModel)
```

Single entry in the |CTXOMAP file.
From `helpdeco.h`: CTXOMAPREC

<a id="winhlp.lib.internal_files.ctxomap.CtxoMapFile"></a>

## CtxoMapFile Objects

```python
class CtxoMapFile(InternalFile)
```

Parses the |CTXOMAP file, which contains a simple array of
MapID -> TopicOffset mappings for Windows 3.0 help files.

From `helpdec1.c` CTXOMAPDump function:
- First 2 bytes: number of entries (uint16)
- Followed by entries, each 8 bytes:
  - MapID (int32)
  - TopicOffset (int32)

<a id="winhlp.lib.internal_files.ttlbtree"></a>

# winhlp.lib.internal\_files.ttlbtree

Parser for the |TTLBTREE internal file.

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeIndexEntry"></a>

## TTLBTreeIndexEntry Objects

```python
class TTLBTreeIndexEntry(BaseModel)
```

Structure for |TTLBTREE index-page entries.
From helpfile.md: TTLBTREEINDEXENTRY

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeLeafEntry"></a>

## TTLBTreeLeafEntry Objects

```python
class TTLBTreeLeafEntry(BaseModel)
```

Structure for |TTLBTREE leaf-page entries.
From helpfile.md: TTLBTREELEAFENTRY

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile"></a>

## TTLBTreeFile Objects

```python
class TTLBTreeFile(InternalFile)
```

Parses the |TTLBTREE file, which contains topic title mappings.

From helpfile.md:
If you want to know the topic title assigned using the $-footnote, take a look
into the |TTLBTREE internal file, which contains topic titles ordered by topic
offsets in a B+ tree. (It is used by WinHelp to display the topic titles in
the search dialog).

Structure of |TTLBTREE index page entries:
struct {
    TOPICOFFSET TopicOffset
    short PageNumber
} TTLBTREEINDEXENTRY[NEntries]

Structure of |TTLBTREE leaf page entries:
struct {
    TOPICOFFSET TopicOffset
    STRINGZ TopicTitle
} TTLBTREELEAFENTRY[NEntries]

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.topic_title_map"></a>

#### topic\_title\_map

topic_offset -> topic_title

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.title_topic_map"></a>

#### title\_topic\_map

topic_title -> topic_offset

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_topic_title_for_offset"></a>

#### get\_topic\_title\_for\_offset

```python
def get_topic_title_for_offset(topic_offset: int) -> Optional[str]
```

Gets the topic title for a given topic offset.

**Arguments**:

- `topic_offset` - The topic offset to look up
  

**Returns**:

  Topic title string, or None if not found

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_topic_offset_for_title"></a>

#### get\_topic\_offset\_for\_title

```python
def get_topic_offset_for_title(topic_title: str) -> Optional[int]
```

Gets the topic offset for a given topic title.

**Arguments**:

- `topic_title` - The topic title to look up
  

**Returns**:

  Topic offset, or None if not found

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_all_topic_titles"></a>

#### get\_all\_topic\_titles

```python
def get_all_topic_titles() -> List[str]
```

Returns a list of all topic titles in the file.

**Returns**:

  List of topic title strings

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_all_topic_offsets"></a>

#### get\_all\_topic\_offsets

```python
def get_all_topic_offsets() -> List[int]
```

Returns a list of all topic offsets in the file.

**Returns**:

  List of topic offsets

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_entry_count"></a>

#### get\_entry\_count

```python
def get_entry_count() -> int
```

Returns the total number of TTLBTREE entries.

**Returns**:

  Number of entries

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.find_titles_by_pattern"></a>

#### find\_titles\_by\_pattern

```python
def find_titles_by_pattern(pattern: str) -> List[tuple]
```

Find topic titles matching a pattern (case insensitive).

**Arguments**:

- `pattern` - String pattern to search for
  

**Returns**:

  List of (topic_title, topic_offset) tuples matching the pattern

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_titles_sorted_by_offset"></a>

#### get\_titles\_sorted\_by\_offset

```python
def get_titles_sorted_by_offset() -> List[tuple]
```

Get all titles sorted by topic offset.

**Returns**:

  List of (topic_offset, topic_title) tuples sorted by offset

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_titles_sorted_alphabetically"></a>

#### get\_titles\_sorted\_alphabetically

```python
def get_titles_sorted_alphabetically() -> List[tuple]
```

Get all titles sorted alphabetically.

**Returns**:

  List of (topic_title, topic_offset) tuples sorted by title

<a id="winhlp.lib.internal_files.ttlbtree.TTLBTreeFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the TTLBTREE data.

**Returns**:

  Dictionary with TTLBTREE statistics

<a id="winhlp.lib.internal_files.xwdata"></a>

# winhlp.lib.internal\_files.xwdata

Parser for the |xWDATA internal file.

<a id="winhlp.lib.internal_files.xwdata.XWDataFile"></a>

## XWDataFile Objects

```python
class XWDataFile(InternalFile)
```

Parses the |xWDATA file, which contains topic offsets for keywords.

From helpfile.md:
The |xWDATA contains an array of topic offsets. The KWDataOffset from the
|xWBTREE tells you where to seek to in the |xWDATA file to read Count topic
offsets.

TOPICOFFSET KeywordTopicOffset[UsedSpace/4]

And the topic offset retrieved tells you which location the Keyword was
assigned to. It is -1L if the Keyword is assigned to a macro using the [MACROS]
section of HCRTF 4.0 (see description of |Rose file).

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_topic_offset"></a>

#### get\_topic\_offset

```python
def get_topic_offset(index: int) -> Optional[int]
```

Gets a topic offset by index.

**Arguments**:

- `index` - Zero-based index into the topic offset array
  

**Returns**:

  Topic offset, or None if index is out of range

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_topic_offsets_range"></a>

#### get\_topic\_offsets\_range

```python
def get_topic_offsets_range(start_offset: int, count: int) -> List[int]
```

Gets a range of topic offsets starting from a byte offset.
This is used with KWDataOffset from |xWBTREE entries.

**Arguments**:

- `start_offset` - Byte offset into the data (not index)
- `count` - Number of topic offsets to retrieve
  

**Returns**:

  List of topic offsets

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_all_topic_offsets"></a>

#### get\_all\_topic\_offsets

```python
def get_all_topic_offsets() -> List[int]
```

Returns all topic offsets in the file.

**Returns**:

  List of all topic offsets

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_topic_offset_count"></a>

#### get\_topic\_offset\_count

```python
def get_topic_offset_count() -> int
```

Returns the total number of topic offsets.

**Returns**:

  Number of topic offsets

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.is_macro_offset"></a>

#### is\_macro\_offset

```python
def is_macro_offset(topic_offset: int) -> bool
```

Checks if a topic offset represents a macro reference.

**Arguments**:

- `topic_offset` - The topic offset to check
  

**Returns**:

  True if the offset is -1 (macro reference), False otherwise

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_valid_topic_offsets"></a>

#### get\_valid\_topic\_offsets

```python
def get_valid_topic_offsets() -> List[int]
```

Returns only valid topic offsets (excludes macro references).

**Returns**:

  List of topic offsets that are not -1

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_macro_count"></a>

#### get\_macro\_count

```python
def get_macro_count() -> int
```

Returns the number of macro references (topic offsets that are -1).

**Returns**:

  Number of macro references

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.find_offset_index"></a>

#### find\_offset\_index

```python
def find_offset_index(topic_offset: int) -> List[int]
```

Find all indices where a specific topic offset appears.

**Arguments**:

- `topic_offset` - The topic offset to search for
  

**Returns**:

  List of indices where the topic offset appears

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_unique_topic_offsets"></a>

#### get\_unique\_topic\_offsets

```python
def get_unique_topic_offsets() -> List[int]
```

Returns unique topic offsets (removes duplicates).

**Returns**:

  List of unique topic offsets

<a id="winhlp.lib.internal_files.xwdata.XWDataFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the xWDATA data.

**Returns**:

  Dictionary with xWDATA statistics

<a id="winhlp.lib.internal_files.xwmap"></a>

# winhlp.lib.internal\_files.xwmap

Parser for the |xWMAP internal file.

<a id="winhlp.lib.internal_files.xwmap.XWMapEntry"></a>

## XWMapEntry Objects

```python
class XWMapEntry(BaseModel)
```

Structure for |xWMAP entries.
From helpfile.md and helldeco.h: KWMAPREC

<a id="winhlp.lib.internal_files.xwmap.XWMapEntry.keyword_number"></a>

#### keyword\_number

FirstRec - number of first keyword on leaf-page

<a id="winhlp.lib.internal_files.xwmap.XWMapEntry.page_number"></a>

#### page\_number

PageNum - B+ tree page number

<a id="winhlp.lib.internal_files.xwmap.XWMapFile"></a>

## XWMapFile Objects

```python
class XWMapFile(InternalFile)
```

Parses the |xWMAP file, which contains keyword map for faster scrolling.

From helpfile.md:
The |xWMAP contains an array that tells you where to find the n-th keyword in
the |xWBTREE. You don't need to use this file but it allows for faster
scrolling lists of alphabetically ordered Keywords. (WinHelp search dialog).

struct {
    long KeywordNumber        number of first keyword on leaf-page
    unsigned short PageNum    B+ tree page number
} xWMAP[UsedSpace/6]

From helldeco.h: KWMAPREC
typedef struct KWMAPREC {
    int32_t FirstRec;         /* index number of first keyword on leaf page */
    uint16_t PageNum;         /* page number that keywords are associated with */
} KWMAPREC;

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.keyword_page_map"></a>

#### keyword\_page\_map

keyword_number -> page_number

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_page_for_keyword_number"></a>

#### get\_page\_for\_keyword\_number

```python
def get_page_for_keyword_number(keyword_number: int) -> Optional[int]
```

Gets the B+ tree page number for a keyword number.

**Arguments**:

- `keyword_number` - The keyword number to look up
  

**Returns**:

  B+ tree page number, or None if not found

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.find_page_for_keyword_range"></a>

#### find\_page\_for\_keyword\_range

```python
def find_page_for_keyword_range(keyword_number: int) -> Optional[int]
```

Finds the appropriate page for a keyword number using range lookup.
This handles cases where the exact keyword number isn't in the map.

**Arguments**:

- `keyword_number` - The keyword number to find a page for
  

**Returns**:

  B+ tree page number, or None if no suitable page found

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_all_entries"></a>

#### get\_all\_entries

```python
def get_all_entries() -> List[XWMapEntry]
```

Returns all xWMAP entries.

**Returns**:

  List of all xWMAP entries

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_entry_count"></a>

#### get\_entry\_count

```python
def get_entry_count() -> int
```

Returns the total number of xWMAP entries.

**Returns**:

  Number of entries

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_keyword_number_range"></a>

#### get\_keyword\_number\_range

```python
def get_keyword_number_range() -> tuple
```

Gets the range of keyword numbers covered by this map.

**Returns**:

  Tuple of (min_keyword_number, max_keyword_number), or (0, 0) if empty

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_page_numbers"></a>

#### get\_page\_numbers

```python
def get_page_numbers() -> List[int]
```

Gets all unique page numbers referenced in the map.

**Returns**:

  List of unique page numbers

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_entries_for_page"></a>

#### get\_entries\_for\_page

```python
def get_entries_for_page(page_number: int) -> List[XWMapEntry]
```

Gets all entries that reference a specific page number.

**Arguments**:

- `page_number` - The page number to search for
  

**Returns**:

  List of entries referencing the page

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_entries_sorted_by_keyword_number"></a>

#### get\_entries\_sorted\_by\_keyword\_number

```python
def get_entries_sorted_by_keyword_number() -> List[XWMapEntry]
```

Gets all entries sorted by keyword number.

**Returns**:

  List of entries sorted by keyword number

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_entries_sorted_by_page_number"></a>

#### get\_entries\_sorted\_by\_page\_number

```python
def get_entries_sorted_by_page_number() -> List[XWMapEntry]
```

Gets all entries sorted by page number.

**Returns**:

  List of entries sorted by page number

<a id="winhlp.lib.internal_files.xwmap.XWMapFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the xWMAP data.

**Returns**:

  Dictionary with xWMAP statistics

<a id="winhlp.lib.internal_files.catalog"></a>

# winhlp.lib.internal\_files.catalog

Parser for the |CATALOG internal file.

<a id="winhlp.lib.internal_files.catalog.CatalogHeader"></a>

## CatalogHeader Objects

```python
class CatalogHeader(BaseModel)
```

Header for the |CATALOG file.
From `helpdeco.h`: CATALOGHEADER

<a id="winhlp.lib.internal_files.catalog.CatalogHeader.magic"></a>

#### magic

Should be 0x1111

<a id="winhlp.lib.internal_files.catalog.CatalogHeader.always8"></a>

#### always8

Should always be 8

<a id="winhlp.lib.internal_files.catalog.CatalogHeader.always4"></a>

#### always4

Should always be 4

<a id="winhlp.lib.internal_files.catalog.CatalogHeader.entries"></a>

#### entries

Number of topic entries

<a id="winhlp.lib.internal_files.catalog.CatalogHeader.zero"></a>

#### zero

30 zero bytes padding

<a id="winhlp.lib.internal_files.catalog.CatalogFile"></a>

## CatalogFile Objects

```python
class CatalogFile(InternalFile)
```

Parses the |CATALOG file, which contains sequential topic mapping.

The CATALOG file maps topic numbers (1, 2, 3...) to topic offsets.
This provides a simple sequential access mechanism for topics.

From `helpdec1.c` CatalogDump function:
- CATALOGHEADER (40 bytes): magic, always8, always4, entries, zero[30]
- Followed by entries number of 32-bit topic offsets

<a id="winhlp.lib.internal_files.gmacros"></a>

# winhlp.lib.internal\_files.gmacros

Parser for the |GMACROS internal file.

<a id="winhlp.lib.internal_files.gmacros.GMacroEntry"></a>

## GMacroEntry Objects

```python
class GMacroEntry(BaseModel)
```

Single macro entry in the |GMACROS file.
From helpdeco.c GMACROS parsing logic.

<a id="winhlp.lib.internal_files.gmacros.GMacroEntry.length"></a>

#### length

Length of the record

<a id="winhlp.lib.internal_files.gmacros.GMacroEntry.offset"></a>

#### offset

Offset of second string (exit macro)

<a id="winhlp.lib.internal_files.gmacros.GMacroEntry.entry_macro"></a>

#### entry\_macro

Entry macro string

<a id="winhlp.lib.internal_files.gmacros.GMacroEntry.exit_macro"></a>

#### exit\_macro

Exit macro string

<a id="winhlp.lib.internal_files.gmacros.GMacrosFile"></a>

## GMacrosFile Objects

```python
class GMacrosFile(InternalFile)
```

Parses the |GMACROS file, which contains global macros.

Global macros are executed when entering or exiting help contexts.

From helldeco.c parsing logic:
- First 4 bytes: count or group number
- Followed by records, each containing:
  - len (4 bytes): length of record
  - off (4 bytes): offset of second string in record
  - First string at position 8: entry macro
  - Second string at position off: exit macro

<a id="winhlp.lib.internal_files.chartab"></a>

# winhlp.lib.internal\_files.chartab

CHARTAB parser for Windows HLP files.

CHARTAB files (*.tbl) contain character mapping tables for fonts.
They are created by MediaView compilers and stored as internal files
using a specific binary structure.

Based on the helpdeco C reference implementation and documentation.

<a id="winhlp.lib.internal_files.chartab.ChartabHeader"></a>

## ChartabHeader Objects

```python
class ChartabHeader(BaseModel)
```

Header structure for CHARTAB files.

<a id="winhlp.lib.internal_files.chartab.ChartabHeader.magic"></a>

#### magic

Should be 0x5555

<a id="winhlp.lib.internal_files.chartab.ChartabHeader.unknown_fields"></a>

#### unknown\_fields

Unknown fields array

<a id="winhlp.lib.internal_files.chartab.ChartabCharEntry"></a>

## ChartabCharEntry Objects

```python
class ChartabCharEntry(BaseModel)
```

A character entry in the CHARTAB table.

<a id="winhlp.lib.internal_files.chartab.ChartabLigature"></a>

## ChartabLigature Objects

```python
class ChartabLigature(BaseModel)
```

A ligature entry in the CHARTAB table.

<a id="winhlp.lib.internal_files.chartab.ChartabFile"></a>

## ChartabFile Objects

```python
class ChartabFile(InternalFile)
```

Parses CHARTAB (Character Mapping Table) files.

From documentation:
MediaView compilers store character mapping tables listed in the [CHARTAB]
section in internal *.tbl files using the following binary structure:

struct {
    unsigned short Magic /* 0x5555 */
    unsigned short Size
    unsigned short Unknown1[2]
    unsigned short Entries
    unsigned short Ligatures
    unsigned short LigLen
    unsigned short Unknown[13]
} CHARTAB
charentry[Entries]
unsigned char Ligature[Ligatures][LigLen]

<a id="winhlp.lib.internal_files.chartab.ChartabFile.get_character_mapping"></a>

#### get\_character\_mapping

```python
def get_character_mapping(char_code: int) -> Optional[dict]
```

Get character mapping information for a given character code.

<a id="winhlp.lib.internal_files.chartab.ChartabFile.get_all_mappings"></a>

#### get\_all\_mappings

```python
def get_all_mappings() -> Dict[int, dict]
```

Get all character mappings.

<a id="winhlp.lib.internal_files.chartab.ChartabFile.has_ligatures"></a>

#### has\_ligatures

```python
def has_ligatures() -> bool
```

Check if the CHARTAB file contains ligature data.

<a id="winhlp.lib.internal_files.chartab.ChartabFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Get statistics about the CHARTAB file.

<a id="winhlp.lib.internal_files.grp"></a>

# winhlp.lib.internal\_files.grp

GRP file parser for Windows HLP files.

GRP files handle MediaView group files (.GRP) that contain group+ footnotes
assigned to topics in MediaView files. These are used for organizing topics
into groups with optional bitmaps.

Based on the helpdeco C reference implementation and documentation.

<a id="winhlp.lib.internal_files.grp.GroupHeader"></a>

## GroupHeader Objects

```python
class GroupHeader(BaseModel)
```

Header structure for GRP files.

<a id="winhlp.lib.internal_files.grp.GroupHeader.magic"></a>

#### magic

Should be 0x000A3333

<a id="winhlp.lib.internal_files.grp.GroupHeader.bitmap_size"></a>

#### bitmap\_size

max. 64000 equalling 512000 topics

<a id="winhlp.lib.internal_files.grp.GroupHeader.last_topic"></a>

#### last\_topic

first topic in help file has topic number 0

<a id="winhlp.lib.internal_files.grp.TopicRange"></a>

## TopicRange Objects

```python
class TopicRange(BaseModel)
```

A range of topics in a group.

<a id="winhlp.lib.internal_files.grp.GRPFile"></a>

## GRPFile Objects

```python
class GRPFile(InternalFile)
```

Parses GRP (MediaView Group) files.

GRP files contain group+ footnotes assigned to topics in MediaView files.
They have a specific structure with a header containing magic number 0x000A3333,
bitmap size, and topic ranges.

Structure from documentation:
- Magic: 0x000A3333
- BitmapSize: max. 64000 equalling 512000 topics
- LastTopic: first topic in help file has topic number 0
- Topic ranges and group assignments
- Optional bitmap data

<a id="winhlp.lib.internal_files.grp.GRPFile.topic_to_group"></a>

#### topic\_to\_group

Maps topic number to group ID

<a id="winhlp.lib.internal_files.grp.GRPFile.help_file"></a>

#### help\_file

circular back-ref, not serialized

<a id="winhlp.lib.internal_files.grp.GRPFile.get_group_for_topic"></a>

#### get\_group\_for\_topic

```python
def get_group_for_topic(topic_number: int) -> Optional[int]
```

Get the group ID for a given topic number.

<a id="winhlp.lib.internal_files.grp.GRPFile.get_topics_in_group"></a>

#### get\_topics\_in\_group

```python
def get_topics_in_group(group_id: int) -> List[int]
```

Get all topic numbers in a given group.

<a id="winhlp.lib.internal_files.grp.GRPFile.get_all_groups"></a>

#### get\_all\_groups

```python
def get_all_groups() -> List[int]
```

Get all group IDs in the file.

<a id="winhlp.lib.internal_files.grp.GRPFile.has_bitmap"></a>

#### has\_bitmap

```python
def has_bitmap() -> bool
```

Check if the GRP file contains bitmap data.

<a id="winhlp.lib.internal_files.grp.GRPFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Get statistics about the GRP file.

<a id="winhlp.lib.internal_files.viola"></a>

# winhlp.lib.internal\_files.viola

Parser for the |VIOLA internal file.

<a id="winhlp.lib.internal_files.viola.ViolaEntry"></a>

## ViolaEntry Objects

```python
class ViolaEntry(BaseModel)
```

Single entry in the |VIOLA file.
From `helpdeco.h`: VIOLAREC

<a id="winhlp.lib.internal_files.viola.ViolaEntry.topic_offset"></a>

#### topic\_offset

TOPICOFFSET

<a id="winhlp.lib.internal_files.viola.ViolaEntry.window_number"></a>

#### window\_number

Window number assigned to topic

<a id="winhlp.lib.internal_files.viola.ViolaFile"></a>

## ViolaFile Objects

```python
class ViolaFile(InternalFile)
```

Parses the |VIOLA file, which contains window assignments for topics.

The VIOLA file is structured as a B+ tree where leaf pages contain
VIOLAREC entries that map topic offsets to window numbers.

From helpdeco.c:
- Uses GetFirstPage/GetNextPage to iterate through B+ tree leaf pages
- Each leaf page contains n VIOLAREC entries
- Each VIOLAREC is 8 bytes: TopicOffset (4) + WindowNumber (4)

<a id="winhlp.lib.internal_files.system"></a>

# winhlp.lib.internal\_files.system

Parser for the |SYSTEM internal file.

<a id="winhlp.lib.internal_files.system.SystemHeader"></a>

## SystemHeader Objects

```python
class SystemHeader(BaseModel)
```

Structure at the beginning of the |SYSTEM file.
From `helpdeco.h`: SYSTEMHEADER

<a id="winhlp.lib.internal_files.system.SecWindow"></a>

## SecWindow Objects

```python
class SecWindow(BaseModel)
```

Structure for a secondary window definition in the |SYSTEM file.
From `helpdeco.h`: SECWINDOW

<a id="winhlp.lib.internal_files.system.KeyIndex"></a>

## KeyIndex Objects

```python
class KeyIndex(BaseModel)
```

Defines a keyword index.
From `helpdeco.h`: KEYINDEX

<a id="winhlp.lib.internal_files.system.DLLMaps"></a>

## DLLMaps Objects

```python
class DLLMaps(BaseModel)
```

Defines mappings for 16-bit and 32-bit DLLs.
From `helpfile.md`.

<a id="winhlp.lib.internal_files.system.DefFont"></a>

## DefFont Objects

```python
class DefFont(BaseModel)
```

Default dialog font, Windows 95 (HCW 4.00)
From `helpfile.md`.

<a id="winhlp.lib.internal_files.system.SystemFile"></a>

## SystemFile Objects

```python
class SystemFile(InternalFile)
```

Parses the |SYSTEM file, which contains crucial metadata about the
help file's version, compression, and configuration.

<a id="winhlp.lib.internal_files.system.SystemFile.encoding"></a>

#### encoding

Default Windows Western European

<a id="winhlp.lib.internal_files.system.SystemFile.icon"></a>

#### icon

Type 5: ICON file data

<a id="winhlp.lib.internal_files.system.SystemFile.cnt_filename"></a>

#### cnt\_filename

Type 10: CNT filename

<a id="winhlp.lib.internal_files.system.SystemFile.groups"></a>

#### groups

Type 13: GROUPS definitions

<a id="winhlp.lib.internal_files.system.SystemFile.dllmaps"></a>

#### dllmaps

Type 19: DLLMAPS definitions

<a id="winhlp.lib.internal_files.system.SystemFile.keyword_indices"></a>

#### keyword\_indices

Characters that have keyword index files (from type 14 records)

<a id="winhlp.lib.internal_files.system.SystemFile.is_mvp"></a>

#### is\_mvp

Is this a MultiMedia Viewer file?

<a id="winhlp.lib.internal_files"></a>

# winhlp.lib.internal\_files

winhlp.lib.internal_files - Internal file parsers

Parsers for the various internal files within HLP files.

<a id="winhlp.lib.internal_files.bitmap"></a>

# winhlp.lib.internal\_files.bitmap

Parser for bitmap files (|bmN internal files).

<a id="winhlp.lib.internal_files.bitmap.HotspotInfo"></a>

## HotspotInfo Objects

```python
class HotspotInfo(BaseModel)
```

Structure for hotspot information within bitmaps.
From helpdeco.h: HOTSPOT

<a id="winhlp.lib.internal_files.bitmap.BitmapHeader"></a>

## BitmapHeader Objects

```python
class BitmapHeader(BaseModel)
```

Structure for bitmap file headers.
Based on the C code analysis.

<a id="winhlp.lib.internal_files.bitmap.ExtractedBitmap"></a>

## ExtractedBitmap Objects

```python
class ExtractedBitmap(BaseModel)
```

Represents an extracted bitmap with its data and metadata.

<a id="winhlp.lib.internal_files.bitmap.ExtractedBitmap.format_type"></a>

#### format\_type

"bmp", "wmf", "shg", etc.

<a id="winhlp.lib.internal_files.bitmap.BitmapFile"></a>

## BitmapFile Objects

```python
class BitmapFile(InternalFile)
```

Parses bitmap files (|bm0, |bm1, etc.) which contain images and hotspot data.

Based on the analysis of helpdeco.c bitmap extraction code.

<a id="winhlp.lib.internal_files.bitmap.BitmapFile.extract_bitmap_as_bmp"></a>

#### extract\_bitmap\_as\_bmp

```python
def extract_bitmap_as_bmp(bitmap_index: int = 0) -> Optional[bytes]
```

Extracts a bitmap as a standard Windows BMP file.
Returns the complete BMP file data including headers.

<a id="winhlp.lib.internal_files.bitmap.BitmapFile.extract_image"></a>

#### extract\_image

```python
def extract_image(bitmap_index: int = 0) -> Optional[tuple]
```

Extract a picture as (extension, bytes), for any picture type.

Bitmaps (DDB/DIB) are wrapped as a standard .bmp; metafiles (type 8) are
returned as raw .wmf metafile bytes. helpdeco writes a placeable-metafile
header for WMFs, but the bare metafile record stream is the portable form
and is what the decompressed picture data already contains.
Returns None if the index is out of range.

<a id="winhlp.lib.internal_files.bitmap.BitmapFile.get_hotspot_context_names"></a>

#### get\_hotspot\_context\_names

```python
def get_hotspot_context_names() -> Dict[int, str]
```

Gets context names for all hotspots using reverse hashing.
Returns a dictionary mapping hotspot hash values to context names.

<a id="winhlp.lib.internal_files.rose"></a>

# winhlp.lib.internal\_files.rose

Parser for the |Rose internal file.

<a id="winhlp.lib.internal_files.rose.RoseIndexEntry"></a>

## RoseIndexEntry Objects

```python
class RoseIndexEntry(BaseModel)
```

Structure for |Rose index-page entries.
From helpfile.md: RoseINDEXENTRY

<a id="winhlp.lib.internal_files.rose.RoseLeafEntry"></a>

## RoseLeafEntry Objects

```python
class RoseLeafEntry(BaseModel)
```

Structure for |Rose leaf-page entries.
From helpfile.md: RoseLEAFENTRY

<a id="winhlp.lib.internal_files.rose.RoseLeafEntry.topic_title"></a>

#### topic\_title

Display string for search dialog

<a id="winhlp.lib.internal_files.rose.RoseFile"></a>

## RoseFile Objects

```python
class RoseFile(InternalFile)
```

Parses the |Rose file, which contains macro definitions from [MACROS] section.

From helpfile.md:
The |Rose internal file contains all definitions from the [MACROS] section of a
Windows 95 (HCW 4.00) help project file. It is built using a B+ tree. Keywords
only appear using hash values but are listed in the |KWBTREE with a TopicPos in
the associated |KWDATA array of -1L.

Structure of |Rose index page entries:
struct {
    long KeywordHash
    short PageNumber
} RoseINDEXENTRY[NEntries]

Structure of |Rose leaf page entries:
struct {
    long KeywordHash
    STRINGZ Macro
    STRINGZ TopicTitle      not a real topic title but the string
                           displayed in the search dialog where
                           normally topic titles are listed
} RoseLEAFENTRY[NEntries]

<a id="winhlp.lib.internal_files.rose.RoseFile.macro_map"></a>

#### macro\_map

keyword_hash -> RoseLeafEntry

<a id="winhlp.lib.internal_files.rose.RoseFile.get_macro_by_hash"></a>

#### get\_macro\_by\_hash

```python
def get_macro_by_hash(keyword_hash: int) -> Optional[RoseLeafEntry]
```

Gets a macro entry by its keyword hash.

**Arguments**:

- `keyword_hash` - The keyword hash to look up
  

**Returns**:

  Rose entry, or None if not found

<a id="winhlp.lib.internal_files.rose.RoseFile.get_macro_string_by_hash"></a>

#### get\_macro\_string\_by\_hash

```python
def get_macro_string_by_hash(keyword_hash: int) -> Optional[str]
```

Gets just the macro string by its keyword hash.

**Arguments**:

- `keyword_hash` - The keyword hash to look up
  

**Returns**:

  Macro string, or None if not found

<a id="winhlp.lib.internal_files.rose.RoseFile.get_all_keyword_hashes"></a>

#### get\_all\_keyword\_hashes

```python
def get_all_keyword_hashes() -> List[int]
```

Returns a list of all keyword hashes in the file.

**Returns**:

  List of keyword hash values

<a id="winhlp.lib.internal_files.rose.RoseFile.get_all_macros"></a>

#### get\_all\_macros

```python
def get_all_macros() -> List[str]
```

Returns a list of all macro strings in the file.

**Returns**:

  List of macro strings

<a id="winhlp.lib.internal_files.rose.RoseFile.get_all_entries"></a>

#### get\_all\_entries

```python
def get_all_entries() -> List[RoseLeafEntry]
```

Returns all Rose entries.

**Returns**:

  List of all Rose entries

<a id="winhlp.lib.internal_files.rose.RoseFile.get_entry_count"></a>

#### get\_entry\_count

```python
def get_entry_count() -> int
```

Returns the total number of Rose entries.

**Returns**:

  Number of entries

<a id="winhlp.lib.internal_files.rose.RoseFile.find_macros_by_pattern"></a>

#### find\_macros\_by\_pattern

```python
def find_macros_by_pattern(pattern: str) -> List[RoseLeafEntry]
```

Find macro entries where the macro string contains a pattern (case insensitive).

**Arguments**:

- `pattern` - String pattern to search for
  

**Returns**:

  List of Rose entries matching the pattern

<a id="winhlp.lib.internal_files.rose.RoseFile.find_by_topic_title_pattern"></a>

#### find\_by\_topic\_title\_pattern

```python
def find_by_topic_title_pattern(pattern: str) -> List[RoseLeafEntry]
```

Find macro entries where the topic title contains a pattern (case insensitive).

**Arguments**:

- `pattern` - String pattern to search for
  

**Returns**:

  List of Rose entries matching the pattern

<a id="winhlp.lib.internal_files.rose.RoseFile.get_entries_sorted_by_hash"></a>

#### get\_entries\_sorted\_by\_hash

```python
def get_entries_sorted_by_hash() -> List[RoseLeafEntry]
```

Get all entries sorted by keyword hash.

**Returns**:

  List of entries sorted by keyword hash

<a id="winhlp.lib.internal_files.rose.RoseFile.get_entries_sorted_by_macro"></a>

#### get\_entries\_sorted\_by\_macro

```python
def get_entries_sorted_by_macro() -> List[RoseLeafEntry]
```

Get all entries sorted alphabetically by macro string.

**Returns**:

  List of entries sorted by macro string

<a id="winhlp.lib.internal_files.rose.RoseFile.get_entries_sorted_by_topic_title"></a>

#### get\_entries\_sorted\_by\_topic\_title

```python
def get_entries_sorted_by_topic_title() -> List[RoseLeafEntry]
```

Get all entries sorted alphabetically by topic title.

**Returns**:

  List of entries sorted by topic title

<a id="winhlp.lib.internal_files.rose.RoseFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the Rose data.

**Returns**:

  Dictionary with Rose statistics

<a id="winhlp.lib.internal_files.phrimage"></a>

# winhlp.lib.internal\_files.phrimage

Parser for the |PhrImage internal file.

<a id="winhlp.lib.internal_files.phrimage.PhrImageFile"></a>

## PhrImageFile Objects

```python
class PhrImageFile(InternalFile)
```

Parses the |PhrImage file, which contains phrase strings for Hall compression.

Based on helldeco.c PhraseLoad function:
The |PhrImage file stores the actual phrase strings used in Hall compression.
It works with |PhrIndex to provide phrase compression in Windows 95 help files.

From helpfile.md:
The |PhrImage file stores the phrases. A phrase is not NUL-terminated. Use
PhraseOffset[NumPhrase] and PhraseOffset[NumPhrase+1] to locate beginning
and end of the phrase string. |PhrImage is LZ77 compressed if
PhrImageCompressedSize is not equal to PhrImageSize.

<a id="winhlp.lib.internal_files.phrimage.PhrImageFile.get_phrase"></a>

#### get\_phrase

```python
def get_phrase(phrase_number: int) -> Optional[str]
```

Gets a phrase by its number.

**Arguments**:

- `phrase_number` - Zero-based phrase index
  

**Returns**:

  The phrase string, or None if not found

<a id="winhlp.lib.internal_files.phrimage.PhrImageFile.get_phrase_count"></a>

#### get\_phrase\_count

```python
def get_phrase_count() -> int
```

Returns the total number of phrases stored.

<a id="winhlp.lib.internal_files.phrimage.PhrImageFile.get_raw_phrase_data"></a>

#### get\_raw\_phrase\_data

```python
def get_raw_phrase_data(start_offset: int, end_offset: int) -> bytes
```

Gets raw phrase data between two offsets.

**Arguments**:

- `start_offset` - Starting byte offset in decompressed data
- `end_offset` - Ending byte offset in decompressed data
  

**Returns**:

  Raw phrase bytes, or empty bytes if invalid range

<a id="winhlp.lib.internal_files.phrimage.PhrImageFile.decode_phrase_bytes"></a>

#### decode\_phrase\_bytes

```python
def decode_phrase_bytes(phrase_bytes: bytes) -> str
```

Decode phrase bytes to string using appropriate encoding.

**Arguments**:

- `phrase_bytes` - Raw phrase bytes
  

**Returns**:

  Decoded phrase string

<a id="winhlp.lib.internal_files.phrimage.PhrImageFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> dict
```

Returns statistics about the phrase data.

**Returns**:

  Dictionary with phrase statistics

<a id="winhlp.lib.ann"></a>

# winhlp.lib.ann

Parser for Windows Help Annotation (.ANN) files.

Based on helpfile.md documentation:
"An annotation file created by WinHelp uses the same basic file format as
a Windows help file. The first 16 bytes contain the same header as a help
file, with same Magic."

ANN files contain user annotations for help topics and follow this structure:
- @VERSION: Contains version info (0x08 0x62 0x6D 0x66 0x01 0x00)
- @LINK: Contains number of annotations and TOPICOFFSET for each annotation
- n!0: Individual annotation text files (e.g., "12345!0") containing plain ANSI text

<a id="winhlp.lib.ann.AnnotationReference"></a>

## AnnotationReference Objects

```python
class AnnotationReference(BaseModel)
```

Reference to an annotation in the @LINK file.

<a id="winhlp.lib.ann.AnnotationReference.unknown1"></a>

#### unknown1

always 0 according to docs

<a id="winhlp.lib.ann.AnnotationReference.unknown2"></a>

#### unknown2

always 0 according to docs

<a id="winhlp.lib.ann.VersionFile"></a>

## VersionFile Objects

```python
class VersionFile(InternalFile)
```

Parser for @VERSION internal file in ANN files.

<a id="winhlp.lib.ann.LinkFile"></a>

## LinkFile Objects

```python
class LinkFile(InternalFile)
```

Parser for @LINK internal file in ANN files.

<a id="winhlp.lib.ann.AnnotationTextFile"></a>

## AnnotationTextFile Objects

```python
class AnnotationTextFile(InternalFile)
```

Parser for individual annotation text files (e.g., "12345!0").

<a id="winhlp.lib.ann.AnnotationFile"></a>

## AnnotationFile Objects

```python
class AnnotationFile()
```

Parser for Windows Help Annotation (.ANN) files.

ANN files use the same basic file format as Windows help files but contain
user annotations for help topics instead of help content.

<a id="winhlp.lib.ann.AnnotationFile.__init__"></a>

#### \_\_init\_\_

```python
def __init__(filepath: str)
```

Initialize ANN file parser.

**Arguments**:

- `filepath` - Path to the .ANN annotation file

<a id="winhlp.lib.ann.AnnotationFile.get_annotations"></a>

#### get\_annotations

```python
def get_annotations() -> List[Dict]
```

Get all annotations with their topic offsets and text.

**Returns**:

  List of annotation dictionaries with 'topic_offset' and 'text' keys

<a id="winhlp.lib.ann.AnnotationFile.get_annotation_for_topic"></a>

#### get\_annotation\_for\_topic

```python
def get_annotation_for_topic(topic_offset: int) -> Optional[str]
```

Get annotation text for a specific topic offset.

**Arguments**:

- `topic_offset` - The topic offset to look up
  

**Returns**:

  Annotation text or None if not found

<a id="winhlp.lib.ann.AnnotationFile.get_statistics"></a>

#### get\_statistics

```python
def get_statistics() -> Dict
```

Get statistics about the annotation file.

**Returns**:

  Dictionary with annotation file statistics

<a id="winhlp.lib.compression"></a>

# winhlp.lib.compression

Decompression algorithms for HLP files.

<a id="winhlp.lib.compression.lz77_decompress"></a>

#### lz77\_decompress

```python
def lz77_decompress(data: bytes) -> bytes
```

Decompresses LZ77 compressed data from a HLP file.

Optimized implementation based on helldec1.c from helpdeco.
Uses circular buffer and efficient bit processing like the C version.

<a id="winhlp.lib.compression.phrase_decompress"></a>

#### phrase\_decompress

```python
def phrase_decompress(data: bytes, phrases: List[str]) -> bytes
```

Decompresses phrase-compressed data.

From helpfile.md:
Take the next character. If it's value is 0 or above 15 emit it. Else
multiply it with 256, subtract 256 and add the value of the next character.
Divide by 2 to get the phrase number. Emit the phrase from the |Phrase file
and append a space if the division had a remainder (the number was odd).

<a id="winhlp.lib.compression.hall_decompress"></a>

#### hall\_decompress

```python
def hall_decompress(data: bytes, phrases: List[str]) -> bytes
```

Decompresses Hall-compressed data (Windows 95 HCW 4.00).

From helpfile.md:
Take the next character (ch). If ch is even emit the phrase number ch/2.
Else if the least two bits are 01 multiply by 64, add 64 and the value of
the next character. Emit the Phrase using this number. If the least three
bits are 011 copy the next ch/8+1 characters. If the least four bits are
0111 emit ch/16+1 spaces. If the least four bits are 1111 emit ch/16+1 NUL's.

<a id="winhlp.lib.compression.runlen_decompress"></a>

#### runlen\_decompress

```python
def runlen_decompress(data: bytes) -> bytes
```

Decompresses run-length compressed data.

Based on helpdeco's DeRun function. The algorithm works with a global
count variable that tracks run-length state:
- If count & 0x7F is non-zero, we're in a run
- If count & 0x80 is set, emit characters one by one
- Otherwise emit the full run at once
- When count reaches 0, read next signed byte as new count

From C code:
signed char count; /* for run len decompression */
count = (signed char)c;

<a id="winhlp.lib.compression.decompress"></a>

#### decompress

```python
def decompress(method: int, data: bytes, phrases: List[str] = None) -> bytes
```

Decompresses data using the specified method, matching helpdeco's approach.

Method values:
- 0: copy (no decompression)
- 1: runlen decompression
- 2: LZ77 decompression
- 3: runlen and LZ77 decompression

<a id="winhlp.lib.directory"></a>

# winhlp.lib.directory

Parses the internal file directory of a HLP file.

<a id="winhlp.lib.directory.FileHeader"></a>

## FileHeader Objects

```python
class FileHeader(BaseModel)
```

Structure at the start of each internal file.
From `helpdeco.h`: FILEHEADER

<a id="winhlp.lib.directory.DirectoryLeafEntry"></a>

## DirectoryLeafEntry Objects

```python
class DirectoryLeafEntry(BaseModel)
```

The structure of directory leaf-pages.

From `helpfile.md`:
struct
{
    STRINGZ FileName     varying length NUL-terminated string
    long FileOffset      offset of FILEHEADER of internal file FileName
                         relative to beginning of help file
}
DIRECTORYLEAFENTRY[NEntries]

<a id="winhlp.lib.directory.Directory"></a>

## Directory Objects

```python
class Directory(BaseModel)
```

The internal directory which is used to associate FileNames and FileOffsets.
The directory is structured as a B+ tree.

<a id="winhlp.lib"></a>

# winhlp.lib

winhlp.lib - Core library components

Internal modules for parsing HLP file structures.

