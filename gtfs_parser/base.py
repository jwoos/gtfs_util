import abc


class Base(abc.ABC):
    def __init__(self, *args, **kwargs):
        self.arsg = args

        for k, v in kwargs.items():
            setattr(self, k, v)
