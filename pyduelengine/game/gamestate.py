from pyduelengine.player.playerstate import PlayerState

class GameState:
    """
    Holds the complete gamestate, including both players and shared zones.
    """
    def __init__(self) -> None:
        """Initializes a new GameState with two players and default values."""
        self.player1 = PlayerState(name="Player 1")
        self.player2 = PlayerState(name="Player 2")

        self.turn_number = 1
        self.current_player = self.player1
        self.current_phase = "Draw"