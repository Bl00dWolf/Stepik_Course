import abc


class ChessPiece:
    hor_pos = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    def __init__(self, horizontal: str, vertical: int):
        self.horizontal = horizontal
        self.vertical = vertical

    @abc.abstractmethod
    def can_move(self):
        pass


class King(ChessPiece):
    def can_move(self, horizontal: str, vertical: int):
        if self.horizontal == horizontal and self.vertical == vertical:
            return False
        if abs(super().hor_pos[self.horizontal] - super().hor_pos[horizontal]) <= 1 and abs(
                self.vertical - vertical) <= 1:
            return True
        return False


class Knight(ChessPiece):
    def can_move(self, horizontal: str, vertical: int):
        if self.horizontal == horizontal and self.vertical == vertical:
            return False
        if (super().hor_pos[self.horizontal] - super().hor_pos[horizontal]) ** 2 + (self.vertical - vertical) ** 2 == 5:
            return True
        return False


# еще вариант:
# from abc import ABC, abstractmethod
#
#
# class ChessPiece(ABC):
#     def __init__(self, horizontal, vertical):
#         self.horizontal = horizontal
#         self.vertical = vertical
#
#     @abstractmethod
#     def can_move(self, horizontal, vertical):
#         pass
#
#
# class King(ChessPiece):
#     def can_move(self, horizontal, vertical):
#         can = abs(ord(horizontal) - ord(self.horizontal)) + abs(vertical - self.vertical)
#         return all(
#             (
#                 abs(ord(horizontal) - ord(self.horizontal)) <= 1,
#                 abs(vertical - self.vertical) <= 1,
#                 can in (1, 2)
#             )
#         )
#
#
# class Knight(ChessPiece):
#     def can_move(self, horizontal, vertical):
#         return (ord(self.horizontal) - ord(horizontal)) ** 2 + (self.vertical - vertical) ** 2 == 5

