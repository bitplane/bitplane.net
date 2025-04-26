# ✅ upd8

Version tracking for Python classes

## 🍐 wut?

Give your objects a version number that updates when you make changes.

## ⬇️  installation

```bash
pip install upd8
or
uv pip install upd8
```

## ▶️ Usage

### Simple updates

```python
>>> import upd8
>>> v = upd8.Versioned()
>>> v.version
0
>>> v.change()
1
>>> v.change()
2
```

### Automatic versioning

Fields will update the version when you change them.

```python
from upd8 import Versioned, field

class Doggo(Versioned):
    name = field("Pupper")
    legs = field(4)
```

```python
>>> d = Doggo()
>>> d.legs -= 1
>>> d.name = "Tripod"
>>> d.version
2
```

### Manual updates

`change` can be used as a context manager, and changes can be aborted by
raising `AbortChange`:

```python
>>> from upd8 import
>>> d = Doggo()
>>> d.legs = 1
>>> with d.change:
        if not d.legs:
            raise AbortChange()
        d.legs -= 1
>>> d.version
1
```

You can use `async with Versioned.change` from within asynchronous code.

### Thread safety

If you're not using automatic updating fields, you can add thread safety to
Versioned objects by decorating method with `@waits`, and avoid the context
manager indenting your code with the `@changes`.

These work on `async` methods too.

```python
class World(Versioned):
    _population: int = 8_000_000_000

    @changes
    def bottleneck(self, amount: float) -> int:
        survivors = int(self._population * amount)
        if survivors <= 0 or survivors == self._population:

            # set the return value in the AbortChange exception
            raise AbortChange(self._population)

        self._population = survivors
        return self._population

    @waits
    @property
    def population(self):
        return self._population
```

## 🔗 links

* [🏠 home](https://bitplane.net/dev/python/upd8)
* [📖 pydoc](https://bitplane.net/dev/python/upd8/pydoc)
* [🐍 pypi](https://pypi.org/project/upd8)
* [🐱 github](https://github.com/bitplane/upd8)

## ⚖️ License

Licensed under the WTFPL with one additional clause:

1. Don't blame me.

