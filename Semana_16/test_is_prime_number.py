import pytest
from modules.is_prime_number import is_prime_number

def test_is_prime_number_with_only_prime_numbers ():
    list_of_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

    result = is_prime_number(list_of_numbers)

    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def test_is_prime_number_with_long_list():
    list_of_numbers = [83, 27, 56, 91, 12, 45, 68, 33, 77, 24, 58, 39, 62, 73, 11, 94, 88, 66, 17, 35, 49, 28, 64, 19, 86, 22, 31, 79, 53, 47]
    
    result = is_prime_number(list_of_numbers)

    assert result == [83, 73, 11, 17, 19, 31, 79, 53, 47]

def test_is_prime_number_with_strings_on_list():
    list_of_numbers = [1, 5, 'a', 9]

    with pytest.raises (TypeError):
        is_prime_number(list_of_numbers)