import json
from zipfile import ZipFile


def is_correct_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except:
        return False


ddata = []
with ZipFile('data.zip') as zippy:
    for file in zippy.infolist():
        if not file.is_dir() and file.filename.endswith('.json'):
            with zippy.open(file.filename) as f_rd:
                data = f_rd.read().decode('UTF-8', errors='ignore')
            if is_correct_json(data):
                ddata.append(json.loads(data))

for di in ddata:
    ddata = list(
        sorted(filter(lambda x: x['team'] == 'Arsenal', ddata), key=lambda x: (x['first_name'], x['last_name'])))

[print(f'{di["first_name"]} {di["last_name"]}') for di in ddata]
