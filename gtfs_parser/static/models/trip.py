from sqlalchemy import Column
from sqlalchemy.types import String, Integer, DECIMAL, Enum

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import BikeAllowed, WheelchairBoarding


MAPPING = {
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('trip_')


class Trip(Base):
    __tablename__ = 'trip'

    id = Column(
        'id',
        String,
        primary_key=True,
    )

    route_id = Column(
        'route_id',
        String,
    )

    service_id = Column(
        'service_id',
        String,
    )

    headsign = Column(
        'headsign',
        String,
        nullable=True,
    )

    short_name = Column(
        'short_name',
        String,
        nullable=True,
    )

    direction = Column(
        'direction',
        Enum(Direction),
        nullable=True,
    )

    block_id = Column(
        'block_id',
        String,
        nullable=True,
    )

    shape_id = Column(
        'shape_id',
        String,
        nullable=True,
    )

    wheelchar_accessible = Column(
        'wheelchar_accessible',
        Enum(WheelchairBoarding),
        nullable=True,
    )

    bikes_allowed = column(
        'bikes_allowed',
        Enum(BikeAllowed),
        nullable=True,
    )
