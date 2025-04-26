<a id="upd8"></a>

# upd8

upd8 - Track updates to Python objects

<a id="upd8._field"></a>

# upd8.\_field

Field descriptor for Versioned classes.

<a id="upd8._field.field"></a>

## field Objects

```python
class field(Generic[T])
```

Declarative versioned field with a default value.

**Example**:

  class Counter(Versioned):
- `count` - int = field(0)
- `name` - str = field("default")

<a id="upd8._versioned"></a>

# upd8.\_versioned

Base class for objects with versioning and thread-safe access.

<a id="upd8._versioned.Versioned"></a>

## Versioned Objects

```python
class Versioned()
```

Base class for objects whose state changes should be trackable via a version number.
Includes a reentrant lock for thread safety when modifying or accessing state.

<a id="upd8._versioned.Versioned.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initializes version to 0 and creates a reentrant lock.

<a id="upd8._versioned.Versioned.version"></a>

#### version

```python
@property
def version() -> int
```

Returns the current version number of this object.

<a id="upd8._versioned.Versioned.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Makes Versioned objects hashable based on identity and current version.
Useful for caching mechanisms that depend on object state.

<a id="upd8._versioned.Versioned.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: Any) -> bool
```

Equality check based on identity and version.
Two Versioned objects are equal if they are the same object instance
and have the same version number.

<a id="upd8._decorator"></a>

# upd8.\_decorator

Decorators for Versioned objects.

<a id="upd8._decorator.changes"></a>

#### changes

```python
def changes(method)
```

Decorate state mutating methods with this.
Works with both synchronous and asynchronous methods.
Automatically uses the change context manager.

If a method raises AbortChange, the exception is caught and the method
returns the return value passed to the exception.

<a id="upd8._decorator.waits"></a>

#### waits

```python
def waits(method)
```

Decorate state awaiting methods with this.
Works with both synchronous and asynchronous methods.
Automatically acquires the lock for thread-safe access.

<a id="upd8._change"></a>

# upd8.\_change

Helper for applying changes in a context manager or the update method

<a id="upd8._change._Change"></a>

## \_Change Objects

```python
class _Change()
```

Helper class that provides both method call and context manager functionality
for version tracking. Supports both synchronous and asynchronous contexts.

<a id="upd8._change._Change.__call__"></a>

#### \_\_call\_\_

```python
def __call__()
```

Called when used as a method

<a id="upd8._change._Change.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__()
```

Called when used as a synchronous context manager

<a id="upd8._change._Change.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(exc_type, exc_val, exc_tb)
```

Called when exiting the synchronous context

<a id="upd8._change._Change.__aenter__"></a>

#### \_\_aenter\_\_

```python
async def __aenter__()
```

Called when used as an asynchronous context manager

<a id="upd8._change._Change.__aexit__"></a>

#### \_\_aexit\_\_

```python
async def __aexit__(exc_type, exc_val, exc_tb)
```

Called when exiting the asynchronous context

<a id="upd8._exception"></a>

# upd8.\_exception

Exception classes for the upd8 package.

<a id="upd8._exception.AbortChange"></a>

## AbortChange Objects

```python
class AbortChange(Exception)
```

Raise this exception to exit a @changes decorated method
without incrementing the version.

Can optionally include a return value.

