from collections import Counter


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street: str, house: str, flat: str):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street: str):
        if self.delivery_data:
            return list(Counter([dev_data[1] for dev_data in self.delivery_data if dev_data[0] == street]).keys())
        return []

    def get_flats_for_house(self, street: str, house: str):
        if self.delivery_data:
            return list(Counter([dev_data[2] for dev_data in self.delivery_data if
                                 dev_data[0] == street and dev_data[1] == house]).keys())
        return []
