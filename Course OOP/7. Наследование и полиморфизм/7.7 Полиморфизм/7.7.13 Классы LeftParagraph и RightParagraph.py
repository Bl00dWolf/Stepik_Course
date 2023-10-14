class LeftParagraph:
    def __init__(self, length: int):
        self._max_length_ = length
        self._data_ = ['']

    def add(self, words: str) -> None:
        words = words.split()
        for i in range(len(words)):
            if len(self._data_[-1] + ' ' + words[i]) > self._max_length_:
                self._data_.append('')
            self._data_[-1] += words[i] + ' '

    def end(self) -> None:
        self._data_ = list(map(str.strip, self._data_))
        print('\n'.join(self._data_))
        self._data_ = ['']


class RightParagraph:
    def __init__(self, length: int):
        self._max_length_ = length
        self._data_ = ['']
        self._cur_max_len_ = 0

    def add(self, words: str) -> None:
        words = words.split()
        for i in range(len(words)):
            if len(self._data_[-1] + words[i]) > self._max_length_:
                self._data_.append('')
            self._data_[-1] += words[i] + ' '

    def end(self) -> None:
        self._data_ = list(map(str.strip, self._data_))

        for i in range(len(self._data_)):
            self._data_[i] = f'{self._data_[i]:>{self._max_length_}}' + ' '

        print('\n'.join(self._data_))
        self._data_ = ['']

# мой вариант полная фигня, замучился с этими проблемами, переписывать с общим классом не хочу уже =) Извините.
# Сам виноват конечно
#
# вот норм вариант
# from abc import ABC, abstractmethod
#
#
# class Paragraph(ABC):
#     def __init__(self, length):
#         self._size = length
#         self._paragraph = ['']
#
#     def add(self, words):
#         words = words.split()
#         for word in words:
#             if len(self._paragraph[-1] + f' {word}') > self._size:
#                 self._paragraph.append('')
#             self._paragraph[-1] = (self._paragraph[-1] + f' {word}').lstrip()
#
#     @abstractmethod
#     def end(self):
#         pass
#
#
# class LeftParagraph(Paragraph):
#     def end(self):
#         for line in self._paragraph:
#             print(line)
#         self._paragraph = ['']
#
#
# class RightParagraph(Paragraph):
#     def end(self):
#         for line in self._paragraph:
#             print(line.rjust(self._size))
#         self._paragraph = ['']
