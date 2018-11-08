# routes.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import RouteType
from gtfs_parser.model import MixIn


class Route(Base, MixIn):
    __tablename__ = 'route'
    __table_args__ = (
        # schema.ForeignKeyConstraint(['agency_id'], ['agency.id']),
    )

    PREFIX = 'route_'

    NAME_MAPPING = {
        'route_desc': 'description',
    }
    DATA_MAPPING = {}

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
