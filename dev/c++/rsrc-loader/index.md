# Windows RSRC loader

If you're gonna support loading resources like icons and sounds in other
people's binaries, like if you have your own GUI toolkit and want icons in it,
or to load strings and other things from binaries, but the whole engine is
cross-platform, then you're gonna need a RSRC loader, right?

Well, probably not. But I told myself that anyway because it was a good excuse
to write a parser for them and expose it as part of Irrlicht's virtual
filesystem. Writing parsers is a lot more fun than you'd actually imagine.

This makes the [.ico and .cur texture loader](../ico-loader) work with EXE and
DLL files.

TODO: find source code and link it.
