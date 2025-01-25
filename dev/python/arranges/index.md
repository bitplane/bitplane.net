# Arranges

## Range string fields for Pydantic BaseModels

I needed a way to parse batches of byte, row and line and other object ranges
in my `merge-files` app, in a way that I can just drop it in as a string field
type. The reason for this is so the machine-generated command line help is
flat and readable by humans.

It it kinda grew into a monster so I've split it out into this separate
package. The main feature is a pair of classes that can represent ranges:

* ⛓️ `Segment` is a class that can be treated like a `set` and its constructor is
  compatible with `range` and `slice`. It is derived from `str` so is easy to
  compare and serializes nicely. It is immutable, hashable and has a stable
  string representation.
* 🏔️ `Ranges` is an ordered `tuple` of `Segment`s. It is also immutable and
  derived from `str` like the above. It can be constructed from comma-separated
  Python-style slice notation strings (e.g. `"1:10, 20:"`, `"0x00:0xff` and
  `":"`), integers, `slice`s, `range`s, integers and (nested) iterables of the
  above.
* ♾️ An `inf` singleton that is a `float` with a value of `math.inf` but has an
  `__index__` that returns `sys.maxsize` and compares equal to infinity and
  `maxsize`, and its string representation is `"inf"`.

The range class is designed to be used as fields in Pydantic `BaseModel`s,
but can be used anywhere you need a range. They are not designed with speed in
mind, and comparisons usually use the canonical string form by converting other
things into `Ranges` objects. Their preferred pronoun is they/them.

## Constraints

I made them to select lines or bytes in a stream of data, so they:

* 🔢 only support `int`s;
* ≮ do not allow negative indices, the minimum is 0 and the maximum is
  unbounded;
* ✅ are compatible with `range` and `slice`, but `step` is fixed to `1`. If
  you pass something with a step into its constructor it'll be converted to
  a list of `int`s (`range(0, 10, 2)` becomes `"0,2,4,6,8"`);
* ∪ do not support duplicate ranges. Ranges are merged together as they are
  added to the `Ranges` object;
* 🐍 they are unpydantic in that its constructors are duck-typed, which is
  what I need;
* ☣️ they violate the Zen of Python by having multiple ways to do the same
  thing, but I found that useful; and
* ⚠️ Currently the interface is *unstable*, so lock the exact version in if
  you don't want breaking changes.

## Installation

`pip install arranges` if you want to use them. You'll need Python 3.10 or
above.

### Hacking

To add features etc you'll ideally need `git`, `make`, `bash` and something
with a debugger. Config for Visual Studio Code is included.

Clone the repo and `make dev` to make the venv, install dependencies, then
`code .` to open the project up in the venv with tests and debugging and all
that jazz.

Type `make help` to see the other options, or run the one-liner scripts in the
`./build` dir if you want to run steps without all that fancy caching nonsense.

## Usage

* [📖 RTFM](https://bitplane.net/dev/python/arranges/)
* [🧪 Read the tests](https://github.com/bitplane/arranges/)
* [🐍 Read the pydocs](https://bitplane.net/dev/python/arranges/pydoc)

## License

Free as in freedom from legalese; the [WTFPL with a warranty clause](LICENSE.md).
