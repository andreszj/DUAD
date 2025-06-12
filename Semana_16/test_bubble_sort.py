import random
import pytest
from modules.bubble_sort import bubble_sort

def test_bubble_sort_with_short_list():

    list_to_sort = [4,7,1,8]
    result = bubble_sort(list_to_sort)

    assert result == [1,4,7,8]

def test_bubble_sort_with_long_list():
    in_order = False
    list_to_sort = []

    for i in range (0,100):
        new_number = random.randint(0,1000)
        list_to_sort.append(new_number)
    
    result = bubble_sort(list_to_sort)

    for index in range (len(result)):
        if index > 0:
            current_number = result [index]
            prev_number = result[index-1]
            if prev_number < current_number:
                in_order = True
            else:
                in_order = False

    assert in_order 

def test_bubble_sort_with_empty_list():
    list_to_sort = []
    result = bubble_sort(list_to_sort)

    assert result == []

def test_bubble_sort_with_something_different_than_a_list():
    list_to_sort = "HELLO"
    
    with pytest.raises(TypeError):
        bubble_sort(list_to_sort)
