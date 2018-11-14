from gtfs_util.realtime.models.base import Base

from collections import namedtuple


class Alert(namedtuple(
    'Alert',
    [
        'active_period',
        'description_text',
        'effect',
        'header_text',
        'informed_entity',
    ],
)):
    pass
