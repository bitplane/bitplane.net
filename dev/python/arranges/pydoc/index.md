<a id="arranges"></a>

# arranges

<a id="arranges.segment"></a>

# arranges.segment

<a id="arranges.segment.start_stop_to_str"></a>

#### start\_stop\_to\_str

```python
def start_stop_to_str(start: range_idx, stop: range_idx) -> str
```

Returns a string representation of a segment from start to stop.

<a id="arranges.segment.Segment"></a>

## Segment Objects

```python
class Segment(str)
```

A single range segment that's a string and can be hashed.

<a id="arranges.segment.Segment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(start: range_idx, stop: range_idx = None)
```

Construct a new string with the canonical form of the segment.

<a id="arranges.segment.Segment.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls, start: range_idx, stop: range_idx = None) -> str
```

Construct a new string with the canonical form of the segment.

<a id="arranges.segment.Segment.__or__"></a>

#### \_\_or\_\_

```python
def __or__(other: "Segment") -> "Segment"
```

Return the union of this segment and the other one

<a id="arranges.segment.Segment.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

Iterate over the values in this segment

<a id="arranges.segment.Segment.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Get the length of this segment

<a id="arranges.segment.Segment.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__() -> bool
```

True if we have a length

<a id="arranges.segment.Segment.last"></a>

#### last

```python
@property
def last() -> int
```

Gets the last value in this range. Will return inf if the segment
has no end, and -1 if it has no contents,

<a id="arranges.segment.Segment.from_str"></a>

#### from\_str

```python
@classmethod
@lru_cache
def from_str(cls, value: str) -> "Segment"
```

Construct from a string.

<a id="arranges.segment.Segment.sort_key"></a>

#### sort\_key

```python
@staticmethod
def sort_key(value: "Segment") -> tuple[int, int]
```

Sort key function for sorting range segments

<a id="arranges.segment.Segment.isdisjoint"></a>

#### isdisjoint

```python
def isdisjoint(other: Any) -> bool
```

Return True if this range is disjoint from the other range

<a id="arranges.segment.Segment.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: Any) -> bool
```

Compare two segments

<a id="arranges.segment.Segment.isconnected"></a>

#### isconnected

```python
def isconnected(other: "Segment") -> bool
```

True if this range is adjacent to or overlaps the other segment,
so they can be joined together.

<a id="arranges.segment.Segment.isadjacent"></a>

#### isadjacent

```python
def isadjacent(other: "Segment") -> bool
```

True if this range is adjacent to the other range

<a id="arranges.segment.Segment.intersects"></a>

#### intersects

```python
def intersects(other: "Segment") -> bool
```

True if this range intersects the other range.

<a id="arranges.segment.Segment.__lt__"></a>

#### \_\_lt\_\_

```python
def __lt__(other: "Segment") -> bool
```

Compare segments by (start, stop) tuple

<a id="arranges.segment.Segment.__le__"></a>

#### \_\_le\_\_

```python
def __le__(other: "Segment") -> bool
```

Compare segments by (start, stop) tuple

<a id="arranges.segment.Segment.__gt__"></a>

#### \_\_gt\_\_

```python
def __gt__(other: "Segment") -> bool
```

Compare segments by (start, stop) tuple

<a id="arranges.segment.Segment.__ge__"></a>

#### \_\_ge\_\_

```python
def __ge__(other: "Segment") -> bool
```

Compare segments by (start, stop) tuple

<a id="arranges.segment.Segment.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(other: Any) -> bool
```

Membership test. Supports integers, strings, ranges and iterables.

<a id="arranges.utils"></a>

# arranges.utils

Some quacky type helpers so we don't have to use isinstance everywhere

<a id="arranges.utils._Boundless"></a>

## \_Boundless Objects

```python
class _Boundless(float)
```

A class that represents a boundless end of a range

<a id="arranges.utils._Boundless.huge"></a>

#### huge

An enormous number that's used as a stand-in for infinity

<a id="arranges.utils._Boundless.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other) -> bool
```

Is this boundless?

<a id="arranges.utils._Boundless.__index__"></a>

#### \_\_index\_\_

```python
def __index__() -> int
```

When used as an index, return a huge integer rather than infinity.

This is necessary because CPython doesn't allow lengths larger than
sys.maxsize, and Python has no way to represent infinity as an integer.

<a id="arranges.utils._Boundless.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Make this hashable so it can be used in sets

<a id="arranges.utils.inf"></a>

#### inf

A boundless end of a range. When used as a stop value it's infinite, but when
used as a length it's the largest index integer possible in cpython.

<a id="arranges.utils.to_int"></a>

#### to\_int

```python
def to_int(value: str, default: int) -> int
```

Convert a string to an integer. If the string is empty, return the default

<a id="arranges.utils.is_rangelike"></a>

#### is\_rangelike

```python
def is_rangelike(obj: Any) -> bool
```

Check if a value is a range-like object

<a id="arranges.utils.is_intlike"></a>

#### is\_intlike

```python
def is_intlike(value: Any) -> bool
```

Can this object be converted to an integer?

<a id="arranges.utils.is_iterable"></a>

#### is\_iterable

```python
def is_iterable(value: Any) -> bool
```

Is this object iterable?

<a id="arranges.utils.as_type"></a>

#### as\_type

```python
def as_type(cls: Type[T], value: Any) -> T
```

Convert a value to a type, if necessary.

Saves a bit of construction time if the value is already the right type.

<a id="arranges.utils.try_hash"></a>

#### try\_hash

```python
def try_hash(obj: Any) -> int | None
```

Try to hash an object. If it can't be hashed, return None

<a id="arranges.utils.force_hash"></a>

#### force\_hash

```python
def force_hash(value)
```

Force a hash for any value, using str() fallback for unhashable types

<a id="arranges.utils.as_key"></a>

#### as\_key

```python
def as_key(k)
```

Convert a key to a Ranges object.

A lot of the time we'll have N when we don't mean ":N"
So this converts keys to ranges, but not int-like objects.

<a id="arranges.dict"></a>

# arranges.dict

<a id="arranges.dict.Dict"></a>

## Dict Objects

```python
class Dict()
```

Range-to-value mapping using slice syntax.

Stores mappings from ranges to values efficiently without storing
individual positions. Supports slice syntax: d[100:200] = "value"

<a id="arranges.dict.Dict.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, value)
```

Set a range to a value: d[100:200] = "highlight"

<a id="arranges.dict.Dict.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key)
```

Get value for a range or position: d[150] or d[100:200]

<a id="arranges.dict.Dict.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(key)
```

Check if a position/range is covered: 150 in d

<a id="arranges.dict.Dict.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(key)
```

Delete a key and update ranges

<a id="arranges.dict.Dict.clear"></a>

#### clear

```python
def clear()
```

Clear all items and update ranges

<a id="arranges.dict.Dict.pop"></a>

#### pop

```python
def pop(key, *args)
```

Pop a key and update ranges

<a id="arranges.dict.Dict.popitem"></a>

#### popitem

```python
def popitem()
```

Pop an item and update ranges

<a id="arranges.dict.Dict.update"></a>

#### update

```python
def update(*args, **kwargs)
```

Update dict and ranges

<a id="arranges.dict.Dict.setdefault"></a>

#### setdefault

```python
def setdefault(key, default=None)
```

Set default and update ranges if key was added

<a id="arranges.dict.Dict.get"></a>

#### get

```python
def get(key, default=None)
```

Get value with default, converting key

<a id="arranges.dict.Dict.__or__"></a>

#### \_\_or\_\_

```python
def __or__(other)
```

Union operator (|): return new Dict with combined contents

<a id="arranges.dict.Dict.__ror__"></a>

#### \_\_ror\_\_

```python
def __ror__(other)
```

Reverse union operator: other | self

<a id="arranges.dict.Dict.__ior__"></a>

#### \_\_ior\_\_

```python
def __ior__(other)
```

Inplace union operator (|=): update self with other

<a id="arranges.dict.Dict.copy"></a>

#### copy

```python
def copy()
```

Return a copy of this Dict

<a id="arranges.dict.Dict.keys"></a>

#### keys

```python
def keys()
```

Return view of range keys

<a id="arranges.dict.Dict.values"></a>

#### values

```python
def values()
```

Return view of values

<a id="arranges.dict.Dict.items"></a>

#### items

```python
def items()
```

Return view of (range_key, value) pairs

<a id="arranges.dict.Dict.__len__"></a>

#### \_\_len\_\_

```python
def __len__()
```

Return number of stored ranges

<a id="arranges.dict.Dict.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__()
```

Return True if not empty

<a id="arranges.dict.Dict.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

Iterate over range keys

<a id="arranges.dict.Dict.__reversed__"></a>

#### \_\_reversed\_\_

```python
def __reversed__()
```

Iterate over range keys in reverse order

<a id="arranges.dict.Dict.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other)
```

Check equality with another dict

<a id="arranges.dict.Dict.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

String representation

<a id="arranges.dict.Dict.ranges"></a>

#### ranges

```python
@property
def ranges()
```

Union of all stored ranges (for compatibility)

<a id="arranges.ranges"></a>

# arranges.ranges

<a id="arranges.ranges.Ranges"></a>

## Ranges Objects

```python
class Ranges(str)
```

A range set that can be hashed and converted to a string.

<a id="arranges.ranges.Ranges.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: Any, stop: range_idx | None = None)
```

Construct a new string with the canonical form of the range.

<a id="arranges.ranges.Ranges.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls, value: Any, stop: range_idx | None = None) -> str
```

Construct a new string with the canonical form of the range.

This becomes "self" in __init__, so we're always a string

<a id="arranges.ranges.Ranges.construct_str"></a>

#### construct\_str

```python
@classmethod
def construct_str(cls, value, stop) -> str
```

Create a string representation of a range series

<a id="arranges.ranges.Ranges.from_str"></a>

#### from\_str

```python
@classmethod
def from_str(cls, value: str) -> tuple[Segment]
```

Construct from a string.

<a id="arranges.ranges.Ranges.iterable_to_str"></a>

#### iterable\_to\_str

```python
@classmethod
def iterable_to_str(cls, iterable: Iterable) -> str
```

Convert an iterable of ranges to a string

<a id="arranges.ranges.Ranges.from_hashable_iterable"></a>

#### from\_hashable\_iterable

```python
@classmethod
@lru_cache
def from_hashable_iterable(cls, value: tuple[Any]) -> tuple[Segment]
```

Cache the result of from_iterable

<a id="arranges.ranges.Ranges.from_iterable"></a>

#### from\_iterable

```python
@classmethod
def from_iterable(cls, iterable: Iterable) -> tuple[Segment]
```

Sort and merge a list of ranges.

<a id="arranges.ranges.Ranges.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__()
```

The hash of the string (which is what these things are)

<a id="arranges.ranges.Ranges.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Get the total length of all ranges

<a id="arranges.ranges.Ranges.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__() -> bool
```

True if this range has any elements

<a id="arranges.ranges.Ranges.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: Any) -> bool
```

Compare the two lists based on their string representations

<a id="arranges.ranges.Ranges.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key)
```

Support slicing and indexing of ranges.

<a id="arranges.ranges.Ranges.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(other: Any) -> bool
```

Are all of the other ranges in our ranges?

<a id="arranges.ranges.Ranges.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

Iterate over the values in our ranges.

Note that this could be boundless.

<a id="arranges.ranges.Ranges.intersects"></a>

#### intersects

```python
def intersects(other: Any) -> bool
```

True if this range overlaps with the other range

<a id="arranges.ranges.Ranges.union"></a>

#### union

```python
def union(other) -> "Ranges"
```

Return the union of this range and the other

<a id="arranges.ranges.Ranges.__or__"></a>

#### \_\_or\_\_

```python
def __or__(other: "Ranges") -> "Ranges"
```

Return the union of this range and the other

<a id="arranges.ranges.Ranges.__and__"></a>

#### \_\_and\_\_

```python
def __and__(other: "Ranges") -> "Ranges"
```

Return the intersection of this range and the other

<a id="arranges.ranges.Ranges.__le__"></a>

#### \_\_le\_\_

```python
def __le__(other: "Ranges") -> bool
```

Subset operator (<=): True if self is a subset of other

<a id="arranges.ranges.Ranges.__lt__"></a>

#### \_\_lt\_\_

```python
def __lt__(other: "Ranges") -> bool
```

Proper subset operator (<): True if self is a proper subset of other

<a id="arranges.ranges.Ranges.__ge__"></a>

#### \_\_ge\_\_

```python
def __ge__(other: "Ranges") -> bool
```

Superset operator (>=): True if self is a superset of other

<a id="arranges.ranges.Ranges.__gt__"></a>

#### \_\_gt\_\_

```python
def __gt__(other: "Ranges") -> bool
```

Proper superset operator (>): True if self is a proper superset of other

<a id="arranges.ranges.Ranges.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(other: "Ranges") -> "Ranges"
```

Relative complement operator (-): Return elements in self that are not in other

<a id="arranges.ranges.Ranges.__invert__"></a>

#### \_\_invert\_\_

```python
def __invert__()
```

The inverse of this range

<a id="arranges.ranges.Ranges.validate"></a>

#### validate

```python
@classmethod
def validate(cls, value: Any) -> "Ranges"
```

Validate a value and convert it to a Range

<a id="arranges.ranges.Ranges.first"></a>

#### first

```python
@property
def first()
```

The start value of the first segment.
Called "first" rather than "start" so that Ranges are not "range-like" things.

<a id="arranges.ranges.Ranges.last"></a>

#### last

```python
@property
def last()
```

The last value of the final segment.
Exposing "last" rather than "stop" so that Ranges are not "range-like" things.

