<a id="filefrag"></a>

# filefrag

<a id="filefrag.device"></a>

# filefrag.device

<a id="filefrag.device.Device"></a>

## Device Objects

```python
class Device()
```

Represents a device; the backing store of a filesystem.

<a id="filefrag.filemap"></a>

# filefrag.filemap

<a id="filefrag.filemap.FileMap"></a>

## FileMap Objects

```python
class FileMap()
```

Contains a mapping of a file to physical locations on the storage device.

<a id="filefrag.filemap.FileMap.update"></a>

#### update

```python
def update()
```

(re)read the data, updating the internal state.

<a id="filefrag.filemap.FileMap.check_stale"></a>

#### check\_stale

```python
def check_stale() -> bool
```

Returns true is the data the path points to is different to when it
was loaded.

<a id="filefrag.filemap.FileMap.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

Iterates over the extents in the file.

<a id="filefrag.filefrag"></a>

# filefrag.filefrag

<a id="filefrag.filefrag.main"></a>

#### main

```python
def main()
```

Entrypoint for command line app.

<a id="filefrag.extent"></a>

# filefrag.extent

<a id="filefrag.extent.Extent"></a>

## Extent Objects

```python
class Extent()
```

Represents a range of data inside a file.

These have a logical position in the file, and a physical position on the
device. The length of an extent can't be smaller than the block size of the
filesystem holding it, so the length of all extents might be a bit longer
than the file it represents.

<a id="filefrag.extent.Extent.is_last"></a>

#### is\_last

```python
@property
def is_last() -> bool
```

True if this is the last extent in the file map.

<a id="filefrag.extent.Extent.is_unknown"></a>

#### is\_unknown

```python
@property
def is_unknown() -> bool
```

If the extent is unknown, the physical location and other details
returned are unreliable.

<a id="filefrag.extent.Extent.is_delayed_allocation"></a>

#### is\_delayed\_allocation

```python
@property
def is_delayed_allocation() -> bool
```

True if the extent is in the process of being allocated, so the physical
location will be set to 0 for the moment. Check again later

<a id="filefrag.extent.Extent.is_encoded"></a>

#### is\_encoded

```python
@property
def is_encoded() -> bool
```

An extent may be encoded in some way, like being compressed or stored in
a way where it'll need to be decoded before it can be read.

<a id="filefrag.extent.Extent.is_encrypted"></a>

#### is\_encrypted

```python
@property
def is_encrypted() -> bool
```

If so, the extent contains encrypted data, you'll need to decrypt it if
you want the data inside.

<a id="filefrag.extent.Extent.is_not_aligned"></a>

#### is\_not\_aligned

```python
@property
def is_not_aligned() -> bool
```

True if the extent is misaligned with the filesystem's block or cluster
sizes, if True then expect degraded performance.

<a id="filefrag.extent.Extent.is_inline"></a>

#### is\_inline

```python
@property
def is_inline() -> bool
```

True if the extent is stored with the filesystem's metadata rather than
in the data section.

<a id="filefrag.extent.Extent.is_tail_packed"></a>

#### is\_tail\_packed

```python
@property
def is_tail_packed() -> bool
```

True if the extent is the leftover bits at the end of a file that have
been packed together with other extents to save space. If this is true,
it's likely not_aligned too.

<a id="filefrag.extent.Extent.is_unwritten"></a>

#### is\_unwritten

```python
@property
def is_unwritten() -> bool
```

True if the data was allocated, but not yet written to the device.

<a id="filefrag.extent.Extent.is_merged"></a>

#### is\_merged

```python
@property
def is_merged() -> bool
```

If so, the extent is merged with other extents for reporting purposes.
How this is done is filesystem-dependent.

<a id="filefrag.extent.Extent.is_shared"></a>

#### is\_shared

```python
@property
def is_shared() -> bool
```

This extent might share a physical location with other extents. Seen in
copy-on-write filesystems with deduplication or snapshots (btrfs, zfs)

<a id="filefrag.fie"></a>

# filefrag.fie

<a id="filefrag.fie.get_extents"></a>

#### get\_extents

```python
def get_extents(fd)
```

This function retrieves all extents for a given file descriptor

<a id="filefrag.__main__"></a>

# filefrag.\_\_main\_\_

Entry point for the package

