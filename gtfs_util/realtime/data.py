from datetime import date, datetime, timedelta


def flatten_dict(x, keys=set()):
    data = {}
    for k, v in x.items():
        if k not in keys:
            data[k] = v
        else:
            key, value = v.items()[0]
            data[f'{k}{key}'] = value
    return data


def transform_active_period(x):
    for active in x:
        start = active.get('start')
        if start:
            active['start'] = int(start)

        end = active.get('end')
        if end:
            active['end'] = int(end)

    return x


def transform_stop_time_update(x):
    for stop in x:
        stop['arrival']['time'] = int(stop['arrival']['time'])
        stop['departure']['time'] = int(stop['departure']['time'])

    return x


def transform_trip(x):
    transforms = {'start_date', 'end_date'}
    return {
        k: int(v) if k in transforms else v
        for k, v in x.items()
    }


def to_date(x):
    return datetime.strptime(x, '%Y%m%d').date()


def to_datetime(x):
    return datetime.fromtimestamp(int(x))
