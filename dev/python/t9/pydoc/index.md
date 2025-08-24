<a id="t9"></a>

# t9

Import from those modules directly or use the main package imports.

<a id="t9.makepy9"></a>

# t9.makepy9

Py9.py - a predictive text dictionary in the style of Nokia's T9

File Format...
  Header:
    String[7]     = "PY9DICT:"
    Unsigned Long = Number of words
    Unsigned Long = root node's start position

  Node block:
    Unsigned Long[4] =

<a id="t9.utils"></a>

# t9.utils

Utility functions for PY9 T9 text input system.

<a id="t9.utils.getkey"></a>

#### getkey

```python
def getkey(word)
```

Convert a word to T9 keypress sequence.

Example: "hello" -> "43556"

<a id="t9.utils.get_wordlists_dir"></a>

#### get\_wordlists\_dir

```python
def get_wordlists_dir()
```

Get the path to the wordlists directory.

<a id="t9.utils.draw_keypad"></a>

#### draw\_keypad

```python
def draw_keypad()
```

Draw a T9 keypad layout for reference.

<a id="t9.maket9"></a>

# t9.maket9

T9.py - a predictive text dictionary in the style of Nokia's T9

File Format...
  Header:
    String[7]     = "PY9DICT:"
    Unsigned Long = Number of words
    Unsigned Long = root node's start position

  Node block:
    Unsigned Long[4] =

<a id="t9.demo"></a>

# t9.demo

T9 demo application.

<a id="t9.demo.clear_screen"></a>

#### clear\_screen

```python
def clear_screen()
```

Clear the terminal screen.

<a id="t9.demo.get_input"></a>

#### get\_input

```python
def get_input()
```

Get a single character input, handling different platforms.

<a id="t9.demo.handle_input"></a>

#### handle\_input

```python
def handle_input(char, input_obj)
```

Handle input character and return True if should exit.

<a id="t9.demo.draw_screen"></a>

#### draw\_screen

```python
def draw_screen(input_obj)
```

Draw the complete T9 interface screen.

<a id="t9.demo.run_demo"></a>

#### run\_demo

```python
def run_demo(dict_file=None)
```

Run the T9 demo application.

<a id="t9.key"></a>

# t9.key

Dictionary node class for PY9 T9 text input system.

<a id="t9.key.SaveState"></a>

## SaveState Objects

```python
class SaveState(IntEnum)
```

Node save state for dictionary file operations.

<a id="t9.key.SaveState.UNCHANGED"></a>

#### UNCHANGED

Node doesn't need any file operation

<a id="t9.key.SaveState.UPDATE"></a>

#### UPDATE

Existing node needs reference update

<a id="t9.key.SaveState.NEW"></a>

#### NEW

New node needs full save to file

<a id="t9.key.T9Key"></a>

## T9Key Objects

```python
class T9Key()
```

Dictionary node for file-based keypress dictionary storage.

<a id="t9.key.T9Key.save"></a>

#### save

```python
def save(f)
```

Save the node and all child nodes to file f.
Used when creating dictionary file.

<a id="t9.key.T9Key.savenode"></a>

#### savenode

```python
def savenode(f)
```

Save just this node to the file.
Used to add or overwrite a node.

<a id="t9.key.T9Key.loadnode"></a>

#### loadnode

```python
def loadnode(f)
```

Load a node from an open file object.

<a id="t9.mode"></a>

# t9.mode

Input modes for PY9 T9 text input system.

<a id="t9.mode.InputMode"></a>

## InputMode Objects

```python
class InputMode(IntEnum)
```

Available input modes.

<a id="t9.mode.InputMode.NAVIGATE"></a>

#### NAVIGATE

Navigate/predictive mode

<a id="t9.mode.InputMode.EDIT_WORD"></a>

#### EDIT\_WORD

Edit complete word mode

<a id="t9.mode.InputMode.EDIT_CHAR"></a>

#### EDIT\_CHAR

Edit individual characters mode

<a id="t9.mode.InputMode.TEXT_LOWER"></a>

#### TEXT\_LOWER

Lowercase text entry mode

<a id="t9.mode.InputMode.TEXT_UPPER"></a>

#### TEXT\_UPPER

Uppercase text entry mode

<a id="t9.mode.InputMode.NUMERIC"></a>

#### NUMERIC

Numeric entry mode

<a id="t9.mode.get_label"></a>

#### get\_label

```python
def get_label(mode)
```

Get the display label for a mode.

<a id="t9.mode.get_help"></a>

#### get\_help

```python
def get_help(mode)
```

Get the key help text for a mode.

<a id="t9.cli"></a>

# t9.cli

Command-line interface for PY9 T9 text input system.

<a id="t9.cli.run_demo"></a>

#### run\_demo

```python
def run_demo(dict_file=None)
```

Run the T9 demo application.

<a id="t9.cli.generate_dict"></a>

#### generate\_dict

```python
def generate_dict(wordlist, output, language="Unknown", comment="")
```

Generate a T9 dictionary from a wordlist file.

<a id="t9.cli.main"></a>

#### main

```python
def main()
```

Main CLI entry point.

<a id="t9.dict"></a>

# t9.dict

Dictionary class for PY9 T9 text input system.

<a id="t9.dict.T9Dict"></a>

## T9Dict Objects

```python
class T9Dict()
```

T9 dictionary for word lookups and modifications.

<a id="t9.dict.T9Dict.__init__"></a>

#### \_\_init\_\_

```python
def __init__(dict_file)
```

Create a T9 dictionary class and load file header info.

dict_file: path to dictionary file

File format:
- word count (4 bytes)
- root node pos (4 bytes)
- language string (variable)
- comment string (variable)

<a id="t9.dict.T9Dict.getwords"></a>

#### getwords

```python
def getwords(digits)
```

Get possible words for a T9 digit sequence.

**Returns**:

  - If len(result[0]) == len(digits): exact match found
  - If len(result[0]) > len(digits): lookahead used
  - If len(result[0]) < len(digits): lookbehind used

<a id="t9.dict.T9Dict.addword"></a>

#### addword

```python
def addword(word)
```

Add a word to the dictionary.
Raises KeyError if word already exists.

<a id="t9.dict.T9Dict.delword"></a>

#### delword

```python
def delword(word)
```

Delete a word from the dictionary.
Not implemented yet.

<a id="t9.input"></a>

# t9.input

Input parser class for PY9 T9 text input system.

<a id="t9.input.T9Input"></a>

## T9Input Objects

```python
class T9Input()
```

T9 input parser that handles keypresses and text manipulation.

Send keypresses with sendkeys(), retrieve display text with gettext(),
get raw text with text().

<a id="t9.input.T9Input.__init__"></a>

#### \_\_init\_\_

```python
def __init__(dict_file,
             defaulttxt="",
             defaultmode=0,
             keydelay=0.5,
             numeric=False)
```

Create a new input parser.

dict_file: dictionary file name
defaulttxt: text to start with
defaultmode: mode to start in (NAVIGATE=Predictive, TEXT_LOWER, TEXT_UPPER, NUMERIC)
keydelay: key timeout in TXT mode
numeric: NOT IMPLEMENTED YET

<a id="t9.input.T9Input.gettext"></a>

#### gettext

```python
def gettext()
```

Get current text including cursor for display.
For raw text use .text()

<a id="t9.input.T9Input.text"></a>

#### text

```python
def text()
```

Get text buffer without cursor.

<a id="t9.input.T9Input.posword"></a>

#### posword

```python
def posword()
```

Get word with position marker.

<a id="t9.input.T9Input.setword"></a>

#### setword

```python
def setword()
```

Change current word to first valid match.

<a id="t9.input.T9Input.nextword"></a>

#### nextword

```python
def nextword()
```

In edit mode 1, move to next word if possible.

<a id="t9.input.T9Input.nextchar"></a>

#### nextchar

```python
def nextchar()
```

In edit mode 2, select next letter in the group.

<a id="t9.input.T9Input.addkeypress"></a>

#### addkeypress

```python
def addkeypress(key)
```

Add a keypress to current input.

<a id="t9.input.T9Input.sendkeys"></a>

#### sendkeys

```python
def sendkeys(keys)
```

Send action keys (0-9, U/D/L/R/S).

UDLRS = UP, DOWN, LEFT, RIGHT, SELECT

Navigation mode:
    0-9: start new word
    ULR: navigate cursor
    D: backspace
    S: switch to text mode

Edit mode (1+2):
    0-9: append keystroke
    Complete word (mode 1):
        LR: accept word
        U: change word
        D: backspace
        S: character edit mode
    Incomplete word (mode 2):
        L: back letter
        R: confirm letter
        U: change letter
        D: delete char
        S: change case

Text modes (3+4):
    0-9: character input
    ULR: navigate
    D: backspace
    S: cycle modes

Number mode (5):
    0-9: numbers
    ULR: navigate
    D: backspace
    S: back to navigation

<a id="t9.constants"></a>

# t9.constants

Constants for PY9 T9 text input system.

<a id="t9.constants.Key"></a>

## Key Objects

```python
class Key(Enum)
```

T9 input keys - string values match the actual key characters used.

<a id="t9.constants.Key.SELECT"></a>

#### SELECT

Mode switch/Select

<a id="t9.constants.Key.UP"></a>

#### UP

Up/Previous word

<a id="t9.constants.Key.DOWN"></a>

#### DOWN

Down/Delete/Backspace

<a id="t9.constants.Key.LEFT"></a>

#### LEFT

Left/Back

<a id="t9.constants.Key.RIGHT"></a>

#### RIGHT

Right/Forward

