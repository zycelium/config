from dataclasses import dataclass


def dataconfig(_cls=None, *, file="config.ini"):
    def wrap(cls):
        setattr(cls, "_file", file)
        wrapped_cls = dataclass(cls)
        return wrapped_cls

    if _cls is None:
        return wrap

    return wrap(_cls)
