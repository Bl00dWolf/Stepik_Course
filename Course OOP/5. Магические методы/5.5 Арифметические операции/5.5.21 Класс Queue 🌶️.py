class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def __str__(self):
        return f'{" -> ".join(map(str, self.queue))}'

    def add(self, *other):
        self.queue.extend(other)

    def pop(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            return None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if len(self.queue) == len(other.queue) and self.queue == other.queue:
                return True
            return False
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            new_queue = self.queue
            new_queue.extend(other.queue)
            return self.__class__(*new_queue)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.queue.extend(other.queue)
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.queue):
                return self.__class__()
            return self.__class__(*self.queue[other:])
        return NotImplemented
