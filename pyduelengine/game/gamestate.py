from pyduelengine.game.phases import GamePhase
from pyduelengine.player.player import Player

class GameState:
    """
    Holds the complete gamestate, including both players and shared zones.
    """
    def __init__(
        self,
        player_1: Player,
        player_2: Player,
    ) -> None:
        """Initializes the GameState with two players.

        Args:
            player_1 (Player): The first player.
            player_2 (Player): The second player.
        """

        self.player_1 = player_1
        self.player_2 = player_2

        # Initialize the game phase and current player
        self.current_phase = GamePhase.DRAW
        self.current_player = self.player_1
        self.non_current_player = self.player_2
        self.current_turn = 1