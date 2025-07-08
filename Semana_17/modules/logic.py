import os

class DataList: 

    def __init__(self):
        self.data_list = []

    def add_new_data(self, new_data): 

        item_exist = False
        for item in self.data_list:
            if item == new_data:
                item_exist = True
        if not item_exist:
            self.data_list.append(new_data)

        # print (self.data_list)
        
    def sort_data_list (self): 

        for outer_index in range (0, len(self.data_list)-1):
            changes_done = False
            for index in range (0, len (self.data_list)-1-outer_index):
                current_data = self.data_list [index]
                next_data = self.data_list [index+1]
                if current_data > next_data:
                    self.data_list[index] = next_data
                    self.data_list[index+1] = current_data
                    changes_done = True
            if not changes_done:
                break

        # print (self.data_list)

class Account:

    def __init__(self,customer, number_of_process, initial_amount):
        self.customer = customer
        self.number_of_processes = number_of_process
        self.balance = initial_amount
        self.transaction = []
        self.count = 0
        self.expense = 0
        self.income = 0
        self.last_transaction = {}
        
    def reset(self,customer,number_of_process, initial_amount):
        self.__init__(customer,number_of_process, initial_amount) 

    def add_income(self,new_income,category,title):

        current_movement = {
            'Name' : self.customer,
            'Account Number' : self.number_of_processes,
        }
        self.income += new_income
        self.count = self.count + 1
        self.balance += new_income
        
        current_movement ['#'] = self.count
        current_movement ['Category'] = category
        current_movement ['Title'] = title
        current_movement ['Expense'] = 0.0
        current_movement ['Income'] = new_income

        self.last_transaction = current_movement
        self.transaction.append(current_movement)
        
        print (self.transaction)
        print (self.balance)
        print (f'INCOMES: {self.income}')

    def add_expense(self,new_expense,category,title):
        current_movement = {
            'Name' : self.customer,
            'Account Number' : self.number_of_processes,
        }
        self.expense += new_expense
        self.count = self.count + 1
        self.balance -= new_expense

        current_movement ['#'] = self.count
        current_movement ['Category'] = category
        current_movement ['Title'] = title
        current_movement ['Expense'] = new_expense
        current_movement ['Income'] = 0.0

        self.last_transaction = current_movement
        self.transaction.append(current_movement)
        
        print (self.transaction)
        print (self.balance)
        print (f'EXPENSES: {self.expense}')


# Data decoding, file handling, and GUI updating functions:

def decode_imported_account_activity(data_imported, file_path):
    
    balance = 0

    if os.path.exists(file_path):
        for index in range (0, len(data_imported)):
            name = data_imported[index]['Name']
            account_number = data_imported[index]['Account Number']        
            balance = balance + float(data_imported[index]['Income']) - float(data_imported[index]['Expense'])

        account = Account(name,account_number,balance)
        account.reset(name,account_number,balance)
        account.transaction = data_imported

        account.count = int(data_imported[index]['#'])

    else:
        account = Account('','',0)
    
    return account


def decode_transactions_to_print(transactions):
    
    list_to_print = []
    aux_list = []
    for index in range (0, len (transactions)):
        for key, value in transactions[index].items():
            if key != 'Name' and key != 'Account Number':
                aux_list.append (value)
        list_to_print.append(aux_list)
        aux_list = []
    
    return list_to_print


def decode_list_to_print(list_to_decode):
    
    aux_list = []
    list_to_print =[]

    for item in list_to_decode:
        aux_list.append(item)
        list_to_print.append (aux_list)
        aux_list = []
    
    return list_to_print 


def update_main_window(window,account,list_to_print):

    window['-NAME-'].update(account.customer) 
    window['-ACCOUNT NUMBER-'].update("Account number: "+account.number_of_processes) 
    window['-MAIN TABLE-'].update(list_to_print) 
    window['-BALANCE-'].update([account.balance]) 