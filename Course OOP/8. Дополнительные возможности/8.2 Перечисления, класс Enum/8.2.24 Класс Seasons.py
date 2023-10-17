from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, country: str) -> str:
        ru = ('зима', 'весна', 'лето', 'осень')
        en = tuple(day.name.lower() for day in Seasons)

        if country.lower() == 'ru':
            return dict(zip(self.__class__, ru))[self]
        elif country.lower() == 'en':
            return dict(zip(self.__class__, en))[self]
