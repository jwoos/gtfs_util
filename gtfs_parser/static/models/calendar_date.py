from sqlalchemy import Column, types, UniqueConstraint

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import ExceptionType


MAPPING = {
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('calendar_')


class CalendarDate(Base):
    __tablename__ = 'calendar_date'
    __table_args__ = (
        UniqueConstraint('service_id', 'exception_type'),
    )

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    service_id = Column(
        'service_id',
        types.String,
        nullable=False,
    )

    exception_type = Column(
        'exception_type',
        types.Enum(ExceptionType),
        nullable=False,
    )
