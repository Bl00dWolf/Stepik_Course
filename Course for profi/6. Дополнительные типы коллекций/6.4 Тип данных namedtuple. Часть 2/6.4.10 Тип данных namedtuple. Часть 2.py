from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open('data.pkl', 'rb') as file:
    animals = pickle.load(file)

for animal in animals:
    for field, value in zip(Animal._fields, animal):
        print(field, ': ', value, sep='')
    print()