def fill_up_missing_dates(dates):
    from datetime import datetime, timedelta
    formatt = '%d.%m.%Y'
    dates = [datetime.strptime(d, formatt).date() for d in dates]
    dates = [datetime.fromordinal(d).date().strftime(formatt) for d in
             range(datetime.toordinal(min(dates)), datetime.toordinal(max(dates)) + 1)]
    return dates


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))

# Еще вариант
# def fill_up_missing_dates(dates):
#     pattern = '%d.%m.%Y'
#     dates = [datetime.strptime(d, pattern) for d in dates]
#     start, end = min(dates), max(dates)
#     days = (end - start).days
#     return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]