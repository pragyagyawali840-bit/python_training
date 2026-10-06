class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print("Error: Insufficint funds!")
        else:
            self.balance -= amount
            print(f"Your current fund is {self.balance}")
    def check_balace(self):
        return self.balance

acc= BankAccount()
acc.deposit(100); acc.withdraw(30)