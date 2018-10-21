# calendar_dates.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import ExceptionType


class ServiceUpdate(Base):
    __tablename__ = 'service_update'
    __table_args__ = (
        schema.UniqueConstraint('service_id', 'exception_type'),
    )

    PREFIX = 'calendar_date_'

    NAME_MAPPING = {}
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'service_id',
        'exception_type',
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
