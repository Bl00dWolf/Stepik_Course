from copy import deepcopy


class Selfie:
    def __init__(self):
        self.__states = []

    def n_states(self):
        return len(self.__states)

    def save_state(self):
        self.__states.append(deepcopy(self))

    def recover_state(self, index: int):
        try:
            return self.__states[index]
        except IndexError:
            return self

# еще вариант:
# import pickle
# from itertools import count
#
#
# class Selfie:
#     def __init__(self):
#         self._states = {}
#         self._state = count()
# 
#     def save_state(self):
#         self._states[next(self._state)] = pickle.dumps(self)
#
#     def recover_state(self, n):
#         obj = self._states.get(n)
#         return pickle.loads(obj) if obj else self
#
#     def n_states(self):
#         return len(self._states)
