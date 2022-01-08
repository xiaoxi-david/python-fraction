import pytest
from fraction import Fraction


def test_invalid_string_numerator():
    with pytest.raises(ValueError) as e:
        Fraction("1", 2)
    assert str(e.value) == "The numerator must be an integer."


def test_invalid_float_numerator():
    with pytest.raises(ValueError) as e:
        Fraction(1.0, 2)
    assert str(e.value) == "The numerator must be an integer."


def test_invalid_string_denominator():
    with pytest.raises(ValueError) as e:
        Fraction(1, "2")
    assert str(e.value) == "The denominator must be a non-zero integer."


def test_invalid_float_denominator():
    with pytest.raises(ValueError) as e:
        Fraction(1, 2.0)
    assert str(e.value) == "The denominator must be a non-zero integer."


def test_invalid_nonzero_denominator():
    with pytest.raises(ValueError) as e:
        Fraction(1, 0)
    assert str(e.value) == "The denominator must be a non-zero integer."


def test_str():
    assert str(Fraction(1, 2)) == "1/2"


def test_repr():
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"


def test_simplify():
    assert Fraction(4, 8).simplify() == Fraction(1, 2)


def test_sum():
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)


def test_add_inv():
    assert Fraction(1, 2).add_inv() == Fraction(-1, 2)


def test_sub():
    assert Fraction(5, 6) - Fraction(1, 2) == Fraction(1, 3)


def test_mul():
    assert Fraction(2, 3) * Fraction(2, 3) == Fraction(4, 9)


def test_mul_inv():
    assert Fraction(2, 3).mul_inv() == Fraction(3, 2)


def test_div():
    assert Fraction(2, 5) / Fraction(3, 5) == Fraction(2, 3)


def test_eq():
    assert Fraction(2, 4) == Fraction(1, 2)


def test_ineq():
    assert Fraction(1, 2) != Fraction(1, 3)
