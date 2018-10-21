# stops.txt

from sqlalchemy import Column, tyoes, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import LocationType


class Stop(Base):
    __tablename__ = 'stop'
    __tablename__ = ()

    PREFIX = 'stop_'

    NAME_MAPPING = {
        'stop_desc': 'description',
        'stop_lat': 'latitude',
        'stop_lon': 'longitude',
    }
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'code',
        'name',
        'description'
        'longitude',
        'latitude',
        'zone_id',
        'location_type',
        'parent_station',
        'timezone',
        'wheelchair_boarding',
    )

    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    code = Column(
        'code',
        types.String,
        nullable=True,
    )

    name = Column(
        'name',
        types.String,
        nullable=False,
    )

    description = Column(
        'description',
        types.String,
        nullable=True,
    )

    longitude = Column(
        'longitude',
        types.DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
    )

    latitude = Column(
        'latitude',
        types.DECIMAL(
            precision=9,
            decimal_return_scale=6,
            asdecimal=True,
        ),
    )

    zone_id = Column(
        'zone_id',
        types.String,
        nullable=True,
    )

    location_type = Column(
        'location_type',
        types.Enum(LocationType),
        nullable=True,
    )

    parent_station = Column(
        'parent_station',
        types.Bool,
        nullable=True,
    )

    timezone = Column(
        'timezone',
        types.String,
        nullable=True,
    )

    wheelchair_boarding = Column(
        'wheelchair_boarding',
        types.Enum(WheelchairBoarding),
        nullable=True,
    )
