from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self) -> tuple[str, int]:
        return self.name, self.value

    def code_class(self) -> str:
        rus_codes = {100: 'информация', 200: 'успех', 305: 'перенаправление', 404: 'ошибка клиента',
                     502: 'ошибка сервера'}

        return rus_codes[self.value]
