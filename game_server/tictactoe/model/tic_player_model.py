from tictactoe.constants.spacestates import EMPTY, X, O
from tictactoe.constants.gamestates import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW

class TicTacToePlayerModel(object):

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
    
    def set_id(self, x_id):
        self.x_id = x_id

    def __str__(self):
        return self.name + " " + self.id + " " + self.side
    # @classmethod
    # def getAll(self):
    #     pass
    
if __name__ == "__main__":
    player = TicTacToePlayerModel()
    player.print_player()
    pass