from dataclasses import dataclass


@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int
