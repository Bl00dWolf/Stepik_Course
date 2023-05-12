from functools import wraps
import json


def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapper
