from typing import Type
try:
    from typing_extensions import Final as FinalType
    from importlib import metadata as importlib_metadata
    Final = FinalType[str]
except ImportError:
    Final = str

from mypy.plugin import Plugin

from .plugin import FlaskSQLAlchemyPlugin


__version__: Final = "0.0.1"


def plugin(version: str) -> Type[Plugin]:
    return FlaskSQLAlchemyPlugin
