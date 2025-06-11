import pytest
from modules.invert_string import invert_string

def test_invert_string_with_short_sentence ():
    string_to_invert = "Hello World"

    result = invert_string(string_to_invert)

    assert result == "dlroW olleH"

def test_invert_string_with_long_sentence ():
    string_to_invert = "She always drinks coffee before starting her work in the morning"

    result = invert_string(string_to_invert)

    assert result == "gninrom eht ni krow reh gnitrats erofeb eeffoc sknird syawla ehS"

def test_invert_string_with_alphanumerical_sentence():
    string_to_invert = "A7dK92LmXq18ZrT5vFbN0cWgY3HpEeM4sJoUlRt98BnCmAxQ"

    result = invert_string(string_to_invert)

    assert result == "QxAmCnB89tRlUoJs4MeEpH3YgWc0NbFv5TrZ81qXmL29Kd7A"