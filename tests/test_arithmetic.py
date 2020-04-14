import pytest

def test_addition():
    a = 5
    b = 2

    assert a + b == 7


def test_subtraction():
    a = 5
    b = 2

    assert a - b == 3


def test_multiplication():
    a = 5
    b = 2

    assert a * b == 10


def test_division():
    a = 5
    b = 5

    assert a / b == 1


def test_pi():
    from math import pi
    
    pi_approx = 22.0/7

    assert abs(pi - pi_approx) < 0.01

