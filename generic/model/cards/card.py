class Card():

    def __init__(self, rank, suit, is_face_up=False):
        self.rank = rank
        self.suit = suit
        self.is_face_up = is_face_up
        
    def flip(self):
        self.is_face_up = True

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)

if __name__ == "__main__":
    card = Card()
    pass