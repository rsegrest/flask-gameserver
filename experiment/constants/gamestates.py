from enum import Enum
class GameStates(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    DRAW = 2
    X_WON = 3
    O_WON = 4