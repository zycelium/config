from dataclasses import dataclass
from pathlib import Path


def locate(file, paths, auto, file_path=""):
    if file_path:
        return Path(file_path)
    elif auto:
        for _path in paths:
            path = Path(_path).joinpath(file)
            if path.exists():
                return path
        return Path(".").joinpath(file)
    else:
        raise FileNotFoundError(f"File {file!r} not found at {paths}.")


def dataconfig(
    _cls=None,
    *,
    file="config.ini",
    paths=None,
    auto=True,
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
):
    def wrap(cls):
        setattr(cls, "_file", file)
        setattr(cls, "_paths", paths or ["."])
        setattr(cls, "_auto", auto)
        wrapped_cls = dataclass(
            cls,
            init=init,
            repr=repr,
            eq=eq,
            order=order,
            unsafe_hash=unsafe_hash,
            frozen=frozen,
        )
        return wrapped_cls

    if _cls is None:
        return wrap

    return wrap(_cls)
