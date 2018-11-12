# agency.txt

from gtfs_parser.static import data
from gtfs_parser.static.models.base import Base
from gtfs_parser.model import MixIn, Field

from sqlalchemy import Column, types, schema


class Agency(Base, MixIn):
    __tablename__ = 'agency'
    __table_args__ = ()

    PREFIX = 'agency_'

    NAME_MAPPING = {
        'agency_lang': 'language',
    }
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'name',
        'url',
        'timezone',
        'language',
        'phone',
        'fare_url',
        'email',
    )

    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    name = Column(
        'name',
        types.String,
        nullable=False,
    )

    url = Column(
        'url',
        types.String,
        nullable=False,
    )

    timezone = Column(
        'timezone',
        types.String,
        nullable=False,
    )

    language = Column(
        'language',
        types.String,
        nullable=True,
    )

    phone = Column(
        'phone',
        types.String,
        nullable=True,
    )

    fare_url = Column(
        'fare_url',
        types.String,
        nullable=True,
    )

    email = Column(
        'email',
        types.String,
        nullable=True,
    )
