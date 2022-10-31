from model.tictactoe_model import TicTacToeModel
from model.tic_player_model import TicTacToePlayerModel
from constants.spacestates import EMPTY, X, O
from constants.gamestates import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW

class TicTacToeController(): # Model):
    def __init__(self):
        # super().__init__()
        self.model = TicTacToeModel()
        pass
    
    def set_model(self, model):
        self.model = model
    
    def is_board_full(self):
        self.model.is_board_full()
    
    def is_space_empty(self, spacenum):
        return self.model.is_space_empty(spacenum)

    def get_board_state(self):
        return self.model.get_board()
    
    def set_board_state(self, board):
        self.model.set_board(board)
    
    def has_game_started(self):
        return self.model.has_game_started
    
    def register_a_player(self, name, id):
        if self.model.player_x == None:
            self.model.player_x = TicTacToePlayerModel(name, id, X)
            return X
        if self.model.player_o == None:
            self.model.player_o = TicTacToePlayerModel(name, id, O)
            return O
        return None

    def num_players_registered(self):
        count = 0
        if self.model.player_x != None:
            count += 1
        if self.model.player_o != None:
            count += 1
        return count

    def is_turn_current(self, side):
        print('ttt_cont--is_turn_current: '+str(side))
        if side+'_TURN' == self.model.game_status:
            return True
        return False
    
    def does_player_id_match(self, side, player_id):
        if side == X:
            return self.model.player_x.id == player_id
        if side == O:
            return self.model.player_o.id == player_id
        return False

    def check_for_win(self):
        return self.model.has_winner()

    def check_for_draw(self):
        return self.model.is_board_full()

    def make_move(self, side, spacenum):
        print('make_move: side: %s, spacenum: %s' % (str(side), str(spacenum)))
        self.model.set_spacenum(side, spacenum)
        is_winner = self.check_for_win()
        is_draw = self.check_for_draw()
        if (is_winner == False) and (is_draw == False):
            self.change_turn()
        if is_winner:
            print('is_winner')
            self.model.game_status = side + "_WON"
        elif is_draw:
            print('is_draw')
            self.model.game_status = DRAW
    
    def try_move(self, side, player_id, spacenum):
        print("make_move: side: %s, player_id: %s, spacenum: %s" % (str(side), str(player_id), str(spacenum)))
        
        if self.is_space_empty(spacenum):
            print('space is empty')
            if self.is_turn_current(side):
                print('turn is current')
                if self.does_player_id_match(side, player_id):
                    print('player id matches')
                    self.make_move(side, spacenum)
                    return True
                else:
                    print('player id does not match')
            else:
                print('turn is not current')
        return False
        # self.model.set_spacenum(side, spacenum)
        # Check if game is over
        # Check if game is a draw
        # Change turn

    def clear_board(self):
        self.model.board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
        return

    def start_game(self):
        self.model.game_started = True
        self.model.game_status = X_TURN
        self.clear_board()
        return

    def set_player_name(self, player, name):
        if player == X:
            self.model.set_player_x(name)
        elif player == O:
            self.model.set_player_o(name)

    def get_player_name(self, player):
        if player == X:
            return self.model.get_player_x()
        elif player == O:
            return self.model.get_player_o()

    def get_sides(self):
        return "X: "+str(self.model.player_x)+", O: "+str(self.model.player_o)

    def get_player_names(self):
        return (str(self.model.get_player_x()), str(self.model.get_player_o()))

    def get_current_turn(self):
        if (self.model.game_status == X_TURN):
            return X
        elif (self.model.game_status == O_TURN):
            return O
        return None

    def set_current_turn(self, side):
        self.model.game_status = side+"_TURN"

    def change_turn(self):
        if self.model.game_status == X_TURN:
            self.model.game_status = O_TURN
        else:
            self.model.game_status = X_TURN

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
