from dataclasses import dataclass


def dataconfig(_cls):
    def wrap():
        wrapped_cls = dataclass(_cls)
        return _cls

    return wrap
