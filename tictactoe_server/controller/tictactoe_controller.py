from model.tictactoe_model import TicTacToeModel
from model.tic_player_model import TicTacToePlayerModel
from constants.spacestates import EMPTY, X, O
from constants.gamestates import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW

class TicTacToeController(): # Model):
    def __init__(self):
        # super().__init__()
        self.model = TicTacToeModel()
        pass
    
    def is_board_full(self):
        self.model.is_board_full()

    def get_board_state(self):
        return self.model.get_board()
    
    def has_game_started(self):
        return self.model.has_game_started
    
    def register_a_player(self, name, id):
        if self.model.player_x == None:
            self.model.player_x = TicTacToePlayerModel(name, id, X)
            return True
        if self.model.player_o == None:
            self.model.player_o = TicTacToePlayerModel(name, id, O)
            return True
        return False

    def num_players_registered(self):
        count = 0
        if self.model.player_x != None:
            count += 1
        if self.model.player_o != None:
            count += 1
        return count

    def make_move(self, player, spacenum):
        self.model.set_spacenum(player, spacenum)

    def start_game(self):
        self.model.game_started = True
        self.model.game_status = X_TURN
        return

    def set_player_name(self, player, name):
        if player == X:
            self.model.set_player_x(name)
        elif player == O:
            self.model.set_player_o(name)

    def get_player_name(self, player):
        if player == X:
            return self.model.get_player_x()
        elif player == X:
            return self.model.get_player_o()

    def get_sides(self):
        return "X: "+str(self.model.player_x)+", O: "+str(self.model.player_o)

    def get_player_names(self):
        return (str(self.model.get_player_x()), str(self.model.get_player_o()))

    def get_current_turn(self):
        return self.model.get_current_turn()

    def change_turn(self):
        if self.model.current_turn == X:
            self.model.current_turn = O
        else:
            self.model.current_turn = X

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
