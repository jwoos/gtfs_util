import asyncio

from gtfs_parser.realtime.models import (
    alert,
    trip_update,
    vehicle
)
from gtfs_parser import util

import aiofiles
from google.protobuf.json_format import MessageToDict
from google.transit import gtfs_realtime_pb2


async def _read_async(data, file=True):
    feed = gtfs_realtime_pb2.FeedMessage()

    if file:
        async with aiofiles.open(data, 'rb') as f:
            feed.ParseFromString(await f.read())
    else:
        feed.ParseFromString(data)

    return feed


async def load_async(*args, model=False, file=True):
    ops = (
        _read_async(arg, file=file)
        for arg in args
    )
    feeds = await asyncio.gather(*ops)

    return _parse(feeds, model=model)


def _read(data, file=True):
    feed = gtfs_realtime_pb2.FeedMessage()

    if file:
        with open(data, 'rb') as f:
            feed.ParseFromString(f.read())
    else:
        feed.ParseFromString(data)

    return feed


def load(*args, model=False, file=True):
    feeds = (
        _read(arg, file=file)
        for arg in args
    )

    return _parse(feeds, model=model)


def _parse(feeds, model=False):
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
