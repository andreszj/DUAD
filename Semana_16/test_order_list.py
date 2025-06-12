import pytest
from modules.order_list import generate_new_list

def test_generate_new_list_with_some_numbers_in_list():
    text_to_order = "python-house-1-car-dog-56788-children-book"

    result = generate_new_list(text_to_order)
    
    assert result == ['1', '56788', 'book', 'car', 'children', 'dog', 'house', 'python']

def test_generate_new_list_with_long_list():
    text_to_order = "apple-chair-blue-run-sky-mountain-drive-happy-mirror-light-green-fast-book-sound-pizza-dream-fire-clock-jump-desk"

    result = generate_new_list(text_to_order)
    
    assert result == [
    'apple', 'blue', 'book', 'chair', 'clock',
    'desk', 'dream', 'drive', 'fast', 'fire',
    'green', 'happy', 'jump', 'light', 'mirror',
    'mountain', 'pizza', 'run', 'sky', 'sound'
]

def test_generate_new_list_with_different_type():
    text_to_order = 1235

    with pytest.raises(TypeError):
        generate_new_list(text_to_order)