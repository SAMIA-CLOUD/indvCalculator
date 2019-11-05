from math import sqrt


def squar_rot(a):
    if float(a) < 0:
        return "nan"
    return round(sqrt(int(a)), 8)
