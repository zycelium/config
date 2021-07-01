from zycelium.dataconfig import dataconfig


@dataconfig(frozen=True)
class Config:
    name: str = "World"


# Following line throws: 
#   dataclasses.FrozenInstanceError: cannot assign to field 'name'
config = Config().load()

# To properly load a frozen dataconfig, pass `replace=True` to load().
# Comment-out the line above and uncomment below for expected behaviour:

# config = Config().load(replace=True)

print(f"Hello, {config.name}!")
