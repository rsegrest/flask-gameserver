
from controller.tictactoe_controller import TicTacToeController
from model.tic_player_model import TicTacToePlayerModel
from model.tictactoe_model import TicTacToeModel
from constants.spacestates import EMPTY, X, O
from constants.gamestates import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW

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
    
    def test_try_move(self):
        game = TicTacToeController()
        model = TicTacToeModel()
        playerx = TicTacToePlayerModel("playerx", 1, X)
        playero = TicTacToePlayerModel("playero", 2, O)

        model.set_player_x(playerx)
        model.set_player_o(playero)
        model.game_status = X_TURN
        game.set_model(model)

        game.try_move(X,1,0)
        assert game.get_board_state()[0][0] == X
        assert game.get_board_state()[0][1] == EMPTY
        assert game.get_current_turn() == O

    def test_cats(self):
        game = TicTacToeController()
        model = TicTacToeModel()
        playerx = TicTacToePlayerModel("playerx", 1, X)
        playero = TicTacToePlayerModel("playero", 2, O)
        model.board = [
            [EMPTY,O,X],
            [X,X,O],
            [O,X,O]
        ]

        # model.game_started = True
        # model.game_status = X_TURN
        # model.current_turn = X

        model.set_player_x(playerx)
        model.set_player_o(playero)
        print('model before assignment: ', model.board_to_string())
        # print('model before assignment : %s' %s model.print_board())
        game.set_model(model)
        print('model after assignment: ', game.model.board_to_string())
        
        # game.start_game()
        model.game_status = X_TURN
        game.try_move(X,1,0)
        assert game.model.board[0][0] == X
        assert game.model.game_status == DRAW
    
    def test_x_win(self):
        game = TicTacToeController()
        model = TicTacToeModel()
        playerx = TicTacToePlayerModel("playerx", 1, X)
        playero = TicTacToePlayerModel("playero", 2, O)
        model.board = [
            [EMPTY,O,X],
            [X,X,O],
            [X,O,O]
        ]

        model.game_started = True
        model.game_status = X_TURN
        model.current_turn = X

        model.set_player_x(playerx)
        model.set_player_o(playero)
        game.set_model(model)
        
        game.try_move(X,1,0)
        assert game.get_board_state()[0][0] == X
        assert game.model.game_status == X_WON
    
    def test_o_win(self):
        game = TicTacToeController()
        model = TicTacToeModel()
        playerx = TicTacToePlayerModel("playerx", 1, X)
        playero = TicTacToePlayerModel("playero", 2, O)
        model.board = [
            [EMPTY,X,EMPTY],
            [X,X,O],
            [EMPTY,EMPTY,O]
        ]

        model.game_started = True
        model.game_status = O_TURN
        model.current_turn = O

        model.set_player_x(playerx)
        model.set_player_o(playero)
        game.set_model(model)
        
        game.try_move(O,2,2)
        assert game.model.game_status == O_WON