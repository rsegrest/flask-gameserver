import random
from datetime import datetime

class ServerSessionModel():

    def __init__(self):
        self.room_list = ['room1', 'room2', 'room3']
        self.game_types_list = [
            'TicTacToe',
            'Connect Four',
            'Yahtzee',
            'Poker',
            'Blackjack'
        ]

    def get_game_types_list(self):
        return self.game_types_list

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        output_string = 'Server State: '
        # output_string = "Room Name: " + self.room_name + "\n\tGame Type: " + str(self.game_type)
        # output_string += "\n\tCreation Time: " + str(self.creation_time)
        # if self.start_time is not None:
        #     output_string += "\n\tStart Time: " + str(self.start_time)
        # if self.completion_time is not None:
        #     output_string += "\n\tCompletion Time: " + str(self.completion_time)
        # output_string += "\n\tGame Session State: " + str(self.get_game_session_state())
        # output_string += "\n\tPlayer List: " + str(self.player_list)
        return output_string

if __name__ == "__main__":
    server_state = ServerSessionModel()
    pass