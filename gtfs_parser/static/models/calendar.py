from sqlalchemy import Column, types

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import CalendarAvailable


MAPPING = {
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('calendar_')


class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    monday = Column(
        'monday',
        types.Enum(CalendarAvailable),
        nullable=False,
    )

    tuesday = Column(
        'tuesday',
        types.Enum(CalendarAvailable),
        nullable=False,
    )

    wednesday = Column(
        'wednesday',
        types.Enum(CalendarAvailable),
        nullable=False,
    )

    thursday = Column(
        'thursday',
        types.Enum(CalendarAvailable),
        nullable=False,
    )

    friday = Column(
        'friday',
        types.Enum(CalendarAvailable),
        nullable=False,
    )

    saturday = Column(
        'saturday',
        types.Enum(CalendarAvailable),
        nullable=False,
    )

    sunday = Column(
        'sunday',
        types.Enum(CalendarAvailable),
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
