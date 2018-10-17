from google.protobuf.json_format import MessageToDict
from google.transit import gtfs_realtime_pb2


def load(filename, model=False):
    if model:
        raise NotImplementedError()

    with open(filename, 'rb') as f:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(f.read())

        raw_data = MessageToDict(feed)
        data = {
            'trip_update': [],
            'vehicle': [],
        }

        for inner_id, inner_data in raw_data.items():
            if 'trip_update' in inner_data:
                data['trip_update'].append(inner_data)
            else:
                data['vehicle'].append(inner_data)

        return data
