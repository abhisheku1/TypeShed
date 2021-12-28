from typing import Any, Callable, NoReturn

TIMEOUT_MAX: int
error = RuntimeError

def start_new_thread(function: Callable[..., Any], args: tuple[Any, ...], kwargs: dict[str, Any] = ...) -> None: ...
def exit() -> NoReturn: ...
def get_ident() -> int: ...
def allocate_lock() -> LockType: ...
def stack_size(size: int | None = ...) -> int: ...

class LockType(object):
    locked_status: bool
    def __init__(self) -> None: ...
    def acquire(self, waitflag: bool | None = ..., timeout: int = ...) -> bool: ...
    def __enter__(self, waitflag: bool | None = ..., timeout: int = ...) -> bool: ...
    def __exit__(self, typ: Any, val: Any, tb: Any) -> None: ...
    def release(self) -> bool: ...
    def locked(self) -> bool: ...

def interrupt_main() -> None: ...
