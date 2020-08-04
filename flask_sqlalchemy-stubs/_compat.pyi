from sqlalchemy.util._collections import immutabledict
from typing import Any, Iterator

PY2: Any

def iteritems(d: Any) -> Iterator[Any]: ...
def itervalues(d: immutabledict[Any, Any]) -> Iterator[Any]: ...

xrange = range
string_types: Any

def to_str(x: str, charset: str = ..., errors: str = ...) -> str: ...
