# transfers.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base
from gtfs_parser.enum import TransferType


class Transfer(Base):
    __tablename__ = 'transfer'
    __table_args__ = ()

    PREFIX = 'transfer_'

    NAME_MAPPING = {
        'min_transfer_time': 'minimum_time',
    }
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'type',
        'minimum_time',
    )

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
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
