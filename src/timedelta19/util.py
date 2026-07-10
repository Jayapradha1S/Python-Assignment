from datetime import datetime


def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"

    d1 = datetime.strptime(t1, fmt)
    d2 = datetime.strptime(t2, fmt)

    return abs(int((d1 - d2).total_seconds()))