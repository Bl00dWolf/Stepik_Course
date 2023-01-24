from zipfile import ZipFile, ZipInfo
from datetime import datetime

with ZipFile('workbook.zip') as zippy:
    files = []
    for file in zippy.infolist():
        y, m, d, H, M, S = file.date_time
        if not file.is_dir() and datetime(year=y, month=m, day=d, hour=H, minute=M, second=S) > datetime(year=2021,
                                                                                                         month=11,
                                                                                                         day=30,
                                                                                                         hour=14,
                                                                                                         minute=22,
                                                                                                         second=00):
            files.append(file.filename.rsplit('/', maxsplit=1)[-1])
print(*sorted(files), sep='\n')
