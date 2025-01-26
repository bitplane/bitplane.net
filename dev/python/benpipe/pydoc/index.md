<a id="benpipe"></a>

# benpipe

Entry point when run as a package

<a id="benpipe.benpipe"></a>

# benpipe.benpipe

<a id="benpipe.benpipe.to_json"></a>

#### to\_json

```python
def to_json(bencoded_data)
```

Convert bencoded data to JSON.

<a id="benpipe.benpipe.to_bencode"></a>

#### to\_bencode

```python
def to_bencode(json_data)
```

Convert JSON data to bencoded format.

<a id="benpipe.benpipe.try_both"></a>

#### try\_both

```python
def try_both()
```

Attempt bencode -> JSON. If that fails, assume input is JSON and try JSON -> bencode.

<a id="benpipe.__main__"></a>

# benpipe.\_\_main\_\_

Entry point when run as a package

