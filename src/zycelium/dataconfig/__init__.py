from dataclasses import dataclass


def dataconfig(_cls=None, *, file="config.ini", paths=None):
    def wrap(cls):
        setattr(cls, "_file", file)
        setattr(cls, "_paths", paths)
        wrapped_cls = dataclass(cls)
        return wrapped_cls

    if _cls is None:
        return wrap

    return wrap(_cls)
