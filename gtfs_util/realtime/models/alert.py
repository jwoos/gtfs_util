from gtfs_util.realtime.models.base import Base

from collections import namedtuple


class Alert(namedtuple(
    'Alert',
    [
        'informed_entity',
        'header_text',
    ],
)):
    pass
