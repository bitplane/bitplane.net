# arrayfile

A file-backed numeric array using struct.pack. Does not support inserts or
slicing.

Smaller than relying on numpy though.

## Installation

```bash
pip install arrayfile
```

## Usage

### Temporary Array

This creates an array in your temp dir:

```python
from arrayfile import Array

# Create a temporary array with float data
arr = Array('f')
arr.append(3.14)
arr.append(2.71)
arr.extend([1.41, 1.73])

print(f"Length: {len(arr)}")
print(f"Values: {[arr[i] for i in range(len(arr))]}")
arr.close()  # Clean up resources
```

### Persistent Array

You can use the same file, if you want to persist your data across sessions:

```python
from arrayfile import Array

# Create and populate an array file
arr = Array('i', 'numbers.array', 'w+b')
for i in range(1000):
    arr.append(i * 2)
arr.close()

# Reopen the same file later
arr = Array('i', 'numbers.array', 'r+b')
print(f"Array has {len(arr)} elements")
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")

# Add more data
arr.append(2000)
arr.close()
```

## Context manager

It has a finalizer in case you forget to call `close()`, but if you like to keep
your code tidy, you can use a context manager, like so:

```python
from arrayfile import Array

# Using double precision floats with context manager
with Array('d', 'measurements.array', 'w+b') as arr:
    arr.extend([3.141592653589793, 2.718281828459045, 1.4142135623730951])

    print(f"Stored {len(arr)} precise measurements")
    for i, value in enumerate(arr):
        print(f"  {i}: {value:.15f}")
```

