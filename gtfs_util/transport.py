from gtfs_parse.base import Base


class Transport(Base):
    def __init__(
        self,
        trips=None,
        stops=None,
        stop_times=None,

    ):
        self.trips = trips
        if self.trips is None:
            trips = {}

        self.stops = stops
        if self.stops is None:
            stops = {}

        self.stop_times = stop_times
        if self.stop_times is None:
            stops = {}
