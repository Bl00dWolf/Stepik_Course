import re

for coord in open(0):
    coord = re.match(r'\((-?\d+\.?\d*),\s*(-?\d+\.?\d*)\)', coord)
    x, y = float(coord.group(1)), float(coord.group(2))
    print('True' if -90 <= float(x) <= 90 and -180 <= float(y) <= 180 else 'False')