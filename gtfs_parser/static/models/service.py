# calendar.txt

from sqlalchemy import Column, types, schema

from gtfs_parser.static.models.base import Base


class Service(Base):
    __tablename__ = 'service'
    __table_args__ = ()

    PREFIX = 'calendar_'

    NAME_MAPPING = {}
    DATA_MAPPING = {}

    FIELDS = (
        'id',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
        'start_date',
        'end_date',
    )


    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    monday = Column(
        'monday',
        types.Bool,
        nullable=False,
    )

    tuesday = Column(
        'tuesday',
        types.Bool,
        nullable=False,
    )

    wednesday = Column(
        'wednesday',
        types.Bool,
        nullable=False,
    )

    thursday = Column(
        'thursday',
        types.Bool,
        nullable=False,
    )

    friday = Column(
        'friday',
        types.Bool,
        nullable=False,
    )

    saturday = Column(
        'saturday',
        types.Bool,
        nullable=False,
    )

    sunday = Column(
        'sunday',
        types.Bool,
        nullable=False,
    )

    start_date = Column(
        'start_date',
        types.Date,
        nullable=False,
    )

    end_date = Column(
        'end_date',
        types.Date,
        nullable=False,
    )
