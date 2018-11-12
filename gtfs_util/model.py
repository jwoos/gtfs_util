import abc
from collections import namedtuple


class Base(abc.ABC):
    def __init__(self, *args, **kwargs):
        self.arsg = args

        for k, v in kwargs.items():
            setattr(self, k, v)


class Field(namedtuple(
    'Field',
    [
        'name',
        'type',
    ]
)):
    pass


# class MixIn(abc.ABC):
class MixIn:
    PREFIX = ''

    NAME_MAPPING = {}
    DATA_MAPPING = {}

    FIELDS = ()

    def json(self):
        return {
            k: getattr(self, k, None) for k in self.FIELDS
        }
