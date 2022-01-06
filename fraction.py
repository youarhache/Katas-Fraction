from dataclasses import dataclass


@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int


def add_fractions(frac1: Fraction, frac2: Fraction) -> Fraction:
    if frac1.denominator != frac2.denominator:
        return Fraction(frac1.numerator*frac2.denominator + frac2.numerator*frac1.denominator,
                    frac1.denominator*frac2.denominator)

    return Fraction(frac1.numerator + frac2.numerator,
                    frac1.denominator)
