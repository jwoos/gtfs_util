# routes.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.enum import RouteType
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


class Route(Base, MixIn):
    __tablename__ = 'route'
    __table_args__ = (
        # schema.ForeignKeyConstraint(['agency_id'], ['agency.id']),
    )

    PREFIX = 'route_'

    NAME_MAPPING = {
        'route_desc': 'description',
    }
    DATA_MAPPING = {
        'type': data.to_enum(RouteType),
        'sort_order': int,
    }

    FIELDS = (
        'id',
        'agency_id',
        'short_name',
        'long_name',
        'description',
        'type',
        'url',
        'color',
        'text_color',
        'sort_order',
    )

    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    agency_id = Column(
        'agency_id',
        types.String,
        nullable=True,
    )

    short_name = Column(
        'short_name',
        types.String,
        nullable=False,
    )

    long_name = Column(
        'long_name',
        types.String,
        nullable=False,
    )

    description = Column(
        'description',
        types.String,
        nullable=True,
    )

    type = Column(
        'type',
        types.Enum(RouteType),
        nullable=False
    )

    url = Column(
        'url',
        types.String,
        nullable=True,
    )

    color = Column(
        'color',
        types.String,
        nullable=True,
    )

    text_color = Column(
        'text_color',
        types.String,
        nullable=True,
    )

    sort_order = Column(
        'sort_order',
        types.Integer,
        nullable=True,
    )
