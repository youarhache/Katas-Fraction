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


def test_when_adding_2_7ths_and_3_7th_then_return_5_7ths():
    two_sevenths = Fraction(2, 7)
    three_sevenths = Fraction(3, 7)

    result = add_fractions(two_sevenths, three_sevenths)

    assert isinstance(result, Fraction)
    assert result.numerator == 5
    assert result.denominator == 7


def test_when_adding_1_half_and_1_third_then_return_5_6ths():
    frac1 = Fraction(1, 2)
    frac2 = Fraction(1, 3)

    result = add_fractions(frac1, frac2)

    assert isinstance(result, Fraction)
    assert result.numerator == 5
    assert result.denominator == 6