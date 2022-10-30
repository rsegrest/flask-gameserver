import model.c4_player_model as cpm
from model.c4_model import C4Model
from constants.spacestates import EMPTY, B,R
def func(x):
    return x + 1

class TestModel:
    # def test_board(self):
    #     assert True
    def test_answer(self):
        assert func(4) == 5
        
    # Test win conditions
    # def test_is_board_full(self):
    #     board = C4Model()
    #     board.set_board([
    #         [O,X,O],
    #         [X,X,O],
    #         [O,O,X]
    #     ])
    #     resultval = board.is_board_full()
    #     winner = board.has_winner()
    #     assert winner == False
    #     assert resultval == True

    # def test_has_diagonal_match_true(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,O,O],
    #         [EMPTY,X,O],
    #         [EMPTY,EMPTY,X]
    #     ])
    #     resultval = board.has_diagonal_match()
    #     winner = board.has_winner()
    #     assert winner == True
    #     assert resultval == True

    # def test_has_diagonal_match_false(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,O,O],
    #         [EMPTY,X,EMPTY],
    #         [EMPTY,EMPTY,EMPTY]
    #     ])
    #     resultval = board.has_diagonal_match()
    #     winner = board.has_winner()
    #     assert winner == False
    #     assert resultval == False

    # def test_first_row_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [O,O,O],
    #         [X,X,EMPTY],
    #         [EMPTY,X,EMPTY]
    #     ])
    #     resultval = board.has_horizontal_match()
    #     winner = board.has_winner()
    #     assert winner == True
    #     assert resultval == True

    # def test_second_row_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,O,O],
    #         [X,X,X],
    #         [EMPTY,X,O]
    #     ])
    #     resultval = board.has_horizontal_match()
    #     winner = board.has_winner()
    #     assert winner == True
    #     assert resultval == True

    # def test_third_row_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,O,O],
    #         [O,X,O],
    #         [X,X,X]
    #     ])
    #     resultval = board.has_horizontal_match()
    #     winner = board.has_winner()
    #     assert winner == True
    #     assert resultval == True

    # def test_no_horizontal_row_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,O,O],
    #         [EMPTY,X,EMPTY],
    #         [EMPTY,EMPTY,EMPTY]
    #     ])
    #     resultval = board.has_horizontal_match()
    #     winner = board.has_winner()
    #     assert winner == False
    #     assert resultval == False

    # def test_first_col_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [O,O,EMPTY],
    #         [O,X,X],
    #         [O,X,EMPTY]
    #     ])
    #     resultval = board.has_vertical_match()
    #     winner = board.has_winner()
    #     assert winner == True
    #     assert resultval == True

    # def test_second_col_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,X,O],
    #         [EMPTY,X,O],
    #         [O,X,O]
    #     ])
    #     resultval = board.has_vertical_match()
    #     winner = board.has_winner()
    #     assert winner == True
    #     assert resultval == True

    # def test_third_col_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,O,X],
    #         [O,O,X],
    #         [O,X,X]
    #     ])
    #     resultval = board.has_vertical_match()
    #     winner = board.has_winner()
    #     assert winner == True
    #     assert resultval == True

    # def test_no_vertical_col_win(self):
    #     board = TicTacToeModel()
    #     board.set_board([
    #         [X,O,O],
    #         [EMPTY,X,EMPTY],
    #         [EMPTY,EMPTY,EMPTY]
    #     ])
    #     resultval = board.has_vertical_match()
    #     winner = board.has_winner()
    #     assert winner == False
    #     assert resultval == False