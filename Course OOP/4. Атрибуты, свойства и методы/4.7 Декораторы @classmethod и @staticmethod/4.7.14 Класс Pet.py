class Pet:
    pets = []

    def __init__(self, name: str):
        self.name = name
        Pet.pets.append(self)

    @staticmethod
    def first_pet():
        if Pet.pets:
            return Pet.pets[0]
        return None

    @staticmethod
    def last_pet():
        if Pet.pets:
            return Pet.pets[-1]
        return None

    @staticmethod
    def num_of_pets():
        return len(Pet.pets)