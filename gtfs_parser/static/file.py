import asyncio
from csv import DictReader
from io import BytesIO
import json
import zipfile

from gtfs_parser.util import TextZipFile
from gtfs_parser import constants
from gtfs_parser.static.models import (
    agency,
    service,
    service_update,
    route,
    point,
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
    constants.POINT_FILENAME: point.Point,
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


async def load_aiter(*args, model=False, file=True, chunk_size=1):
    for arg in args:
        with TextZipFile(arg, 'r') as z:
            infos = z.infolist()
            for info in infos:
                name = info.filename
                with z.open(name, 'r') as f:
                    reader = DictReader(f)
                    static_model = FILENAME_MODEL_MAPPING[name]
                    reader.fieldnames = normalize_names(static_model, reader.fieldnames)

                    buffer = []

                    for line in reader:
                        normalized_line = normalize_data(static_model, line)

                        if model:
                            data = static_model(**normalized_line)
                        else:
                            data = (normalized_line, arg, name)

                        if chunk_size > 1:
                            buffer.append(data)
                            if len(buffer) == chunk_size:
                                yield buffer
                                buffer = []
                        else:
                            yield data

                    yield buffer


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


def load_iter(*args, model=False, file=True, chunk_size=1):
    if not file:
        args = [BytesIO(arg) for arg in args]

    for arg in args:
        with TextZipFile(arg, 'r') as z:
            infos = z.infolist()
            for info in infos:
                name = info.filename
                with z.open(name, 'r') as f:
                    reader = DictReader(f)
                    static_model = FILENAME_MODEL_MAPPING[name]
                    reader.fieldnames = normalize_names(static_model, reader.fieldnames)

                    buffer = []

                    for line in reader:
                        normalized_line = normalize_data(static_model, line)

                        if model:
                            data = (static_model(**normalized_line), arg, name)
                        else:
                            data = (normalized_line, arg, name)

                        if chunk_size > 1:
                            buffer.append(data)
                            if len(buffer) == chunk_size:
                                yield buffer
                                buffer = []
                        else:
                            yield data

                    yield buffer

        if not file:
            arg.close()


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


def normalize_data(model, raw_data):
    transforms = model.DATA_MAPPING

    return {
        k: v if not transforms.get(k) else transforms[k](v)
        for k, v in raw_data.items()
    }
