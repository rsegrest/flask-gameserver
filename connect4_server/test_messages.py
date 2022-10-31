import model.c4_player_model as cpm
from model.c4_model import C4Model
from constants.spacestates import EMPTY,B,R

from app import app

def func(x):
    return x + 1

class TestMessages:
    def test_answer(self):
        assert func(4) == 5
        
    # # Test win conditions
    def test_is_board_full(self):
        board = C4Model()
        board.set_board([
            [B,R,B,B,R,B,B],
            [B,R,B,B,R,B,B],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [B,R,B,B,R,B,B],
        ])
        resultval = board.is_board_full()
        winner = board.has_winner()
        assert winner == False
        assert resultval == True

    def test_has_diagonal_match_true(self):
        board = C4Model()
        board.set_board([
            [R,R,B,B,R,B,B],
            [B,R,B,B,R,B,B],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [B,R,B,B,R,B,B],
        ])
        resultval = board.has_diagonal_match()
        winner = board.has_winner()
        assert winner == True
        assert resultval == True

    def test_has_diagonal_match_false(self):
        board = C4Model()
        board.set_board([
            [B,EMPTY,EMPTY,EMPTY,R,EMPTY,EMPTY],
            [B,EMPTY,EMPTY,EMPTY,R,B,B],
            [R,EMPTY,EMPTY,EMPTY,EMPTY,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [B,R,B,B,R,B,B],
        ])
        resultval = board.has_diagonal_match()
        horizresultval = board.has_horizontal_match()
        vertresultval = board.has_vertical_match()
        winner = board.has_winner()
        assert resultval == False
        assert horizresultval == False
        assert vertresultval == False
        assert winner == False
        

    def test_first_row_win(self):
        board = C4Model()
        board.set_board([
            [B,B,B,B,EMPTY,EMPTY,EMPTY],
            [B,R,B,B,R,B,B],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [B,R,B,B,R,B,B],
        ])
        resultval = board.has_horizontal_match()
        winner = board.has_winner()
        assert winner == True
        assert resultval == True

    def test_second_row_win(self):
        board = C4Model()
        board.set_board([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [B,B,B,B,EMPTY,EMPTY,EMPTY],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [B,R,B,B,R,B,B],
        ])
        resultval = board.has_horizontal_match()
        winner = board.has_winner()
        assert winner == True
        assert resultval == True

    def test_third_row_win(self):
        board = C4Model()
        board.set_board([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [B,B,B,B,EMPTY,EMPTY,EMPTY],
            [R,B,R,R,B,R,R],
            [R,R,B,R,B,R,R],
            [R,B,R,R,B,R,R],
        ])
        resultval = board.has_horizontal_match()
        winner = board.has_winner()
        assert winner == True
        assert resultval == True

    def test_no_horizontal_row_win(self):
        board = C4Model()
        board.set_board([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [B,EMPTY,B,EMPTY,EMPTY,EMPTY,EMPTY],
            [R,EMPTY,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
        ])
        resultval = board.has_horizontal_match()
        winner = board.has_winner()
        assert winner == False
        assert resultval == False

    def test_first_col_win(self):
        board = C4Model()
        board.set_board([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [R,EMPTY,B,EMPTY,EMPTY,EMPTY,EMPTY],
            [R,EMPTY,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
        ])
        resultval = board.has_vertical_match()
        winner = board.has_winner()
        assert winner == True
        assert resultval == True

    def test_second_col_win(self):
        board = C4Model()
        board.set_board([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [B,B,B,EMPTY,EMPTY,EMPTY,EMPTY],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
        ])
        resultval = board.has_vertical_match()
        winner = board.has_winner()
        assert winner == True
        assert resultval == True

    def test_third_col_win(self):
        board = C4Model()
        board.set_board([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [B,EMPTY,R,EMPTY,EMPTY,EMPTY,EMPTY],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
            [R,B,R,R,B,R,R],
        ])
        resultval = board.has_vertical_match()
        winner = board.has_winner()
        assert resultval == True
        assert winner == True

    def test_no_vertical_col_win(self):
        board = C4Model()
        board.set_board([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [R,B,R,R,B,R,R],
            [B,R,B,B,R,B,B],
        ])
        resultval = board.has_vertical_match()
        winner = board.has_winner()
        assert winner == False
        assert resultval == False