import abc


class Base(abc.ABC):
    @abc.abstracmethod
    def __init__(self):
        raise NotImplementedError()
