# 🔦 torch_weightsonly

Torch finally decided to stop loading and executing arbitrary code, and to
tell everyone about it every time they load a model. The warnings were
annoying me, so I made an auto-monkey-patch module that makes submodules
safe, and put it on pypi.

To use it:

```bash
pip install torch_weightsonly
```

Then either import it as a replacement:

```python
import torch_weightsonly as torch
```

Or import it before a module that depends on torch:

```python
import torch_weightsonly  # noqa
import whisper
```

And providing you aren't doing anything unsafe, the warnings will go away and
your code will work as normal.

* [🐍 pypi](https://pypi.org/project/torch-weightsonly/)
* [😸 github](https://github.com/bitpane/torch_weightsonly)

