def add_attr_to_class(**attrs):
    def decor(cls):
        for atr, value in attrs.items():
            setattr(cls, atr, value)
        return cls

    return decor


@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass


print(MyClass.first_attr)
print(MyClass.second_attr)
