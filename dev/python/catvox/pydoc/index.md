<a id="catvox"></a>

# catvox

<a id="catvox.utils"></a>

# catvox.utils

<a id="catvox.utils.classproperty"></a>

# catvox.utils.classproperty

<a id="catvox.utils.classproperty.classproperty"></a>

## classproperty Objects

```python
class classproperty()
```

Our old friend, the class property.

<a id="catvox.utils.monkeypipe"></a>

# catvox.utils.monkeypipe

<a id="catvox.transcribe"></a>

# catvox.transcribe

<a id="catvox.transcribe.whisper"></a>

# catvox.transcribe.whisper

<a id="catvox.transcribe.whisper.Whisper"></a>

## Whisper Objects

```python
class Whisper()
```

<a id="catvox.transcribe.whisper.Whisper.transcribe"></a>

#### transcribe

```python
def transcribe(audio, max_length, duration)
```

Run the transcription loop in the foreground:
- Read audio from `audio.read()`
- Accumulate until `duration` seconds have passed, then run `model.transcribe(buffer)`
- If stable, print transcript.
- If max_length reached, print whatever we have.

<a id="catvox.inputs"></a>

# catvox.inputs

<a id="catvox.inputs.Input"></a>

## Input Objects

```python
class Input(abc.ABC)
```

<a id="catvox.inputs.Input.start"></a>

#### start

```python
@abc.abstractmethod
def start(device=None)
```

Start capturing audio.

<a id="catvox.inputs.Input.stop"></a>

#### stop

```python
@abc.abstractmethod
def stop()
```

Stop capturing audio.

<a id="catvox.inputs.Input.is_running"></a>

#### is\_running

```python
@property
def is_running()
```

Return True if audio capture is currently running.

<a id="catvox.inputs.Input.sample_rate"></a>

#### sample\_rate

```python
@property
def sample_rate()
```

Return the samplerate of the audio source.

<a id="catvox.inputs.Input.devices"></a>

#### devices

```python
@property
def devices()
```

Return a copy of the devices dictionary.
Key and description.

<a id="catvox.inputs.Input.device"></a>

#### device

```python
@property
def device()
```

Return the current device identifier.

<a id="catvox.inputs.Input.read"></a>

#### read

```python
@abc.abstractmethod
def read(timeout=None)
```

Return a chunk of audio samples as a NumPy array, or None if:
- No data is available within 'timeout', or
- The audio is stopped and no more data is forthcoming.

Blocks up to `timeout` seconds if no data is immediately available.

<a id="catvox.inputs.sounddevice"></a>

# catvox.inputs.sounddevice

<a id="catvox.inputs.sounddevice.SoundDevice"></a>

## SoundDevice Objects

```python
class SoundDevice(Input)
```

Audio source using the `sounddevice` library.

<a id="catvox.inputs.sounddevice.SoundDevice.start"></a>

#### start

```python
def start(device=None)
```

Start capturing audio from the selected device.

<a id="catvox.inputs.sounddevice.SoundDevice.stop"></a>

#### stop

```python
def stop()
```

Stop capturing audio.

<a id="catvox.inputs.sounddevice.SoundDevice.read"></a>

#### read

```python
def read(timeout=None)
```

Return a chunk of audio samples as a flat float32 NumPy array.
If no data is available within 'timeout', returns None.
If the source is stopped and no data is left, returns None.

<a id="catvox.inputs.sources"></a>

# catvox.inputs.sources

<a id="catvox.main"></a>

# catvox.main

<a id="catvox.args"></a>

# catvox.args

