from gtfs_parser.realtime.models.base import Base

from collections import namedtuple


class Vehicle(namedtuple(
    'Vehicle',
    [
        'trip',
        'current_stop_sequence',
        'current_status',
        'timestamp',
        'stop_id',
    ],
)):
    pass
