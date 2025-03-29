class BankAccount:
    balance = 0

    def add_money (self, amount):
        self.balance += amount
        print (f'New balance: {self.balance}')
    
    def subtract_money (self, amount):
        self.balance -= amount
        return self.balance


class SavingsAccount (BankAccount):

    def __init__(self, min_balance):
        self.min_balance = min_balance
    def take_out_money (self, amount):
        try:
            if (self.subtract_money (amount) < self.min_balance):
                raise ValueError()
            else:
                self.subtract_money (amount)
                print (f'New balance: {self.balance}')
        except ValueError as error:
            print (f'If you withdraw money, your balance would fall below the minimum')

account = SavingsAccount(1500)
account.add_money (1000)
account.take_out_money (100)
