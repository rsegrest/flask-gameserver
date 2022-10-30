from constants.spacestates import EMPTY, B, R
from constants.gamestates import NOT_STARTED, B_TURN, R_TURN, B_WON, R_WON, DRAW
# import json

class C4PlayerModel(object):

    def __init__(
        self,
        player_name = None,
        player_id = None,
        side = None
    ):
        self.name = player_name
        self.id = player_id
        self.side = side

    def name(self):
        return ("%s %s %s" % (self.name, self.id, self.side))
    
    def get_name(self):
        return self.name
    
    def get_side(self):
        return self.side
    
    def get_id(self):
        return self.id


    def set_name(self, name):
        self.name = name
    
    def set_id(self, id):
        self.id = id

    def __str__(self):
        return self.name + " " + self.id + " " + self.side
    # @classmethod
    # def getAll(self):
    #     pass
    
if __name__ == "__main__":
    board = C4PlayerModel()
    board.print_player()
    pass