from Account import Account
class Savings (Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        self.withdrawal_limit = 100

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print("Withdrawal amount cannot be more than $100")
        else:
                super().withdraw(amount)


    def apply_interest(self):
                    interest = self.get_balance() * self.interest_rate
                    self.deposit(interest)
                    print(f"Interest of {interest} applied. New balance: {self.get_balance()}")

                    print("----Savings Account----")

                   
                   
if __name__ == "__main__":
    savings = Savings("Aaron", 1000)
    print(f"Intitial balance: {savings.get_balance()}")

    savings.deposit(500)
    savings.withdraw(50)
    savings.withdraw(200)
    savings.apply_interest()