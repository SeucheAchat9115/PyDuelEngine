from typing import TYPE_CHECKING
from pyduelengine.phase.phases import GamePhase

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState

class PhaseManager:
    def __init__(
        self, 
        game_state: "GameState"
    ):
        """Initializes the PhaseManager with the current GameState.
        Args:
            game_state (GameState): The current state of the game.
        """
        self.game_state = game_state

    def advance_phase(self) -> None:
        """Advances the game to the next phase."""

        print(f"Advancing from phase: {self.game_state.current_phase.name}")
        if self.game_state.current_phase == GamePhase.END:
            self.game_state.current_phase = GamePhase.DRAW
            self.game_state.current_turn += 1
            self.game_state.current_player = (
                self.game_state.player_1 
                if self.game_state.current_player == self.game_state.player_2 
                else self.game_state.player_2
            )
        else:
            self.game_state.current_phase = GamePhase(self.game_state.current_phase.value + 1)
        print(f"New phase: {self.game_state.current_phase.name}")