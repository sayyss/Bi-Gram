### Bi-Gram

Simple bi-gram implementation using pytorch. 


### Usage
```python
from main import train

model = train("text.txt")
model.generate("this is the", length=10)
```

- train() has configurable parameters given by
```python
    defaults = {
        'epochs': 100,
        'lr': 0.001,
    }

```
