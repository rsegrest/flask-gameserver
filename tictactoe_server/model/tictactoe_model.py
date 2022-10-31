import json
from constants.spacestates import EMPTY, X, O
from constants.gamestates import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW
# from tictactoe_server.model.tic_player_model import TicTacToePlayerModel

class TicTacToeModel():

    def __init__(
        self,
        player_x = None,
        player_o = None,
        room = None,
    ):
        self.player_x = player_x
        self.player_o = player_o

        self.board = [
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY]
        ]

        self.game_status = NOT_STARTED
        # self.current_turn = X

    def name(self):
        return ("%s %s" % (self.x_player_name,self.o_player_name))

    def set_current_turn(self, side):
        self.game_status = side+"_TURN"

    # def register_a_player(self, name, id):
    #     if self.player_x == None:
    #         self.player_x = TicTacToePlayerModel(name, id, X)
    #         return True
    #     if self.player_o == None:
    #         self.player_o = TicTacToePlayerModel(name, id, O)
    #         return True
    #     return False

    # def num_players_registered(self):
    #     count = 0
    #     if self.player_x != None:
    #         count += 1
    #     if self.player_o != None:
    #         count += 1
    #     return count
    
    # CharlotteMaeSegrest@gmail.com
    # Ozzie10282011

    def has_diagonal_match(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != EMPTY):
            return True
        elif (self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != EMPTY):
            return True
        return False

    def has_horizontal_match(self):
        # for loop from 0 to 2:
        for row in self.board:
            if (row[0] == row[1] == row[2] and row[0] != EMPTY):
                return True
        return False

    def has_vertical_match(self):
        # loop through row indexes:
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != EMPTY):
                return True
        return False

    def has_winner(self):
        if (self.has_diagonal_match() or self.has_horizontal_match() or self.has_vertical_match()):
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for space in row:
                if space == EMPTY:
                    return False
        return True

    def is_space_empty(self, spacenum):
        print("spacenum: %s" % spacenum)
        row = int(spacenum) // 3
        col = int(spacenum) % 3
        print("row: %s" % str(row))
        print("col: %s" % str(col))
        print("board: %s" % self.board)
        return self.board[row][col] == EMPTY

    def set_board(self, board):
        self.board = board

    def start_game(self):
        self.game_started = True
    
    def end_game(self):
        self.game_started = False

    def has_game_started(self):
        return self.game_status != NOT_STARTED

    def get_current_turn(self):
        # return self.game_status
        if self.game_status == X_TURN:
            return X
        elif self.game_status == O_TURN:
            return O
        return None

    def get_board(self):
        return self.board

    def get_room(self):
        return self.room
    
    def set_room(self, roomname):
        self.room = roomname

    def board_to_string(self):
        return json.dumps(self.board)

    def print_board(self):
        # print("Board:")
        # print(self.board[0])
        # print(self.board[1])
        # print(self.board[2])
        print(self.board_to_string())

    def get_player_x(self):
        if (self.player_x is None):
            return None
        return self.player_x.name

    def get_player_o(self):
        if (self.player_o is None):
            return None
        return self.player_o.name

    def get_x_id(self):
        if (self.player_x is None):
            return None
        return self.player_x.id

    def get_o_id(self):
        if (self.player_o is None):
            return None
        return self.player_o.id

    def set_player_x(self, player):
        self.player_x = player

    def set_player_o(self, player):
        self.player_o = player

    def set_spacenum(self, side, spacenum):
        row = int(spacenum) // 3
        col = int(spacenum) % 3
        self.board[row][col] = side
        
    def get_player_names(self):
        return [self.player_x.name, self.player_o.name]

    # @classmethod
    # def getAll(self):
    #     pass
    
if __name__ == "__main__":
    board = TicTacToeModel()
    board.print_board()
    pass