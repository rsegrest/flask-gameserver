
from controller.c4_controller import C4Controller
from model.c4_player_model import C4PlayerModel
from model.c4_model import C4Model
from constants.spacestates import EMPTY, R, B
from constants.gamestates import NOT_STARTED, R_TURN, B_TURN, R_WON, B_WON, DRAW, NUM_ROWS, NUM_COLS

def func(x):
    return x + 1

class TestController:
    # def test_board(self):
    #     assert True
    def test_is_space_empty(self):
        game = C4Controller()
        game.set_board_state([
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [EMPTY,B,R, EMPTY, EMPTY, EMPTY, EMPTY],
            [B,B,R, EMPTY, EMPTY, EMPTY, EMPTY],
            [R,R,EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        ])
        check_space_0 = game.is_space_empty([0,0])
        check_space_1 = game.is_space_empty([5,0])
        check_space_5 = game.is_space_empty([5,1])
        check_space_8 = game.is_space_empty([5,6])

        assert check_space_0 == True
        assert check_space_1 == False
        assert check_space_5 == False
        assert check_space_8 == True
        
    def test_is_turn_current(self):
        game = C4Controller()
        game.set_current_turn(B)
        check_turn_0 = game.is_turn_current(B)
        check_turn_1 = game.is_turn_current(R)
        game.change_turn()
        check_turn_2 = game.is_turn_current(B)
        check_turn_3 = game.is_turn_current(R)
        assert check_turn_0 == True
        assert check_turn_1 == False
        assert check_turn_2 == False
        assert check_turn_3 == True
    
    def test_does_player_id_match(self):
        game = C4Controller()
        model = C4Model()

        playerBlack = C4PlayerModel("playerBlack", 1, B)
        playerRed = C4PlayerModel("playerRed", 2, R)

        model.set_player_black(playerBlack)
        model.set_player_red(playerRed)
        game.set_model(model)
        
        check_id_match_0 = game.does_player_id_match(B,1) # true
        check_id_match_1 = game.does_player_id_match(R,2) # true
        check_id_match_2 = game.does_player_id_match(B,3) # false
        check_id_match_3 = game.does_player_id_match(R,1) # false
        
        assert check_id_match_0 == True
        assert check_id_match_1 == True
        assert check_id_match_2 == False
        assert check_id_match_3 == False
    
    # def test_try_move(self):
    #     game = C4Controller()
    #     model = C4Model()
    #     playerBlack = C4PlayerModel("playerBlack", 1, B)
    #     playerRed = C4PlayerModel("playerRed", 2, R)

    #     model.set_player_black(playerBlack)
    #     model.set_player_red(playerRed)
    #     game.set_model(model)
        
    #     game.try_move(B,1,0)
    #     NOT CORRECT -- FAILING
    #     assert game.get_board_state()[0][0] == B
    #     assert game.get_board_state()[0][1] == EMPTY
    #     assert game.get_current_turn() == R

    # def test_cats(self):
        # game = Connect4Controller()
        # model = Connect4Model()
        # playerBlack = Connect4PlayerModel("playerBlack", 1, B)
        # playerRed = Connect4PlayerModel("playerRed", 2, R)
        # model.board = [
        #     [EMPTY,O,X],
        #     [X,X,O],
        #     [O,X,O]
        # ]

        # model.game_started = True
        # model.game_status = B_TURN
        # model.current_turn = B

        # model.set_player_black(playerBlack)
        # model.set_player_red(playerRed)
        # game.set_model(model)
        
        # game.try_move(B,1,0)
        # assert game.get_board_state()[0][0] == B
        # assert game.model.game_status == DRAW
    
    # def test_black_win(self):
    #     game = C4Controller()
    #     model = C4Model()
    #     playerBlack = C4PlayerModel("playerBlack", 1, B)
    #     playerRed = C4PlayerModel("playerRed", 2, R)
    #     model.board = [
    #         [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    #         [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    #         [EMPTY,R,B,EMPTY,EMPTY,EMPTY,EMPTY],
    #         [EMPTY,R,B,R,EMPTY,EMPTY,EMPTY],
    #         [B,B,R,R,EMPTY,EMPTY,EMPTY],
    #         [B,R,R,R,EMPTY,EMPTY,EMPTY]
    #     ]

    #     model.game_started = True
    #     model.game_status = B_TURN
    #     model.current_turn = B

    #     model.set_player_black(playerBlack)
    #     model.set_player_red(playerRed)
    #     game.set_model(model)
        
    #     game.try_move(B,1,3)
    #     # WRONG
    #     assert game.get_board_state()[2][3] == B
    #     assert game.model.game_status == B_WON
    
    # def test_red_win(self):
    #     game = C4Controller()
    #     model = C4Model()
    #     playerBlack = C4PlayerModel("playerBlack", 1, B)
    #     playerRed = C4PlayerModel("playerRed", 2, R)
    #     model.board = [
    #         [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    #         [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    #         [EMPTY,R,B,EMPTY,EMPTY,EMPTY,EMPTY],
    #         [EMPTY,R,B,R,EMPTY,EMPTY,EMPTY],
    #         [B,B,R,R,EMPTY,EMPTY,EMPTY],
    #         [B,R,R,R,EMPTY,EMPTY,EMPTY]
    #     ]

    #     model.game_started = True
    #     model.game_status = R_TURN
    #     model.current_turn = R

    #     model.set_player_black(playerBlack)
    #     model.set_player_red(playerRed)
    #     game.set_model(model)
        
    #     game.try_move(R,2,4)
    #     # CHECK MOVE IS BEING MADE CORRECTLY -- new test case?
    #     assert game.get_board_state()[2][4] == B
    #     assert game.model.game_status == R_WON