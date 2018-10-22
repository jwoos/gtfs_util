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
        types.BOOLEAN,
        nullable=False,
    )

    tuesday = Column(
        'tuesday',
        types.BOOLEAN,
        nullable=False,
    )

    wednesday = Column(
        'wednesday',
        types.BOOLEAN,
        nullable=False,
    )

    thursday = Column(
        'thursday',
        types.BOOLEAN,
        nullable=False,
    )

    friday = Column(
        'friday',
        types.BOOLEAN,
        nullable=False,
    )

    saturday = Column(
        'saturday',
        types.BOOLEAN,
        nullable=False,
    )

    sunday = Column(
        'sunday',
        types.BOOLEAN,
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
