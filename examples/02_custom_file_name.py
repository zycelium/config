from zycelium.dataconfig import dataconfig


@dataconfig(file="custom_config.ini")
class Config:
    name: str = "World"

config = Config()
config.load()

print(f"Hello, {config.name}!")
