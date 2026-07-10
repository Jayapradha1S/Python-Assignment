import calendar

def find_day(month, date, year):
    wkd = calendar.weekday(year, month, date)
    r = calendar.day_name[wkd].upper()
    return r