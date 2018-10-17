from sqlalchemy import Column, types, UniqueConstraint

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import ExceptionType


MAPPING = {
    'shape_pt_lat': 'point_latitude',
    'shape_pt_lon': 'point_longitude',
    'shape_dist_traveled': 'distance_traveled',
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('shape_')


class Shape(Base):
    __tablename__ = 'shape'
    __table_args__ = ()

    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    point_latitude = Column(
        'point_latitude',
        types.DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
        nullable=False,
    )

    point_longitude = Column(
        'point_longitude',
        types.DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
        nullable=False,
    )

    distance_traveled = Column(
        'distance_traveled',
        types.Float,
        nullable=True,
    )
