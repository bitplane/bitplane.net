#!/bin/sh
set -x

uname -a

man wc > manpage.txt
cat manpage.txt

echo "Tests for --help and -h"
wc  -h
echo $?
wc --help
echo $?

echo "does help go to stderr?"
wc -h     2> /dev/null
wc --help 2> /dev/null

echo "is - supported?" | wc -
echo $?

echo "how's your formatting?"

