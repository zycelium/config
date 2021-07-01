from zycelium.dataconfig import dataconfig


@dataconfig
class Config:
    name: str = "World"

config = Config()
config.load()

print(f"Hello, {config.name}!")
