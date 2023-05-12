from datetime import date, datetime
def date_formatter(country_code: str):
    def gdate(ddate):
        ctr_format = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d', 'br': '%d/%m/%Y', 'fr': '%d.%m.%Y',
                      'pt': '%d-%m-%Y'}
        return datetime.strftime(ddate, ctr_format[country_code])
    return gdate

# date_ru = date_formatter('ru')
# today = date(2022, 1, 25)
# print(date_ru(today))

# еще вариант
# from datetime import datetime, date
# def date_formatter(country_code):
#     d = {'ru': '%d.%m.%Y',
#          'us': '%m-%d-%Y',
#          'ca': '%Y-%m-%d',
#          'br': '%d/%m/%Y',
#          'fr': '%d.%m.%Y',
#          'pt': '%d-%m-%Y'}
#     return lambda date_obj: date_obj.strftime(d[country_code])