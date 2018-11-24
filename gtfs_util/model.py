from abc import ABC
from collections import namedtuple


class Base(ABC):
    def __init__(self, *args, **kwargs):
        self.arsg = args

        for k, v in kwargs.items():
            setattr(self, k, v)


class MixIn:
    PREFIX = ''

    NAME_MAPPING = {}
    DATA_MAPPING = {}

    FIELDS = ()

    def json(self, whitelist=set(), blacklist=set()):
        if blacklist:
            return {
                k: getattr(self, k, None) for k in self.FIELDS - blacklist
            }

        if whitelist:
            return {
                k: getattr(self, k, None) for k in whitelist & self.FIELDS
            }

        return {
            k: getattr(self, k, None) for k in self.FIELDS
        }
