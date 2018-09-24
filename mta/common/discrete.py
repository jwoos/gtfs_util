import abc
from collections import namedtuple
from csv import DictReader


def persist(elems):
    for elem in elems:
        elem.persist()


class BaseDiscreteCommon(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def parse(filename):
        raise NotImplementedError()

    @abc.abstractmethod
    def persist(self):
        raise NotImplementedError()


class DiscreteRoute(namedtuple(
    'DiscreteRoute',
    [
        'id',
        'agency_id',
        'short_name',
        'long_name',
        'description',
        'type',
        'url',
        'color',
        'text_color',
    ],
)):
    MAPPING = {
        'id': 'route_id',
        'agency_id': 'agency_id',
        'short_name': 'route_short_name',
        'long_name': 'route_long_name',
        'description': 'route_desc',
        'type': 'route_type',
        'url': 'route_url',
        'color': 'route_color',
        'text_color': 'route_text_color',
    }

    @staticmethod
    def parse(filename):
        with open(filename, 'r') as file:
            reader = DictReader(file)
            return {
                row['route_id']: DiscreteRoute(**{
                    k: row[v] for k, v in DiscreteRoute.MAPPING.items()
                }) for row in reader
            }

    def persist(self):
        pass


class DiscreteStop(BaseDiscreteCommon, namedtuple(
    'DiscreteStop',
    [
        'id',
        'code',
        'name',
        'description',
        'latitude',
        'longitude',
        'zone_id',
        'url',
        'location_type',
        'parent_station',
    ],
)):
    MAPPING = {
        'id': 'stop_id',
        'code': 'stop_code',
        'name': 'stop_name',
        'description': 'stop_desc',
        'latitude': 'stop_lat',
        'longitude': 'stop_lon',
        'zone_id': 'zone_id',
        'url': 'stop_url',
        'location_type': 'location_type',
        'parent_station': 'parent_station',
    }

    @staticmethod
    def parse(filename):
        with open(filename, 'r') as file:
            reader = DictReader(file)
            return {
                row['stop_id']: DiscreteStop(**{
                    k: row[v] for k, v in DiscreteStop.MAPPING.items()
                }) for row in reader
            }


class DiscreteStopTime(BaseDiscreteCommon, namedtuple(
    'DiscreteStopTime',
    [
        'trip_id',
        'arrival_time',
        'departure_time',
        'id',
        'sequence',
        'headsign',
        'pickup_type',
        'drop_off_type',
        'shape_dist_traveled',
    ],
)):
    MAPPING = {
        'id': 'trip_id',
        'arrival_time': 'arrival_time',
        'departure_time': 'departure_time',
        'id': 'stop_id',
        'sequence': 'stop_sequence',
        'headsign': 'stop_headsign',
        'pickup_type': 'pickup_type',
        'drop_off_type': 'drop_off_type',
        'shape_dist_traveled': 'shape_dist_traveled',
    }

    @staticmethod
    def parse(filename):
        with open(filename, 'r') as file:
            reader = DictReader(file)
            return {
                row['stop_id']: DiscreteStopTime(**{
                    k: row[v] for k, v in DiscreteStopTime.MAPPING.items()
                }) for row in reader
            }


class DiscreteTrip(BaseDiscreteCommon, namedtuple(
    'DiscreteTrip',
    [
        'route_id',
        'service_id',
        'id',
        'headsign',
        'direction_id',
        'block_id',
        'shape_id',
    ]
)):
    MAPPING = {
        'route_id': 'route_id',
        'sevice_id': 'service_id',
        'id': 'trip_id',
        'headsign': 'trip_headsign',
        'direction_id': 'direction_id',
        'block_id': 'block_id',
        'shape_id': 'shape_id',
    }

    @staticmethod
    def parse(filename):
        with open(filename, 'r') as file:
            reader = DictReader(file)
            return {
                row['trip_id']: DiscreteTrip(**{
                    k: row[v] for k, v in DiscreteTrip.MAPPING.items()
                }) for row in reader
            }
