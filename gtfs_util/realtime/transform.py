from gtfs_parser.realtime.models import (
    alert,
    trip_update,
    vehicle
)


MODEL_MAPPING = {
    'trip_update': trip_update.TripUpdate,
    'alert': alert.Alert,
    'vehicle': vehicle.Vehicle,
}


def to_model(raw_data):
    data = {}

    for k, v in raw_data.items():
        model = MODEL_MAPPING[k]

        data[k] = [model(**x) for x in v]

    return data


def to_json(data):
    raise NotImplementedError()
