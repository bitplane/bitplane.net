# Some tools

The [tools dir](https://github.com/bitplane/undockit/tree/master/tools) contains
some executable Dockerfiles that you can use. These have been pushed to Docker
Hub [here](https://hub.docker.com/u/bitplanenet). You can execute them yourself,
or use the prebuilt versions, for example:

```bash
undockit install docker.io/bitplanenet/whisper
```

## Speech to Text

### `whisper`

Whisper is OpenAI's speech to text model. Run `whisper some_file.whatever` and
it'll create subtitles in a bunch of formats. It can also be used to translate
as it transcribes. See `--help` for more info.

## Song separation

### `spleeter`

Spleeter is Deezer's song separation model. You can make karaoke tracks with it
by splitting out the vocals. It does other things like drums, bass and so on,
and you can train it on your own files. By default it does the karaoke thing,

### `demucs`

Demucs is Facebook's song splitting model. Same as the above really.


