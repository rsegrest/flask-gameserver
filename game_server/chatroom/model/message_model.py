import datetime
import json
# from chatroom.model import EMPTY, X, O
# from chatroom.model import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW


class MessageModel():

    def __init__(
        self,
        user_id,
        user_name,
        content,
        room,
        is_private = False,
        to_user = None,
        timestamp = None
        # user_list = None,
        # message_list = None,
        # room_list = None,
        # private_message_list = None
    ):
        self.user_id = user_id
        self.user_name = user_name
        self.content = content
        self.room = room
        if (is_private):
            self.is_private = True
            self.to_user = to_user
        if (timestamp is None):
            self.timestamp = datetime.datetime.now()
        else:
            self.timestamp = timestamp
    
    # def name(self):
    #     return ("%s %s" % (self.x_player_name,self.o_player_name))

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def get_content(self):
        return self.content

    def get_room(self):
        return self.room
    
    def get_is_private(self):
        return self.is_private

    def get_to_user(self):
        return self.to_user
    
    # TODO: Handle single and double quotes in content
    def convert_to_json(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "content": self.content,
            "timestamp": str(self.timestamp)
        }

if __name__ == "__main__":
    message = MessageModel()
    # message.print_board()
    pass