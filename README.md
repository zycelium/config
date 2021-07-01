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

Config file name: `"config.ini"`

Paths to look for the config file (current working directory): `["."]`

### Specify file-name for configuration:

```python
from zycelium.dataconfig import dataconfig


@dataconfig(file="custom_config.ini")
class Config:
    name: str = "World"

config = Config().load()

print(f"Hello, {config.name}!")
```

In this example, we specify the file-name on this line:
`@dataconfig(file="custom_config.ini")` with keyword arguments
`file="custom_config.ini"` passed to `@dataconfig()`.

### Specify file-lookup-paths:

```python
from zycelium.dataconfig import dataconfig


@dataconfig(paths=[".", "examples", "/usr/local/etc])
class Config:
    name: str = "World"

config = Config().load()

print(f"Hello, {config.name}!")
```

Here, we pass `paths=[".", "examples"]` to `@dataconfig()`
to specify the paths on filesystem where `dataconfig` should
look for the default `"config.ini"` file. We can also specify
the filename along with the paths. Paths can be relative 
to current working directory or absolute.