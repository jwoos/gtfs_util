from gtfs_util.realtime.models.base import Base

from collections import namedtuple


class TripUpdate(namedtuple(
    'TripUpdate',
    [
        'trip',
        'stop_time_update',
    ]
)):
    pass