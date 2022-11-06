from dataclasses import dataclass
from typing import List

from generic.model.cards.card import Card


@dataclass
class Deck():
    cards: List[Card]
