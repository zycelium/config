import click
from zycelium.dataconfig import dataconfig


@dataconfig
class Config:
    name: str = "World"


config = Config()
config.load()


@click.command()
@click.option("--name")
@config.click_option()
def test_cmd(name):
    print(f"Hello, {name}!")
    print(f"Hello, {config.name}!")


test_cmd()