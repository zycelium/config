from dataclasses import dataclass, is_dataclass
from zycelium.dataconfig import dataconfig


def test_dataconfig_init():
    @dataconfig
    class Config:
        pass

    config = Config()
    assert is_dataclass(config)
