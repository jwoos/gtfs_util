from sqlalchemy import Column
from sqlalchemy.types import String, Integer, DECIMAL, Enum

from gtfs_parser.models.base import Base
from gtfs_parser.enum import LocationType, ParentStation, WheelchairBoarding


MAPPING = {
    'stop_desc': 'description',
    'stop_lat': 'latitude',
    'stop_lon': 'longitude',
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('stop_')


class Stop(Base):
    __tablename__ = 'stop'

    id = Column(
        'id',
        String,
        primary_key=True,
    )

    code = Column(
        'code',
        String,
        nullable=True,
    )

    name = Column(
        'name',
        String,
    )

    description = Column(
        'description',
        String,
    )

    longitude = Column(
        'longitude',
        DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
    )

    latitude = Column(
        'latitude',
        DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
    )

    zone_id = Column(
        'zone_id',
        String,
        nullable=True,
    )

    location_type = Column(
        'location_type',
        Enum(LocationType),
        nullable=True,
    )

    parent_station = Column(
        'parent_station',
        Enum(ParentStation),
        nullable=True,
    )

    timezone = Column(
        'timezone',
        String,
        nullable=True,
    )

    wheelchair_boarding = Column(
        'wheelchair_boarding',
        Enum(WheelchairBoarding),
        nullable=True,
    )
