import calendar
import datetime
from calendar import monthrange


def deltatime(t1: datetime, t2: datetime):
    dm = 0
    dy = 0
    lm = calendar.monthrange(t1.year, t1.month)
    if t2.day < t1.day:
        delta_d = lm[1] - t1.day + t2.day
        dm = 1
    else:
        delta_d = t2.day - t1.day

    if t2.month < t1.month:
        delta_m = 12 - t1.month + t2.month - dm
        dy = 1
    else:
        delta_m = t2.month - t1.month - dm

    delta_y = t2.year - t1.year - dy

    return f'{delta_y} г {delta_m} м {delta_d} д'



date_from = datetime.datetime.strptime(input(), '%d.%m.%Y')
date_to = datetime.datetime.strptime(input(), '%d.%m.%Y')
delta = deltatime(date_from, date_to)
print (delta)

