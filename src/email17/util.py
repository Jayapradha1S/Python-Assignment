import re


def fun(s):
    pattern = r'^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return bool(re.match(pattern, s))


def filter_emails(emails):
    return sorted(list(filter(fun, emails)))