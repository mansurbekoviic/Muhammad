class BankAccount:
    def __init__(self, account_number, balans):
        self.account_number = account_number
        self.balans = balans

    def deposit(self, amount):
        self.balans += amount

    def withdraw(self, amount):
        if self.balans >= amount:
            self.balans -= amount
        else:
            print("Balans yetarli emas")

    def balans(self):
        return self.balans

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balans, interest_rate):
        super().__init__(account_number, balans)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balans * self.interest_rate
        self.deposit(interest)

savings_account = SavingsAccount("1000000", 1000, 0.5)

savings_account.deposit(500)
savings_account.withdraw(200)

balans = SavingsAccount.get_balans(300)
print(f"Current balance: {balans}")
