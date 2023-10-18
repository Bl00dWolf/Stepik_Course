from enum import Flag, auto


class MovieGenres(Flag):
    ACTION, COMEDY, DRAMA, FANTASY, HORROR = (auto() for _ in range(5))


class Movie:
    def __init__(self, name: str, genres: MovieGenres):
        self.name = name
        self.genres = genres

    def __repr__(self):
        return f'{self.name}'

    def in_genre(self, genre: MovieGenres) -> bool:
        return genre in self.genres

