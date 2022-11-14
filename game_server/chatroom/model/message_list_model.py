import json
# from chatroom.model import EMPTY, X, O
# from chatroom.model import NOT_STARTED, X_TURN, O_TURN, X_WON, O_WON, DRAW
from chatroom.__fixtures__.sampledata import get_sample_message_list
from chatroom.model.message_model import MessageModel as Message
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
        for i in range(message_count):
            a_msg = self.message_list[0]['room1'][0][i]
            message_array.append(str(a_msg.convert_to_json()))
        # print('returning message_array:')
        return message_array
    
    def add_message(self, username, content):
        msg = Message(user_id=0, user_name=username, content=content, room='room1')
        self.message_list[0]['room1'][0].append(msg)
        print('message_list is now : ')
        for i in range(len(self.message_list[0]['room1'][0])):
            print(self.message_list[0]['room1'][0][i].convert_to_json())
        return
    
    def output(self):
        output_str = ''
        num_msgs = len(self.message_list[0]['room1'][0])
        for i in range(num_msgs):
            output_str += str(self.message_list[0]['room1'][0][i]) + '\n'
        return output_str
    
    def __str__(self) -> str:
        output_str = ''
        num_msgs = len(self.message_list[0]['room1'][0])
        for i in range(num_msgs):
            output_str += str(self.message_list[0]['room1'][0][i].convert_to_json()) + '\n'
        return output_str

if __name__ == "__main__":
    message = MessageListModel()
    # message.print_board()
    pass