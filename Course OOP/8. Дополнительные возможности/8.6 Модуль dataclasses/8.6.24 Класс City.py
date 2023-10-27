import dataclasses


@dataclasses.dataclass
class City:
    name: str
    population: int
    founded: int
