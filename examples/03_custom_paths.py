from zycelium.dataconfig import dataconfig


@dataconfig(paths=[".", "examples"])
class Config:
    name: str = "World"

config = Config().load()

print(f"Hello, {config.name}!")
