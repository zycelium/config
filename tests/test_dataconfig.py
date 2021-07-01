from dataclasses import dataclass, is_dataclass
from zycelium.dataconfig import dataconfig

TEST_FILE_NAME = "test.ini"


def test_dataconfig_init_bare():
    @dataconfig
    class Config:
        pass

    config = Config()
    assert is_dataclass(config)


def test_dataconfig_init_with_file():
    @dataconfig(file=TEST_FILE_NAME)
    class Config:
        pass

    config = Config()
    assert is_dataclass(config)
    assert config._file == TEST_FILE_NAME