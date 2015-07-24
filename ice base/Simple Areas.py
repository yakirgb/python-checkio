from math import pi, sqrt
from operator import mul

def simple_areas(*args):
    def circle(d):
        return (d / 2)**2 * pi

    def triangle(a, b, c):
        return sqrt((a+b+c)*(a+b-c)*(a-b+c)*(b+c-a))/4

    switch = {
        1: circle,
        2: mul,
        3: triangle
    }
    return switch[len(args)](*args)