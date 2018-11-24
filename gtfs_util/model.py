from collections import namedtuple


class Base(abc.ABC):
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
                k: getattr(self, k, None) for k in self.FIELDS if k not in blacklist
            }

        if whitelist:
            return {
                k: getattr(self, k, None) for k in self.FIELDS if k in whitelist
            }

        return {
            k: getattr(self, k, None) for k in self.FIELDS
        }
