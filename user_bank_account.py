class BankAccount:
    
    def __init__(self, intRate, balance, accountName):
        self.intRate = intRate
        self.balance = balance
        self.accountName = accountName
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f'The users interest rate is {self.intRate}% and balance is {self.balance}')

    def yield_interest_rate(self):
        if self.balance > 0:
            self.balance = (self.balance * self.intRate) + self.balance
            self.display_account_info()
        else:
            print('We are sorry, your account is negative')

class User:

    all_users = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.listAccounts = []
        self.account = BankAccount(intRate=.05,balance=0,accountName='')

    # Add accountName?
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    # How can I make a deposit into the correct account using the accountName?
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def new_account(self,accountName):
        self.acount = BankAccount(intRate=.05,balance=0,accountName='')
        self.account.accountName = accountName
        self.listAccounts.append(self.account)
        return self

    def display_account_balance(self):
        print(f'User: {self.name}, Account Name: "{self.account.accountName}", Balance: {self.account.balance}')
    
    def print_accounts(self):
        print(f'{self.name} has the following accounts:')
        for i in self.listAccounts:
            print(i.accountName)

    @classmethod
    def every_user(cls):
        for i in cls.all_users:
            print(f'User: {cls.all_users}')

# Creating a user profile
paige = User('Paige', 'milosevicpaige@gmail.com')

# Opening a new account called 'Checking'
paige.new_account('Checking')
paige.print_accounts()

# Make deposit into account
paige.make_deposit(500).make_withdrawl(50).display_account_balance()

# How do I create an instance of a bank account and store it in a list of accounts associated with the user?
# Why is my newAccount not storing in the listAccounts list? Why is it now showing when I print it?