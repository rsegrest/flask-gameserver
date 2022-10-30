from model.c4_model import C4Model
from model.c4_player_model import C4PlayerModel
from constants.spacestates import EMPTY, B, R
from constants.gamestates import NOT_STARTED, B_TURN, R_TURN, B_WON, R_WON, DRAW, NUM_ROWS, NUM_COLS

class C4Controller(): # Model):
    def __init__(self):
        # super().__init__()
        self.model = C4Model()
        pass
    
    def set_model(self, model):
        self.model = model
    
    def is_board_full(self):
        self.model.is_board_full()
    
    def does_column_have_space(self, column):
        return self.is_space_empty((0, column))

    def is_space_empty(self, space):
        return self.model.is_space_empty(space)

    def get_board_state(self):
        return self.model.get_board()
    
    def set_board_state(self, board):
        self.model.set_board(board)
    
    def has_game_started(self):
        return self.model.has_game_started
    
    def register_a_player(self, name, id):
        if self.model.player_black == None:
            self.model.player_black = C4PlayerModel(name, id, B)
            return B
        if self.model.player_red == None:
            self.model.player_red = C4PlayerModel(name, id, R)
            return R
        return None

    def num_players_registered(self):
        count = 0
        if self.model.player_black != None:
            count += 1
        if self.model.player_red != None:
            count += 1
        return count

    def is_turn_current(self, side):
        print('c4_cont--is_turn_current: '+str(side))
        if side+'_TURN' == self.model.game_status:
            return True
        return False
    
    def does_player_id_match(self, side, player_id):
        if side == B:
            return self.model.player_black.id == player_id
        if side == R:
            return self.model.player_red.id == player_id
        return False

    def check_for_win(self):
        return self.model.has_winner()

    def check_for_draw(self):
        return self.model.is_board_full()

    def get_lowest_empty_row(self, column):
        last_empty_row = None
        for i in range(NUM_ROWS-1):
            if self.model.board[i][column] == EMPTY:
                last_empty_row = i
            else:
                break
        return last_empty_row

    def make_move(self, side, column):
        print('make_move: side: %s, column: %s' % (str(side), str(column)))
        # self.model.set_space(side, space)
        lowest_empty_row = self.get_lowest_empty_row(column)
        self.model.set_space(side, [lowest_empty_row, column])

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
    
    def try_move(self, side, player_id, column):
        print("make_move: side: %s, player_id: %s, column: %s" % (str(side), str(player_id), str(column)))
        
        if self.does_column_have_space(column):
            print('column has empty space')
            if self.is_turn_current(side):
                print('turn is current')
                if self.does_player_id_match(side, player_id):
                    print('player id matches')
                    self.make_move(side, column)
                    return True
                else:
                    print('player id does not match')
            else:
                print('turn is not current')
        return False
        # pass

    def clear_board(self):
        # pass
        cleared_board = []
        for i in range(NUM_ROWS):
            row = []
            for j in range(NUM_COLS):
                row.append(EMPTY)
            cleared_board.append(row)
        return

    def start_game(self):
        self.model.game_started = True
        self.model.game_status = B_TURN
        self.clear_board()
        return

    def set_player_name(self, player, name):
        if player == B:
            self.model.set_player_black(name)
        elif player == R:
            self.model.set_player_red(name)

    def get_player_name(self, player):
        if player == B:
            return self.model.get_player_black()
        elif player == R:
            return self.model.get_player_red()

    def get_sides(self):
        return "X: "+str(self.model.player_x)+", O: "+str(self.model.player_o)

    def get_player_names(self):
        return (str(self.model.get_player_x()), str(self.model.get_player_o()))

    def get_current_turn(self):
        if (self.model.game_status == B_TURN):
            return X
        elif (self.model.game_status == R_TURN):
            return O
        return None

    def set_current_turn(self, side):
        self.model.game_status = side+"_TURN"

    def change_turn(self):
        if self.model.game_status == B_TURN:
            self.model.game_status = R_TURN
        else:
            self.model.game_status = B_TURN

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
