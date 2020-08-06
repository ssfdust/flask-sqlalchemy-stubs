from __future__ import annotations
from flask.app import Flask
from flask_sqlalchemy.model import DefaultMeta, Model as BaseModel
from mypy_extensions import NoReturn as NoReturn
import sqlalchemy as _sa
from sqlalchemy.orm.query import Query
from sqlalchemy.engine.default import DefaultExecutionContext
from sqlalchemy.engine.base import Connection, Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.mapper import Mapper
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import Session as SessionBase, sessionmaker
from sqlalchemy.sql.schema import MetaData, Table
from sqlalchemy.sql.selectable import Select
from sqlite3 import Cursor
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, Union, TypeVar, Protocol, Type

_M = TypeVar("_M")
_T = TypeVar('_T')

models_committed: Any
before_models_committed: Any

class _DebugQueryTuple(Tuple[str, Tuple[Any, ...], float, float, Any]):
    statement: str
    parameters: Tuple[Any, ...]
    start_time: float
    end_time: float
    context: Any
    @property
    def duration(self) -> float: ...

class SignallingSession(SessionBase):
    app: Any = ...
    def __init__(
        self,
        db: SQLAlchemy,
        autocommit: bool = ...,
        autoflush: bool = ...,
        **options: Any
    ) -> None: ...
    def get_bind(
        self, mapper: Optional[Mapper] = ..., clause: Optional[Select] = ...
    ) -> Engine: ...

class _SessionSignalEvents:
    @classmethod
    def register(cls, session: SessionBase) -> None: ...
    @classmethod
    def unregister(cls, session: SessionBase) -> None: ...
    @staticmethod
    def record_ops(
        session: SessionBase,
        flush_context: Optional[Any] = ...,
        instances: Optional[Any] = ...,
    ) -> None: ...
    @staticmethod
    def before_commit(session: SessionBase) -> None: ...
    @staticmethod
    def after_commit(session: SessionBase) -> None: ...
    @staticmethod
    def after_rollback(session: SessionBase) -> None: ...

class _EngineDebuggingSignalEvents:
    engine: Any = ...
    app_package: Any = ...
    def __init__(self, engine: Engine, import_name: str) -> None: ...
    def register(self) -> None: ...
    def before_cursor_execute(
        self,
        conn: Connection,
        cursor: Cursor,
        statement: str,
        parameters: Tuple[Any, ...],
        context: Any,
        executemany: bool,
    ) -> None: ...
    def after_cursor_execute(
        self,
        conn: Connection,
        cursor: Cursor,
        statement: str,
        parameters: Tuple[Any, ...],
        context: Any,
        executemany: bool,
    ) -> None: ...

def get_debug_queries() -> List[_DebugQueryTuple]: ...

class Pagination:
    query: BaseQuery
    page: int
    per_page: int
    total: int
    items: List[Any]
    def __init__(
        self,
        query: Optional[BaseQuery],
        page: int,
        per_page: int,
        total: Optional[int],
        items: List[Any],
    ) -> None: ...
    @property
    def pages(self) -> int: ...
    def prev(self, error_out: bool = ...) -> Pagination: ...
    @property
    def prev_num(self) -> int: ...
    @property
    def has_prev(self) -> bool: ...
    def next(self, error_out: bool = ...) -> Pagination: ...
    @property
    def has_next(self) -> bool: ...
    @property
    def next_num(self) -> int: ...
    def iter_pages(
        self,
        left_edge: int = ...,
        left_current: int = ...,
        right_current: int = ...,
        right_edge: int = ...,
    ) -> Iterator[int]: ...

class BaseQuery(Query[_M]):
    def get_or_404(self, ident: int, description: Optional[str] = ...) -> _M: ...
    def first_or_404(self, description: Optional[str] = ...) -> _M: ...
    def paginate(
        self,
        page: Optional[int] = ...,
        per_page: Optional[int] = ...,
        error_out: bool = ...,
        max_per_page: Optional[int] = ...,
        count: bool = ...,
    ) -> Pagination: ...

class _QueryProperty:
    sa: SQLAlchemy = ...
    def __init__(self, sa: SQLAlchemy) -> None: ...
    def __get__(self, obj: Optional[Any], type: DefaultMeta) -> BaseQuery: ...

class _EngineConnector:
    def __init__(
        self, sa: SQLAlchemy, app: Flask, bind: Optional[str] = ...
    ) -> None: ...
    def get_uri(self) -> str: ...
    def get_engine(self) -> Engine: ...
    def get_options(self, sa_url: URL, echo: bool) -> Dict[str, Any]: ...

def get_state(app: Flask) -> _SQLAlchemyState: ...

class _SQLAlchemyState:
    db: SQLAlchemy
    connectors: Any
    def __init__(self, db: SQLAlchemy) -> None: ...

class SQLAlchemy:
    def __init__(
        self,
        app: Optional[Flask] = ...,
        use_native_unicode: bool = ...,
        session_options: Optional[Dict[str, Callable[..., Any]]] = ...,
        metadata: Optional[Any] = ...,
        query_class: type = ...,
        model_class: type = ...,
        engine_options: Union[Dict[str, str], Dict[str, type], None] = ...,
    ) -> None:
        # from sqlalchemy
        self.session: SessionBase
        self.ARRAY = _sa.ARRAY
        self.BIGINT = _sa.BIGINT
        self.BINARY = _sa.BINARY
        self.BLANK_SCHEMA = _sa.BLANK_SCHEMA
        self.BLOB = _sa.BLOB
        self.BOOLEAN = _sa.BOOLEAN
        self.BigInteger = _sa.BigInteger
        self.Binary = _sa.Binary
        self.Boolean = _sa.Boolean
        self.CHAR = _sa.CHAR
        self.CLOB = _sa.CLOB
        self.CheckConstraint = _sa.CheckConstraint
        self.Column = _sa.Column
        self.ColumnDefault = _sa.ColumnDefault
        self.Constraint = _sa.Constraint
        self.DATE = _sa.DATE
        self.DATETIME = _sa.DATETIME
        self.DDL = _sa.DDL
        self.DECIMAL = _sa.DECIMAL
        self.Date = _sa.Date
        self.DateTime = _sa.DateTime
        self.DefaultClause = _sa.DefaultClause
        self.Enum = _sa.Enum
        self.FLOAT = _sa.FLOAT
        self.FetchedValue = _sa.FetchedValue
        self.Float = _sa.Float
        self.ForeignKey = _sa.ForeignKey
        self.ForeignKeyConstraint = _sa.ForeignKeyConstraint
        self.INT = _sa.INT
        self.INTEGER = _sa.INTEGER
        self.Index = _sa.Index
        self.Integer = _sa.Integer
        self.Interval = _sa.Interval
        self.JSON = _sa.JSON
        self.LargeBinary = _sa.LargeBinary
        self.MetaData = _sa.MetaData
        self.NCHAR = _sa.NCHAR
        self.NUMERIC = _sa.NUMERIC
        self.NVARCHAR = _sa.NVARCHAR
        self.Numeric = _sa.Numeric
        self.PassiveDefault = _sa.PassiveDefault
        self.PickleType = _sa.PickleType
        self.PrimaryKeyConstraint = _sa.PrimaryKeyConstraint
        self.REAL = _sa.REAL
        self.SMALLINT = _sa.SMALLINT
        self.Sequence = _sa.Sequence
        self.SmallInteger = _sa.SmallInteger
        self.String = _sa.String
        self.TEXT = _sa.TEXT
        self.TIME = _sa.TIME
        self.TIMESTAMP = _sa.TIMESTAMP
        self.Table: Callable[..., _sa.Table] = _sa.Table
        self.Text = _sa.Text
        self.ThreadLocalMetaData = _sa.ThreadLocalMetaData
        self.Time = _sa.Time
        self.TypeDecorator = _sa.TypeDecorator
        self.Unicode = _sa.Unicode
        self.UnicodeText = _sa.UnicodeText
        self.UniqueConstraint = _sa.UniqueConstraint
        self.VARBINARY = _sa.VARBINARY
        self.VARCHAR = _sa.VARCHAR
        self.text = _sa.text
        self.alias = _sa.alias
        self.all_ = _sa.all_
        self.and_ = _sa.and_
        self.asc = _sa.asc
        self.between = _sa.between
        self.bindparam = _sa.bindparam
        self.case = _sa.case
        self.cast = _sa.cast
        self.collate = _sa.collate
        self.column = _sa.column
        self.delete = _sa.delete
        self.desc = _sa.desc
        self.distinct = _sa.distinct
        self.except_ = _sa.except_
        self.except_all = _sa.except_all
        self.exists = _sa.exists
        self.extract = _sa.extract
        self.false = _sa.false
        self.func = _sa.func
        self.funcfilter = _sa.funcfilter
        self.insert = _sa.insert
        self.inspect = _sa.inspect
        self.intersect = _sa.intersect
        self.intersect_all = _sa.intersect_all
        self.join = _sa.join
        self.lateral = _sa.lateral
        self.literal = _sa.literal
        self.literal_column = _sa.literal_column
        self.modifier = _sa.modifier
        self.not_ = _sa.not_
        self.null = _sa.null
        # self.nullsfirst = _sa.nullsfirst
        # self.nullslast = _sa.nullslast
        self.or_ = _sa.or_
        self.outerjoin = _sa.outerjoin
        self.outparam = _sa.outparam
        self.select = _sa.select
        self.subquery = _sa.subquery
        self.table = _sa.table
        self.tablesample = _sa.tablesample
        self.true = _sa.true
        self.tuple_ = _sa.tuple_
        self.type_coerce = _sa.type_coerce
        self.union = _sa.union
        self.union_all = _sa.union_all
        self.update = _sa.update
        self.within_group = _sa.within_group
        self.class_mapper = _sa.orm.class_mapper
        self.backref = _sa.orm.backref
        self.relationship = _sa.orm.relationship

    @property
    def metadata(self) -> MetaData: ...
    def create_scoped_session(
        self, options: Optional[Dict[str, Callable[..., Any]]] = ...
    ) -> scoped_session: ...
    def create_session(self, options: Dict[str, type]) -> sessionmaker: ...
    def make_declarative_base(
        self, model: _T, metadata: Optional[Any] = ...
    ) -> _T: ...
    def init_app(self, app: Flask) -> None: ...
    def apply_pool_defaults(self, app: Flask, options: Dict[Any, Any]) -> None: ...
    def apply_driver_hacks(
        self, app: Flask, sa_url: URL, options: Dict[str, int]
    ) -> None: ...
    @property
    def engine(self) -> Engine: ...
    def make_connector(
        self, app: Flask = ..., bind: Optional[str] = ...
    ) -> _EngineConnector: ...
    def get_engine(
        self, app: Optional[Flask] = ..., bind: Optional[str] = ...
    ) -> Engine: ...
    def create_engine(self, sa_url: URL, engine_opts: Dict[str, Any]) -> Engine: ...
    def get_app(self, reference_app: Optional[Flask] = ...) -> Flask: ...
    def get_tables_for_bind(self, bind: Optional[str] = ...) -> List[Any]: ...
    def get_binds(self, app: Flask = ...) -> Dict[Any, Engine]: ...
    def create_all(self, bind: str = ..., app: Optional[Flask] = ...) -> None: ...
    def drop_all(self, bind: str = ..., app: Optional[Flask] = ...) -> None: ...
    def reflect(self, bind: str = ..., app: Optional[Flask] = ...) -> None: ...

class _BoundDeclarativeMeta(DefaultMeta):
    def __init__(cls, name: Any, bases: Any, d: Any) -> None: ...

class FSADeprecationWarning(DeprecationWarning): ...
