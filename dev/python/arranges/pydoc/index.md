<a id="arranges"></a>

# arranges

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

<a id="arranges.ranges.Ranges.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: Any) -> bool
```

Compare the two lists based on their string representations

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

<a id="arranges.ranges.Ranges.__get_pydantic_core_schema__"></a>

#### \_\_get\_pydantic\_core\_schema\_\_

```python
@classmethod
def __get_pydantic_core_schema__(cls, source_type: Any,
                                 handler: GetCoreSchemaHandler) -> CoreSchema
```

For automatic validation in pydantic

<a id="arranges.segment"></a>

# arranges.segment

<a id="arranges.segment.start_stop_to_str"></a>

#### start\_stop\_to\_str

```python
def start_stop_to_str(start: range_idx, stop: range_idx) -> str
```

Returns a string representation of a range from start to stop.

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

Construct a new string with the canonical form of the range.

<a id="arranges.segment.Segment.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls, start: range_idx, stop: range_idx = None) -> str
```

Construct a new string with the canonical form of the range.

<a id="arranges.segment.Segment.__or__"></a>

#### \_\_or\_\_

```python
def __or__(other: "Segment") -> "Segment"
```

Return the union of this range and the other range

<a id="arranges.segment.Segment.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

Iterate over the values in this range

<a id="arranges.segment.Segment.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Get the length of this range

<a id="arranges.segment.Segment.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__() -> bool
```

True if this range has a length

<a id="arranges.segment.Segment.last"></a>

#### last

```python
@property
def last() -> int
```

Gets the last value in this range. Will return inf if the range
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

Sort key function for sorting ranges

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

True if this range is adjacent to or overlaps the other range, and so they
can be joined together.

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

