import abc

from mta.gtfs import realtime

import aiohttp
import requests


FEED_BASE_URL = 'https://datamine.mta.info/mta_esi.php?key={key}&feed_id={feed_id}'


async def fetch_feed_async(feed_id, key, loop=None):
    url = FEED_BASE_URL.format(key=key, feed_id=feed_id)

    # TODO
    filename = None

    return parse_feed(filename)

def fetch_feed_sync(feed_id, key):
    url = FEED_BASE_URL.format(key=key, feed_id=feed_id)

    # TODO
    filename = None

    return parse_feed(filename)


def parse_feed(filename):
    feed = realtime.FeedMessage()
    with open(filename, 'rb') as file:
        content = file.read()
        feed.ParseFromString(content)
        return entity


class Subway(abc.ABC):
    def __init__(self, stops, schedule):
        self.stops = stops
        self.schedule = schedule


class A(Subway):
    pass


class C(Subway):
    pass


class E(Subway):
    pass
