from gtfs_util.model import MixIn
from gtfs_util.realtime import data

from collections import namedtuple


class VehiclePosition(namedtuple(
    'VehiclePosition',
    [
        'trip',
        'position',
        'timestamp',
        'stop_id',
        'vehicle',
    ],
), MixIn):
    NAME_MAPPING = {}
    DATA_MAPPING = {
        'timestamp': int,
        'trip': data.transform_trip,
    }

    FIELDS = (
        'trip',
        'position',
        'timestamp',
        'stop_id',
        'vehicle',
    )
