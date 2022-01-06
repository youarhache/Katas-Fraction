from fraction import Fraction


def test_can_create_fraction():
    my_fraction = Fraction(1,2)

    assert isinstance(my_fraction, Fraction)