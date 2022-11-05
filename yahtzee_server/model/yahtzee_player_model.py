from constants.gamestates import NOT_STARTED
# import json

class YahtzeePlayerModel(object):

    def __init__(
        self,
        player_name = None,
        player_num = None,
        player_id = None,
    ):
        self.name = player_name
        self.player_num = player_num
        self.id = player_id

    def name(self):
        return ("%s %s %s" % (self.name, self.player_num, self.id))
    
    def get_name(self):
        return self.name
    
    def get_player_num(self):
        return self.player_num
    
    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name
    
    def set_id(self, x_id):
        self.x_id = x_id

    def __str__(self):
        return self.name + " " + self.player_num + " " + self.id
    # @classmethod
    # def getAll(self):
    #     pass
    
if __name__ == "__main__":
    player = YahtzeePlayerModel()
    player.print_player()
    pass