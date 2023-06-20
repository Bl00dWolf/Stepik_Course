class Temperature:
    def __init__(self, temperature: int | float):
        self.temperature = temperature

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def to_fahrenheit(self):
        return 9 / 5 * self.temperature + 32

    @classmethod
    def from_fahrenheit(cls, temperature: int | float):
        temperature = 5 / 9 * (temperature - 32)
        return cls(temperature)

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)
