import abc


class MixIn(abc.ABC):
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
        return cls.NAME_MAPPING.get(name, None) or name.strip(cls.PREFIX)

    @classmethod
    def data_transform(cls, data):
        return cls.DATA_MAPPING.get(name, lambda x: x)(data)
