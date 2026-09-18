from bank_account import BankAccount


# Create first account
account1 = BankAccount("Arif", "1001", 5000)

print("----- Account 1 -----")
account1.display_account_details()


# Deposit money
print("\n----- Deposit -----")
account1.deposit(2000)
account1.check_balance()


# Withdraw money
print("\n----- Withdraw -----")
account1.withdraw(1000)
account1.check_balance()


# Try to withdraw more money than available
print("\n----- Withdrawal Validation -----")
account1.withdraw(10000)
account1.check_balance()


# Create second account
account2 = BankAccount("Rahul", "1002", 3000)

print("\n----- Account 2 -----")
account2.display_account_details()


# Change bank name
print("\n----- Change Bank Name -----")
BankAccount.change_bank_name("XYZ Bank")


# Check both accounts after changing bank name
print("\n----- Updated Account 1 -----")
account1.display_account_details()

print("\n----- Updated Account 2 -----")
account2.display_account_details()


# Display total number of accounts
print("\n----- Total Accounts -----")
print("Total bank accounts:", BankAccount.total_accounts)