from dataclasses import dataclass


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
