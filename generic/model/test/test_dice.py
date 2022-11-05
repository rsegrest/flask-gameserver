import generic.model.dice as dice
# from constants.spacestates import EMPTY, X, O
def func(x):
    return x + 1

class TestDice:
    # def test_board(self):
    #     assert True
    def test_answer(self):
        assert func(4) == 5
    
    # Test 
    def test_init(self):
        d = dice.Dice(10,2)
        assert d.num_dice == 2
        assert d.num_sides == 10

    def test_roll(self):
        d = dice.Dice(6,5)
        result = d.roll()
        assert result['total'] >= 5
        assert result['total'] <= 30

        for i in range(5):
            assert result['rolls'][i] >= 1
            assert result['rolls'][i] <= 6
        assert len(result['rolls']) == 5

    def test_roll_result(self):
        d = dice.Dice(6,5)
        result = d.roll_result()
        assert result >= 5
        assert result <= 30

    def test_str(self):
        d = dice.Dice(6,5)
        assert str(d) == "5d6"
