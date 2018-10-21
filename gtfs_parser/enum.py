from enum import Enum


class LocationType(Enum):
    STOP = 0
    STATION = 1
    STATION_ENTRANCE = 2


class WheelchairBoarding(Enum):
    NO_INFORMATION = 0
    ACCESSIBLE = 1
    NOT_ACCESSIBLE = 2


class RouteType(Enum):
    TRAM = 0
    SUBWAY = 1
    RAIL = 2
    BUS = 3
    FERRY = 4
    CABLE_CAR = 5
    GONDOLA = 6
    FUNICULAR = 7


class PickupType(Enum):
    SCHEDULED = 0
    NOT_AVAILABLE = 1
    PHONE = 2
    COORDINATE = 3


class DropoffType(Enum):
    SCHEDULED = 0
    NOT_AVAILABLE = 1
    PHONE = 2
    COORDINATE = 3


class ExceptionType(Enum):
    ADDED = 1
    REMOVED = 2


class TransferType(Enum):
    RECOMMENDED = 0
    TIMED = 1
    MINIMUM_WAIT = 2
    NOT_AVAILABLE = 3
