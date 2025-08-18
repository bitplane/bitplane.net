# 🔠 psf2flf

```
                 ▄█▀█▄  ▄█▀▀█▄   ▄█▀█▄  ▀██      ▄█▀█▄
▀█▄▀▀█▄ ▄█▀▀▀▀  ▄██▄      ▄▄█▀  ▄██▄     ██     ▄██▄
 ██▄▄█▀  ▀▀▀█▄   ██     ▄█▀ ▄▄   ██      ██ ▄    ██
▄██▄    ▀▀▀▀▀   ▀▀▀▀    ▀▀▀▀▀▀  ▀▀▀▀      ▀▀    ▀▀▀▀
```

Converts PSF bitmap fonts to Figlet fonts, combining multiple fonts with
different charsets into a unicode representation.


## Known issues

* PSF1 fonts that don't have a Unicode table aren't inferred, and will spit out
  warnings.
* You'll need to pass a control file to render the unicode glyphs:

```
flc2a
# Set UTF-8 input mode
u
```

