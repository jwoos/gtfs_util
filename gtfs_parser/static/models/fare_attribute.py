# fare_attributes.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.model import MixIn, Field


class Fare(Base, MixIn):
    __tablename__ = 'fare'
    __table_args__ = (
        schema.ForeignKeyConstraint(['agency_id'], ['agency.id']),
    )

    PREFIX = 'fare_'

    NAME_MAPPING = {}
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'price',
        'currency_type',
        'payment_method',
        'transfers',
        'agency_id',
        'transfer_duration',
    )

    id = Column(
        'id',
        types.String,
        primary_key=True,
    )

    price = Column(
        'price',
        types.Float,
        nullable=False,
    )

    currency_type = Column(
        'currency_type',
        types.String,
        nullable=False,
    )

    payment_method = Column(
        'payment_method',
        types.BOOLEAN,
        nullable=False,
    )

    transfers = Column(
        'transfers',
        types.Integer,
        nullable=False,
    )

    agency_id = Column(
        'agency_id',
        types.String,
        nullable=True,
    )

    transfer_duration = Column(
        'transfer_duration',
        types.Integer,
        nullable=True,
    )
