import datetime

def add_gigasecond(birth_date: datetime.datetime) -> datetime.datetime:
    return birth_date + datetime.timedelta(seconds=pow(10,9))
