from sqlalchemy import Column
from sqlalchemy.types import String, Integer

from gtfs_parser.models.base import Base
from gtfs_parser.enum import RouteType


MAPPING = {
    'route_desc': 'description',
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('route_')


class Route(Base):
    __tablename__ = 'route'

    id = Column(
        'id',
        String,
        primary_key=True,
    )

    agency_id = Column(
        'agency_id',
        String,
        nullable=True,
    )

    short_name = Column(
        'short_name',
        String,
    )

    long_name = Column(
        'long_name',
        String,
    )

    description = Column(
        'description',
        String,
        nullable=True,
    )

    type = Column(
        'type',
        Enum(RouteType)
    )

    url = Column(
        'url',
        String,
        nullable=True,
    )

    color = Column(
        'color',
        String,
        nullable=True,
    )

    text_color = Column(
        'text_color',
        String,
        nullable=True,
    )

    sort_order = Column(
        'sort_order',
        Integer,
        nullable=True,
    )
