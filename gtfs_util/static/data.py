from datetime import datetime, date, timedelta


def to_generic(_type, nullable=False):
    def _xform(x):
        if x != '' and x is not None:
            return _type(x)
        elif nullable:
            return None
        else:
            return _type()

    return _xform


def to_bool(val=None, nullable=False):
    def _xform(x):
        if val:
            return x == '1' or x == ''
        elif nullable:
            return x == '1' if x != '0' else None
        else:
            return x == '1'

    return _xform


def to_enum(enum):
    def _xform(char):
        return enum(int(char))

    return _xform


def to_datetime(x):
    pass


def to_date(x):
    return datetime.strptime(x, '%Y%m%d').date()


# Use a DateTime to store time - everything except the time won't matter
def to_time(x):
    return datetime.strptime(f'1900-01-01 {x}', '%Y-%m-%d %H:%M:%S')


def to_timedelta(val):
    vals = [int(x) for x in val.split(':')]
    return timedelta(hours=vals[0], minutes=vals[1], seconds=vals[2])
