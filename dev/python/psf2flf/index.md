# 🔠 psf2flf

```text
                 ▄█▀█▄  ▄█▀▀█▄   ▄█▀█▄  ▀██      ▄█▀█▄
▀█▄▀▀█▄ ▄█▀▀▀▀  ▄██▄      ▄▄█▀  ▄██▄     ██     ▄██▄
 ██▄▄█▀  ▀▀▀█▄   ██     ▄█▀ ▄▄   ██      ██ ▄    ██
▄██▄    ▀▀▀▀▀   ▀▀▀▀    ▀▀▀▀▀▀  ▀▀▀▀      ▀▀    ▀▀▀▀
```

Converts PSF bitmap fonts to Figlet fonts, combining multiple fonts with
different charsets into a unicode representation.

```bash
pip install psf2flf
psf2flf --help
```

* [📺 youtube](https://youtu.be/EgWMlwm8vMw)
* [🏠 home](https://bitplane.net/dev/python/psf2flf)
* [🐍 pypi](https://pypi.org/project/psf2flf)
* [😺 github](https://github.com/bitplane/psf2flf)

## Known issues

* 🔠 PSF1 fonts that don't have a Unicode table aren't inferred, and will spit
  out warnings.
* 🔨 You'll need to pass a control file to render the unicode glyphs:

```flc
flc2a
# Set UTF-8 input mode
u
```

## LICENSE

WTFPL with one additional clause:

1. Don't blame me

That is, do what you like, but you're on your own.
