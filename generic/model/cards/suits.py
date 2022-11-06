from generic.model.cards.suit import Suit

spades = Suit(
    name="Spades",
    abbreviation="S",
    icon="♠",
    priority=1
)
hearts = Suit(
    name="Hearts",
    abbreviation="H",
    icon="♥",
    priority=2
)
diamonds = Suit(
    name="Diamonds",
    abbreviation="D",
    icon="♦",
    priority=3
)
clubs = Suit(
    name="Clubs",
    abbreviation="C",
    icon="♣",
    priority=4
)
Suits = [spades, hearts, diamonds, clubs]