import re


class CaseHelper:
    @staticmethod
    def is_snake(string: str):
        return True if re.fullmatch(r'([a-z]+_*[a-z]+)+', string) else False

    @staticmethod
    def is_upper_camel(string: str):
        return True if re.fullmatch(r'([A-Z][a-z]+)+', string) else False

    @staticmethod
    def to_snake(string: str):
        string = re.sub(r'\B([A-Z])', r'\1_', string)
        return string.lower()

    @staticmethod
    def to_upper_camel(string: str):
        # string = re.sub(r'([a-z]_|\b[a-z])', fr'\1'.upper(), string)
        # return string
        # re.findall(r'([a-z]_|\b[a-z])', string)
        try:
            for i in range(len(string)):
                if i == 0:
                    string = string[0].upper() + string[1:]
                elif string[i] == '_':
                    string = string[:i] + string[i + 1].upper() + string[i + 2:]
        except IndexError:
            pass
        return string


# print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
