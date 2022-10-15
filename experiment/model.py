from constants.spacestates import SpaceStates
from constants.gamestates import GameStates
# import json

class Model(object):

    def __init__(self, x_player_name = None, o_player_name = None):
        self.x_name = x_player_name
        self.o_name = o_player_name
        self.board = [
            [SpaceStates.EMPTY,SpaceStates.EMPTY,SpaceStates.EMPTY],
            [SpaceStates.EMPTY,SpaceStates.EMPTY,SpaceStates.EMPTY],
            [SpaceStates.EMPTY,SpaceStates.EMPTY,SpaceStates.EMPTY]
        ]
        self.game_status = GameStates.NOT_STARTED
        self.current_turn = SpaceStates.X

    def name(self):
        return ("%s %s" % (self.x_player_name,self.o_player_name))


    def start_game(self):
        self.game_started = True
    
    def end_game(self):
        self.game_started = False

    def has_game_started(self):
        return self.game_started

    def get_current_turn(self):
        return self.current_turn

    def get_board(self):
        return self.board
    
    def print_board(self):
        print("Board:")
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        
    def get_player_x(self):
        return self.x_name
    
    def get_player_o(self):
        return self.o_name
    
    def set_player_x(self, name):
        self.x_name = name
    
    def set_player_o(self, name):
        self.o_name = name

    def set_spacenum(self, player, spacenum):
        row = spacenum // 3
        col = spacenum % 3
        self.board[row][col] = player

    @classmethod
    def getAll(self):
        pass
    
if __name__ == "__main__":
    board = Model()
    board.print_board()
    pass