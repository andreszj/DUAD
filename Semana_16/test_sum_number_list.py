import pytest
from modules.sum_number_list import sum_number_list

def test_sum_number_list_with_large_numbers():
    list_of_numbers = [123134,245346,34678,8569696]

    result = sum_number_list (list_of_numbers)

    assert result == list_of_numbers[0] + list_of_numbers[1] + list_of_numbers[2]  + list_of_numbers[3]

def test_sum_number_list_with_decimal():
    list_of_numbers = [123.00,23.15,25.5,24.0]

    result = sum_number_list (list_of_numbers)

    assert result == list_of_numbers[0] + list_of_numbers[1] + list_of_numbers[2]  + list_of_numbers[3]

def test_sum_number_list_with_strings_in_the_list():
    list_of_numbers = [5,7,8,'a']

    with pytest.raises(TypeError):
        sum_number_list(list_of_numbers)