#!/usr/bin/env python3

import numpy as np


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def conjugate(self):
        return Complex(self.a, -self.b)

    def modulus(self):
        return np.sqrt(self.a**2 + self.b**2)

    def __add__(self, other):
        try:
            return Complex(self.a + other.a, self.b + other.b)
        except AttributeError:
            return Complex(self.a + other, self.b)

    def __radd__(self, other):
        return Complex(self.a + other, self.b)

    def __sub__(self, other):
        try:
            return Complex(self.a - other.a, self.b - other.b)
        except AttributeError:
            return Complex(self.a - other, self.b)

    def __rsub__(self, other):
        return Complex(self.a - other, self.b)

    def __mul__(self, other):
        try:
            return Complex(self.a * other.a - self.b * other.b,
                           self.a * other.b + self.b * other.a)
        except AttributeError:
            return Complex(self.a * other, self.b * other)

    def __rmul__(self, other):
        return Complex(self.a * other, self.b * other)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __complex__(self):
        return self.a, self.b
