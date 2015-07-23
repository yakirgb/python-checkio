from datetime import timedelta, date

def checkio(dateA, dateB):
    days = 0
    while dateB >= dateA:
        if dateB.isoweekday() in (6,7):
            days += 1
        dateB -= timedelta(1)
    return days

print(checkio(date(2013,2,2), date(2013,2,3)))
