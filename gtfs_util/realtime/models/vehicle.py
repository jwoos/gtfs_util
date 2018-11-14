from gtfs_util.realtime.models.base import Base

from collections import namedtuple


class Vehicle(namedtuple(
    'Vehicle',
    [
        'trip',
        'position',
        'timestamp',
        'stop_id',
        'vehicle',
    ],
)):
    pass
