import asyncio

from gtfs_util.realtime.models import (
    alert,
    trip_update,
    vehicle_position,
)
from gtfs_util import util

import aiofiles
from google.protobuf.json_format import MessageToDict
from google.transit import gtfs_realtime_pb2
from google.protobuf.message import DecodeError


def safe_parse_from_string(feed, data):
    okay = True

    try:
        feed.ParseFromString(data)
    except DecodeError:
        okay = False

    return okay


async def _read_async(data, file=True):
    feed = gtfs_realtime_pb2.FeedMessage()

    if file:
        async with aiofiles.open(data, 'rb') as f:
            okay = safe_parse_from_string(feed, await f.read())
            if not okay:
                feed = None
    else:
        okay = safe_parse_from_string(feed, data)
        if not okay:
            feed = None

    return feed


async def load_async(*args, model=False, file=True):
    ops = (
        x for x in (
            _read_async(arg, file=file)
            for arg in args
        ) if x
    )
    feeds = await asyncio.gather(*ops)

    return _parse(feeds, model=model)


async def load_aiter(*args, model=False, file=True, chunk_size=1):
    raise NotImplementedError()


def _read(data, file=True):
    feed = gtfs_realtime_pb2.FeedMessage()

    if file:
        with open(data, 'rb') as f:
            okay = safe_parse_from_string(feed, f.read())
            if not okay:
                feed = None
    else:
        okay = safe_parse_from_string(feed, data)
        if not okay:
            feed = None

    return feed


def load(*args, model=False, file=True):
    feeds = (
        x for x in (
            _read(arg, file=file)
            for arg in args
        ) if x
    )

    return _parse(feeds, model=model)


def load_iter(*args, model=False, file=True, chunk_size=1) -> (dict, str, str):
    raise NotImplementedError()


def _parse(feeds, model=False):
    data = {
        'trip_update': [],
        'vehicle_position': [],
        'alert': [],
    }

    for feed in feeds:
        raw_data = MessageToDict(feed)

        for inner_data in raw_data['entity']:
            normalized_inner_data = normalize_names(inner_data)

            if 'trip_update' in normalized_inner_data:
                normalized_inner_data = normalize_data(trip_update.TripUpdate, normalized_inner_data['trip_update'])
                if model:
                    data['trip_update'].append(
                        trip_update.TripUpdate(**(normalized_inner_data))
                    )
                else:
                    data['trip_update'].append(normalized_inner_data)

            elif 'alert' in normalized_inner_data:
                normalized_inner_data = normalize_data(alert.Alert, normalized_inner_data['alert'])
                if model:
                    data['alert'].append(
                        alert.Alert(**normalized_inner_data)
                    )
                else:
                    data['alert'].append(normalized_inner_data)

            elif 'vehicle' in normalized_inner_data:
                normalized_inner_data = normalize_data(vehicle_position.VehiclePosition, normalized_inner_data['vehicle'])
                if model:
                    data['vehicle_position'].append(
                        vehicle.Vehicle(**normalized_inner_data)
                    )
                else:
                    data['vehicle_position'].append(normalized_inner_data)

    return data


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


def normalize_data(model, raw_data):
    data = {}

    for k, v in raw_data.items():
        transform = model.DATA_MAPPING.get(k)
        if transform:
            data[k] = transform(v)
        else:
            data[k] = v

    return data
