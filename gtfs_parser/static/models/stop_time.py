from sqlalchemy import Column, types, ForeignKey

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import PickupType, DropoffType


MAPPING = {
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('stop_')


class StopTime(Base):
    __tablename__ = 'stop_time'

    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    trip_id = Column(
        'trip_id',
        types.String,
        nullable=False,
    )

    arrival_time = Column(
        'arrival_time',
        types.Datetime,
        nullable=False,
    )

    departure_time = Column(
        'departure_time',
        types.Datetime,
        nullable=False,
    )

    stop_id = Column(
        'stop_id',
        types.String,
        nullable=False,
    )

    stop_sequence = Column(
        'stop_sequence',
        types.Integer,
        nullable=False,
    )

    stop_headsign = Column(
        'stop_headsign',
        types.String,
        nullable=True,
    )

    pickup_type = Column(
        'pickup_type',
        types.Enum(PickupType),
        nullable=True,
    )

    dropoff_type = Column(
        'dropoff_type',
        types.Enum(DropoffType),
        nullable=True,
    )

    shape_dist_traveled = Column(
        'shape_dist_traveled',
        types.Float,
        nullable=True,
    )

    timepoint = Column(
        'timepoint',
        types.Enum(TimePoint),
        nullable=True,
    )
