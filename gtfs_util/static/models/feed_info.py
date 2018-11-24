# feed_info.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


class Feed(Base, MixIn):
    __tablename__ = 'feed'
    __table_args__ = ()

    PREFIX = 'feed_'

    NAME_MAPPING = {
        'feed_lang': 'language',
    }
    DATA_MAPPING = {
        'start_date': data.to_date,
        'end_date': data.to_date,
    }

    FIELDS = {
        'id',
        'publisher_name',
        'publisher_url',
        'language',
        'start_date',
        'end_date',
        'version',
        'contact_email',
        'contact_url',
    }

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    publisher_name = Column(
        'publisher_name',
        types.String,
        nullable=False,
    )

    publisher_url = Column(
        'publisher_url',
        types.String,
        nullable=False,
    )

    language = Column(
        'language',
        types.String,
        nullable=False,
    )

    start_date = Column(
        'start_date',
        types.Date,
        nullable=True,

    )

    end_date = Column(
        'end_date',
        types.Date,
        nullable=True,
    )

    version = Column(
        'version',
        types.String,
        nullable=False,
    )

    contact_email = Column(
        'contact_email',
        types.String,
        nullable=False,
    )

    contact_url = Column(
        'contact_url',
        types.String,
        nullable=False,
    )
