from enum import Enum

class GamePhase(Enum):
    DRAW = "Draw"
    STANDBY = "Standby"
    MAIN1 = "Main1"
    BATTLE = "Battle"
    MAIN2 = "Main2"
    END = "End"

PHASE_ORDER = [
    GamePhase.DRAW,
    GamePhase.STANDBY,
    GamePhase.MAIN1,    
    GamePhase.BATTLE,
    GamePhase.MAIN2,    
    GamePhase.END
]