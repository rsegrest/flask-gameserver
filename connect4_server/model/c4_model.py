from constants.spacestates import EMPTY, B, R
from constants.gamestates import NOT_STARTED, B_TURN, R_TURN, B_WON, R_WON, DRAW, NUM_COLS, NUM_ROWS, GAME_ABORTED

from model.c4_player_model import C4PlayerModel
# import json

class C4Model():

    def __init__(
        self,
        player_black = None,
        player_red = None,
        room = None,
    ):
        self.player_black = player_black
        self.player_red = player_red

        self.board = [
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
        ]

        self.game_status = NOT_STARTED
        # self.current_turn = X

    def name(self):
        return ("%s %s" % (self.black_player_name,self.red_player_name))

    def set_current_turn(self, side):
        self.game_status = side+"_TURN"
    
    def has_diagonal_match(self):
        # pass
        # CHECK FORWARD DIAGONALS
        for row in range(NUM_ROWS-3):
            for col in range(NUM_COLS-3):
                if (self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] and self.board[row][col] != EMPTY):
                    print("row, col: %s, %s" % (row, col))
                    return True
        for row in range(NUM_ROWS-4):
            for col in range(4,(NUM_COLS-1)):
                print("row, col: %s, %s" % (row, col))
                if (self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] == self.board[row+4][col-4] and self.board[row][col] != EMPTY):
                    return True
        return False

    def has_horizontal_match(self):
        # for loop from 0 to 2:
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS-3):
                if (self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] and self.board[row][col] != EMPTY):
                    return True
        return False

    def has_vertical_match(self):
        # loop through row indexes:
        for col in range(NUM_COLS):
            for row in range(NUM_ROWS-3):
                print("row, col: %s, %s" % (row, col))
                if (self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] and self.board[row][col] != EMPTY):
                    print('vertical match found at row %s, col %s' % (row, col))
                    return True
        return False

    def has_winner(self):
        if (self.has_diagonal_match() or self.has_horizontal_match() or self.has_vertical_match()):
            return True
        return False

    def is_board_full(self):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if self.board[row][col] == EMPTY:
                    return False
        return True

    def is_space_empty(self, space):
        print("space: "+str(space[0])+", "+str(space[1]))
        row = int(space[0])
        col = int(space[1]) 
        print("row: %s" % str(row))
        print("col: %s" % str(col))
        print("board: %s" % self.board)
        return self.board[row][col] == EMPTY

    def set_board(self, board):
        self.board = board

    def start_game(self):
        self.game_status = B_TURN
    
    def end_game(self):
        self.game_status = DRAW

    def has_game_started(self):
        return self.game_status != NOT_STARTED

    def get_current_turn(self):
        # return self.game_status
        if self.game_status == B_TURN:
            return B
        elif self.game_status == R_TURN:
            return R
        return None

    def get_board(self):
        return self.board

    def get_room(self):
        return self.room
    
    def set_room(self, roomname):
        self.room = roomname

    def print_board(self):
        print("Board:")
        boardString = ''

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if self.board[row][col] == EMPTY:
                    boardString += '_'
                elif self.board[row][col] == B:
                    boardString += 'B'
                elif self.board[row][col] == R:
                    boardString += 'R'
            boardString += '\n'
        print(boardString)
        return boardString

    def get_player_black(self):
        if (self.player_black is None):
            return None
        return self.player_black.name

    def get_player_red(self):
        if (self.player_red is None):
            return None
        return self.player_red.name

    def get_black_id(self):
        if (self.player_black is None):
            return None
        return self.player_black.id

    def get_red_id(self):
        if (self.player_red is None):
            return None
        return self.player_red.id

    def set_player_black(self, player):
        self.player_black = player

    def set_player_red(self, player):
        self.player_red = player

    def set_space(self, side, space):
        print("set_space: ")
        print("side: %s" % side)
        print("space: "+str(space[0])+", "+str(space[1]))
        row = int(space[0])
        col = int(space[1])
        self.board[row][col] = side
        self.print_board()
        
    def get_player_names(self):
        return [self.player_black.name, self.player_red.name]

    # @classmethod
    # def getAll(self):
    #     pass
    
if __name__ == "__main__":
    board = C4Model()
    board.print_board()
    pass