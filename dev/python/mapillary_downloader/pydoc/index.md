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
def convert_to_webp(jpg_path, output_path=None, delete_original=True)
```

Convert a JPG image to WebP format, preserving EXIF metadata.

**Arguments**:

- `jpg_path` - Path to the JPG file
- `output_path` - Optional path for the WebP output. If None, uses jpg_path with .webp extension
- `delete_original` - Whether to delete the original JPG after conversion (default: True)
  

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

<a id="mapillary_downloader.tar_sequences"></a>

# mapillary\_downloader.tar\_sequences

Tar sequence directories for efficient Internet Archive uploads.

<a id="mapillary_downloader.tar_sequences.tar_sequence_directories"></a>

#### tar\_sequence\_directories

```python
def tar_sequence_directories(collection_dir)
```

Tar all sequence directories in a collection for faster IA uploads.

**Arguments**:

- `collection_dir` - Path to collection directory (e.g., mapillary-user-quality/)
  

**Returns**:

  Tuple of (tarred_count, total_files_tarred)

<a id="mapillary_downloader.ia_check"></a>

# mapillary\_downloader.ia\_check

Check if collections exist on Internet Archive.

<a id="mapillary_downloader.ia_check.check_ia_exists"></a>

#### check\_ia\_exists

```python
def check_ia_exists(collection_name)
```

Check if a collection exists on Internet Archive.

**Arguments**:

- `collection_name` - Name of the collection (e.g., mapillary-username-original-webp)
  

**Returns**:

  Boolean indicating if the collection exists on IA

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

<a id="mapillary_downloader.downloader.get_cache_dir"></a>

#### get\_cache\_dir

```python
def get_cache_dir()
```

Get XDG cache directory for staging downloads.

**Returns**:

  Path to cache directory for mapillary_downloader

<a id="mapillary_downloader.downloader.MapillaryDownloader"></a>

## MapillaryDownloader Objects

```python
class MapillaryDownloader()
```

Handles downloading Mapillary data for a user.

<a id="mapillary_downloader.downloader.MapillaryDownloader.__init__"></a>

#### \_\_init\_\_

```python
def __init__(client,
             output_dir,
             username=None,
             quality=None,
             max_workers=128,
             tar_sequences=True,
             convert_webp=False,
             check_ia=True)
```

Initialize the downloader.

**Arguments**:

- `client` - MapillaryClient instance
- `output_dir` - Base directory to save downloads (final destination)
- `username` - Mapillary username (for collection directory)
- `quality` - Image quality (for collection directory)
- `max_workers` - Maximum number of parallel workers (default: 128)
- `tar_sequences` - Whether to tar sequence directories after download (default: True)
- `convert_webp` - Whether to convert images to WebP (affects collection name)
- `check_ia` - Whether to check if collection exists on Internet Archive (default: True)

<a id="mapillary_downloader.downloader.MapillaryDownloader.download_user_data"></a>

#### download\_user\_data

```python
def download_user_data(bbox=None, convert_webp=False)
```

Download all images for a user using streaming queue-based architecture.

**Arguments**:

- `bbox` - Optional bounding box [west, south, east, north]
- `convert_webp` - Convert images to WebP format after download

<a id="mapillary_downloader.metadata_reader"></a>

# mapillary\_downloader.metadata\_reader

Streaming metadata reader with filtering.

<a id="mapillary_downloader.metadata_reader.MetadataReader"></a>

## MetadataReader Objects

```python
class MetadataReader()
```

Streams metadata.jsonl line-by-line with filtering.

This avoids loading millions of image dicts into memory.

<a id="mapillary_downloader.metadata_reader.MetadataReader.__init__"></a>

#### \_\_init\_\_

```python
def __init__(metadata_file)
```

Initialize metadata reader.

**Arguments**:

- `metadata_file` - Path to metadata.jsonl or metadata.jsonl.gz

<a id="mapillary_downloader.metadata_reader.MetadataReader.iter_images"></a>

#### iter\_images

```python
def iter_images(quality_field=None, downloaded_ids=None)
```

Stream images from metadata file with filtering.

**Arguments**:

- `quality_field` - Optional field to check exists (e.g., 'thumb_1024_url')
- `downloaded_ids` - Optional set of already downloaded IDs to skip
  

**Yields**:

  Image metadata dicts that pass filters

<a id="mapillary_downloader.metadata_reader.MetadataReader.get_all_ids"></a>

#### get\_all\_ids

```python
def get_all_ids()
```

Get set of all image IDs in metadata file.

**Returns**:

  Set of image IDs (for building seen_ids)

<a id="mapillary_downloader.metadata_reader.MetadataReader.mark_complete"></a>

#### mark\_complete

```python
@staticmethod
def mark_complete(metadata_file)
```

Append completion marker to metadata file.

**Arguments**:

- `metadata_file` - Path to metadata.jsonl

<a id="mapillary_downloader.worker"></a>

# mapillary\_downloader.worker

Worker process for parallel image download and conversion.

<a id="mapillary_downloader.worker.worker_process"></a>

#### worker\_process

```python
def worker_process(work_queue, result_queue, worker_id)
```

Worker process that pulls from queue and processes images.

**Arguments**:

- `work_queue` - Queue to pull work items from
- `result_queue` - Queue to push results to
- `worker_id` - Unique worker identifier

<a id="mapillary_downloader.worker.download_and_convert_image"></a>

#### download\_and\_convert\_image

```python
def download_and_convert_image(image_data, output_dir, quality, convert_webp,
                               session)
```

Download and optionally convert a single image.

This function is designed to run in a worker process.

**Arguments**:

- `image_data` - Image metadata dict from API
- `output_dir` - Base output directory path
- `quality` - Quality level (256, 1024, 2048, original)
- `convert_webp` - Whether to convert to WebP
- `session` - requests.Session with auth already configured
  

**Returns**:

  Tuple of (image_id, bytes_downloaded, success, error_msg)

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

<a id="mapillary_downloader.logging_config.add_file_handler"></a>

#### add\_file\_handler

```python
def add_file_handler(log_file, level=logging.INFO)
```

Add a file handler to the logger for archival.

**Arguments**:

- `log_file` - Path to log file
- `level` - Logging level for file handler

<a id="mapillary_downloader.ia_meta"></a>

# mapillary\_downloader.ia\_meta

Internet Archive metadata generation for Mapillary collections.

<a id="mapillary_downloader.ia_meta.parse_collection_name"></a>

#### parse\_collection\_name

```python
def parse_collection_name(directory)
```

Parse username and quality from directory name.

**Arguments**:

- `directory` - Path to collection directory (e.g., mapillary-username-original or mapillary-username-original-webp)
  

**Returns**:

  Tuple of (username, quality) or (None, None) if parsing fails

<a id="mapillary_downloader.ia_meta.get_date_range"></a>

#### get\_date\_range

```python
def get_date_range(metadata_file)
```

Get first and last captured_at dates from metadata.jsonl.gz.

**Arguments**:

- `metadata_file` - Path to metadata.jsonl.gz file
  

**Returns**:

  Tuple of (first_date, last_date) as ISO format strings, or (None, None)

<a id="mapillary_downloader.ia_meta.count_images"></a>

#### count\_images

```python
def count_images(metadata_file)
```

Count number of images in metadata.jsonl.gz.

**Arguments**:

- `metadata_file` - Path to metadata.jsonl.gz file
  

**Returns**:

  Number of images

<a id="mapillary_downloader.ia_meta.write_meta_tag"></a>

#### write\_meta\_tag

```python
def write_meta_tag(meta_dir, tag, values)
```

Write metadata tag files in rip format.

**Arguments**:

- `meta_dir` - Path to .meta directory
- `tag` - Tag name
- `values` - Single value or list of values

<a id="mapillary_downloader.ia_meta.generate_ia_metadata"></a>

#### generate\_ia\_metadata

```python
def generate_ia_metadata(collection_dir)
```

Generate Internet Archive metadata for a Mapillary collection.

**Arguments**:

- `collection_dir` - Path to collection directory (e.g., ./mapillary_data/mapillary-username-original)
  

**Returns**:

  True if successful, False otherwise

<a id="mapillary_downloader.worker_pool"></a>

# mapillary\_downloader.worker\_pool

Adaptive worker pool for parallel processing.

<a id="mapillary_downloader.worker_pool.AdaptiveWorkerPool"></a>

## AdaptiveWorkerPool Objects

```python
class AdaptiveWorkerPool()
```

Worker pool that scales based on throughput.

Monitors throughput every 30 seconds and adjusts worker count:
- If throughput increasing: add workers (up to max)
- If throughput plateauing/decreasing: reduce workers

<a id="mapillary_downloader.worker_pool.AdaptiveWorkerPool.__init__"></a>

#### \_\_init\_\_

```python
def __init__(worker_func,
             min_workers=4,
             max_workers=16,
             monitoring_interval=10)
```

Initialize adaptive worker pool.

**Arguments**:

- `worker_func` - Function to run in each worker (must accept work_queue, result_queue)
- `min_workers` - Minimum number of workers
- `max_workers` - Maximum number of workers
- `monitoring_interval` - Seconds between throughput checks

<a id="mapillary_downloader.worker_pool.AdaptiveWorkerPool.start"></a>

#### start

```python
def start()
```

Start the worker pool.

<a id="mapillary_downloader.worker_pool.AdaptiveWorkerPool.submit"></a>

#### submit

```python
def submit(work_item)
```

Submit work to the pool (blocks if queue is full).

<a id="mapillary_downloader.worker_pool.AdaptiveWorkerPool.get_result"></a>

#### get\_result

```python
def get_result(timeout=None)
```

Get a result from the workers.

**Returns**:

  Result from worker, or None if timeout

<a id="mapillary_downloader.worker_pool.AdaptiveWorkerPool.check_throughput"></a>

#### check\_throughput

```python
def check_throughput(total_processed)
```

Check throughput and adjust workers if needed.

**Arguments**:

- `total_processed` - Total number of items processed so far

<a id="mapillary_downloader.worker_pool.AdaptiveWorkerPool.shutdown"></a>

#### shutdown

```python
def shutdown(timeout=2)
```

Shutdown the worker pool gracefully.

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

