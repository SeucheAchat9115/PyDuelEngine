from pyduelengine.phase.phases import GamePhase
from pyduelengine.player.playerstate import PlayerState

class GameState:
    """
    Holds the complete gamestate, including both players and shared zones.
    """
    def __init__(
        self,
        player_1_name: str,
        player_1_deck_list: str,
        player_2_name: str,
        player_2_deck_list: str
    ) -> None:
        """Initializes the GameState with two players.

        Args:
            player_1_name (str): The name of player 1.
            player_1_deck_list (str): The deck list of player 1.
            player_2_name (str): The name of player 2.
            player_2_deck_list (str): The deck list of player 2.
        """

        self.player_1_state = PlayerState(
            name=player_1_name,
            deck_list=player_1_deck_list
        )
        self.player_2_state = PlayerState(
            name=player_2_name,
            deck_list=player_2_deck_list
        )

        # Initialize the game phase and current player
        self.current_phase = GamePhase.DRAW
        self.current_player = self.player_1_state.name
        self.non_current_player = self.player_2_state.name
        self.current_turn = 1