from model.lower_card_model import LowerCardModel as lcm
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
        is_result_zero = lcm.calculate_three_of_a_kind_box_score(zero_matches)
        pair_is_result_zero = lcm.calculate_three_of_a_kind_box_score(two_ones)
        two_pair_is_result_zero = lcm.calculate_three_of_a_kind_box_score(two_pairs)
        three_threes_result = lcm.calculate_three_of_a_kind_box_score(three_threes)
        four_sixes_result = lcm.calculate_three_of_a_kind_box_score(four_sixes)
        five_fives_result = lcm.calculate_three_of_a_kind_box_score(five_fives)
        
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
        is_result_zero = lcm.calculate_four_of_a_kind_box_score(zero_matches)
        pair_is_result_zero = lcm.calculate_four_of_a_kind_box_score(two_ones)
        two_pair_is_result_zero = lcm.calculate_four_of_a_kind_box_score(two_pairs)
        three_threes_result = lcm.calculate_four_of_a_kind_box_score(three_threes)
        four_sixes_result = lcm.calculate_four_of_a_kind_box_score(four_sixes)
        five_fives_result = lcm.calculate_four_of_a_kind_box_score(five_fives)
        
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
        is_result_zero = lcm.calculate_yahtzee_box_score(zero_matches)
        pair_is_result_zero = lcm.calculate_yahtzee_box_score(two_ones)
        two_pair_is_result_zero = lcm.calculate_yahtzee_box_score(two_pairs)
        three_threes_result = lcm.calculate_yahtzee_box_score(three_threes)
        four_sixes_result = lcm.calculate_yahtzee_box_score(four_sixes)
        five_fives_result = lcm.calculate_yahtzee_box_score(five_fives)
        
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
        is_result_zero = lcm.calculate_chance_box_score(zero_matches)
        pair_is_result_zero = lcm.calculate_chance_box_score(two_ones)
        two_pair_is_result_zero = lcm.calculate_chance_box_score(two_pairs)
        three_threes_result = lcm.calculate_chance_box_score(three_threes)
        four_sixes_result = lcm.calculate_chance_box_score(four_sixes)
        five_fives_result = lcm.calculate_chance_box_score(five_fives)
        
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
        is_result_zero = lcm.calculate_full_house_box_score(zero_matches)
        pair_is_result_zero = lcm.calculate_full_house_box_score(two_ones)
        two_pair_is_result_zero = lcm.calculate_full_house_box_score(two_pairs)
        full_house_result = lcm.calculate_full_house_box_score(full_house)
        four_sixes_result = lcm.calculate_full_house_box_score(four_sixes)
        five_fives_result = lcm.calculate_full_house_box_score(five_fives)
        
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
        large_straight_result = lcm.calculate_small_straight_box_score(large_straight)
        small_straight_result = lcm.calculate_small_straight_box_score(small_straight)
        two_pair_is_result_zero = lcm.calculate_small_straight_box_score(two_pairs)
        full_house_result = lcm.calculate_small_straight_box_score(full_house)
        four_sixes_result = lcm.calculate_small_straight_box_score(four_sixes)
        five_fives_result = lcm.calculate_small_straight_box_score(five_fives)
        
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
        large_straight_result = lcm.calculate_large_straight_box_score(large_straight)
        small_straight_result = lcm.calculate_large_straight_box_score(small_straight)
        two_pair_is_result_zero = lcm.calculate_large_straight_box_score(two_pairs)
        full_house_result = lcm.calculate_large_straight_box_score(full_house)
        four_sixes_result = lcm.calculate_large_straight_box_score(four_sixes)
        five_fives_result = lcm.calculate_large_straight_box_score(five_fives)
        
        assert large_straight_result == 40
        assert small_straight_result == 0
        assert two_pair_is_result_zero == 0
        assert full_house_result == 0
        assert four_sixes_result == 0
        assert five_fives_result == 0


    def calculate_score(self):
        total = 0
        total += self.calculate_three_of_a_kind_box_score()
        total += self.calculate_four_of_a_kind_box_score()
        total += self.calculate_yahtzee_box_score()
        total += self.calculate_chance_box_score()
        total += self.calculate_full_house_box_score()
        total += self.calculate_small_straight_box_score()
        total += self.calculate_large_straight_box_score()
        return total

    # def test_count_matches(self):
    #     zero_matches = [1,2,3,4,5]
    #     two_ones = [1,1,3,4,5]
    #     two_pairs = [2,2,3,3,5]
    #     three_threes = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     zero_matches_result = YahtzeeModel.count_matches(zero_matches)
    #     two_ones_result = YahtzeeModel.count_matches(two_ones)
    #     two_pairs_result = YahtzeeModel.count_matches(two_pairs)
    #     three_threes_result = YahtzeeModel.count_matches(three_threes)
    #     four_sixes_result = YahtzeeModel.count_matches(four_sixes)
    #     five_fives_result = YahtzeeModel.count_matches(five_fives)

    #     assert zero_matches_result == [1,1,1,1,1,0]
    #     assert two_ones_result[0] == 2
    #     assert two_pairs_result == [0,2,2,0,1,0]
    #     assert three_threes_result == [2,0,3,0,0,0]
    #     assert four_sixes_result == [0,0,1,0,0,4]
    #     assert five_fives_result == [0,0,0,0,5,0]

    # def test_max_matches(self):
    #     zero_matches = [1,2,3,4,5]
    #     two_ones = [1,1,3,4,5]
    #     two_pairs = [2,2,3,3,5]
    #     three_threes = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     zero_matches_result = YahtzeeModel.max_matches(zero_matches)
    #     two_ones_result = YahtzeeModel.max_matches(two_ones)
    #     two_pairs_result = YahtzeeModel.max_matches(two_pairs)
    #     three_threes_result = YahtzeeModel.max_matches(three_threes)
    #     four_sixes_result = YahtzeeModel.max_matches(four_sixes)
    #     five_fives_result = YahtzeeModel.max_matches(five_fives)

    #     assert zero_matches_result == 1
    #     assert two_ones_result == 2
    #     assert two_pairs_result == 2
    #     assert three_threes_result == 3
    #     assert four_sixes_result == 4
    #     assert five_fives_result == 5

    # def test_has_three_of_a_kind(self):
    #     zero_matches = [1,2,3,4,5]
    #     two_ones = [1,1,3,4,5]
    #     two_pairs = [2,2,3,3,5]
    #     three_threes = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     zero_matches_result = YahtzeeModel.has_three_of_a_kind(zero_matches)
    #     two_ones_result = YahtzeeModel.has_three_of_a_kind(two_ones)
    #     two_pairs_result = YahtzeeModel.has_three_of_a_kind(two_pairs)
    #     three_threes_result = YahtzeeModel.has_three_of_a_kind(three_threes)
    #     four_sixes_result = YahtzeeModel.has_three_of_a_kind(four_sixes)
    #     five_fives_result = YahtzeeModel.has_three_of_a_kind(five_fives)

    #     assert zero_matches_result == False
    #     assert two_ones_result == False
    #     assert two_pairs_result == False
    #     assert three_threes_result == True
    #     assert four_sixes_result == True
    #     assert five_fives_result == True

    # def test_has_four_of_a_kind(self):
    #     zero_matches = [1,2,3,4,5]
    #     two_ones = [1,1,3,4,5]
    #     two_pairs = [2,2,3,3,5]
    #     three_threes = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     zero_matches_result = YahtzeeModel.has_four_of_a_kind(zero_matches)
    #     two_ones_result = YahtzeeModel.has_four_of_a_kind(two_ones)
    #     two_pairs_result = YahtzeeModel.has_four_of_a_kind(two_pairs)
    #     three_threes_result = YahtzeeModel.has_four_of_a_kind(three_threes)
    #     four_sixes_result = YahtzeeModel.has_four_of_a_kind(four_sixes)
    #     five_fives_result = YahtzeeModel.has_four_of_a_kind(five_fives)

    #     assert zero_matches_result == False
    #     assert two_ones_result == False
    #     assert two_pairs_result == False
    #     assert three_threes_result == False
    #     assert four_sixes_result == True
    #     assert five_fives_result == True

    # def test_has_yahtzee(self):
    #     zero_matches = [1,2,3,4,5]
    #     two_ones = [1,1,3,4,5]
    #     two_pairs = [2,2,3,3,5]
    #     three_threes = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     zero_matches_result = YahtzeeModel.has_yahtzee(zero_matches)
    #     two_ones_result = YahtzeeModel.has_yahtzee(two_ones)
    #     two_pairs_result = YahtzeeModel.has_yahtzee(two_pairs)
    #     three_threes_result = YahtzeeModel.has_yahtzee(three_threes)
    #     four_sixes_result = YahtzeeModel.has_yahtzee(four_sixes)
    #     five_fives_result = YahtzeeModel.has_yahtzee(five_fives)

    #     assert zero_matches_result == False
    #     assert two_ones_result == False
    #     assert two_pairs_result == False
    #     assert three_threes_result == False
    #     assert four_sixes_result == False
    #     assert five_fives_result == True

    # def test_has_full_house(self):
    #     zero_matches = [1,2,3,4,5]
    #     two_ones = [1,1,3,4,5]
    #     two_pairs = [2,2,3,3,5]
    #     full_house = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     zero_matches_result = YahtzeeModel.has_full_house(zero_matches)
    #     two_ones_result = YahtzeeModel.has_full_house(two_ones)
    #     two_pairs_result = YahtzeeModel.has_full_house(two_pairs)
    #     full_house_result = YahtzeeModel.has_full_house(full_house)
    #     four_sixes_result = YahtzeeModel.has_full_house(four_sixes)
    #     five_fives_result = YahtzeeModel.has_full_house(five_fives)

    #     assert zero_matches_result == False
    #     assert two_ones_result == False
    #     assert two_pairs_result == False
    #     assert full_house_result == True
    #     assert four_sixes_result == False
    #     assert five_fives_result == False

    # def test_has_large_straight(self):
    #     large_straight = [1,2,3,4,5]
    #     short_straight = [1,3,4,5,6]
    #     two_pairs = [2,2,3,3,5]
    #     full_house = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     large_straight_result = YahtzeeModel.has_large_straight(large_straight)
    #     short_straight_result = YahtzeeModel.has_large_straight(short_straight)
    #     two_pairs_result = YahtzeeModel.has_large_straight(two_pairs)
    #     full_house_result = YahtzeeModel.has_large_straight(full_house)
    #     four_sixes_result = YahtzeeModel.has_large_straight(four_sixes)
    #     five_fives_result = YahtzeeModel.has_large_straight(five_fives)

    #     assert large_straight_result == True
    #     assert short_straight_result == False
    #     assert two_pairs_result == False
    #     assert full_house_result == False
    #     assert four_sixes_result == False
    #     assert five_fives_result == False

    # def test_has_short_straight(self):
    #     large_straight = [1,2,3,4,5]
    #     short_straight = [1,3,4,5,6]
    #     two_pairs = [2,2,3,3,5]
    #     full_house = [1,1,3,3,3]
    #     four_sixes = [6,6,6,6,3]
    #     five_fives = [5,5,5,5,5]

    #     large_straight_result = YahtzeeModel.has_short_straight(large_straight)
    #     short_straight_result = YahtzeeModel.has_short_straight(short_straight)
    #     two_pairs_result = YahtzeeModel.has_short_straight(two_pairs)
    #     full_house_result = YahtzeeModel.has_short_straight(full_house)
    #     four_sixes_result = YahtzeeModel.has_short_straight(four_sixes)
    #     five_fives_result = YahtzeeModel.has_short_straight(five_fives)

    #     assert large_straight_result == True
    #     assert short_straight_result == True
    #     assert two_pairs_result == False
    #     assert full_house_result == False
    #     assert four_sixes_result == False
    #     assert five_fives_result == False

    def test_str(self):
        pass
