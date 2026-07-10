from src.timedelta19.util import time_delta


def test_sample_case1():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"

    assert time_delta(t1, t2) == 25200


def test_sample_case2():
    t1 = "Sat 02 May 2015 19:54:36 +0530"
    t2 = "Fri 01 May 2015 13:54:36 -0000"

    assert time_delta(t1, t2) == 88200


def test_same_time():
    t1 = "Mon 01 Jan 2024 10:00:00 +0000"
    t2 = "Mon 01 Jan 2024 10:00:00 +0000"

    assert time_delta(t1, t2) == 0


def test_one_hour_difference():
    t1 = "Mon 01 Jan 2024 11:00:00 +0000"
    t2 = "Mon 01 Jan 2024 10:00:00 +0000"

    assert time_delta(t1, t2) == 3600