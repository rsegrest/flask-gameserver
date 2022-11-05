from model.yahtzee_model import YahtzeeModel
# from constants.gamestates import NOT_STARTED
# import json

class UpperCardModel(object):

    # def __new__(cls, *args, **kwargs):
    #     print("1. Create a new instance of Point.")
    #     return super().__new__(cls)
 
    def __init__(self):
        self.ones_box = None
        self.twos_box = None
        self.threes_box = None
        self.fours_box = None
        self.fives_box = None
        self.sixes_box = None

    # print("2. Initialize the new instance of Point.")
    # self.roll_value_array = roll_value_array

    # def __repr__(self) -> str:
    #     return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def save_roll_as_ones(self, roll):
        self.ones_box = roll
    
    def save_roll_as_twos(self, roll):
        self.twos_box = roll
    
    def save_roll_as_threes(self, roll):
        self.threes_box = roll
    
    def save_roll_as_fours(self, roll):
        self.fours_box = roll
    
    def save_roll_as_fives(self, roll):
        self.fives_box = roll
    
    def save_roll_as_sixes(self, roll):
        self.sixes_box = roll
    

    @staticmethod
    def calculate_ones_box_score(roll):
        counts = YahtzeeModel.count_matches(roll)
        return counts[0]*1

    @staticmethod
    def calculate_twos_box_score(roll):
        counts = YahtzeeModel.count_matches(roll)
        return counts[1]*2

    @staticmethod
    def calculate_threes_box_score(roll):
        counts = YahtzeeModel.count_matches(roll)
        return counts[2]*3
    
    @staticmethod
    def calculate_fours_box_score(roll):
        counts = YahtzeeModel.count_matches(roll)
        return counts[3]*4
    
    @staticmethod
    def calculate_fives_box_score(roll):
        counts = YahtzeeModel.count_matches(roll)
        return counts[4]*5
    
    @staticmethod
    def calculate_sixes_box_score(roll):
        counts = YahtzeeModel.count_matches(roll)
        return counts[5]*6

    def calculate_score(self):
        total = 0
        total += UpperCardModel.calculate_ones_box_score(self.ones_box)
        total += UpperCardModel.calculate_twos_box_score(self.twos_box)
        total += UpperCardModel.calculate_threes_box_score(self.threes_box)
        total += UpperCardModel.calculate_fours_box_score(self.fours_box)
        total += UpperCardModel.calculate_fives_box_score(self.fives_box)
        total += UpperCardModel.calculate_sixes_box_score(self.sixes_box)
        return total

    def __str__(self):
        return "Upper Card:\n\nOnes: {}\nTwos: {}\nThrees: {}\nFours: {}\nFives: {}\nSixes: {}\n\nTotal: {}".format(
            self.ones_box,
            self.twos_box,
            self.threes_box,
            self.fours_box,
            self.fives_box,
            self.sixes_box,
            self.calculate_score()
        )
    
    
if __name__ == "__main__":
    ucm = UpperCardModel()
    print(str(ucm))
    pass