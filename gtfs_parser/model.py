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

    def jsonify(self):
        return {
            k: getattr(self, k, None) for k in self.FIELDS
        }

    @classmethod
    def name_transform(cls, name):
        return cls.NAME_MAPPING.get(name, None) or name.replace(cls.PREFIX, '')

    @classmethod
    def data_transform(cls, data):
        return cls.DATA_MAPPING.get(name, lambda x: x)(data)
