from csv import DictReader
import json
import zipfile

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
    'agency.txt': agency.Agency,
    'calendar.txt': service.Service,
    'calendar_dates.txt': service_update.ServiceUpdate,
    'routes.txt': route.Route,
    'shapes.txt': shape.Shape,
    'stop_times.txt': stop_time.StopTime,
    'stops.txt': stop.Stop,
    'transfers.txt': transfer.Transfer,
    'trips.txt': trip.Trip,
}


def load(filename, model=False):
    if model:
        raise NotImplementedError()

    with zipfile.ZipFile(filename, 'r') as f:
        infos = f.infolist()
        data = {
            i.filename: DictReader(f.read(i.filename).decode().split('\r\n'))
            for i in infos
        }

        # TODO clean up fieldnames to match model
        # for file, reader in data.items():
            # reader.fieldnames = [x for x in reader.fieldnames]

    return data


def load_file(filename, model=False):
    if model:
        raise NotImplementedError()

    with open(filename, 'r') as f:
        return DictReader(f.read().split('\r\n'))


def normalize_names(raw_data):
    data = None
