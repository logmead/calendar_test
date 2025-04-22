import datetime as dt
from pytz import UTC

def NOW():
    return dt.datetime.now().replace(tzinfo=UTC)


def TODAY():
    return NOW().date()

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

START_YEAR = 2010

def get_months(current_date):
    MONTHS = []
    sub = []
    for i in range(1, 13):
        dat = dt.date(year=current_date.year, month=i, day=1)
        sub.append({
            'name' : dat.strftime("%b"),
            'string' : dat.strftime("%Y-%m-%d"),
        })
        if len(sub) == 4:
            MONTHS.append(sub)
            sub = []
    return MONTHS


def get_years(current_date):

    YEARS = []
    sub = []
    for i in range(START_YEAR, TODAY().year + 1):
        dat = dt.date(year=i, month=current_date.month, day=1)
        sub.append({
            'name' : i,
            'string' : dat.strftime("%Y-%m-%d"),
        })
        if len(sub) == 4:
            YEARS.append(sub)
            sub = []

    if len(sub) > 0 and len(sub) < 4:
        YEARS.append(sub)
        

    return YEARS
