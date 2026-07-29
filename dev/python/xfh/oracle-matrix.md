# Original-code oracle

The test oracle runs preserved XPK software under headless FS-UAE. It uses
Workbench 3.1, XPK master 4.16, Xvfb, and Mesa software rendering. No emulator
window is displayed on the host desktop.

For each safe case, the oracle:

1. creates deterministic input;
2. packs and unpacks it with the original Amiga software;
3. decodes the packed container with `xfh`;
4. compares both outputs byte-for-byte;
5. records modes, exclusions, sizes, and SHA-256 hashes as JSON.

The matrix covers every numeric mode for core codecs and reported mode
boundaries for other codecs. Compact representative containers are committed as
hexadecimal fixtures in `tests/fixtures/oracle`; Amiga binaries, ROMs, private
files, and full workspaces are not distributed.

Known original-tool failures are explicit exclusions:

- empty input can produce a header rejected by the same XPK master;
- some packer and vector combinations hang;
- ELZX and SLZX hang when their external LZX command is invoked at mode 100;
- SMPL selects raw chunks for all tested inputs;
- CYB1, CYB2, DHUF, and DMCB cannot produce useful compressed fixtures.

The ELZX and SLZX oracle uses the original LZX 1.21R dependency. LHLB uses its
original `lh.library` dependency. Dependency hashes are recorded, but the
binaries are not redistributed.

Run the tooling described in [`tools/fsuae/README.md`](../tools/fsuae/README.md)
to create an isolated workspace or verify generated containers.
