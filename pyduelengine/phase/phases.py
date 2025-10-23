from enum import Enum

class GamePhase(Enum):
    DRAW = 1
    STANDBY = 2
    MAIN1 = 3
    BATTLE = 4
    MAIN2 = 5
    END = 6

PHASE_ORDER = [
    GamePhase.DRAW,
    GamePhase.STANDBY,
    GamePhase.MAIN1,    
    GamePhase.BATTLE,
    GamePhase.MAIN2,    
    GamePhase.END
]