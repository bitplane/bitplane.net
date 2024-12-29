# 🐳 Dockerfile.exe

When the kernel runs your shebang, it only does one split. So you can't pass
multiple parameters because they all get stuck together. This sort of thing
will fail:

```sh
#!/bin/sh -c 'echo party pooper'
```

`'-c '` isn't an option, and `-c'echo hello'` won't work either beause it
needs a space after the `-c`.

Same deal with bash.

```shell
$ ./party_pooper
/bin/sh: 0: Illegal option -

$ sh '-c "echo party pooper"'
/bin/sh: 0: Illegal option -

$ sh -c"echo hello"
/bin/sh: 0: Illegal option -h

$ bash -c"boooh"
bash: -c: option requires an argument
```

## ? \[Yn\]

Because the `\0` terminated `argv` list only has 3 args. The binary (`$0`),
everything after it (`$1`) and the name of the file (`$2`).

You can use env with the `-S` flag to work around that; this will work:

```sh
#!/usr/bin/env -S sh -c 'echo hello!'`
```

But it's not POSIX. And might be in `/bin`. It's usually in both so that's
not a problem, but technically correct is the best form of correct.

So I was messing about and found a way around it is using `awk`, which is
POSIX:

```shell
$ cat party_pooper
#!/bin/awk BEGIN {system("hexdump -C /proc/$PPID/cmdline")}

$ ./party_pooper
00000000  2f 62 69 6e 2f 61 77 6b  00 42 45 47 49 4e 20 7b  |/bin/awk.BEGIN {|
00000010  73 79 73 74 65 6d 28 22  68 65 78 64 75 6d 70 20  |system("hexdump |
00000020  2d 43 20 2f 70 72 6f 63  2f 24 50 50 49 44 2f 63  |-C /proc/$PPID/c|
00000030  6d 64 6c 69 6e 65 22 29  7d 00 2e 2f 6d 65 68 00  |mdline")}../meh.|
00000040
```

## YEAH BUT WHYYY?!

So I can make a self-executing Dockerfile of course! The following copies a
Dockerfile to `/tmp`, builds and runs it in that place, then deletes the temp
dir afterwards:

```docker
#!/bin/awk BEGIN { system("t=$(mktemp -d); cat " ARGV[1] " > $t/Dockerfile; cd $t; docker run --rm $(docker build -q .); rm -rf $t") }
FROM alpine

ENTRYPOINT ["sh", "-c", "echo hello world"]
```

Works for the files I've tried it with, so it should probably be more of a
thing!

* [🐱 github](https://docker.com/bitplane/Dockerfile.exe)
* [👽 reddit](https://www.reddit.com/r/docker/comments/1hotp9l/a_shebang_for_dockerfiles/)
* [🐦 x](https://x.com/bitplane/status/1873319793417404709)
