class BankAccount:

    # balance = 0

    def __init__ (self):
        self.balance = 0

    def add_money (self, amount):
        self.balance += amount
        print (f'Balance: {self.balance}')
    
    def subtract_money (self, amount):
        self.balance -= amount


class SavingsAccount (BankAccount):

    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance
    def take_out_money (self, amount):
        try:
            if (self.balance  - amount < self.min_balance):
                raise ValueError()
            else:
                self.subtract_money (amount)
                print (f'Balance: {self.balance}')
        except ValueError:
            print (f'If you withdraw money, your balance would fall below the minimum')
            print (f'Balance: {self.balance}')

account = SavingsAccount(1500)
account.add_money (2000)
account.take_out_money (100)
