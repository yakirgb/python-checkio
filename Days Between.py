from datetime import date
days_diff = lambda d1, d2: abs(date(*d1)-date(*d2)).days
