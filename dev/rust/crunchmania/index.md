# Crunch-Mania in Rust

Compressor and decompressor for Crunch-Mania files — the LZ77/LZH format
that shipped with countless Commodore Amiga demos and intros between
1989 and 1994.

Ported 1:1 from the Python [`crunchmania`][py] package. Same four magic
variants (`CrM!`, `CrM2`, `Crm!`, `Crm2`), same handling of obfuscated
clone magics (`Iron`, `MSS!`, `mss!`, `DCS!`, `CD\xb3\xb9`,
`0x18051973`), same byte-for-byte output — just ~30–60× faster.

[py]: https://github.com/bitplane/crunchmania

## Install

From crates.io:

```bash
cargo install crunchmania
```

Pre-built binaries for Linux (x86_64 / aarch64 musl), macOS (universal)
and Windows are attached to each [GitHub release][releases].

[releases]: https://github.com/bitplane/crunchmania-rs/releases

## Usage

```bash
# Decompress
crunchmania unpack thing.crm thing

# Compress (standard mode; add --sampled for delta mode on sample data)
crunchmania pack thing thing.crm
crunchmania pack sample.raw --sampled

# Inspect header
crunchmania info thing.crm

# Scan a blob for embedded CrM blocks
crunchmania scan disk.adf
```

Short aliases `p`, `u`, `i`, `s` also work.

### Library

```toml
[dependencies]
crunchmania = "0.1"
```

```rust
use crunchmania::{pack, unpack, parse_header};

let header = parse_header(&bytes)?;
let raw = unpack(&bytes)?;
let repacked = pack(&raw, false);
# Ok::<(), crunchmania::CrmError>(())
```

## Links

* [🏠 home](https://bitplane.net/dev/rust/crunchmania)
* [🐱 source](https://github.com/bitplane/crunchmania-rs)
* [🐍 python version](https://github.com/bitplane/crunchmania)
* [📦 crates.io](https://crates.io/crates/crunchmania)

## License

WTFPL with warranty clause: don't blame me.
