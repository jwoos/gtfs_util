from google.protobuf.json_format import MessageToDict
from google.transit import gtfs_realtime_pb2


def load(filename, model=False):
    if model:
        raise NotImplementedError()

    with open(filename, 'rb') as f:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(f.read())
        return MessageToDict(feed)
