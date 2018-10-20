import abc


class Base(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError()
