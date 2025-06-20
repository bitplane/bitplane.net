<a id="blkcache"></a>

# blkcache

<a id="blkcache.file.device"></a>

# blkcache.file.device

Device file abstraction with ioctl support.

Device class that extends File with block device operations like
sector size detection, device sizing, and rotational status.

<a id="blkcache.file.device.BLKGETSIZE64"></a>

#### BLKGETSIZE64

<linux/fs.h> Get device byte-length

<a id="blkcache.file.device.BLKSSZGET"></a>

#### BLKSSZGET

Get block device sector size

<a id="blkcache.file.device.Device"></a>

## Device Objects

```python
class Device(File)
```

Device file with block device operations.

<a id="blkcache.file.device.Device.check"></a>

#### check

```python
@staticmethod
def check(path: Path) -> bool
```

Check if this is a block device.

<a id="blkcache.file.device.Device.device_size"></a>

#### device\_size

```python
def device_size() -> int
```

Get device capacity in bytes using ioctl or fallback methods.

<a id="blkcache.file.device.Device.sector_size"></a>

#### sector\_size

```python
@property
@lru_cache(maxsize=1)
def sector_size() -> int
```

Get device sector size using ioctl.

<a id="blkcache.file"></a>

# blkcache.file

File abstraction package with automatic type detection.

Provides File, Device, and Removable classes with a detect() factory
function that automatically chooses the appropriate class for a given path.

<a id="blkcache.file.detect"></a>

#### detect

```python
def detect(path: Path | str) -> Type[File]
```

Return the most specific file class that can handle this path.

Checks classes in order of specificity: Removable -> Device -> File
Returns the first class whose check() method returns True.

<a id="blkcache.file.mmapped"></a>

# blkcache.file.mmapped

Memory-mapped file abstraction.

MappedFile uses mmap for efficient access to regular files.
Only works with regular files that support memory mapping.

<a id="blkcache.file.mmapped.MMappedFile"></a>

## MMappedFile Objects

```python
class MMappedFile(File)
```

Memory-mapped file with efficient random access.

<a id="blkcache.file.mmapped.MMappedFile.check"></a>

#### check

```python
@staticmethod
def check(path: Path) -> bool
```

Check if this is a regular file that can be memory-mapped.

<a id="blkcache.file.mmapped.MMappedFile.pread"></a>

#### pread

```python
def pread(count: int, offset: int) -> bytes
```

Read count bytes at offset using memory map.

<a id="blkcache.file.mmapped.MMappedFile.pwrite"></a>

#### pwrite

```python
def pwrite(data: bytes, offset: int) -> int
```

Write data at offset using memory map.

<a id="blkcache.file.mmapped.MMappedFile.size"></a>

#### size

```python
def size() -> int
```

Get file size from memory map.

<a id="blkcache.file.base"></a>

# blkcache.file.base

<a id="blkcache.file.base.File"></a>

## File Objects

```python
class File()
```

Base file class with position-independent read/write operations.

<a id="blkcache.file.base.File.check"></a>

#### check

```python
@staticmethod
def check(path: Path) -> bool
```

Check if this class can handle the given path.

<a id="blkcache.file.base.File.depends"></a>

#### depends

```python
def depends(*files)
```

Register file dependencies for cascading cleanup.

<a id="blkcache.file.base.File.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name)
```

Delegate unknown attributes to the underlying file object.

<a id="blkcache.file.base.File.pread"></a>

#### pread

```python
def pread(count: int, offset: int) -> bytes
```

Read count bytes at offset without changing file position.

<a id="blkcache.file.base.File.pwrite"></a>

#### pwrite

```python
def pwrite(data: bytes, offset: int) -> int
```

Write data at offset without changing file position.

<a id="blkcache.file.base.File.size"></a>

#### size

```python
def size() -> int
```

Get file size without changing file position.

<a id="blkcache.file.base.File.fingerprint"></a>

#### fingerprint

```python
def fingerprint(head: int = 65_536) -> str
```

Generate content fingerprint from file header.

<a id="blkcache.file.atomic"></a>

# blkcache.file.atomic

Atomic file writes for frequently-updated or slowly written files.

AtomicFile prevents corruption of small files that are written often,
like ddrescue map files, by writing to "name~" then moving into place.

<a id="blkcache.file.atomic.AtomicFile"></a>

## AtomicFile Objects

```python
class AtomicFile(File)
```

File with atomic write operations via temporary files.

<a id="blkcache.file.atomic.AtomicFile.check"></a>

#### check

```python
@staticmethod
def check(path: Path) -> bool
```

Atomic files can handle any regular file path.

<a id="blkcache.file.filemap"></a>

# blkcache.file.filemap

File mapping for tracking block/sector status.

Pure data structure for tracking status of byte ranges without
any file format dependencies.

<a id="blkcache.file.filemap.STATUS_OK"></a>

#### STATUS\_OK

Successfully read

<a id="blkcache.file.filemap.STATUS_ERROR"></a>

#### STATUS\_ERROR

Read error

<a id="blkcache.file.filemap.STATUS_UNTRIED"></a>

#### STATUS\_UNTRIED

Not tried yet

<a id="blkcache.file.filemap.STATUS_TRIMMED"></a>

#### STATUS\_TRIMMED

Trimmed (not tried because of read error)

<a id="blkcache.file.filemap.STATUS_SLOW"></a>

#### STATUS\_SLOW

Non-trimmed, non-scraped (slow reads)

<a id="blkcache.file.filemap.STATUS_SCRAPED"></a>

#### STATUS\_SCRAPED

Non-trimmed, scraped (slow reads completed)

<a id="blkcache.file.filemap.CACHED"></a>

#### CACHED

Have data

<a id="blkcache.file.filemap.UNCACHED"></a>

#### UNCACHED

Need data

<a id="blkcache.file.filemap.ERROR"></a>

#### ERROR

Can't get data

<a id="blkcache.file.filemap.STATUSES"></a>

#### STATUSES

All valid statuses

<a id="blkcache.file.filemap.FileMap"></a>

## FileMap Objects

```python
class FileMap()
```

Tracks status of byte ranges using efficient transition-based representation.

Pure data structure with no file format dependencies.
Uses slice notation: filemap[start:end] = status

<a id="blkcache.file.filemap.FileMap.__init__"></a>

#### \_\_init\_\_

```python
def __init__(size: int)
```

Initialize with device/file size.

<a id="blkcache.file.filemap.FileMap.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, status)
```

Set status for range using slice notation: filemap[start:end] = status

<a id="blkcache.file.filemap.FileMap.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key)
```

Get status for range using slice notation: filemap[start:end] returns transitions

<a id="blkcache.file.filemap.FileMap.pos"></a>

#### pos

```python
@property
def pos() -> int
```

Current position - first untried byte.

<a id="blkcache.file.filemap.FileMap.status"></a>

#### status

```python
@property
def status() -> str
```

Current status - highest priority status found in transitions.

<a id="blkcache.file.cached"></a>

# blkcache.file.cached

Cache file abstraction.

CacheFile wraps another File and provides read-through caching.
Opens the backing file in its __enter__ method.

<a id="blkcache.file.cached.CachedFile"></a>

## CachedFile Objects

```python
class CachedFile(File)
```

Passthrough cache that wraps another File instance.

<a id="blkcache.file.cached.CachedFile.check"></a>

#### check

```python
@staticmethod
def check(path: Path) -> bool
```

CacheFile doesn't check paths - it's a wrapper.

<a id="blkcache.file.cached.CachedFile.path"></a>

#### path

```python
@property
def path() -> Path
```

Return the backing file's path.

<a id="blkcache.file.cached.CachedFile.size"></a>

#### size

```python
def size() -> int
```

Get size from backing file.

<a id="blkcache.file.cached.CachedFile.sector_size"></a>

#### sector\_size

```python
@property
def sector_size() -> int
```

Get sector size from backing file.

<a id="blkcache.file.cached.CachedFile.pread"></a>

#### pread

```python
def pread(count: int, offset: int) -> bytes
```

Read with cache - try cache first, then backing file.

<a id="blkcache.file.cached.CachedFile.pwrite"></a>

#### pwrite

```python
def pwrite(data: bytes, offset: int) -> int
```

Write through to both cache and backing file.

<a id="blkcache.file.cached.CachedFile.fingerprint"></a>

#### fingerprint

```python
def fingerprint(head: int = 65_536) -> str
```

Get fingerprint from backing file.

<a id="blkcache.file.cached.CachedFile.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name)
```

Delegate unknown attributes to backing file.

<a id="blkcache.file.removable"></a>

# blkcache.file.removable

Removable device abstraction with media change detection.

Removable class extends Device with functionality for optical drives,
USB drives, and other removable media that can be ejected or changed.

<a id="blkcache.file.removable.CDROM_GET_BLKSIZE"></a>

#### CDROM\_GET\_BLKSIZE

Get CDROM block size

<a id="blkcache.file.removable.Removable"></a>

## Removable Objects

```python
class Removable(Device)
```

Removable device with media change detection.

<a id="blkcache.file.removable.Removable.check"></a>

#### check

```python
@staticmethod
def check(path: Path) -> bool
```

Check if this is a removable block device.

<a id="blkcache.file.removable.Removable.sector_size"></a>

#### sector\_size

```python
@property
@lru_cache(maxsize=1)
def sector_size() -> int
```

Get sector size with CDROM-specific ioctl support.

<a id="blkcache.file.removable.Removable.watch_for_changes"></a>

#### watch\_for\_changes

```python
def watch_for_changes(stop_event: threading.Event,
                      callback=None,
                      logger=None) -> None
```

Monitor device for media changes.

**Arguments**:

- `stop_event` - Threading event to signal when to stop monitoring
- `callback` - Function to call on media change (old_id, new_id)
- `logger` - Logger for debug messages

<a id="blkcache.backend"></a>

# blkcache.backend

nbdkit Python backend integration for block-level device caching.

This module serves as the bridge between nbdkit and our file abstraction layer.
It handles the "outside" config (nbdkit parameters) while delegating file
operations to the composed file chain.

<a id="blkcache.backend.lookup"></a>

#### lookup

```python
def lookup(attr: str, handle: int, table=TABLE)
```

Generic attribute lookup for dispatch.

<a id="blkcache.backend.open_file_context"></a>

#### open\_file\_context

```python
def open_file_context(path: Path, mode: str)
```

Generator to manage file lifecycle.

<a id="blkcache.backend.config"></a>

#### config

```python
def config(key: str, val: str) -> None
```

Stores device, cache paths and parses metadata key-value pairs.

<a id="blkcache.backend.config_complete"></a>

#### config\_complete

```python
def config_complete() -> None
```

Validates required parameters.

<a id="blkcache.backend.open"></a>

#### open

```python
def open(_readonly: bool) -> int
```

Opens device and returns handle ID.

<a id="blkcache.backend.get_size"></a>

#### get\_size

```python
def get_size(h: int) -> int
```

Get file size.

<a id="blkcache.backend.pread"></a>

#### pread

```python
def pread(h: int, count: int, offset: int) -> bytes
```

Read data at offset.

<a id="blkcache.backend.close"></a>

#### close

```python
def close(h: int) -> None
```

Close file handle.

<a id="blkcache.ddrescue"></a>

# blkcache.ddrescue

ddrescue file format loading and saving.

Functions to read/write ddrescue-compatible mapfiles with comments,
config, and FileMap data.

<a id="blkcache.ddrescue.iter_filemap_ranges"></a>

#### iter\_filemap\_ranges

```python
def iter_filemap_ranges(filemap: FileMap)
```

Iterate over FileMap transitions yielding (pos, size, status) tuples.

<a id="blkcache.ddrescue.load"></a>

#### load

```python
def load(file, comments: List[str], filemap: FileMap,
         config: Dict[str, str]) -> None
```

Load ddrescue mapfile from file-like object, updating provided containers.

<a id="blkcache.ddrescue.save"></a>

#### save

```python
def save(file, comments: List[str], filemap: FileMap,
         config: Dict[str, str]) -> None
```

Save ddrescue mapfile to file-like object from provided containers.

<a id="blkcache.ddrescue.parse_status"></a>

#### parse\_status

```python
def parse_status(line: str) -> tuple[int, int, str]
```

Parse a status line returning (start, size, status).

<a id="blkcache.main"></a>

# blkcache.main

blkcache – CLI entry-point.

<a id="blkcache.server"></a>

# blkcache.server

blkcache.server – userspace read-through cache via nbdkit + nbdfuse.

