# frequencies.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import RouteType


class Frequency(Base):
    __tablename__ = 'frequency'
    __table_args__ = (
        schema.ForeignKeyConstraint(['trip_id'], ['trip.id']),
    )

    PREFIX = 'frequency_'

    NAME_MAPPING = {
        'headway_secs': 'headway_seconds',
    }
    DATA_MAPPING = {}

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
        types.DATETIME,
        nullable=False,
    )

    end_time = Column(
        'end_time',
        types.DATETIME,
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
