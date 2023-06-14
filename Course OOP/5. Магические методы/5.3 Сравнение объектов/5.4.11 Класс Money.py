class Money:
    def __init__(self, money: int | float):
        self.money = money

    def __str__(self):
        return f'{self.money} руб.'

    def __pos__(self):
        money = self.money
        if self.money < 0:
            money = abs(self.money)
        return self.__class__(money)

    def __neg__(self):
        money = self.money
        if self.money > 0:
            money = -self.money
        return self.__class__(money)


money = Money(-100)

print(money)
print(+money)
print(-money)
