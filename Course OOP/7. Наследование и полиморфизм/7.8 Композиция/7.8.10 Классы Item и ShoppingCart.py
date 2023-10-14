class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items: list[Item] | tuple[Item] = None):
        if items is None:
            items = []
        self.items = list(items)

    def __repr__(self):
        return '\n'.join(repr(i) for i in self.items)

    def add(self, item: Item) -> None:
        self.items.append(item)

    def total(self) -> int:
        return sum([item.price for item in self.items])

    def remove(self, item_name: str) -> None:
        # self.items = list(filter(lambda x: x.name != item_name, self.items))
        self.items = [item for item in self.items if item.name != item_name]
