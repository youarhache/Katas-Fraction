from dataclasses import dataclass


@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int


def add_fractions(frac1: Fraction, frac2: Fraction) -> Fraction:
    numerator = frac1.numerator*frac2.denominator + frac2.numerator*frac1.denominator
    denominator = frac1.denominator*frac2.denominator
    gcd_fraction = gcd(numerator, denominator)
    if gcd_fraction == 1:
        return Fraction(numerator, denominator)
    else:
        return Fraction(numerator/gcd_fraction, denominator/gcd_fraction)


def gcd(a:int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)