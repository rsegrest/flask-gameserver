import random

from generic.model.cards.card import Card
from generic.model.cards.deck import Deck
from generic.model.cards.rank import Rank
from generic.model.cards.suit import Suit


class StandardDeck():

    def __new__(cls):
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(Card(rank, suit))
        return Deck(cards)

    def __init__(self):
        self.deck = StandardDeck()

    def shuffle(self):
        for i in range(len(self.cards)):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def draw(self):
        return self.cards.pop()

    def __str__(self):
        return self.deck.__str__()

if __name__ == "__main__":
    card = Card()
    pass