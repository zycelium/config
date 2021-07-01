from zycelium.dataconfig import dataconfig


@dataconfig(paths=[".", "examples", "/usr/local/etc"])
class Config:
    name: str = "World"

config = Config()
config.load()

print(f"Hello, {config.name}!")
