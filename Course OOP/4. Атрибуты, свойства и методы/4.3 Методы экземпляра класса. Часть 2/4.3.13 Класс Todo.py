class Todo:
    def __init__(self):
        self.things = []

    def add(self, task: str, priority: int):
        self.things.append((task, priority))

    def get_by_priority(self, n: int):
        if self.things:
            return [task[0] for task in self.things if task[1] == n]
        return []

    def get_low_priority(self):
        if self.things:
            low_pr = min(self.things, key=lambda x: x[1])[1]
            return [task[0] for task in self.things if task[1] == low_pr]
        return []

    def get_high_priority(self):
        if self.things:
            high_pr = max(self.things, key=lambda x: x[1])[1]
            return [task[0] for task in self.things if task[1] == high_pr]
        return []
