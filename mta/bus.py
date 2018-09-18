import abc

from mta.gtfs import realtime


FEED_BASE_URL = ''


class Bus(abc.ABC):
    def __init__(self, stops, schedule):
        self.stops = stops
        self.schedule = schedule
