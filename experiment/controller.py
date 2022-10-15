from model import Model
from constants.spacestates import SpaceStates
from constants.gamestates import GameStates

class Controller(): # Model):
    def __init__(self):
        # super().__init__()
        self.model = Model()
        pass
    
    def get_board_state(self):
        return self.model.get_board()

    def make_move(self, player, spacenum):
        self.model.set_spacenum(player, spacenum)

    def start_game(self):
        self.model.game_started = True

    def set_player_name(self, player, name):
        if player == SpaceStates.X:
            self.model.set_player_x(name)
        elif player == SpaceStates.O:
            self.model.set_player_o(name)

    def get_player_name(self, player):
        if player == SpaceStates.X:
            return self.model.get_player_x()
        elif player == SpaceStates.X:
            return self.model.get_player_o()

    def get_current_turn(self):
        return self.model.get_current_turn()

    def change_turn(self):
        if self.model.current_turn == SpaceStates.X:
            self.model.current_turn = SpaceStates.O
        else:
            self.model.current_turn = SpaceStates.X

    def start():
        pass
        # view.startView()
        # input = raw_input()
        # if input == 'y':
        #     return showAll()
        # else:
        #     return view.endView()

    if __name__ == "__main__":
        #running controller function
        start()
