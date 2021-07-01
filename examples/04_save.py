from zycelium.dataconfig import dataconfig

FILE_NAME = "newconfig.ini"

@dataconfig(file=FILE_NAME)
class Config:
    name: str = "World"

config = Config()

config.save()
# config.save(overwrite=True)

print(f"Saved config to file: {FILE_NAME}.")
