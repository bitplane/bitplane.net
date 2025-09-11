# Iteration

`Ranges` objects are sequences of integers that you can iterate over.

```python
from arranges import Ranges

assert list(Ranges("start:3, 10")) == [0, 1, 2, 10]
```

## Cardinality of the address range

The length of a range is the number of elements it contains. But because ranges
can be boundless, we have a special `inf` value that represents an infinite int
as Python doesn't have or support one.

This value is `math.inf`, but when returned from `len` it becomes `sys.maxsize`
as it only supports ints that are this size or smaller. When comparing `inf` to
`sys.maxsize` it'll return `True`, but this doesn't work in all directions:

```python
import math
import sys
from arranges import Ranges, inf

assert len(Ranges("1,2,3,4,10:20")) == 14

full = Ranges(":")

assert len(full) == sys.maxsize
assert len(full) == inf
assert sys.maxsize == inf
assert full.stop == inf
assert inf - 100 == sys.maxsize

# Careful though, this does not hold
assert len(full) != math.inf

# because it's an int
assert type(len(full)) is int
```

## Truthiness

Empty ranges are, of course, Falsey.

```python
from arranges import Ranges, Segment

assert Ranges(":")
assert Segment(10)

assert not Ranges("")
```
