class PhoneNumber:
    def __init__(self, phone_number: str):
        if ' ' in phone_number:
            phone_number = phone_number.replace(' ', '')
        self.phone_number = phone_number

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"

    def __str__(self):
        return f'({self.phone_number[0:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'
