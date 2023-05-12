def get_min_max(data: list) -> tuple:
    if data:
        return min(enumerate(data), key=lambda x: x[1])[0], max(enumerate(data), key=lambda x: x[1])[0]
