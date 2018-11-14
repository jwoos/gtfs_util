from datetime import date, datetime, timedelta


def to_date(x):
    return datetime.strptime(x, '%Y%m%d').date()


def to_datetime(x):
    return datetime.from_timestamp(int(x))
