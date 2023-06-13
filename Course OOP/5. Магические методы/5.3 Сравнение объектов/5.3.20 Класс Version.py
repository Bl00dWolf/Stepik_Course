from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version

    def __repr__(self):
        norm_ver = ['0', '0', '0']
        ver = self.version.split('.')
        for i in range(len(ver)):
            norm_ver[i] = ver[i]

        return f'{self.__class__.__name__}({repr(".".join(norm_ver))})'

    def __str__(self):
        norm_ver = ['0', '0', '0']
        ver = self.version.split('.')
        for i in range(len(ver)):
            norm_ver[i] = ver[i]

        return ".".join(norm_ver)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            sver = list(int(x) for x in self.version.split('.'))
            over = list(int(x) for x in other.version.split('.'))

            while len(sver) < 3:
                sver.append(0)

            while len(over) < 3:
                over.append(0)

            return sver == over
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            sver = list(int(x) for x in self.version.split('.'))
            over = list(int(x) for x in other.version.split('.'))

            while len(sver) < 3:
                sver.append(0)

            while len(over) < 3:
                over.append(0)

            return sver < over
        return NotImplemented

# еще вариант
#
# from functools import total_ordering
#
#
# @total_ordering
# class Version:
#     def __init__(self, version):
#         self._parts = [int(i) for i in version.split('.')]
#         self._parts += [0] * (3 - len(self._parts))
#
#     def __str__(self):
#         return '{}.{}.{}'.format(*self._parts)
#
#     def __repr__(self):
#         return "Version('{}.{}.{}')".format(*self._parts)
#
#     def __eq__(self, other):
#         if isinstance(other, Version):
#             return self._parts == other._parts
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Version):
#             return self._parts < other._parts
#         return NotImplemented

