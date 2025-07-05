import pytest
from modules.logic import decode_transactions_to_print, decode_imported_account_activity, decode_list_to_print

def test_decode_transactions_to_print_with_different_type():

    list_to_try = 0

    with pytest.raises (TypeError):
        decode_transactions_to_print(list_to_try)

def test_decode_transactions_to_print_with_short_valid_type():

    list_to_try = [{'Name': 'Andres', 'Account Number': '020891', '#': '1', 'Category': 'Salary', 'Title': 'CEFA', 'Expense': '0', 'Income': '15000.0'}]

    result = decode_transactions_to_print(list_to_try)

    assert result == [['1', 'Salary', 'CEFA', '0', '15000.0']]


def test_decode_transactions_to_print_with_multiple_data():

    list_to_try = [{'Name': 'Andres', 'Account Number': '020891', '#': '1', 'Category': 'Salary', 'Title': 'CEFA', 'Expense': '0', 'Income': '15000.0'}, {'Name': 'Andres', 'Account Number': '020891', '#': '2', 'Category': 'Food', 'Title': 'BK', 'Expense': '15.0', 'Income': '0'}, {'Name': 'Andres', 'Account Number': '020891', '#': '3', 'Category': 'School', 'Title': 'Lyfter', 'Expense': '4000.0', 'Income': '0'}]

    result = decode_transactions_to_print(list_to_try)

    assert result == [['1', 'Salary', 'CEFA', '0', '15000.0'], ['2', 'Food', 'BK', '15.0', '0'], ['3', 'School', 'Lyfter', '4000.0', '0']]  

def test_decode_imported_account_activity_with_last_activity():

    # decode_imported_account_activity(data_imported, file_path)
    file_path = 'last_activity.csv'
    data_imported = [{'Name': 'Andres', 'Account Number': '020891', '#': '1', 'Category': 'Salary', 'Title': 'CEFA', 'Expense': '0', 'Income': '15000.0'}, {'Name': 'Andres', 'Account Number': '020891', '#': '2', 'Category': 'Food', 'Title': 'BK', 'Expense': '15.0', 'Income': '0'}, {'Name': 'Andres', 'Account Number': '020891', '#': '3', 'Category': 'School', 'Title': 'Lyfter', 'Expense': '4000.0', 'Income': '0'}]

    result = decode_imported_account_activity(data_imported, file_path).balance

    assert result == 10985.0

def test_decode_imported_account_activity_with_no_existing_path_file_and_real_data():

    # decode_imported_account_activity(data_imported, file_path)
    file_path = 'hola.csv'
    data_imported = [{'Name': 'Andres', 'Account Number': '020891', '#': '1', 'Category': 'Salary', 'Title': 'CEFA', 'Expense': '0', 'Income': '15000.0'}, {'Name': 'Andres', 'Account Number': '020891', '#': '2', 'Category': 'Food', 'Title': 'BK', 'Expense': '15.0', 'Income': '0'}, {'Name': 'Andres', 'Account Number': '020891', '#': '3', 'Category': 'School', 'Title': 'Lyfter', 'Expense': '4000.0', 'Income': '0'}]

    result = decode_imported_account_activity(data_imported, file_path).balance

    assert result == 0

def test_decode_imported_account_activity_with_real_path_file_and_different_type_data():

    file_path = 'last_activity.csv'
    data_imported = [{'Name': 'Andres', 'Account Number': '020891', '#': '1', 'Category': 'Salary', 'Title': 'CEFA', 'Expense': 'Y', 'Income': 'X'}, {'Name': 'Andres', 'Account Number': '020891', '#': '2', 'Category': 'Food', 'Title': 'BK', 'Expense': '15.0', 'Income': '0'}, {'Name': 'Andres', 'Account Number': '020891', '#': '3', 'Category': 'School', 'Title': 'Lyfter', 'Expense': '4000.0', 'Income': '0'}]

    with pytest.raises(ValueError):
        decode_imported_account_activity(data_imported, file_path).balance

def test_decode_list_to_print_with_different_type():
    list_to_decode = 0

    with pytest.raises (TypeError):
        decode_list_to_print(list_to_decode)

def test_decode_list_to_print_with_long_list():
    list_to_decode = [
    "apple", "river", "cloud", "mountain", "keyboard", "dream", "book", "lamp",
    "guitar", "forest", "mirror", "sky", "train", "robot", "coffee", "pencil",
    "bridge", "wallet", "phone", "dragon", "planet", "music", "cookie", "glass"
    ]
    result_list = [
    ['apple'],
    ['river'],
    ['cloud'],
    ['mountain'],
    ['keyboard'],
    ['dream'],
    ['book'],
    ['lamp'],
    ['guitar'],
    ['forest'],
    ['mirror'],
    ['sky'],
    ['train'],
    ['robot'],
    ['coffee'],
    ['pencil'],
    ['bridge'],
    ['wallet'],
    ['phone'],
    ['dragon'],
    ['planet'],
    ['music'],
    ['cookie'],
    ['glass']
]

    result = decode_list_to_print(list_to_decode)

    assert result == result_list
    