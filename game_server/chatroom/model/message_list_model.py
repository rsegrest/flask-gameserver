import json
# from chatroom.model import EMPTY, X, O
# from chatroom.model import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW
from chatroom.__fixtures__.sampledata import get_sample_message_list

class MessageListModel():

    def __init__(
        self,
        # user_id,
        # user_name,
        # content,
        # room,
        # is_private = False,
        # to_user = None,
        # user_list = None,
        # message_list = None,
        # room_list = None,
        # private_message_list = None
    ):
        self.message_list = [{
            'room1': []
        }]
        self.initialize_with_sample_data()

    def initialize_with_sample_data(self):
        self.message_list[0]['room1'].append(get_sample_message_list())

    def get_message_list(self):
        message_count = len(self.message_list[0]['room1'][0])
        message_array = []
        print('count is:')
        print(message_count)
        for i in range(message_count):
            a_msg = self.message_list[0]['room1'][0][i]
            print('a_msg is:'+str(a_msg.convert_to_json()))
            message_array.append(str(a_msg.convert_to_json()))
        # print('returning message_array:')
        return message_array
            


if __name__ == "__main__":
    message = MessageListModel()
    # message.print_board()
    pass