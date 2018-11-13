# frequencies.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.enum import RouteType
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


class Frequency(Base, MixIn):
    __tablename__ = 'frequency'
    __table_args__ = (
        # schema.ForeignKeyConstraint(['trip_id'], ['trip.id']),
    )

    PREFIX = 'frequency_'

    NAME_MAPPING = {
        'headway_secs': 'headway_seconds',
    }
    DATA_MAPPING = {
        'start_time': data.to_timedelta,
        'end_time': data.to_timedelta,
        'headway_seconds': int,
        'exact_times': data.to_bool(val=True),
    }

    FIELDS = (
        'id',
        'trip_id',
        'start_time',
        'end_time',
        'headway_seconds',
        'exact_times',
    )

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    trip_id = Column(
        'trip_id',
        types.String,
        nullable=False,
    )

    start_time = Column(
        'start_time',
        types.Interval,
        nullable=False,
    )

    end_time = Column(
        'end_time',
        types.Interval,
        nullable=False,
    )

    headway_seconds = Column(
        'headway_seconds',
        types.Integer,
        nullable=False,
    )

    exact_times = Column(
        'exact_times',
        types.BOOLEAN,
        nullable=True,
    )
