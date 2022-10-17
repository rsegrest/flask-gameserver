
from controller.tictactoe_controller import TicTacToeController
from model.tic_player_model import TicTacToePlayerModel
from model.tictactoe_model import TicTacToeModel
from constants.spacestates import EMPTY, X, O

def func(x):
    return x + 1

class TestController:
    # def test_board(self):
    #     assert True
    def test_is_space_empty(self):
        game = TicTacToeController()
        game.set_board_state([
            [EMPTY,X,O],
            [X,X,O],
            [O,O,EMPTY]
        ])
        check_space_0 = game.is_space_empty(0)
        check_space_1 = game.is_space_empty(1)
        check_space_5 = game.is_space_empty(5)
        check_space_8 = game.is_space_empty(8)

        assert check_space_0 == True
        assert check_space_1 == False
        assert check_space_5 == False
        assert check_space_8 == True
        
    def test_is_turn_current(self):
        game = TicTacToeController()
        game.set_current_turn(X)
        check_turn_0 = game.is_turn_current(X)
        check_turn_1 = game.is_turn_current(O)
        game.change_turn()
        check_turn_2 = game.is_turn_current(X)
        check_turn_3 = game.is_turn_current(O)
        assert check_turn_0 == True
        assert check_turn_1 == False
        assert check_turn_2 == False
        assert check_turn_3 == True
    
    def test_does_player_id_match(self):
        game = TicTacToeController()
        model = TicTacToeModel()

        playerx = TicTacToePlayerModel("playerx", 1, X)
        playero = TicTacToePlayerModel("playero", 2, O)

        model.set_player_x(playerx)
        model.set_player_o(playero)
        game.set_model(model)
        
        check_id_match_0 = game.does_player_id_match(X,1) # true
        check_id_match_1 = game.does_player_id_match(O,2) # true
        check_id_match_2 = game.does_player_id_match(X,3) # false
        check_id_match_3 = game.does_player_id_match(O,1) # false
        
        assert check_id_match_0 == True
        assert check_id_match_1 == True
        assert check_id_match_2 == False
        assert check_id_match_3 == False