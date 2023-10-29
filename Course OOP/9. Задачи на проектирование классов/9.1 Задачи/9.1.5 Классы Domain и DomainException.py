import re


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, domain: str):
        if not re.fullmatch(r'^\w+\.\w{2,}$', domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    def __repr__(self):
        return f'{self.domain}'

    @classmethod
    def from_url(cls, url: str):
        match = re.match(r'^https?://(\w+\.\w{2,})$', url)
        if not match:
            raise DomainException('Недопустимый домен, url или email')
        return cls(match.group(1))

    @classmethod
    def from_email(cls, email: str):
        match = re.match(r'^[a-zA-Z]+@(\w+\.\w{2,})$', email)
        if not match:
            raise DomainException('Недопустимый домен, url или email')
        return cls(match.group(1))


emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org', 'abc@@mail.ru',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru', 'abc@.ru']

# еще вариант:
# import re
#
#
# class DomainException(Exception):
#     pass
#
#
# class Domain:
#     __CORRECT_DOMAIN = r'\w+\.\w+'
#     __CORRECT_URL = fr'^https?://(?P<domain>{__CORRECT_DOMAIN})$'
#     __CORRECT_EMAIL = fr'\w+@(?P<domain>{__CORRECT_DOMAIN})'
#
#     def __init__(self, domain):
#         if not re.fullmatch(self.__CORRECT_DOMAIN, domain):
#             raise DomainException('Недопустимый домен, url или email')
#         self.domain = domain
#
#     def __str__(self):
#         return self.domain
#
#     @classmethod
#     def from_url(cls, url):
#         url = re.match(cls.__CORRECT_URL, url)
#         if not url:
#             raise DomainException('Недопустимый домен, url или email')
#         return cls(url.group('domain'))
#
#     @classmethod
#     def from_email(cls, email):
#         email = re.match(cls.__CORRECT_EMAIL, email)
#         if not email:
#             raise DomainException('Недопустимый домен, url или email')
#         return cls(email.group('domain'))