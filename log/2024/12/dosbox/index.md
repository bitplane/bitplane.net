---
features: ["dosbox"]
---
# 💾 dosbox here too

The asciinema thing works well, but dosbox uses a framebuffer so I can't record
my old apps. So I decided to add another player.

This time I've embedded [js-dos](https://js-dos.com), same trick as before. Add
the `dosbox` feature to the front matter and if there's a `whatever.dos.zip`
link in a bullet point, it'll run it in a DOS emulator.

* [💾 curs](/dev/c/curs/CURS.dos.zip)
* [💾 textrot](/dev/c/textrot/textrot.dos.zip)
