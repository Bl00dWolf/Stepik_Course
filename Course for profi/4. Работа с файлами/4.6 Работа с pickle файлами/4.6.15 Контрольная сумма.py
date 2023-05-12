import pickle

filename, checksum = input(), int(input())

with open(filename, 'rb') as file:
    data = pickle.load(file)

cur_check = 0
if isinstance(data, list) and len(list(filter(lambda x: isinstance(x, int), data))) != 0:
    cur_check = max(filter(lambda x: isinstance(x, int), data)) * min(filter(lambda x: isinstance(x, int), data))
elif isinstance(data, dict):
    cur_check = sum(filter(lambda x: isinstance(x, int), data.keys()))

# print('Контрольные суммы совпадают') if cur_check == checksum else print('Контрольные суммы не совпадают')
print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][checksum == cur_check])
