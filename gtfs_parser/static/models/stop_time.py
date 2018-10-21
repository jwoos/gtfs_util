# stop_times.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import PickupType, DropoffType


class StopTime(Base):
    __tablename__ = 'stop_time'
    __table_args__ = (
        schema.ForeignKeyConstraint(['trip_id'], ['trip.id']),
        schema.ForeignKeyConstraint(['stop_id'], ['stop.id']),
    )

    PREFIX = 'stop_time_'

    NAME_MAPPING = {
        'shape_dist_traveled': 'shape_distance_traveled',
    }
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'trip_id',
        'arrival_time',
        'departure_time',
        'stop_id',
        'stop_sequence',
        'stop_headsign',
        'pickup_type',
        'dropoff_type',
        'shape_distance_traveled',
        'timepoint',
    )

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

    shape_distance_traveled = Column(
        'shape_distance_traveled',
        types.Float,
        nullable=True,
    )

    timepoint = Column(
        'timepoint',
        types.Enum(TimePoint),
        nullable=True,
    )
