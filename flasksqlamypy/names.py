try:
    from typing_extensions import Final as FinalType
    Final = FinalType[str]
except ImportError:
    Final = str

COLUMN_NAME: Final = "sqlalchemy.sql.schema.Column"
GROUPING_NAME: Final = "sqlalchemy.sql.elements.Grouping"
GINO_NAME: Final = "flask_sqlalchemy.SQLAlchemy"
RELATIONSHIP_NAME: Final = "sqlalchemy.orm.relationships.RelationshipProperty"
DECLARATIVE_BASE_NAME: Final = "flask_sqlalchemy.SQLAlchemy.make_declarative_base"
