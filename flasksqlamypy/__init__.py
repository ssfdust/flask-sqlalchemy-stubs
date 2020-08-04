from typing import Type
from typing_extensions import Final

from mypy.plugin import Plugin

from .plugin import FlaskSQLAlchemyPlugin

from importlib import metadata as importlib_metadata


__version__: Final[str] = "0.0.1"


def plugin(version: str) -> Type[Plugin]:
    return FlaskSQLAlchemyPlugin
