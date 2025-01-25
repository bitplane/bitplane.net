# Constructing Range and Ranges

You can create them from:

1. strings
2. range-like objects
3. sequences of ints or these things, or other sequences
4. explicitly, like you would create a `range` or `slice`

## Range from a string

```python
from arranges import Ranges

# Create ranges from a string. Like a slice but without the square brackets.

the_full_range = Ranges(":")  # an endless sequence starting at 0
the_empty_range = Ranges("")  # start, stop and len() are all 0
from_0_to_99 = Ranges("0:100")
skip_10_items = Ranges("10:")  # boundless, goes to infinity
access_by_index = Ranges("0")  # just the first item

# Decimal, hexadecimal, octal and binary are supported. Note that octal uses
# Python's 0o prefix, not 0 like in C.
gbc_palette = Ranges("0xff68:0xff88")
skip_bmp_header = Ranges("0o66:end")  # skip "54", "0x36" or "0b1100110" bytes

# "end" and "inf" are the same. You can also use "start" instead of 0.
the_full_range_again = Ranges("start:inf")

# whitespace is ignored during construction
first_kilobyte = Ranges("start : 0x400")

# They are simplified when converted to str, which they can be compared with.
assert first_kilobyte == ":1024"

# Comparisons work in both directions
assert "000001:000002" == Ranges("1")

# and the hash is the same as the string
w = Ranges("6 : 8")
assert hash(w) == hash("6:8")

# so you can use them as dict keys
d = {"6:8": "width"}
d[w] = "GIF file width"
assert d == {"6:8": "GIF file width"}
```

## Ranges from a string

```python
from arranges import Ranges

# You can put gaps in your range using commas.
pages_2_to_5_and_20 = Ranges("2:6, 20")

# The ranges are sorted and combined as they are added
overlapping = Ranges("start:10, 14, 1:3")
assert overlapping == ":10,14"
```

## Ranges from range-like objects

If it has a start, stop and step attribute then it quacks like a range so you
can pass it in as the value.

```python
from arranges import Ranges

from_slice = Ranges(slice(10, 20))
from_range = Ranges(range(10, 20))
from_other = Ranges(Ranges("10:20"))

assert from_slice == from_range == from_other == "10:20"
```

## Ranges from sequences

```python
from arranges import Ranges

l = list(range(100))
t = tuple(range(100))
i = (i for i in range(100))

assert Ranges(l) == Ranges(t) == Ranges(i) == ":100"

jumble = Ranges([0, [2, 4], ["1:3"], 3, 4, range(10, 20)])

assert jumble == "5,10:20"
```

## Explicitly creating Ranges

You can create them in the same way as `range` or `slice` objects which have a
slightly different syntax to slice notation.

```python
from arranges import Ranges, inf

assert Ranges(10, inf) == "10:"

# Ranges("10") is not the same as Ranges(10)
assert Ranges(10) == ":10"
assert Ranges("10") == 10 == Ranges(10, 11)
```
