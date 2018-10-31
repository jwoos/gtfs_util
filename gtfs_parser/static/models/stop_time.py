# stop_times.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import PickupDropOffType
from gtfs_parser.model import MixIn


class StopTime(Base, MixIn):
    __tablename__ = 'stop_time'
    __table_args__ = (
        schema.ForeignKeyConstraint(['trip_id'], ['trip.id']),
        schema.ForeignKeyConstraint(['stop_id'], ['stop.id']),
    )

    PREFIX = 'stop_time_'

    NAME_MAPPING = {
        'drop_off_type': 'dropoff_type',
        'shape_dist_traveled': 'shape_distance_traveled',
        'timepoint': 'exact_times',
    }
    DATA_MAPPING = {
        'exact_times': lambda x: (x == 1) or (x is None)
    }

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
        'exact_times',
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
        types.DATETIME,
        nullable=False,
    )

    departure_time = Column(
        'departure_time',
        types.DATETIME,
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
        types.Enum(PickupDropOffType),
        nullable=True,
    )

    dropoff_type = Column(
        'dropoff_type',
        types.Enum(PickupDropOffType),
        nullable=True,
    )

    shape_distance_traveled = Column(
        'shape_distance_traveled',
        types.Float,
        nullable=True,
    )

    exact_times = Column(
        'exact_times',
        types.BOOLEAN,
        nullable=True,
    )
