from _typeshed import structseq
from typing import Any, Optional
from typing_extensions import final

@final
class struct_group(structseq[Any], tuple[str, Optional[str], int, list[str]]):
    @property
    def gr_name(self) -> str: ...
    @property
    def gr_passwd(self) -> str | None: ...
    @property
    def gr_gid(self) -> int: ...
    @property
    def gr_mem(self) -> list[str]: ...

def getgrall() -> list[struct_group]: ...
def getgrgid(id: int) -> struct_group: ...
def getgrnam(name: str) -> struct_group: ...
