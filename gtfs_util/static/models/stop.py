# stops.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.enum import LocationType
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


class Stop(Base, MixIn):
    __tablename__ = 'stop'
    __table_args__ = ()

    PREFIX = 'stop_'

    NAME_MAPPING = {
        'stop_desc': 'description',
        'stop_lat': 'latitude',
        'stop_lon': 'longitude',
        'wheelchair_boarding': 'wheelchair_accessible'
    }
    DATA_MAPPING = {
        'location_type': data.to_enum(LocationType),
        'wheelchair_accessible': data.to_bool(nullable=True),
        'latitude': float,
        'longitude': float,
    }

    FIELDS = {
        'id',
        'code',
        'name',
        'description',
        'longitude',
        'latitude',
        'zone_id',
        'location_type',
        'parent_station',
        'timezone',
        'url',
        'wheelchair_accessible',
    }

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
        types.Numeric(9, 6, asdecimal=True),
    )

    latitude = Column(
        'latitude',
        types.Numeric(9, 6, asdecimal=True),
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
        types.String,
        nullable=True,
    )

    timezone = Column(
        'timezone',
        types.String,
        nullable=True,
    )

    url = Column(
        'url',
        types.String,
        nullable=True,
    )

    wheelchair_accessible = Column(
        'wheelchair_accessible',
        types.BOOLEAN,
        nullable=True,
    )
