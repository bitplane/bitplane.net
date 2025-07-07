# texxd

A hex editor built with Textual.

## Usage

```bash
uvx texxd file.bin
# or
pip install texxd
texxd file.bin
```

## todo

- [ ] support drag-select
- [ ] style text
  - [ ] Change Highlighter to Styler (use CSS to style rendered text)
  - [ ] find as CSS classes
  - [ ] binary diff tool as a highlighter
- [ ] Design better cursor nav
  - [ ] vim style normal and edit modes (i, o, a to enter edit, esc = normal)
  - [x] support editing by default
