def checkio(data):
    srt = sorted(data)
    mid = len(data)//2
    if len(data) % 2:
            return srt[mid]
    else:
        med = (srt[mid] + srt[mid-1]) / 2
        return med
print (checkio([1, 300, 2, 200, 1]))
#checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
#checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
#checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
#checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"