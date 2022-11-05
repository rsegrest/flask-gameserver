# from constants.gamestates import NOT_STARTED
# import json

class RollModel(object):

    # def __new__(cls, *args, **kwargs):
    #     print("1. Create a new instance of Point.")
    #     return super().__new__(cls)
 
    def __init__(self, roll_value_array):
        # print("2. Initialize the new instance of Point.")
        self.roll_value_array = roll_value_array

    # def __repr__(self) -> str:
    #     return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        return self.roll_value_array.__str__()
    
if __name__ == "__main__":
    roll = RollModel([1,2,3,4,5])
    print(str(roll))
    pass