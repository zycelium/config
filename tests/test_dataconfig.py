from dataclasses import dataclass, is_dataclass
from zycelium.dataconfig import dataconfig

TEST_FILE_NAME = "test.ini"
DEFAULT_FILE_NAME = "config.ini"


def test_dataconfig_init_bare():
    @dataconfig
    class Config:
        pass

    config = Config()
    assert is_dataclass(config)
    assert config._file == DEFAULT_FILE_NAME


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
    @dataconfig(paths=[".", "tests/"])
    class Config:
        pass

    config = Config()
    assert config._paths == [".", "tests/"]
