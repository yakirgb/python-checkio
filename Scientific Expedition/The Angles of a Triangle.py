from math import acos, degrees
def checkio(a,b,c):
    angles = [0, 0, 0]
    if not (a + b > c) and (a + c > b) and (b + c > a):
        return angles
    angles[0] = round(degrees(acos((a**2 + b**2 - c**2) / (2 * a * b))))
    angles[1] = round(degrees(acos((a**2 + c**2 - b**2) / (2 * a * c))))
    angles[2] = 180 - angles[0] - angles[1]
    return sorted(angles)

print (checkio(2,2,5))
print (checkio(3,4,5))