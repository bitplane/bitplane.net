<a id="vwc"></a>

# vwc

<a id="vwc.vwc"></a>

# vwc.vwc

wc.py — A GNU-compatible `wc` implementation in Python (Cython-friendly).

Usage: wc.py [OPTION]... [FILE]...
  or:  wc.py [OPTION]... --files0-from=F

Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified. A word is a non-zero-length sequence of
printable characters delimited by white space.

With no FILE, or when FILE is -, read standard input.

Options:
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
  -w, --words            print the word counts
  -L, --max-line-length  print the maximum display width
      --files0-from=F    read input from the files specified by
                         NUL-terminated names in file F;
                         If F is - then read names from standard input
      --total=WHEN       when to print a line with total counts;
                         WHEN can be: auto, always, only, never
      --help             display this help and exit
      --version          print version information and exit

Live preview of counts is shown every 200ms to stderr if stderr is a TTY.
Output columns appear in the following fixed order:
  lines, words, chars, bytes, max-line-length

This script is structured for easy Cython porting.

