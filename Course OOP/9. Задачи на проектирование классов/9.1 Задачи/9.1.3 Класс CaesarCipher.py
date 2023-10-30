from string import ascii_letters


class CaesarCipher:
    def __init__(self, shift: int):
        self._shift_ = shift

    @staticmethod
    def __roll__(char: str, shift: int) -> str:
        ord_shift = 65 if char.isupper() else 97
        return chr((ord(char) - ord_shift + shift) % 26 + ord_shift)

    def encode(self, string: str) -> str:
        return ''.join(map(lambda x: self.__roll__(x, self._shift_) if x in ascii_letters else x, string))

    def decode(self, string: str) -> str:
        return ''.join(map(lambda x: self.__roll__(x, -self._shift_) if x in ascii_letters else x, string))


# Еще норм решение
# class CaesarCipher:
#     def __init__(self, shift):
#         self.shift = shift
#
#     def encode(self, text):
#         return ''.join(self.roll(char, self.shift) if char.isascii() and char.isalpha() else char for char in text)
#
#     def decode(self, text):
#         return ''.join(self.roll(char, -self.shift) if char.isascii() and char.isalpha() else char for char in text)
#
#     @staticmethod
#     def roll(char: str, shift: int) -> str:
#         ord_shift = 65 if char.isupper() else 97
#         return chr((ord(char) - ord_shift + shift) % 26 + ord_shift)