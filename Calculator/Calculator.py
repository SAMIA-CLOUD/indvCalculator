from math import sqrt
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square_rot import squar_rot
from Calculator.Square import squaree


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

    def square(self, a):
        self.result = squaree(a)
        return self.result

    def square_root(self, a):
        self.result = squar_rot(a)
        return self.result
