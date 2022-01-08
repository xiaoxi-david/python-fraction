from __future__ import annotations
import math


class Fraction:
    """A library for arithmetic operations on fractions."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initializes a Fraction object"""
        if not isinstance(numerator, int):
            raise ValueError("The numerator must be an integer.")
        elif not isinstance(denominator, int) or denominator == 0:
            raise ValueError("The denominator must be a non-zero integer.")
        else:
            self.numerator = numerator
            self.denominator = denominator

    def simplify(self: Fraction) -> Fraction:
        """Simplifies a Fraction object."""
        gcd = math.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def __repr__(self: Fraction) -> str:
        """Machine-readable representation of a Fraction object."""
        return (
            f"{self.__class__.__name__}({self.numerator}, {self.denominator})"
        )

    def __str__(self: Fraction) -> str:
        """Human-readable representation of a Fraction object."""
        return (
            f"{self.numerator}/{self.denominator}"
            if self.denominator != 1
            else f"{self.numerator}"
        )

    def __add__(self: Fraction, other: Fraction) -> Fraction:
        """Adds two Fraction objects."""
        result = Fraction(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
        return result.simplify()

    def add_inv(self: Fraction) -> Fraction:
        """Returns the additive inverse of a Fraction object."""
        return Fraction(-self.numerator, self.denominator)

    def __sub__(self: Fraction, other: Fraction) -> Fraction:
        """Substrats one Fraction object from another one."""
        result = self + other.add_inv()
        return result.simplify()

    def __mul__(self: Fraction, other: Fraction) -> Fraction:
        """Multiplies two Fraction objects."""
        result = Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
        return result.simplify()

    def mul_inv(self: Fraction) -> Fraction:
        """Returns the multiplicative inverse of a Fraction object."""
        return Fraction(self.denominator, self.numerator)

    def __truediv__(self: Fraction, other: Fraction) -> Fraction:
        """Divides two Fraction objects."""
        result = self * other.mul_inv()
        return result.simplify()

    def __float__(self: Fraction) -> float:
        return self.numerator / self.denominator

    def __eq__(self: Fraction, other: Fraction) -> bool:
        """Checking whether two Fraction objects are equal to each other."""
        return (
            self.numerator * other.denominator
            == other.numerator * self.denominator
        )

    def __ne__(self: Fraction, other: Fraction) -> bool:
        """Checks whether two Fraction objects are not equal to each other."""
        return not self.__eq__(other)

    def __lt__(self: Fraction, other: Fraction) -> bool:
        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )

    def __le__(self: Fraction, other: Fraction) -> bool:
        return (
            self.numerator * other.denominator
            <= other.numerator * self.denominator
        )

    def __gt__(self: Fraction, other: Fraction) -> bool:
        return (
            self.numerator * other.denominator
            > other.numerator * self.denominator
        )

    def __ge__(self: Fraction, other: Fraction) -> bool:
        return (
            self.numerator * other.denominator
            >= other.numerator * self.denominator
        )
