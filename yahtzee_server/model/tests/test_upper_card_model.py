from model.upper_card_model import UpperCardModel as ucm
from model.yahtzee_model import YahtzeeModel
# from flask-gameserver.yahtzee_server.model.lower_card_model import LowerCardModel
# from constants.spacestates import EMPTY, X, O
def func(x):
    return x + 1

class TestUpperCardModel:
    # def test_board(self):
    #     assert True
    def test_answer(self):
        assert func(4) == 5
    
    def test_calculate_ones_box_score(self):
        set_one = [1,2,3,4,5]
        set_two = [1,1,3,4,5]
        set_three = [2,2,3,3,5]
        set_four = [1,1,3,3,3]
        set_five = [6,6,6,6,3]
        set_six = [5,1,1,1,1]

        # is_result_zero = lcm
        set_one_result = ucm.calculate_ones_box_score(set_one)
        set_two_result = ucm.calculate_ones_box_score(set_two)
        set_three_result = ucm.calculate_ones_box_score(set_three)
        set_four_result = ucm.calculate_ones_box_score(set_four)
        set_five_result = ucm.calculate_ones_box_score(set_five)
        set_six_result = ucm.calculate_ones_box_score(set_six)
        
        assert set_one_result == 1
        assert set_two_result == 2
        assert set_three_result == 0
        assert set_four_result == 2
        assert set_five_result == 0
        assert set_six_result == 4

    def test_twos_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_threes = [1,1,3,3,3]
        four_twos = [2,2,2,2,3]
        five_twos = [2,2,2,2,2]

        # is_result_zero = lcm
        is_result_zero = ucm.calculate_twos_box_score(zero_matches)
        pair_is_result_zero = ucm.calculate_twos_box_score(two_ones)
        two_pair_is_result_zero = ucm.calculate_twos_box_score(two_pairs)
        three_threes_result = ucm.calculate_twos_box_score(three_threes)
        four_twos_result = ucm.calculate_twos_box_score(four_twos)
        five_twos_result = ucm.calculate_twos_box_score(five_twos)
        
        assert is_result_zero == 2
        assert pair_is_result_zero == 0
        assert two_pair_is_result_zero == 4
        assert three_threes_result == 0
        assert four_twos_result == 8
        assert five_twos_result == 10

    def test_threes_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_threes = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        is_result_zero = ucm.calculate_threes_box_score(zero_matches)
        pair_is_result_zero = ucm.calculate_threes_box_score(two_ones)
        two_pair_is_result_zero = ucm.calculate_threes_box_score(two_pairs)
        three_threes_result = ucm.calculate_threes_box_score(three_threes)
        four_sixes_result = ucm.calculate_threes_box_score(four_sixes)
        five_fives_result = ucm.calculate_threes_box_score(five_fives)
        
        assert is_result_zero == 3
        assert pair_is_result_zero == 3
        assert two_pair_is_result_zero == 6
        assert three_threes_result == 9
        assert four_sixes_result == 3
        assert five_fives_result == 0
    
    def test_calculate_fours_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_fours = [1,1,4,4,4]
        four_fours = [4,4,4,4,3]
        five_fives = [5,5,5,5,5]
        five_fours = [4,4,4,4,4]

        # is_result_zero = lcm
        is_result_zero = ucm.calculate_fours_box_score(zero_matches)
        pair_is_result_zero = ucm.calculate_fours_box_score(two_ones)
        two_pair_is_result_zero = ucm.calculate_fours_box_score(two_pairs)
        three_fours_result = ucm.calculate_fours_box_score(three_fours)
        four_fours_result = ucm.calculate_fours_box_score(four_fours)
        five_fives_result = ucm.calculate_fours_box_score(five_fives)
        five_fours_result = ucm.calculate_fours_box_score(five_fours)

        assert is_result_zero == 4
        assert pair_is_result_zero == 4
        assert two_pair_is_result_zero == 0
        assert three_fours_result == 12
        assert four_fours_result == 16
        assert five_fives_result == 0
        assert five_fours_result == 20
    
    def test_calculate_fives_box_score(self):
        zero_matches = [1,2,3,4,5]
        two_ones = [1,1,3,4,5]
        two_pairs = [2,2,3,3,5]
        three_threes = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        is_result_zero = ucm.calculate_fives_box_score(zero_matches)
        pair_is_result_zero = ucm.calculate_fives_box_score(two_ones)
        two_pair_is_result_zero = ucm.calculate_fives_box_score(two_pairs)
        three_threes_result = ucm.calculate_fives_box_score(three_threes)
        four_sixes_result = ucm.calculate_fives_box_score(four_sixes)
        five_fives_result = ucm.calculate_fives_box_score(five_fives)
        
        assert is_result_zero == 5
        assert pair_is_result_zero == 5
        assert two_pair_is_result_zero == 5
        assert three_threes_result == 0
        assert four_sixes_result == 0
        assert five_fives_result == 25
    
    def test_calculate_sixes_box_score(self):
        large_straight = [1,2,3,4,5]
        small_straight = [1,3,4,5,6]
        two_pairs = [2,2,3,3,5]
        full_house = [1,1,3,3,3]
        four_sixes = [6,6,6,6,3]
        five_fives = [5,5,5,5,5]

        # is_result_zero = lcm
        large_straight_result = ucm.calculate_sixes_box_score(large_straight)
        small_straight_result = ucm.calculate_sixes_box_score(small_straight)
        two_pair_is_result_zero = ucm.calculate_sixes_box_score(two_pairs)
        full_house_result = ucm.calculate_sixes_box_score(full_house)
        four_sixes_result = ucm.calculate_sixes_box_score(four_sixes)
        five_fives_result = ucm.calculate_sixes_box_score(five_fives)
        
        assert large_straight_result == 0
        assert small_straight_result == 6
        assert two_pair_is_result_zero == 0
        assert full_house_result == 0
        assert four_sixes_result == 24
        assert five_fives_result == 0

    # def test_calculate_score(self):
    #     total = 0
    #     total += self.calculate_ones_box_score()
    #     total += self.calculate_twos_box_score()
    #     total += self.calculate_threes_box_score()
    #     total += self.calculate_fours_box_score()
    #     total += self.calculate_fives_box_score()
    #     total += self.calculate_sixes_box_score()
    #     return total

    def test_str(self):
        pass
