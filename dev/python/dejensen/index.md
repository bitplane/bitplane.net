# 🧥 dejensen

Remove pauses from presentation videos.

## Why?

Pauses.. are good ... for dramatic effect. When watching? ...
... Not so much.

## How?

```bash
pipx dejensen https://www.youtube.com/watch?v=VIDEO_ID
```

It...

1. Downloads a video using `yt-dlp` (or uses a local file)
2. Extracts word-level timestamps using OpenAI's Whisper
3. Identifies gaps between words that exceed a threshold (default 0.2 seconds)
4. Uses ffmpeg to cut out the gaps and reassemble the video

## Requirements

- 🐍 Python 3.10+
- 📼 ffmpeg and ffprobe must be installed and in PATH

## License

WTFPL + Warranty. Do whatever you like, but don't blame me if your punchlines
land early.
