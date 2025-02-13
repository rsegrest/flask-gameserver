from model.yahtzee_model import YahtzeeModel
from model.yahtzee_player_model import YahtzeePlayerModel
# from constants.spacestates import EMPTY, X, O
from constants.gamestates import NOT_STARTED

class YahtzeeController(): # Model):
    def __init__(self):
        # super().__init__()
        self.model = YahtzeeModel()
        pass
    
    def set_model(self, model):
        # print('model arg board: '+str(model.board_to_string()))
        self.model = model
        # print('my board after assignment: '+str(self.model.board_to_string()))

    def register_player(self, name, id, emit_func):
        pass
        # if (self.num_players_registered() < 2):
        #     print('assigning player')
        #     thisUsername = name # message['name']
        #     side_assigned = self.register_a_player(thisUsername, request.sid)
        #     print('side_assigned', side_assigned)
        #     emit_func('ack_player_username', {
        #         'id': request.sid,
        #         # 'username': tictactoeGame.get_player_names(), # [request.sid]})
        #         'username': thisUsername,
        #         'side': side_assigned, # [request.sid]
        #     }, broadcast=True)
        #     if (self.num_players_registered() == 2):
        #         self.start_game_func()
        #     print('returning True')
        #     return True
        # return False

    def start_game_func(self):
        pass
        # print('start_game: '+str(self.get_player_names()))
        # torf = False
        # if self.num_players_registered() == 2:
        #     self.start_game()
        #     if self.has_game_started():
        #         torf = True
        # print('torf', torf)
        # emit('update_board', { 'board': self.model.board }, broadcast=True)
        # emit('update_game_status', {'status': self.model.game_status }, broadcast=True)
        # emit('ack_start_game', {'starting_game': str(torf)})

    def register_a_player(self, name, id):
        # if self.model.players == []:
        player_num = self.model.players.size()
        self.model.players.append(YahtzeePlayerModel(name, id, player_num))
        return
        # return X
        # return None

    def num_players_registered(self):
        return self.model.players.size()

    def is_turn_current(self, player_num):
        print('yz_cont--is_turn_current: '+str(player_num))
        pass
        # print('ttt_cont--is_turn_current: '+str(side))
        # if side+'_TURN' == self.model.game_status:
            # return True
        # return False
    
    def does_player_id_match(self, side, player_id):
        pass
        # Get player turn , compare to ...?

    def check_for_win(self):
        return self.model.has_winner()

    # NOT NEEDED?
    # def check_for_draw(self):
    #     print(self.model.print_board())
    #     isFull = self.model.is_board_full()
    #     print('check for draw: isFull: %s' % str(isFull))
    #     return isFull

    # TODO: Implement
    def reset_game(self):
        pass
        # self.model.board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
        # return

    # TODO: Implement
    def start_game(self):
        pass
        # self.model.game_started = True
        # self.model.game_status = X_TURN
        # self.clear_board()
        # return

    def set_player_name(self, player_num, name):
        self.model.set_player_name(player_num, name)

    # TODO: Implement
    def get_player_name(self, player_num):
        pass

    # TODO: Implement
    def get_player_names(self):
        pass
        # return (str(self.model.get_player_x()), str(self.model.get_player_o()))

    # TODO: Implement
    def get_current_turn(self):
        pass

    # TODO: Implement
    def set_current_turn(self, player_num):
        pass
        # self.model.game_status = side+"_TURN"

    # TODO: Implement
    def advance_turn(self):
        pass
        # if self.model.game_status == X_TURN:
        #     self.model.game_status = O_TURN
        # else:
        #     self.model.game_status = X_TURN

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
