from typing import Union

from mypy.plugin import (
    ClassDefContext,
    DynamicClassDefContext,
    FunctionContext,
    MethodContext,
)
from mypy.types import Type

from .utils import (
    add_table_to_cls,
    add_query_to_cls,
    add_init_to_cls,
    set_base_cls,
    check_model_values,
    create_dynamic_class,
    get_base_classes_from_arg,
    get_model_from_ctx,
    set_declarative,
)


def declarative_base_hook(ctx: DynamicClassDefContext) -> None:
    base_class = get_base_classes_from_arg(
        ctx, "model_class", "flask_sqlalchemy.model.Model"
    )
    info = create_dynamic_class(
        ctx, base_class, metaclass="flask_sqlalchemy.model.DefaultMeta",
    )

    set_declarative(info)
    # add_metadata(ctx, info)


def model_init_hook(ctx: Union[FunctionContext, MethodContext]) -> Type:
    model = get_model_from_ctx(ctx)

    if "query" not in model.names:
        return ctx.default_return_type

    assert len(ctx.arg_names) == 1
    assert len(ctx.arg_types) == 1

    check_model_values(ctx, model, "values")

    return ctx.default_return_type


def create_db_instance_hook(ctx: DynamicClassDefContext) -> None:
    model_class = get_base_classes_from_arg(
        ctx, "model_class", "flask_sqlalchemy.model.Model"
    )[0]
    query_class = get_base_classes_from_arg(
        ctx, "query_class", "flask_sqlalchemy.BaseQuery"
    )[0]
    set_base_cls(ctx, model_class=model_class, query_class=query_class)


def model_base_class_hook(ctx: ClassDefContext) -> None:
    add_init_to_cls(ctx)
    add_query_to_cls(ctx)
    add_table_to_cls(ctx)


def crud_model_values_hook(ctx: MethodContext) -> Type:
    model = get_model_from_ctx(ctx)
    check_model_values(ctx, model, "values")

    return ctx.default_return_type
