class SortKey:
    def __init__(self, *args):
        self.params = tuple(args)

    def __call__(self, obj):
        keys = []
        for param in self.params:
            keys.append(obj.__getattribute__(param))
        return keys

#
# еще вариант:
# class SortKey:
#     def __init__(self, *attributes):
#         self.attributes = attributes
#
#     def __call__(self, instance):
#         return [getattr(instance, attribute) for attribute in self.attributes]