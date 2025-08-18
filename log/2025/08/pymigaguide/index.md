# 📚 pymigaguide - a vibe coding win

My site is missing quite a few of my old [Amiga games](/dev/amos), and adding
them has been on my todo list for ages. This week I found the old tar-magnolia
machine and a screwdriver large enough to open it, and pulling the disk out, I
found a bunch of Amiga `.guide` files, including one I made for
[Eggit](/dev/amos/eggit).

But couldn't open them in Linux. Fixing this took under 2 hours end-to-end, so
I thought I'd share the process.

## GPT + Gemini + Claude

First I gave GPT-5 a research task to go thoroughly document the `.guide`
format. This was largely to stuff its context with everything it needed to write
some code. Starting with a full spec doc, its bullshit generation is far less
likely to make things up or leave things out.

With that in the pipe, I then asked it to make a parser that parsed the format
into `pydantic` objects. Then a CLI that dumps it to JSON. Then to add Markdown
and HTML.

At this point it tells me to go and make edits to files. Lacking a GPT agent, I
tell it that'll take too much time and ask it to hold on. Give me a textual UI
and a markdown doc of the file format. I `v > ./src/pymigaguide/whatever.py`
these files into a new template project, and finally ask for integration
instructions which go from the clipboard into a todo doc.

Then it's `gemini`'s turn. I point it at the src dir and the todo doc, and let
it work. Gemini's context length makes it great for understanding a dump of
crap, once it's written some basic tests and I throw in some testdata for it,
it fixes the lot and I have a working parser, converter + viewer.

Gemini is currently bad programming. It gets Python indentation wrong and its
tools don't like regex in code because its tools have standard escape string
bugs where it unescapes strings in the outputs. So I then pass it to Claude,
who is slower but far more mature in this area. After a couple of passes back
through GPT I've got a viewer with custom widgets and 3 output formats.

The entire process - from idea to pushing to pypi - took less than 2 hours.

Here's the outputs:

* [🏠 home](/dev/python/pymigaguide)
* [🐍 pypi](https://pypi.org/project/pymigaguide)
* [😺 github](https://github.com/bitplane/pymigaguide)

