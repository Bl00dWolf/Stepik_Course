import json


def is_correct_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except:
        return False
