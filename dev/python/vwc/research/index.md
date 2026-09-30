# Useful

```shell
podman run -it ubuntu          #
podman run -it madworx/netbsd  # login=root
podman run -it alpine          #
```

## Core differences

### --help and -h

| Arg     | impl    | ?  | stdout  |
|---------|---------|----|---------|
| --help  | GNU     | ✅ |   ✅    |
| -h      | GNU     | ✅ |   ✅    |
| --help  | BSD     | ❌ |   ❌    |
| -h      | BSD     | ❌ |   ❌    |
| -h      | BusyBox | ❌ |   ❌    |
| --help  | BusyBox | ✅ |   ❌    |

### `-` as a stream

| impl    | ?  | \d |
|---------|----|----|
| GNU     | ✅ | ✅ |
| BSD     | ❌ | ❌ |
| Busybox | ✅ | ❌ |

### String format

| impl    |  printf             |
|---------|---------------------|
| GNU     | `" %7d %7d %7d %s"` |
| BSD     | `" %7d %7d %7d %s"` |
| Busybox | `"%9d %9d %9d %s"`  |

### Total

### `-m`

### `-w`

## BSD

-h

```shell
netbsd# wc -h
wc: unknown option -- h
usage: wc [-c | -m] [-Llw] [file ...]
```

handling -

```shell
netbsd# yes | head -n10 | wc -
wc: -: No such file or directory
```

```shell
 netbsd# yes | head -n1000 | wc
    1000    1000    2000
netbsd# yes | head -n100000 | wc
  100000  100000  200000
netbsd# yes | head -n10000000 | wc
 10000000 10000000 20000000
netbsd# yes | head -n100000000 | wc
 100000000 100000000 200000000
netbsd#
```

## busybox

--help but not -h

```shell
/ # wc --help
BusyBox v1.37.0 (2025-01-17 18:12:01 UTC) multi-call binary.

Usage: wc [-cmlwL] [FILE]...

Count lines, words, and bytes for FILEs (or stdin)

        -c      Count bytes
        -m      Count characters
        -l      Count newlines
        -w      Count words
        -L      Print longest line length
/ # echo $?
0
/ # wc -h
wc: unrecognized option: h
BusyBox v1.37.0 (2025-01-17 18:12:01 UTC) multi-call binary.

Usage: wc [-cmlwL] [FILE]...

Count lines, words, and bytes for FILEs (or stdin)

        -c      Count bytes
        -m      Count characters
        -l      Count newlines
        -w      Count words
        -L      Print longest line length
/ # echo $?
1
```

--help always goes to stderr

```shell
/ # wc --help > tmp.1
BusyBox v1.37.0 (2025-01-17 18:12:01 UTC) multi-call binary.

Usage: wc [-cmlwL] [FILE]...

Count lines, words, and bytes for FILEs (or stdin)

        -c      Count bytes
        -m      Count characters
        -l      Count newlines
        -w      Count words
        -L      Print longest line length
/ # echo $?
0
```

padding
```shell
/ # yes | head -n1000 | wc
     1000      1000      2000
/ # yes | head -n10000 | wc
    10000     10000     20000
/ # yes | head -n1000000 | wc
  1000000   1000000   2000000
/ # yes | head -n10000000 | wc
 10000000  10000000  20000000
/ # yes | head -n100000000 | wc
100000000 100000000 200000000
/ # yes | head -n1000000000 | wc
1000000000 1000000000 2000000000

looks like "%9d "
```


## GNU

```shell
$ wc --help
Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
printable characters delimited by white space.

With no FILE, or when FILE is -, read standard input.

The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the maximum display width
  -w, --words            print the word counts
      --total=WHEN       when to print a line with total counts;
                           WHEN can be: auto, always, only, never
      --help        display this help and exit
      --version     output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation <https://www.gnu.org/software/coreutils/wc>
or available locally via: info '(coreutils) wc invocation'
$ echo $0
0
```

explicit --help or -h goes to stdout, -uwotm8 to stderr

```shell
(💻​) gaz@blade:~$ wc -wot > /tmp/nope
wc: invalid option -- 'o'
Try 'wc --help' for more information.
(💻​) gaz@blade:~$ echo $?
1
```

ctrl+d

```shell
(💻​) gaz@blade:~$ wc - - -
the first
then press ctrl+d
      2       5      28 -
the second, and more ctrl+d
      1       5      28 -
the third. and once more
      1       5      25 -
      4      15      81 total
```

## Mac

## History

* [IEEE Std 1003.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/wc.html)
