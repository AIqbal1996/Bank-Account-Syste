class BankAccount:

    # Class variables
    bank_name = "ABC Bank"
    total_accounts = 0

    # Constructor
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

        BankAccount.total_accounts += 1

    # Deposit
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    # Withdraw
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)

    # Check balance
    def check_balance(self):
        print("Current balance:", self.balance)

    # Display account details
    def display_account_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Bank Name:", BankAccount.bank_name)

    # Change bank name for all accounts
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name