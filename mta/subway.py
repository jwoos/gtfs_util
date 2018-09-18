from collections import namedtuple
from csv import DictReader

from mta.gtfs import realtime


def parse_stops(filename):
    with open(filename, 'r') as file:
        reader = DictReader(file)
        SubwayStop = namedtuple('SubwayStop', reader.fieldnames)
        return {
            row.stop_id: SubwayStop(**row) for row in reader
        }


class SubwayStop:
    def __init__(
        self,
        id: str,
        code: str,
        name: str,
        description: str,
        latitude: float,
        longitude: float,
        zone: int,
        url: str,
        location_type: int,
        parent_station: int,
    ) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.zone = zone
        self.url = url
        self.location_type = location_type
        self.parent_station = parent_station

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


class RealTimeData:
    pass
