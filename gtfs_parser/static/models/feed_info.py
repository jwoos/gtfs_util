# feed_info.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base


class Feed(Base):
    __tablename__ = 'feed',
    __table_args__ = ()

    PREFIX = 'feed_'

    NAME_MAPPING = {
        'feed_lang': 'language',
    }
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'publisher_name',
        'publisher_url',
        'language',
        'start_date',
        'end_date',
        'version',
        'contact_email',
        'contact_url',
    )

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
