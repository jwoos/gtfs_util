# calendar.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


class Service(Base, MixIn):
    __tablename__ = 'service'
    __table_args__ = (
    )

    PREFIX = 'calendar_'

    NAME_MAPPING = {
        'service_id': 'id',
    }
    DATA_MAPPING = {
        'monday': data.to_bool(nullable=False),
        'tuesday': data.to_bool(nullable=False),
        'wednesday': data.to_bool(nullable=False),
        'thursday': data.to_bool(nullable=False),
        'friday': data.to_bool(nullable=False),
        'saturday': data.to_bool(nullable=False),
        'sunday': data.to_bool(nullable=False),
        'start_date': data.to_date,
        'end_date': data.to_date,
    }

    FIELDS = (
        'id',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
        'start_date',
        'end_date',
    )


    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    monday = Column(
        'monday',
        types.BOOLEAN,
        nullable=False,
    )

    tuesday = Column(
        'tuesday',
        types.BOOLEAN,
        nullable=False,
    )

    wednesday = Column(
        'wednesday',
        types.BOOLEAN,
        nullable=False,
    )

    thursday = Column(
        'thursday',
        types.BOOLEAN,
        nullable=False,
    )

    friday = Column(
        'friday',
        types.BOOLEAN,
        nullable=False,
    )

    saturday = Column(
        'saturday',
        types.BOOLEAN,
        nullable=False,
    )

    sunday = Column(
        'sunday',
        types.BOOLEAN,
        nullable=False,
    )

    start_date = Column(
        'start_date',
        types.Date,
        nullable=False,
    )

    end_date = Column(
        'end_date',
        types.Date,
        nullable=False,
    )
