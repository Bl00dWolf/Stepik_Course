import re
from string import ascii_letters as aslet


class StrExtension:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

    @staticmethod
    def remove_vowels(string: str):
        for vowel in StrExtension.vowels:
            string = string.replace(vowel, '')
        return string

    @staticmethod
    def leave_alpha(string: str):
        for i in string:
            if i not in aslet:
                string = string.replace(i, '')
        return string

    @staticmethod
    def replace_all(string: str, chars: str, char: str):
        for ch in chars:
            string = re.sub(fr'{ch}', fr'{char}', string)
        return string


# еще вариант
# import re
#
#
# class StrExtension:
#     __VOWELS = re.compile(r'[aeiouy]', flags=re.I)
#     __ALPHABET = re.compile(r'[^a-zA-Z]')
#
#     @staticmethod
#     def remove_vowels(string):
#         return StrExtension.__VOWELS.sub('', string)
#
#     @staticmethod
#     def leave_alpha(string):
#         return StrExtension.__ALPHABET.sub('', string)
#
#     @staticmethod
#     def replace_all(string, chars, char):
#         return re.sub(fr'[{chars}]', char, string)