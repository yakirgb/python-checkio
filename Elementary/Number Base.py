def checkio2(*a):
    try:
        return int(*a)
    except ValueError:
        return -1
