import pytest
from dataclasses import FrozenInstanceError
from fraction import Fraction, add_fractions


def test_can_create_fraction():
    my_fraction = Fraction(1,2)

    assert isinstance(my_fraction, Fraction)
    assert my_fraction.numerator == 1
    assert my_fraction.denominator == 2


def test_can_not_modify_fraction():
    my_fraction = Fraction(1,2)

    with pytest.raises(FrozenInstanceError) as e:
        my_fraction.numerator = 3


def test_when_adding_2_fifths_and_1_fifth_then_return_3_fifths():
    two_fifths = Fraction(2, 5)
    one_fifth = Fraction(1, 5)

    result = add_fractions(two_fifths, one_fifth)

    assert isinstance(result, Fraction)
    assert result.numerator == 3
    assert result.denominator == 5
