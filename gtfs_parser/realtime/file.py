from gtfs_parser.realtime.models import (
    alert,
    trip_update,
    vehicle
)
from gtfs_parser import util

from google.protobuf.json_format import MessageToDict
from google.transit import gtfs_realtime_pb2


def load(*args, model=False):
    feeds = []

    for file in args:
        with open(file, 'rb') as f:
            feed = gtfs_realtime_pb2.FeedMessage()
            feeds.append(feed)
            feed.ParseFromString(f.read())

    data = {
        'trip_update': [],
        'vehicle': [],
        'alert': [],
    }

    for feed in feeds:
        raw_data = MessageToDict(feed)

        for inner_data in raw_data['entity']:
            normalized_inner_data = normalize_data(normalize_names(inner_data))

            if 'tripUpdate' in inner_data:
                if model:
                    data['trip_update'].append(
                        trip_update.TripUpdate(**normalized_inner_data['trip_update'])
                    )
                else:
                    data['trip_update'].append(normalized_inner_data['trip_update'])

            if 'alert' in normalized_inner_data:
                if model:
                    data['alert'].append(
                        alert.Alert(**normalized_inner_data['alert'])
                    )
                else:
                    data['alert'].append(normalized_inner_data['alert'])

            if 'vehicle' in normalized_inner_data:
                if model:
                    data['vehicle'].append(
                        vehicle.Vehicle(**normalized_inner_data['vehicle'])
                    )
                else:
                    data['vehicle'].append(normalized_inner_data['vehicle'])

    return data


def normalize(model, raw_data):
    pass


def normalize_names(raw_data):
    data = None

    if isinstance(raw_data, dict):
        data = {
            util.camel_to_snake(k): normalize_names(v)
            for k, v in raw_data.items()
        }

    elif isinstance(raw_data, list):
        data = [
            normalize_names(x) for x in raw_data
        ]

    else:
        data = raw_data

    return data


def normalize_data(raw_data):
    return raw_data
