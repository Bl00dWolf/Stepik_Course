class BankAccount:
    def __init__(self, balance: int | float = 0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: int | float):
        self._balance += amount

    def withdraw(self, amount: int | float):
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError('На счете недостаточно средств')

    def transfer(self, account, amount: int | float):
        self.withdraw(amount)
        account.deposit(amount)
