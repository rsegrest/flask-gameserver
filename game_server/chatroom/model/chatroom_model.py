import json
from game_server.general.model.user_model import UserModel
# from chatroom.model import EMPTY, X, O
# from chatroom.model import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW

class ChatroomModel():

    def __init__(
        self,
        user_list = None,
        message_list = None,
        room_list = None,
        private_message_list = None
    ):
        if (user_list is None):
            self.user_list = []
        else:
            self.user_list = user_list
        if (message_list is None):
            self.message_list = []
        else:
            self.message_list = message_list
        if (room_list is None):
            self.room_list = []
        else:
            self.room_list = room_list
        if (private_message_list is None):
            self.private_message_list = []
        else:
            self.private_message_list = private_message_list

    # def name(self):
    #     return ("%s %s" % (self.x_player_name,self.o_player_name))

    def get_pms_by_user(self, user):
        pass
    
    def get_messages_by_room(self, room):
        pass

    def set_board(self, board):
        self.board = board

    def start_game(self):
        self.game_started = True
    
    def end_game(self):
        self.game_started = False

    def get_board(self):
        return self.board

    def get_room(self):
        return self.room
    
    def set_room(self, roomname):
        self.room = roomname

    
if __name__ == "__main__":
    chatroom = ChatroomModel()
    # chatroom.print_board()
    pass