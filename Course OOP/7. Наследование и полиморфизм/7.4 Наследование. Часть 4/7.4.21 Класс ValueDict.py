class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k

    def keys_of(self, value):
        flt = filter(lambda item: item[1] == value, self.items())
        return (it[0] for it in flt)

# решение лучше =)
# class ValueDict(dict):
#     def key_of(self, value):
#         for k, v in self.items():
#             if v == value:
#                 return k
#
#     def keys_of(self, value):
#         return (k for k, v in self.items() if v == value)
