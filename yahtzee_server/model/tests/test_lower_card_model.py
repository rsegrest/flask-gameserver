from model.lower_card_model import LowerCardModel
from model.yahtzee_model import YahtzeeModel
# from flask-gameserver.yahtzee_server.model.lower_card_model import LowerCardModel
# from constants.spacestates import EMPTY, X, O
def func(x):
    return x + 1

class TestLowerCardModel:
    # def test_board(self):
    #     assert True
    def test_answer(self):
        assert func(4) == 5
    
    def test_calculate_three_of_a_kind_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_threes = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        is_result_zero = LowerCardModel.calculate_three_of_a_kind_box_score(zero_matches)
        pair_is_result_zero = LowerCardModel.calculate_three_of_a_kind_box_score(two_ones)
        two_pair_is_result_zero = LowerCardModel.calculate_three_of_a_kind_box_score(two_pairs)
        three_threes_result = LowerCardModel.calculate_three_of_a_kind_box_score(three_threes)
        four_sixes_result = LowerCardModel.calculate_three_of_a_kind_box_score(four_sixes)
        five_fives_result = LowerCardModel.calculate_three_of_a_kind_box_score(five_fives)
        
        assert is_result_zero == 0
        assert pair_is_result_zero == 0
        assert two_pair_is_result_zero == 0
        assert three_threes_result == 11
        assert four_sixes_result == 27
        assert five_fives_result == 25

    def test_calculate_four_of_a_kind_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_threes = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        is_result_zero = LowerCardModel.calculate_four_of_a_kind_box_score(zero_matches)
        pair_is_result_zero = LowerCardModel.calculate_four_of_a_kind_box_score(two_ones)
        two_pair_is_result_zero = LowerCardModel.calculate_four_of_a_kind_box_score(two_pairs)
        three_threes_result = LowerCardModel.calculate_four_of_a_kind_box_score(three_threes)
        four_sixes_result = LowerCardModel.calculate_four_of_a_kind_box_score(four_sixes)
        five_fives_result = LowerCardModel.calculate_four_of_a_kind_box_score(five_fives)
        
        assert is_result_zero == 0
        assert pair_is_result_zero == 0
        assert two_pair_is_result_zero == 0
        assert three_threes_result == 0
        assert four_sixes_result == 27
        assert five_fives_result == 25

    def test_calculate_yahtzee_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_threes = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        is_result_zero = LowerCardModel.calculate_yahtzee_box_score(zero_matches)
        pair_is_result_zero = LowerCardModel.calculate_yahtzee_box_score(two_ones)
        two_pair_is_result_zero = LowerCardModel.calculate_yahtzee_box_score(two_pairs)
        three_threes_result = LowerCardModel.calculate_yahtzee_box_score(three_threes)
        four_sixes_result = LowerCardModel.calculate_yahtzee_box_score(four_sixes)
        five_fives_result = LowerCardModel.calculate_yahtzee_box_score(five_fives)
        
        assert is_result_zero == 0
        assert pair_is_result_zero == 0
        assert two_pair_is_result_zero == 0
        assert three_threes_result == 0
        assert four_sixes_result == 0
        assert five_fives_result == 50
    
    def test_calculate_chance_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_threes = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        is_result_zero = LowerCardModel.calculate_chance_box_score(zero_matches)
        pair_is_result_zero = LowerCardModel.calculate_chance_box_score(two_ones)
        two_pair_is_result_zero = LowerCardModel.calculate_chance_box_score(two_pairs)
        three_threes_result = LowerCardModel.calculate_chance_box_score(three_threes)
        four_sixes_result = LowerCardModel.calculate_chance_box_score(four_sixes)
        five_fives_result = LowerCardModel.calculate_chance_box_score(five_fives)
        
        assert is_result_zero == 15
        assert pair_is_result_zero == 14
        assert two_pair_is_result_zero == 15
        assert three_threes_result == 11
        assert four_sixes_result == 27
        assert five_fives_result == 25
    
    def test_calculate_full_house_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        full_house = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        is_result_zero = LowerCardModel.calculate_full_house_box_score(zero_matches)
        pair_is_result_zero = LowerCardModel.calculate_full_house_box_score(two_ones)
        two_pair_is_result_zero = LowerCardModel.calculate_full_house_box_score(two_pairs)
        full_house_result = LowerCardModel.calculate_full_house_box_score(full_house)
        four_sixes_result = LowerCardModel.calculate_full_house_box_score(four_sixes)
        five_fives_result = LowerCardModel.calculate_full_house_box_score(five_fives)
        
        assert is_result_zero == 0
        assert pair_is_result_zero == 0
        assert two_pair_is_result_zero == 0
        assert full_house_result == 25
        assert four_sixes_result == 0
        assert five_fives_result == 0
    
    def test_calculate_small_straight_box_score(self):
        large_straight = [1,2,3,4,5]
        small_straight = [1,3,4,5,6]
        two_pairs = [2,2,3,3,5]
        full_house = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        large_straight_result = LowerCardModel.calculate_small_straight_box_score(large_straight)
        small_straight_result = LowerCardModel.calculate_small_straight_box_score(small_straight)
        two_pair_is_result_zero = LowerCardModel.calculate_small_straight_box_score(two_pairs)
        full_house_result = LowerCardModel.calculate_small_straight_box_score(full_house)
        four_sixes_result = LowerCardModel.calculate_small_straight_box_score(four_sixes)
        five_fives_result = LowerCardModel.calculate_small_straight_box_score(five_fives)
        
        assert large_straight_result == 30
        assert small_straight_result == 30
        assert two_pair_is_result_zero == 0
        assert full_house_result == 0
        assert four_sixes_result == 0
        assert five_fives_result == 0
    
    def test_calculate_large_straight_box_score(self):
        large_straight = [1,2,3,4,5]
        small_straight = [1,3,4,5,6]
        two_pairs = [2,2,3,3,5]
        full_house = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        large_straight_result = LowerCardModel.calculate_large_straight_box_score(large_straight)
        small_straight_result = LowerCardModel.calculate_large_straight_box_score(small_straight)
        two_pair_is_result_zero = LowerCardModel.calculate_large_straight_box_score(two_pairs)
        full_house_result = LowerCardModel.calculate_large_straight_box_score(full_house)
        four_sixes_result = LowerCardModel.calculate_large_straight_box_score(four_sixes)
        five_fives_result = LowerCardModel.calculate_large_straight_box_score(five_fives)
        
        assert large_straight_result == 40
        assert small_straight_result == 0
        assert two_pair_is_result_zero == 0
        assert full_house_result == 0
        assert four_sixes_result == 0
        assert five_fives_result == 0


    def test_calculate_score(self):
        large_straight = [1,2,3,4,5]
        small_straight = [1,3,4,5,6]
        two_pairs = [2,2,3,3,5]
        full_house = [1,1,3,3,3]
        yahtzee = [6,6,6,6,6]
        four_sixes = [6,6,6,6,3]
        three_threes = [3,3,3,6,5]
        chance = [6,4,3,5,5]

        lcm = LowerCardModel()
        lcm.large_straight_box = large_straight
        lcm.small_straight_box = small_straight
        lcm.two_pairs_box = two_pairs
        lcm.full_house_box = full_house
        lcm.yahtzee_box = yahtzee
        lcm.four_of_a_kind_box = four_sixes
        lcm.three_of_a_kind_box = three_threes
        lcm.chance_box = chance

        assert lcm.calculate_score() == 175
    
    # This test isn't running?
    def test_str(self):
        large_straight = [1,2,3,4,5]
        small_straight = [1,3,4,5,6]
        two_pairs = [2,2,3,3,5]
        full_house = [1,1,3,3,3]
        yahtzee = [6,6,6,6,6]
        four_sixes = [6,6,6,6,3]
        three_threes = [3,3,3,6,5]
        chance = [6,4,3,5,5]

        lcm = LowerCardModel()
        lcm.large_straight_box = large_straight
        lcm.small_straight_box = small_straight
        lcm.two_pairs_box = two_pairs
        lcm.full_house_box = full_house
        lcm.yahtzee_box = yahtzee
        lcm.four_of_a_kind_box = four_sixes
        lcm.three_of_a_kind_box = three_threes
        lcm.chance_box = chance

        # assert str(lcm) == 'Lower Card:\n\n \n\n 3 of a Kind: [3, 3, 3, 6, 5]\n\n 4 of a Kind: [6, 6, 6, 6, 3]\n\n Full House: [1, 1, 3, 3, 3]\n\n Small Straight: [1, 3, 4, 5, 6]\n\n Large Straight: [1, 2, 3, 4, 5]\n\n Yahtzee: [6, 6, 6, 6, 6]\n\n Chance: [6, 4, 3, 5, 5]\n\n \n\n Total: 175'
        assert str(lcm) == 'Lower Card:\n\n3 of a Kind: [3, 3, 3, 6, 5]\n4 of a Kind: [6, 6, 6, 6, 3]\nFull House: [1, 1, 3, 3, 3]\nSmall Straight: [1, 3, 4, 5, 6]\nLarge Straight: [1, 2, 3, 4, 5]\nYahtzee: [6, 6, 6, 6, 6]\nChance: [6, 4, 3, 5, 5]\n\nTotal: 175'

    # def test_str(self):
    #     pass
