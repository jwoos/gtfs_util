# transfers.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import TransferType
from gtfs_parser.model import MixIn


class Transfer(Base, MixIn):
    __tablename__ = 'transfer'
    __table_args__ = (
        schema.ForeignKeyConstraint(['source_stop_id'], ['stop.id']),
        schema.ForeignKeyConstraint(['destination_stop_id'], ['stop.id']),
    )

    PREFIX = 'transfer_'

    NAME_MAPPING = {
        'from_stop_id': 'source_stop_id',
        'to_stop_id': 'destination_stop_id',
        'min_transfer_time': 'minimum_time',
    }
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'source_stop_id',
        'destination_stop_id',
        'type',
        'minimum_time',
    )

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    source_stop_id = Column(
        'source_stop_id',
        types.String,
        nullable=False,
    )

    destination_stop_id = Column(
        'destination_stop_id',
        types.String,
        nullable=False,
    )

    type = Column(
        'type',
        types.Enum(TransferType),
        nullable=False,
    )

    minimum_time = Column(
        'minimum_time',
        types.Integer,
        nullable=True,
    )
