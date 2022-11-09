from generic.model.cards import Card


# from constants.spacestates import EMPTY, X, O
def func(x):
    return x + 1

class TestCard:
    # def test_board(self):
    #     assert True
    def test_answer(self):
        assert func(4) == 5
    
    # Test 
    def test_init(self):
        pass
        # d = dice.Dice(10,2)
        # assert d.num_dice == 2
        # assert d.num_sides == 10

    def test_str(self):
        pass
        # d = dice.Dice(6,5)
        # assert str(d) == "5d6"
