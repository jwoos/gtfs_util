# trips.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


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
        'direction': data.to_bool(nullable=False),
        'wheelchair_accessible': data.to_bool(nullable=True),
        'bikes_allowed': data.to_bool(nullable=True),
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
