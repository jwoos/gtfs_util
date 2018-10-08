from sqlalchemy import Column
from sqlalchemy.types import String, Integer, DECIMAL, Enum

from gtfs_parser.models.base import Base
from gtfs_parser.enum import LocationType, ParentStation, WheelchairBoarding


MAPPING = {
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('stop_')


class StopTime(Base):
    __tablename__ = 'stop_time'

    id = Column(
        'id',
        String,
        primary_key=True,
    )
