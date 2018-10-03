from sqlalchemy import Column
from sqlalchemy.types import String, Integer, DECIMAL, Enum

from gtfs_parser.models.base import Base


MAPPING = {
}


def transformer(original):
    return MAPPING.get(original, None) or original.strip('trip_')
