from gtfs_util.model import MixIn
from gtfs_util.realtime import data

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
    NAME_MAPPING = {}
    DATA_MAPPING = {
        'active_period': data.transform_active_period,
    }

    FIELDS = (
        'active_period',
        'description_text',
        'effect',
        'header_text',
        'informed_entity',
    )
