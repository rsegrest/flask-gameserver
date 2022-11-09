import random
from datetime import datetime

class GameSessionModel():

    def __init__(self, room_name, game_type, player_list=[]):
        self.room_name = room_name
        self.game_type = game_type
        self.player_list = player_list
        self.creation_time = datetime.now()
        self.start_time = None
        self.completion_time = None

    def start_game(self):
        if self.start_time is None:
            self.start_time = datetime.now()

    def end_game(self):
        if self.completion_time is None:
            self.completion_time = datetime.now()

    def add_player(self, player):
        self.player_list.append(player)

    def get_room_name(self):
        return self.room_name

    def get_game_type(self):
        return self.game_type

    def get_player_list(self):
        return self.player_list

    def get_creation_time(self):
        return self.creation_time

    def get_start_time(self):
        return self.start_time

    def get_completion_time(self):
        return self.completion_time

    def get_game_session_state(self):
        if self.start_time is None:
            return "Not Started"
        if self.completion_time is None:
            return "In Progress"
        else:
            return "Completed"
    
    def is_joinable(self):
        return self.get_game_session_state() == "Not Started"

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        output_string = "Room Name: " + self.room_name + "\n\tGame Type: " + str(self.game_type)
        output_string += "\n\tCreation Time: " + str(self.creation_time)
        if self.start_time is not None:
            output_string += "\n\tStart Time: " + str(self.start_time)
        if self.completion_time is not None:
            output_string += "\n\tCompletion Time: " + str(self.completion_time)
        output_string += "\n\tGame Session State: " + str(self.get_game_session_state())
        output_string += "\n\tPlayer List: " + str(self.player_list)
        return output_string

if __name__ == "__main__":
    user = GameSessionModel()
    pass