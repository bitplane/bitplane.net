<a id="vwc"></a>

# vwc

<a id="vwc.wc.wc"></a>

# vwc.wc.wc

Base class for word count (wc) implementations.
This is the base UNIX implementation.

<a id="vwc.wc.wc.WC"></a>

## WC Objects

```python
class WC()
```

Usage: wc [-cmlwL] [FILE]...

Count lines, words, and bytes for FILEs (or stdin)

<a id="vwc.wc.wc.WC.create_parser"></a>

#### create\_parser

```python
def create_parser() -> argparse.ArgumentParser
```

Create a basic argument parser with core options.

<a id="vwc.wc.wc.WC.add_platform_args"></a>

#### add\_platform\_args

```python
def add_platform_args(parser)
```

Add platform-specific arguments - overridden by subclasses

<a id="vwc.wc.wc.WC.parse_args"></a>

#### parse\_args

```python
def parse_args(argv)
```

Parse command line arguments

<a id="vwc.wc.wc.WC.get_display_width"></a>

#### get\_display\_width

```python
def get_display_width(text)
```

Calculate the display width of text according to POSIX rules.

<a id="vwc.wc.wc.WC.reset_counts"></a>

#### reset\_counts

```python
def reset_counts()
```

Reset file-specific counts.

<a id="vwc.wc.wc.WC.reset_totals"></a>

#### reset\_totals

```python
def reset_totals()
```

Reset total counts.

<a id="vwc.wc.wc.WC.process_line"></a>

#### process\_line

```python
def process_line(line)
```

Process a single line and update instance state.

<a id="vwc.wc.wc.WC.get_counts_array"></a>

#### get\_counts\_array

```python
def get_counts_array(use_totals=False)
```

Get current counts as an array in the standard order.

<a id="vwc.wc.wc.WC.print_line"></a>

#### print\_line

```python
def print_line(counts, filename, file=sys.stdout)
```

Format and print count line for a file, totals or preview.

<a id="vwc.wc.wc.WC.print_totals"></a>

#### print\_totals

```python
def print_totals(file=sys.stdout)
```

Print total counts.

<a id="vwc.wc.wc.WC.print_counts"></a>

#### print\_counts

```python
def print_counts(filename, file=sys.stdout)
```

Print counts for the current file.

<a id="vwc.wc.wc.WC.print_progress"></a>

#### print\_progress

```python
def print_progress(filename)
```

Show progress to stderr if it's a TTY.

<a id="vwc.wc.wc.WC.handle_error"></a>

#### handle\_error

```python
def handle_error(error, filename)
```

Handle file error and report it.

<a id="vwc.wc.wc.WC.set_status"></a>

#### set\_status

```python
def set_status(code)
```

Set the exit status - generic implementation.

<a id="vwc.wc.wc.WC.get_file_names"></a>

#### get\_file\_names

```python
def get_file_names()
```

Files to process, can be overriden

<a id="vwc.wc.wc.WC.get_files"></a>

#### get\_files

```python
def get_files()
```

Get file objects to process based on arguments as a generator.

<a id="vwc.wc.wc.WC.run"></a>

#### run

```python
def run()
```

Process files and print counts.

<a id="vwc.wc.wc.WC.update_totals"></a>

#### update\_totals

```python
def update_totals()
```

Update total counts from current file counts.

<a id="vwc.wc.wc.WC.process_file"></a>

#### process\_file

```python
def process_file(filename, file_obj)
```

Process a file and update instance state.

<a id="vwc.wc"></a>

# vwc.wc

<a id="vwc.wc.get_wc"></a>

#### get\_wc

```python
def get_wc() -> WC
```

Get the appropriate platform implementation by checking the $PATH.

We don't use subprocess in here because the project will be flagged as unsafe
by security tools. Which is fair.

<a id="vwc.wc.linux"></a>

# vwc.wc.linux

<a id="vwc.wc.linux.Linux"></a>

## Linux Objects

```python
class Linux(WC)
```

Shared base class for BusyBox and GNU, since they have similar
implementations.

<a id="vwc.wc.linux.Linux.get_file"></a>

#### get\_file

```python
def get_file(filename)
```

Open a file for reading.
In Linux, '-' is treated as a regular file name.

<a id="vwc.wc.linux.Linux.handle_error"></a>

#### handle\_error

```python
def handle_error(error, filename)
```

In Linux, print the counts on directories.

<a id="vwc.wc.busybox"></a>

# vwc.wc.busybox

<a id="vwc.wc.busybox.BusyBox"></a>

## BusyBox Objects

```python
class BusyBox(Linux)
```

wc - word, line, and byte count

Usage: wc [-cmlwL] [FILE]...

Count lines, words, and bytes for FILEs (or stdin)

<a id="vwc.wc.busybox.BusyBox.add_platform_args"></a>

#### add\_platform\_args

```python
def add_platform_args(parser)
```

BusyBox-specific arguments.

<a id="vwc.wc.busybox.BusyBox.print_line"></a>

#### print\_line

```python
def print_line(counts, filename, file=sys.stdout)
```

Format and print count line for a file with BusyBox formatting.

<a id="vwc.wc.busybox.BusyBox.use_padding"></a>

#### use\_padding

```python
def use_padding()
```

BusyBox-specific padding rules.
BusyBox uses padding for -L only when processing multiple files.

<a id="vwc.wc.gnu"></a>

# vwc.wc.gnu

<a id="vwc.wc.gnu.GNU"></a>

## GNU Objects

```python
class GNU(Linux)
```

wc - print newline, word, and byte counts for each file

Usage: wc [OPTION]... [FILE]...
or: wc [OPTION]... --files0-from=F

Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified. A word is a non-zero-length sequence of
characters delimited by white space.

With no FILE, or when FILE is -, read standard input.

<a id="vwc.wc.gnu.GNU.add_platform_args"></a>

#### add\_platform\_args

```python
def add_platform_args(parser)
```

GNU-specific arguments.

<a id="vwc.wc.gnu.GNU.get_file_names"></a>

#### get\_file\_names

```python
def get_file_names()
```

Return list of file names from --files0-from or args.files.

<a id="vwc.wc.gnu.GNU.print_totals"></a>

#### print\_totals

```python
def print_totals(file=sys.stdout)
```

Print total counts.

<a id="vwc.wc.gnu.GNU.print_counts"></a>

#### print\_counts

```python
def print_counts(filename, file=sys.stdout)
```

Print counts for a file.

<a id="vwc.wc.gnu.GNU.print_line"></a>

#### print\_line

```python
def print_line(counts, filename, file=sys.stdout)
```

GNU-specific line printing using width.

<a id="vwc.wc.gnu.GNU.set_column_width"></a>

#### set\_column\_width

```python
def set_column_width(filenames)
```

Do the same as compute_number_width in GNU's wc.c

<a id="vwc.wc.gnu.GNU.use_padding"></a>

#### use\_padding

```python
def use_padding()
```

GNU-specific padding rules.

<a id="vwc.wc.bsd"></a>

# vwc.wc.bsd

<a id="vwc.wc.bsd.BSD"></a>

## BSD Objects

```python
class BSD(WC)
```

wc - count lines, words, characters, and bytes

Usage: wc [-clmwL] [file ...]

Count lines, words, characters, and bytes for each input file.
With no file, or when file is -, read standard input.

<a id="vwc.wc.bsd.BSD.add_platform_args"></a>

#### add\_platform\_args

```python
def add_platform_args(parser)
```

BSD-specific arguments.

<a id="vwc.wc.bsd.BSD.print_line"></a>

#### print\_line

```python
def print_line(counts, filename, file=sys.stdout)
```

Format and print count line for a file with BSD formatting.

<a id="vwc.main"></a>

# vwc.main

Main entry point for vwc.

<a id="vwc.main.main"></a>

#### main

```python
def main()
```

Main entry point.

