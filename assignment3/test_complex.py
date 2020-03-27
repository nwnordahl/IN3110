from complex import Complex
import numpy as np


def test_add1():
    z_1 = Complex(1, 1)
    z_2 = Complex(1, 1)
    assert z_1 + z_2 == Complex(2, 2)


def test_add2():
    z_1 = Complex(1, 0)
    z_2 = Complex(0, 1)
    assert z_1 + z_2 == Complex(1, 1)


def test_add3():
    z_1 = Complex(0, 0)
    z_2 = Complex(1, 1)
    assert z_1 + z_2 == Complex(1, 1)


def test_sub1():
    z_1 = Complex(1, 1)
    z_2 = Complex(1, 1)
    assert z_1 - z_2 == Complex(0, 0)


def test_sub2():
    z_1 = Complex(1, 0)
    z_2 = Complex(0, 1)
    assert z_1 - z_2 == Complex(1, -1)


def test_sub3():
    z_1 = Complex(0, 0)
    z_2 = Complex(1, 1)
    assert z_1 - z_2 == Complex(-1, -1)


def test_mul1():
    z_1 = Complex(1, 1)
    z_2 = Complex(1, 1)
    assert z_1 * z_2 == Complex(0, 2)


def test_mul2():
    z_1 = Complex(1, 0)
    z_2 = Complex(0, 1)
    assert z_1 * z_2 == Complex(0, 1)


def test_mul3():
    z_1 = Complex(1, 1)
    assert 2 * z_1 == Complex(2, 2)


def test_conjugate1():
    z_1 = Complex(1, 0)
    assert z_1.conjugate() == Complex(1, 0)


def test_conjugate2():
    z_1 = Complex(0, 1)
    assert z_1.conjugate() == Complex(0, -1)


def test_modulus():
    z_1 = Complex(1, 1)
    assert abs(np.sqrt(2) - z_1.modulus()) < 1e-14


def test_eq1():
    z_1 = Complex(0, 0)
    assert z_1 == z_1


def test_eq2():
    z_1 = Complex(1, 0)
    assert z_1 == z_1


def test_eq3():
    z_1 = Complex(1, 1)
    assert z_1 == z_1


def test_add_mixed():
    z_1 = Complex(2, 3)
    assert z_1 + (2 + 2j) == Complex(4, 5)


def test_mul_sub_mixed():
    z_1 = Complex(3, 4)
    assert 4 * z_1 - 2 == Complex(10, 16)
