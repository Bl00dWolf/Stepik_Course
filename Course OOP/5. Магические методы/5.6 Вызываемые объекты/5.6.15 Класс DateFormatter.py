from datetime import date


class DateFormatter:
    __data = {
        "ru": r"%d.%m.%Y",
        "us": r"%m-%d-%Y",
        "ca": r"%Y-%m-%d",
        "br": r"%d/%m/%Y",
        "fr": r"%d.%m.%Y",
        "pt": r"%d-%m-%Y"
    }

    def __init__(self, country_code: str):
        self.country_code = country_code

    def __call__(self, d: date):
        return date.strftime(d, self.__class__.__data[self.country_code])
