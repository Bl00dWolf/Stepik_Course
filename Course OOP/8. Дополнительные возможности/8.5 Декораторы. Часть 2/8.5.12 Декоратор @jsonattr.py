import json


def jsonattr(filename: str):
    data = None
    with open(filename) as fl:
        data = json.load(fl)

    def decor(cls):
        for atr, value in data.items():
            setattr(cls, atr, value)
        return cls

    return decor
