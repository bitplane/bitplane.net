<a id="ienv"></a>

# ienv

<a id="ienv.stats"></a>

# ienv.stats

Stats will go here eventually

<a id="ienv.stats.print_stats"></a>

#### print\_stats

```python
def print_stats()
```

Doesn't do much yet really.

<a id="ienv.squish"></a>

# ienv.squish

This bit moves your files around.

<a id="ienv.squish.BUFFER_SIZE"></a>

#### BUFFER\_SIZE

10MB chunks

<a id="ienv.squish.hash_and_copy"></a>

#### hash\_and\_copy

```python
def hash_and_copy(source, dest=None)
```

If we can't use a hardlink to do a quick copy then we'll have to do a full
copy. This function will hash the file as it copies it, if there's a dest.

<a id="ienv.squish.backup_file"></a>

#### backup\_file

```python
def backup_file(source, dest_dir)
```

You can bet the user will get bored and CTRL+C out and endup with
missing files, which we don't really want. This function tries to
hardlink the file first, and if that fails it'll do a full copy
while hashing its contents. It's not perfect, but it'll make it
pretty hard to lose data.

<a id="ienv.squish.replace_with_symlink"></a>

#### replace\_with\_symlink

```python
def replace_with_symlink(source, dest)
```

Replace the source file with a symlink to the dest file, after the
backup has been made. This is atomic on Linux, but not on Windows.
But either way, if you lose a file because you were interrupted while
renaming one file over the top of another then you're really unlucky,
as well as having a crap OS.

<a id="ienv.squish.process_venv"></a>

#### process\_venv

```python
def process_venv(venv_dir)
```

Actually iterate over all the files.

Make backups into the cache dir, make a link to the backup, copy its attribs
and then move the link over the source.

<a id="ienv.main"></a>

# ienv.main

Entrypoint to the module.

<a id="ienv.venv"></a>

# ienv.venv

Deals with virtual environments.

<a id="ienv.venv.MIN_FILE_SIZE"></a>

#### MIN\_FILE\_SIZE

4k, size of a single block on most filesystems

<a id="ienv.venv.venv_dir"></a>

#### venv\_dir

```python
def venv_dir(directory)
```

Validates a "venv_dir" and acts as a custom type. Not really needed but I like
this sort of thing.

<a id="ienv.venv.get_package_files"></a>

#### get\_package\_files

```python
def get_package_files(venv_dir)
```

Return all the files under site-packages in the given venv.

<a id="ienv.venv.get_large_package_files"></a>

#### get\_large\_package\_files

```python
def get_large_package_files(venv_dir)
```

Return all the files in a venv that are larger than MIN_FILE_SIZE.

<a id="ienv.cache"></a>

# ienv.cache

The cache dir, which lives at ~/.cache/ienv

It's where all your files have been moved to.

<a id="ienv.cache.get_cache_dir"></a>

#### get\_cache\_dir

```python
def get_cache_dir(prefix="~")
```

Return the cache dir, creating it if it doesn't exist.

<a id="ienv.cache.load_venv_list"></a>

#### load\_venv\_list

```python
def load_venv_list(file_path)
```

Load the list of venvs that have been squished.

<a id="ienv.cache.save_venv_list"></a>

#### save\_venv\_list

```python
def save_venv_list(file_path, venvs)
```

Save the list of venvs that have been squished.

<a id="ienv.__main__"></a>

# ienv.\_\_main\_\_

