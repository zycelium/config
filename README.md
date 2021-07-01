# zycelium.dataconfig

Create [dataclasses](https://docs.python.org/3/library/dataclasses.html) backed by configuration files.

## Usage


### Use Defaults

Create a new python script and name it `example.py`

```python
from zycelium.dataconfig import dataconfig


@dataconfig
class Config:
    name: str = "World"

config = Config().load()

print(f"Hello, {config.name}!")
```

Create a `config.ini` file in the same directory as `example.py`

```ini
name = "DataConfig"
```

Finally, from the same directory, run `python example.py` , 
your console session should look something like this:

```console
$ python example.py
Hello, DataConfig!
```

The defaults here are:

Config file name: "config.ini"

Paths to look for the config file (current working directory): ["."]

