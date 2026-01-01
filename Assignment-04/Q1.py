# Concept: Classes & Objects
# Q1. Create a BankAccount class with attributes account_number, owner_name,
# and balance.
# Add methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have sufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def check_balance(self):
        return self.balance


AC1 = BankAccount(7365, "Shivam", 500)

print("1. Deposit\n2. Withdraw\n3. Check balance")
option = int(input("Select one option: "))

if option == 1:
    amt = int(input("Enter amount to deposit: "))
    print("Balance:", AC1.deposit(amt))
elif option == 2:
    amt = int(input("Enter amount to withdraw: "))
    AC1.withdraw(amt)
elif option == 3:
    print("Balance:", AC1.check_balance())
else:
    print("Invalid option")