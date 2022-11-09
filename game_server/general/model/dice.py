import random


class Dice():

    def __init__(self, num_sides=6, num_dice=1):
        self.num_sides = num_sides
        self.num_dice = num_dice
        
    def roll_result(self):
        result = 0
        for i in range(self.num_dice):
            result += random.randint(1, self.num_sides)
        return result

    def roll(self):
        result = []
        for i in range(self.num_dice):
            result.append(random.randint(1, self.num_sides))
        return {
            'rolls': result,
            'total': sum(result)
        }

    def __str__(self):
        return str(self.num_dice) + "d" + str(self.num_sides)

# if __name__ == "__main__":
#     dice = Dice()
#     pass