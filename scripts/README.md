# Useful Scripts

Recurring snippets:
+ https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
```python
import json
from types import SimpleNamespace

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x.name, x.hometown.name, x.hometown.id)
```

+ https://stackoverflow.com/questions/1305532/convert-nested-python-dict-to-object
+ https://stackoverflow.com/questions/4984647/accessing-dict-keys-like-an-attribute
+ https://stackoverflow.com/questions/18283725/how-to-create-a-python-dictionary-with-double-quotes-as-default-quote-format
