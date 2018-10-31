# shapes.txt

from sqlalchemy import Column, types, UniqueConstraint

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import ExceptionType
from gtfs_parser.model import MixIn


class Shape(Base, MixIn):
    __tablename__ = 'shape'
    __table_args__ = ()

    PREFIX = 'shape_'

    NAME_MAPPING = {
        'shape_pt_lat': 'latitude',
        'shape_pt_lon': 'longitude',
        'shape_pt_sequence': 'sequence',
        'shape_dist_traveled': 'distance_traveled',
    }
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'point_latitude',
        'point_longitude',
        'distance_traveled',
        ''
    )

    id = Column(
        'id',
        types.String,
        primary_key=True,
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
