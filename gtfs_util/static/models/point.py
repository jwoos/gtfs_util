# shapes.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.enum import ExceptionType
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


class Point(Base, MixIn):
    __tablename__ = 'point'
    __table_args__ = (
        schema.UniqueConstraint('id', 'shape_id'),
    )

    PREFIX = 'point_'

    NAME_MAPPING = {
        'shape_pt_lat': 'latitude',
        'shape_pt_lon': 'longitude',
        'shape_pt_sequence': 'sequence',
        'shape_dist_traveled': 'distance_traveled',
    }
    DATA_MAPPING = {
        'latitude': float,
        'longitude': float,
        'sequence': int,
        'distance_traveled': data.to_generic(float, nullable=True),
    }

    FIELDS = (
        'id',
        'shape_id'
        'latitude',
        'longitude',
        'sequence',
        'distance_traveled',
    )

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    shape_id = Column(
        'shape_id',
        types.String,
        nullable=False,
    )

    latitude = Column(
        'latitude',
        types.DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
        nullable=False,
    )

    longitude = Column(
        'longitude',
        types.DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
        nullable=False,
    )

    sequence = Column(
        'sequence',
        types.Integer,
        nullable=False,
    )

    distance_traveled = Column(
        'distance_traveled',
        types.Float,
        nullable=True,
    )
