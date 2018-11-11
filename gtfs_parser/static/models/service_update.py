# calendar_dates.txt

from gtfs_parser.static import data
from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import ExceptionType
from gtfs_parser.model import MixIn

from sqlalchemy import Column, types, schema


class ServiceUpdate(Base, MixIn):
    __tablename__ = 'service_update'
    __table_args__ = (
        schema.UniqueConstraint('service_id', 'date'),
    )

    PREFIX = 'calendar_date_'

    NAME_MAPPING = {}
    DATA_MAPPING = {
        'date': data.to_date,
        'exception_type': data.to_enum(ExceptionType),
    }

    FIELDS = (
        'id',
        'date',
        'service_id',
        'exception_type',
    )

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    date = Column(
        'date',
        types.DATE,
        nullable=False,
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
