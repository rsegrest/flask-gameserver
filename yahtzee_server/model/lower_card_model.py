from model.yahtzee_model import YahtzeeModel
# from constants.gamestates import NOT_STARTED
# import json

class LowerCardModel(object):

# Three Of A Kind	At least three dice the same	Sum of all dice	Dice-2.svgDice-3.svgDice-4.svgDice-4.svgDice-4.svg scores 17
# Four Of A Kind	At least four dice the same	Sum of all dice	Dice-4.svgDice-5.svgDice-5.svgDice-5.svgDice-5.svg scores 24
# Full House	Three of one number and two of another	25	Dice-2.svgDice-2.svgDice-5.svgDice-5.svgDice-5.svg scores 25
# Small Straight	Four sequential dice
# (1-2-3-4, 2-3-4-5, or 3-4-5-6)	30	Dice-1.svgDice-3.svgDice-4.svgDice-5.svgDice-6a.svg scores 30
# Large Straight	Five sequential dice
# (1-2-3-4-5 or 2-3-4-5-6)	40	Dice-1.svgDice-2.svgDice-3.svgDice-4.svgDice-5.svg scores 40
# Yahtzee	All five dice the same	50	Dice-3.svgDice-3.svgDice-3.svgDice-3.svgDice-3.svg scores 50
# Chance	Any combination	Sum of all dice	Dice-1.svgDice-1.svgDice-3.svgDice-4.svgDice-5.svg scores 14

    # def __new__(cls, *args, **kwargs):
    #     print("1. Create a new instance of Point.")
    #     return super().__new__(cls)
 
    def __init__(self):
        self.three_of_a_kind_box = None
        self.four_of_a_kind_box = None
        self.full_house_box = None
        self.small_straight_box = None
        self.large_straight_box = None
        self.yahtzee_box = None
        self.chance_box = None

        # print("2. Initialize the new instance of Point.")
        # self.roll_value_array = roll_value_array

    # def __repr__(self) -> str:
    #     return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def save_roll_as_three_of_a_kind(self, roll):
        self.three_of_a_kind_box = roll
    
    def save_roll_as_four_of_a_kind(self, roll):
        self.four_of_a_kind_box = roll
    
    def save_roll_as_full_house(self, roll):
        self.full_house_box = roll
    
    def save_roll_as_small_straight(self, roll):
        self.small_straight_box = roll
    
    def save_roll_as_large_straight(self, roll):
        self.large_straight_box = roll
    
    def save_roll_as_yahtzee(self, roll):
        self.yahtzee_box = roll
    
    def save_roll_as_chance(self, roll):
        self.chance_box = roll

    @staticmethod
    def calculate_three_of_a_kind_box_score(roll):
        if YahtzeeModel.has_three_of_a_kind(roll):
            return sum(roll)
        return 0

    @staticmethod
    def calculate_four_of_a_kind_box_score(roll):
        if YahtzeeModel.has_four_of_a_kind(roll):
            return sum(roll)
        return 0

    @staticmethod
    def calculate_yahtzee_box_score(roll):
        if YahtzeeModel.has_yahtzee(roll):
            return 50
        return 0

    @staticmethod
    def calculate_chance_box_score(roll):
        return sum(roll)

    @staticmethod
    def calculate_full_house_box_score(roll):
        if YahtzeeModel.has_full_house(roll):
            return 25
        return 0

    @staticmethod
    def calculate_small_straight_box_score(roll):
        if YahtzeeModel.has_small_straight(roll):
            return 30
        return 0

    @staticmethod
    def calculate_large_straight_box_score(roll):
        if YahtzeeModel.has_large_straight(roll):
            return 40
        return 0

    def calculate_score(self):
        total = 0
        total += LowerCardModel.calculate_three_of_a_kind_box_score(self.three_of_a_kind_box)
        total += LowerCardModel.calculate_four_of_a_kind_box_score(self.four_of_a_kind_box)
        total += LowerCardModel.calculate_yahtzee_box_score(self.yahtzee_box)
        total += LowerCardModel.calculate_chance_box_score(self.chance_box)
        total += LowerCardModel.calculate_full_house_box_score(self.full_house_box)
        total += LowerCardModel.calculate_small_straight_box_score(self.large_straight_box)
        total += LowerCardModel.calculate_large_straight_box_score(self.small_straight_box)
        return total

    def __str__(self):
    #     pass
        return "LowerCardModel"
    
if __name__ == "__main__":
    lcm = LowerCardModel()
    print(str(lcm))
    pass