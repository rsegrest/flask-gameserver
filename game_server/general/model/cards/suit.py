from dataclasses import dataclass


@dataclass
class Suit:
    name: str
    abbreviation: str
    icon: str
    priority: int

# p = Point(1.5, 2.5)

# print(p)  # Point(x=1.5, y=2.5, z=0.0)