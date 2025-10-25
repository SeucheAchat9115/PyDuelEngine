from enum import Enum

class GamePhase(Enum):
    DRAW = 1
    STANDBY = 2
    MAIN1 = 3
    BATTLE = 4
    MAIN2 = 5
    END = 6