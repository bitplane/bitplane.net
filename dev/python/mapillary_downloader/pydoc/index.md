<a id="mapillary_downloader"></a>

# mapillary\_downloader

Mapillary data downloader.

<a id="mapillary_downloader.webp_converter"></a>

# mapillary\_downloader.webp\_converter

WebP image conversion utilities.

<a id="mapillary_downloader.webp_converter.check_cwebp_available"></a>

#### check\_cwebp\_available

```python
def check_cwebp_available()
```

Check if cwebp binary is available.

**Returns**:

- `bool` - True if cwebp is found, False otherwise

<a id="mapillary_downloader.webp_converter.convert_to_webp"></a>

#### convert\_to\_webp

```python
def convert_to_webp(jpg_path)
```

Convert a JPG image to WebP format, preserving EXIF metadata.

**Arguments**:

- `jpg_path` - Path to the JPG file
  

**Returns**:

  Path object to the new WebP file, or None if conversion failed

<a id="mapillary_downloader.exif_writer"></a>

# mapillary\_downloader.exif\_writer

EXIF metadata writer for Mapillary images.

<a id="mapillary_downloader.exif_writer.decimal_to_dms"></a>

#### decimal\_to\_dms

```python
def decimal_to_dms(decimal)
```

Convert decimal degrees to degrees, minutes, seconds format for EXIF.

**Arguments**:

- `decimal` - Decimal degrees (can be negative)
  

**Returns**:

  Tuple of ((degrees, 1), (minutes, 1), (seconds, 100)) as rational numbers

<a id="mapillary_downloader.exif_writer.timestamp_to_exif_datetime"></a>

#### timestamp\_to\_exif\_datetime

```python
def timestamp_to_exif_datetime(timestamp)
```

Convert Unix timestamp to EXIF datetime string.

**Arguments**:

- `timestamp` - Unix timestamp in milliseconds
  

**Returns**:

  String in format "YYYY:MM:DD HH:MM:SS"

<a id="mapillary_downloader.exif_writer.write_exif_to_image"></a>

#### write\_exif\_to\_image

```python
def write_exif_to_image(image_path, metadata)
```

Write EXIF metadata from Mapillary API to downloaded image.

**Arguments**:

- `image_path` - Path to the downloaded image file
- `metadata` - Dictionary of metadata from Mapillary API
  

**Returns**:

  True if successful, False otherwise

<a id="mapillary_downloader.utils"></a>

# mapillary\_downloader.utils

Utility functions for formatting and display.

<a id="mapillary_downloader.utils.format_size"></a>

#### format\_size

```python
def format_size(bytes_count)
```

Format bytes as human-readable size.

**Arguments**:

- `bytes_count` - Number of bytes
  

**Returns**:

  Formatted string (e.g. "1.23 GB", "456.78 MB")

<a id="mapillary_downloader.utils.format_time"></a>

#### format\_time

```python
def format_time(seconds)
```

Format seconds as human-readable time.

**Arguments**:

- `seconds` - Number of seconds
  

**Returns**:

  Formatted string (e.g. "2h 15m", "45m 30s", "30s")

<a id="mapillary_downloader.__main__"></a>

# mapillary\_downloader.\_\_main\_\_

CLI entry point.

<a id="mapillary_downloader.__main__.main"></a>

#### main

```python
def main()
```

Main CLI entry point.

<a id="mapillary_downloader.downloader"></a>

# mapillary\_downloader.downloader

Main downloader logic.

<a id="mapillary_downloader.downloader.MapillaryDownloader"></a>

## MapillaryDownloader Objects

```python
class MapillaryDownloader()
```

Handles downloading Mapillary data for a user.

<a id="mapillary_downloader.downloader.MapillaryDownloader.__init__"></a>

#### \_\_init\_\_

```python
def __init__(client, output_dir)
```

Initialize the downloader.

**Arguments**:

- `client` - MapillaryClient instance
- `output_dir` - Directory to save downloads

<a id="mapillary_downloader.downloader.MapillaryDownloader.download_user_data"></a>

#### download\_user\_data

```python
def download_user_data(username,
                       quality="original",
                       bbox=None,
                       convert_webp=False)
```

Download all images for a user.

**Arguments**:

- `username` - Mapillary username
- `quality` - Image quality to download (256, 1024, 2048, original)
- `bbox` - Optional bounding box [west, south, east, north]
- `convert_webp` - Convert images to WebP format after download

<a id="mapillary_downloader.logging_config"></a>

# mapillary\_downloader.logging\_config

Logging configuration with colored output for TTY.

<a id="mapillary_downloader.logging_config.ColoredFormatter"></a>

## ColoredFormatter Objects

```python
class ColoredFormatter(logging.Formatter)
```

Formatter that adds color to log levels when output is a TTY.

<a id="mapillary_downloader.logging_config.ColoredFormatter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fmt=None, datefmt=None, use_color=True)
```

Initialize the formatter.

**Arguments**:

- `fmt` - Log format string
- `datefmt` - Date format string
- `use_color` - Whether to use colored output

<a id="mapillary_downloader.logging_config.ColoredFormatter.format"></a>

#### format

```python
def format(record)
```

Format the log record with colors if appropriate.

**Arguments**:

- `record` - LogRecord to format
  

**Returns**:

  Formatted log string

<a id="mapillary_downloader.logging_config.setup_logging"></a>

#### setup\_logging

```python
def setup_logging(level=logging.INFO)
```

Set up logging with timestamps and colored output.

**Arguments**:

- `level` - Logging level to use

<a id="mapillary_downloader.client"></a>

# mapillary\_downloader.client

Mapillary API client.

<a id="mapillary_downloader.client.MapillaryClient"></a>

## MapillaryClient Objects

```python
class MapillaryClient()
```

Client for interacting with Mapillary API v4.

<a id="mapillary_downloader.client.MapillaryClient.__init__"></a>

#### \_\_init\_\_

```python
def __init__(access_token)
```

Initialize the client with an access token.

**Arguments**:

- `access_token` - Mapillary API access token

<a id="mapillary_downloader.client.MapillaryClient.get_user_images"></a>

#### get\_user\_images

```python
def get_user_images(username, bbox=None, limit=2000)
```

Get images uploaded by a specific user.

**Arguments**:

- `username` - Mapillary username
- `bbox` - Optional bounding box [west, south, east, north]
- `limit` - Number of results per page (max 2000)
  

**Yields**:

  Image data dictionaries

<a id="mapillary_downloader.client.MapillaryClient.download_image"></a>

#### download\_image

```python
def download_image(image_url, output_path)
```

Download an image from a URL.

**Arguments**:

- `image_url` - URL of the image to download
- `output_path` - Path to save the image
  

**Returns**:

  Number of bytes downloaded if successful, 0 otherwise

