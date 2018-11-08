# trips.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.model import MixIn


class Trip(Base, MixIn):
    __tablename__ = 'trip'
    __table_args__ = (
        # schema.ForeignKeyConstraint(['route_id'], ['route.id']),
        # schema.ForeignKeyConstraint(['service_id'], ['service.id']),
        # schema.ForeignKeyConstraint(['shape_id'], ['shape.id']),
    )

    PREFIX = 'trip_'

    NAME_MAPPING = {
        'direction_id': 'direction'
    }
    DATA_MAPPING = {
        'wheelchair_accessible': lambda x: x == 1 if x != 0 else None,
        'bikes_allowed': lambda x: x == 1 if x != 0 else None,
    }

    FIELDS = (
        'id',
        'route_id',
        'service_id',
        'headsign',
        'short_name',
        'direction',
        'block_id',
        'shape_id',
        'wheelchair_accessible',
        'bikes_allowed',
    )

    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    route_id = Column(
        'route_id',
        types.String,
        nullable=False,
    )

    service_id = Column(
        'service_id',
        types.String,
        nullable=False,
    )

    headsign = Column(
        'headsign',
        types.String,
        nullable=True,
    )

    short_name = Column(
        'short_name',
        types.String,
        nullable=True,
    )

    direction = Column(
        'direction',
        types.BOOLEAN,
        nullable=True,
    )

    block_id = Column(
        'block_id',
        types.String,
        nullable=True,
    )

    shape_id = Column(
        'shape_id',
        types.String,
        nullable=True,
    )

    wheelchair_accessible = Column(
        'wheelchair_accessible',
        types.BOOLEAN,
        nullable=True,
    )

    bikes_allowed = Column(
        'bikes_allowed',
        types.BOOLEAN,
        nullable=True,
    )
