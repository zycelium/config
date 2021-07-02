from dataclasses import dataclass, is_dataclass, FrozenInstanceError
from pathlib import Path

import click
import pytest
from click.testing import CliRunner

from zycelium.dataconfig import dataconfig, locate

TEST_FILE_NAME = "testconfig.ini"
DEFAULT_FILE_NAME = "config.ini"
TEST_PATHS = [".", "tests/"]
DEFAULT_PATHS = ["."]


def test_dataconfig_init_bare():
    @dataconfig
    class Config:
        pass

    config = Config()
    assert is_dataclass(config)
    assert config._file == DEFAULT_FILE_NAME
    assert config._auto == True
    assert config._paths == DEFAULT_PATHS


def test_dataconfig_init_with_file():
    @dataconfig(file=TEST_FILE_NAME)
    class Config:
        pass

    config = Config()
    assert is_dataclass(config)
    assert config._file == TEST_FILE_NAME


def test_dataconfig_init_without_file():
    @dataconfig()
    class Config:
        pass

    config = Config()
    assert config._file == DEFAULT_FILE_NAME


def test_dataconfig_init_with_paths():
    @dataconfig(paths=TEST_PATHS)
    class Config:
        pass

    config = Config()
    assert config._paths == TEST_PATHS


@pytest.mark.xfail(raises=FrozenInstanceError)
def test_frozen_dataconfig():
    @dataconfig(frozen=True)
    class Config:
        message: str = "test"

    config = Config()
    assert config.message == "test"
    config.message = "fail"


def test_locate():
    path = locate(TEST_FILE_NAME, TEST_PATHS, auto=True)
    assert path == Path("tests").joinpath(TEST_FILE_NAME)


def test_locate_with_file_path():
    path = locate(
        TEST_FILE_NAME, TEST_PATHS, auto=True, file_path=TEST_FILE_NAME
    )
    assert path == Path(TEST_FILE_NAME)


def test_locate_missing_file_auto():
    path = locate(TEST_FILE_NAME, DEFAULT_PATHS, auto=True)
    assert path == Path(".").joinpath(TEST_FILE_NAME)


@pytest.mark.xfail(raises=FileNotFoundError)
def test_locate_missing_file_no_auto():
    path = locate(TEST_FILE_NAME, DEFAULT_PATHS, auto=False)


def test_load_preset_path():
    @dataconfig(file=TEST_FILE_NAME, paths=TEST_PATHS)
    class Config:
        message: str = "test"

    config = Config()
    config.load()

    assert config.message == "hello-test"


def test_load_custom_path():
    @dataconfig
    class Config:
        message: str = "test"

    path = Path("tests/").joinpath(TEST_FILE_NAME)
    config = Config()
    config.load(path=path)

    assert config.message == "hello-test"


def test_load_frozen():
    @dataconfig(frozen=True)
    class Config:
        message: str = "test"

    path = Path("tests/").joinpath(TEST_FILE_NAME)
    config = Config()
    assert config.message == "test"
    # When frozen, load needs to be passed `replace=True`
    # and its returl value must be assigned to config.
    # This avoids accidental assignment while allowing
    # override.
    config = config.load(path=path, replace=True)
    assert config.message == "hello-test"


def test_save():
    @dataconfig(file=TEST_FILE_NAME, paths=TEST_PATHS)
    class Config:
        message: str = "test"

    config = Config()
    config.message = "hello-test"
    config.save(overwrite=True)

    config.load()
    assert config.message == "hello-test"


@pytest.mark.xfail(raises=FileExistsError)
def test_save_no_overwrite():
    @dataconfig(file=TEST_FILE_NAME, paths=TEST_PATHS)
    class Config:
        message: str = "test"

    config = Config()
    config.message = "hello-test"
    config.save(overwrite=False)

    config.load()
    assert config.message == "hello-test"


def test_load_shortcut():
    @dataconfig(file=TEST_FILE_NAME, paths=TEST_PATHS)
    class Config:
        message: str = "test"

    config = Config().load()
    assert config.message == "hello-test"


def test_click_option():
    @dataconfig(file=TEST_FILE_NAME, paths=TEST_PATHS)
    class Config:
        message: str = "test"

    config = Config()

    @click.command()
    @click.option("--message")
    @config.click_option()
    def test_cmd(message):
        print(f"Hello, {message}!")
        print(f"Hello, {config.message}!")

    runner = CliRunner()
    result = runner.invoke(test_cmd, ["--message", "Tests"])
    assert result.exit_code == 0
    assert result.output == 'Hello, Tests!\nHello, Tests!\n'


def test_click_option_frozen_fails():
    @dataconfig(file=TEST_FILE_NAME, paths=TEST_PATHS, frozen=True)
    class Config:
        message: str = "test"

    config = Config()

    @click.command()
    @click.option("--message")
    @config.click_option()
    def test_cmd(message):
        print(f"Hello, {message}!")
        print(f"Hello, {config.message}!")

    runner = CliRunner()
    result = runner.invoke(test_cmd, ["--message", "Tests"])
    assert result.exit_code == 1

