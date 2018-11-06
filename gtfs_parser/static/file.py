import asyncio
from csv import DictReader
from io import BytesIO
import json
import zipfile

from gtfs_parser import constants
from gtfs_parser.static.models import (
    agency,
    service,
    service_update,
    route,
    shape,
    stop_time,
    stop,
    transfer,
    trip,
)


FILENAME_MODEL_MAPPING = {
    constants.AGENCY_FILENAME: agency.Agency,
    constants.SERVICE_FILENAME: service.Service,
    constants.SERVICE_UPDATE_FILENAME: service_update.ServiceUpdate,
    constants.ROUTE_FILENAME: route.Route,
    constants.SHAPE_FILENAME: shape.Shape,
    constants.STOP_TIME_FILENAME: stop_time.StopTime,
    constants.STOP_FILENAME: stop.Stop,
    constants.TRANSFER_FILENAME: transfer.Transfer,
    constants.TRIP_FILENAME: trip.Trip,
}


async def _read_async(data, file=True):
    if file:
        with zipfile.ZipFile(data, 'r') as f:
            infos = f.infolist()
            raw_data = {
                i.filename: DictReader(f.read(i.filename).decode().split('\r\n'))
                for i in infos
            }
    else:
        with BytesIO(data) as buffer:
            with zipfile.ZipFile(buffer, 'r') as f:
                infos = f.infolist()
                raw_data = {
                    i.filename: DictReader(f.read(i.filename).decode().split('\r\n'))
                    for i in infos
                }

    return raw_data


async def load_async(*args, model=False, file=True):
    ops = (
        _read_async(arg, file=fie)
        for arg in args
    )
    feeds = await asyncio.gather(*ops)

    return _parse(feeds, model=model)


def _read(data, file=True):
    if file:
        with zipfile.ZipFile(data, 'r') as f:
            infos = f.infolist()
            raw_data = {
                i.filename: DictReader(f.read(i.filename).decode().split('\r\n'))
                for i in infos
            }
    else:
        with BytesIO(data) as buffer:
            with zipfile.ZipFile(buffer, 'r') as f:
                infos = f.infolist()
                raw_data = {
                    i.filename: DictReader(f.read(i.filename).decode().split('\r\n'))
                    for i in infos
                }

    return raw_data


def load(*args, model=False, file=True):
    feeds = (
        _read(arg, file=file)
        for arg in args
    )

    return _parse(feeds, model=model)


def _parse(feeds, model=False):
    data = {
        'agency.txt': [],
        'stops.txt': [],
        'routes.txt': [],
        'trips.txt': [],
        'stop_times.txt': [],
        'calendar.txt': [],
        'calendar_dates.txt': [],
        'fare_attributes.txt': [],
        'fare_rules.txt': [],
        'shapes.txt': [],
        'frequencies.txt': [],
        'transfers.txt': [],
        'feed_info.txt': [],
    }

    for feed in feeds:
        for file, reader in feed.items():
            static_model = FILENAME_MODEL_MAPPING[file]
            reader.fieldnames = normalize_names(static_model, reader.fieldnames)
            if model:
                data[file] += [static_model(**normalize_data(static_model, x)) for x in reader]
            else:
                data[file] += [normalize_data(static_model, x) for x in reader]

    return data


def normalize_names(model, raw_data):
    data = [
        model.name_transform(name) for name in raw_data
    ]

    return data


## TODO
def normalize_data(model, raw_data):
    return dict(raw_data)
