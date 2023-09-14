from datetime import date


class WeatherWarning:
    @staticmethod
    def rain():
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow():
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature():
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date: date):
        print(date.strftime('%d.%m.%Y'))
        super().snow()

    def snow(self, date: date):
        print(date.strftime('%d.%m.%Y'))
        super().rain()

    def low_temperature(self, date: date):
        print(date.strftime('%d.%m.%Y'))
        super().low_temperature()
