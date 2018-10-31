from csv import DictReader
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


def load(filename, model=False):
    with zipfile.ZipFile(filename, 'r') as f:
        infos = f.infolist()
        raw_data = {
            i.filename: DictReader(f.read(i.filename).decode().split('\r\n'))
            for i in infos
        }

        data = {}

        print(raw_data)

        for file, reader in raw_data.items():
            print(file, reader)
            static_model = FILENAME_MODEL_MAPPING[file]
            reader.fieldnames = normalize_names(static_model, reader.fieldnames)
            if model:
                print(static_model, reader.fieldnames)
                data[file] = [static_model(**normalize_data(static_model, x)) for x in raw_data[file]]
            else:
                data[file] = [normalize_data(static_model, x) for x in raw_data[file]]

    return data


def normalize_names(model, raw_data):
    data = [
        model.name_transform(name) for name in raw_data
    ]

    return data


## TODO
def normalize_data(model, raw_data):
    return dict(raw_data)
