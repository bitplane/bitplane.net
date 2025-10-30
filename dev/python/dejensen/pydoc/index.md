<a id="dejensen"></a>

# dejensen

dejensen - Remove annoying pauses from presentation videos.

<a id="dejensen.transcriber"></a>

# dejensen.transcriber

Audio transcription using Whisper.

<a id="dejensen.transcriber.extract_timestamps"></a>

#### extract\_timestamps

```python
def extract_timestamps(video_path: Path,
                       model_name: str = "base") -> list[dict]
```

Extract word-level timestamps from a video using Whisper.

**Arguments**:

- `video_path` - Path to the video file
- `model_name` - Whisper model to use (tiny, base, small, medium, large)
  

**Returns**:

  List of word dictionaries with 'word', 'start', and 'end' keys

<a id="dejensen.transcriber.save_timestamps"></a>

#### save\_timestamps

```python
def save_timestamps(words: list[dict], output_path: Path) -> None
```

Save word timestamps to a JSON file.

<a id="dejensen.transcriber.load_timestamps"></a>

#### load\_timestamps

```python
def load_timestamps(input_path: Path) -> list[dict]
```

Load word timestamps from a JSON file.

<a id="dejensen.cli"></a>

# dejensen.cli

Command-line interface for dejensen.

<a id="dejensen.cli.main"></a>

#### main

```python
def main()
```

Main entry point for the dejensen CLI.

<a id="dejensen.downloader"></a>

# dejensen.downloader

Video downloading using yt-dlp.

<a id="dejensen.downloader.download_video"></a>

#### download\_video

```python
def download_video(url: str, output_dir: Path) -> Path
```

Download a video using yt-dlp.

**Arguments**:

- `url` - The video URL to download
- `output_dir` - Directory to save the video
  

**Returns**:

  Path to the downloaded video file

<a id="dejensen.gap_detector"></a>

# dejensen.gap\_detector

Detect gaps/pauses in word timestamps.

<a id="dejensen.gap_detector.find_gaps"></a>

#### find\_gaps

```python
def find_gaps(words: list[dict],
              max_gap: float = 0.2) -> list[tuple[float, float]]
```

Find gaps between words that exceed the maximum gap threshold.

**Arguments**:

- `words` - List of word dictionaries with 'start' and 'end' keys
- `max_gap` - Maximum allowed gap in seconds (default 0.2)
  

**Returns**:

  List of (start, end) tuples representing gaps to remove

<a id="dejensen.gap_detector.calculate_keep_segments"></a>

#### calculate\_keep\_segments

```python
def calculate_keep_segments(
        words: list[dict],
        max_gap: float = 0.2,
        video_duration: float | None = None) -> list[tuple[float, float]]
```

Calculate video segments to keep (inverse of gaps).

Extends segments into gaps by half the max_gap threshold on each side to avoid cutting off
breaths, trailing sounds, etc due to Whisper timestamp inaccuracies.

**Arguments**:

- `words` - List of word dictionaries with 'start' and 'end' keys
- `max_gap` - Maximum allowed gap in seconds
- `video_duration` - Total video duration in seconds (if None, uses last word end time)
  

**Returns**:

  List of (start, end) tuples representing segments to keep

<a id="dejensen.video_editor"></a>

# dejensen.video\_editor

Video editing using ffmpeg.

<a id="dejensen.video_editor.get_video_duration"></a>

#### get\_video\_duration

```python
def get_video_duration(video_path: Path) -> float
```

Get the duration of a video file in seconds.

**Arguments**:

- `video_path` - Path to the video file
  

**Returns**:

  Duration in seconds

<a id="dejensen.video_editor.cut_segments"></a>

#### cut\_segments

```python
def cut_segments(video_path: Path,
                 segments: list[tuple[float, float]],
                 output_path: Path,
                 work_dir: Path | None = None) -> None
```

Cut video segments using ffmpeg select filter in a single pass.

**Arguments**:

- `video_path` - Path to the input video
- `segments` - List of (start, end) tuples in seconds
- `output_path` - Path for the output video
- `work_dir` - Unused, kept for compatibility

