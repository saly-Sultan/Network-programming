class BankAccount:

    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}. New balance: ${:.2f}".format(amount, self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Current balance: ${:.2f}".format(self.balance))
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}. New balance: ${:.2f}".format(amount, self.balance))

    def get_balance(self):
        return self.balance

    def __str__(self):
        return "Account Holder: {}nAccount Number: {}nBalance: ${:.2f}".format(
            self.account_holder, self.account_number, self.balance
        )


class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print("Applied interest: ${:.2f}. New balance: ${:.2f}".format(interest, self.balance))

    def __str__(self):
        return "{}, Interest Rate: {:.2%}".format(
            super().__str__(), self.interest_rate
        )


my_account = BankAccount("7833438", "Saly_1")
my_account.deposit(1000.00)
my_account.withdraw(500.00)
print("Current balance: ${:.2f}".format(my_account.get_balance()))

savings_account = SavingsAccount("4520314", "Saly_2", 0.05)
savings_account.apply_interest()
print(savings_account)
