from math import sqrt
from sqlite3 import DataError


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b


def squar_rot(a):
    number_types = (int, float, complex)
    try:
        if isinstance(a, number_types):
            return sqrt(a)
        else:
            raise DataError("Not a numeric type")
    except ValueError:
        return "nan"
    except DataError:
        raise


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square_root(self, a):
        self.result = squar_rot(a)
        return self.result
