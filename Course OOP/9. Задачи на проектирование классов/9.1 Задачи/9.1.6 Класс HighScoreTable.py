class HighScoreTable:
    def __init__(self, max_players: int):
        self._max_players_ = max_players
        self.scores = []

    def update(self, score: int | float):
        if not len(self.scores):
            self.scores.append(score)
        elif score > min(self.scores) or len(self.scores) < self._max_players_:
            self.scores.append(score)

        self.scores.sort(reverse=True)
        if len(self.scores) > self._max_players_:
            self.scores.pop()

    def reset(self):
        self.scores = []


# хоооорош решение:
#
# class HighScoreTable:
#     def __init__(self, limit):
#         self._limit = limit
#         self.scores = []
#
#     def update(self, n):
#         self.scores.append(n)
#         self.scores = sorted(self.scores, reverse=True)[:self._limit]
#
#     def reset(self):
#         self.scores = []
