def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    from datetime import datetime

    new_booked_dates = []
    for ddate in booked_dates:
        if '-' in ddate:
            for d in range(datetime.strptime(ddate[:10], '%d.%m.%Y').toordinal(),
                           datetime.strptime(ddate[11:], '%d.%m.%Y').toordinal() + 1):
                new_booked_dates.append(datetime.fromordinal(d).date())
        else:
            new_booked_dates.append(datetime.strptime(ddate, '%d.%m.%Y').date())

    new_dates_for_booking = []
    if '-' not in date_for_booking:
        new_dates_for_booking.append(datetime.strptime(date_for_booking, '%d.%m.%Y').date())
    else:
        for d in range(datetime.strptime(date_for_booking[:10], '%d.%m.%Y').toordinal(),
                       datetime.strptime(date_for_booking[11:], '%d.%m.%Y').toordinal() + 1):
            new_dates_for_booking.append(datetime.fromordinal(d).date())

    # print(new_booked_dates)
    # print(new_dates_for_booking)

    if len(set(new_dates_for_booking) & set(new_booked_dates)) > 0:
        return False
    else:
        return True


# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021-04.11.2021'
# print(is_available_date(dates, some_date))

# Еще решение

# from datetime import date, time, datetime
# def is_available_date(booked_dates, date_for_booking):
#     ord_booked_dates = []
#     for d in booked_dates:
#         dates = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in d.split('-')]
#         ord_booked_dates.extend(range(dates[0], dates[-1] + 1))
#     dt = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in date_for_booking.split('-')]
#     date_f_b = range(dt[0], dt[-1] + 1)
#     return(all([i not in ord_booked_dates for i in date_f_b]))
