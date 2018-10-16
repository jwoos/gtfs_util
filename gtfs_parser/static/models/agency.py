from sqlalchemy import Column
from sqlalchemy.types import String, Integer

from gtfs_parser.models.base import Base


MAPPING = {
    'agency_lang': 'language',
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('agency_')


class Agency(Base):
    __tablename__ = 'agency'

    id = Column(
        'id',
        String,
        primary_key=True,
    )

    name = Column(
        'name',
        String,
    )

    url = Column(
        'url',
        String,
    )

    timezone = Column(
        'timezone',
        String,
    )

    language= Column(
        'language',
        String,
        nullable=True,
    )

    phone = Column(
        'phone',
        String,
        nullable=True,
    )

    fare_url = Column(
        'fare_url',
        String,
        nullable=True,
    )

    email = Column(
        'email',
        String,
        nullable=True,
    )
