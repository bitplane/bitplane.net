# 🦀 rars

A Rust implementation of RAR.

* [🏠 home](https://bitplane.net/rust/rars)
* [🦀 crate](https://crates.io/crates/rars)
* [🐱 source](https://github.com/bitplane/rars)

## Current Status

`rars` covers the RAR lineage from early `RE~^` archives through RAR 7,
compression and decompression. It's not fast, but it works. ish.

## CLI

Inspect, test, and extract archives:

```sh
rars info archive.rar
rars test archive.rar
rars x archive.rar out/
```

Create archives with specific RAR generation:

```sh
rars a --format rar29 archive.rar files...
rars a --format rar50 --solid --auto-filter archive.rar files...
rars a --format rar70 --store --volume-size 10m archive.part1.rar files...
```

The writer supports stored and compressed members, split volumes, passwords,
header encryption where implemented, comments, RARVM filters, RAR5 quick-open
records, and supported recovery records. Run `rars --help` for the exact option
set.

## Development

Run the test suite:

```sh
cargo test --workspace --all-targets
```

Generate a local coverage report:

```sh
rustup component add llvm-tools-preview
./scripts/coverage.py
```

The script prints a line-coverage summary, saves it to
`target/coverage/summary.txt`, and writes HTML output to
`target/coverage/html/library/index.html` and `target/coverage/html/cli/index.html`.
