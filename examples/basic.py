from mta.gtfs import realtime


feed = realtime.FeedMessage()
file = open('/opt/example/gtfs', 'rb')
content = file.read()
feed.ParseFromString(content)
print(feed.header)
for entity in feed.entity:
    if entity.HasField('trip_update'):
        # trip update
        # print(entity.trip_update)
        pass
    elif entity.HasField('vehicle'):
        # vehicle
        pass
    else:
        # alert
        pass
