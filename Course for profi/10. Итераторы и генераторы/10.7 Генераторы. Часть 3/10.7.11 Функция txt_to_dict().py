def txt_to_dict():
    with open('planets.txt', encoding='UTF-8') as fl:
        line = '1'
        planet = {}
        while True:
            try:
                line = next(fl).strip()
            except StopIteration:
                yield planet
                return

            if not line:
                yield planet
                planet = {}
            else:
                planet[line.split(' = ')[0]] = line.split(' = ')[1]



# planets = txt_to_dict()
# print(*planets)
