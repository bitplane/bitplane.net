# Use in Pydantic models

You'll need Pydantic >=2.3:

```python
from pydantic import BaseModel, Field


class BinaryPatch(BaseModel):
    regions: Ranges


model = BinaryPatch.model_validate_json("""
{
    "regions": "0:10, 20:30, 15:, 0x0b"
}
""")

assert model.regions == ":10,15:"
```
