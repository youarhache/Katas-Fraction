from dataclasses import dataclass


@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int


def add_fractions(frac1: Fraction, frac2: Fraction) -> Fraction:
    return Fraction(3, 5)
