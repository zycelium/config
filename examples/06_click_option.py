import click
from zycelium.dataconfig import dataconfig


@dataconfig
class Config:
    name: str = "World"


config = Config()
# No need to load() config when using click_option()


@click.command()
@click.option("--name")
@config.click_option()
def main(name):
    print(f"Hello, {name}!")
    print(f"Hello, {config.name}!")


main()
