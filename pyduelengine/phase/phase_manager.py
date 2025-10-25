from __future__ import annotations
from typing import TYPE_CHECKING
from pyduelengine.phase.phases import GamePhase

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState

class PhaseManager:
    def __init__(self, gamestate: GameState):
        """Initializes the PhaseManager with the current GameState.
        
        Args:
            gamestate (GameState): The current state of the game.
        """
        self.gamestate = gamestate

    def start_turn(self) -> None:
        """Starts a new turn by setting the phase to DRAW."""
        print(f"Starting turn {self.gamestate.turn_count} for {self.gamestate.current_player.name}")
        self.gamestate.current_phase = GamePhase.DRAW

    def progress_phase(self) -> None:
        """Progresses the game to the next phase."""
        current_phase = self.gamestate.current_phase
        if current_phase == GamePhase.DRAW:
            print(f"Progressing from {current_phase} to {GamePhase.STANDBY}")
            self.gamestate.current_phase = GamePhase.STANDBY
        elif current_phase == GamePhase.STANDBY:
            print(f"Progressing from {current_phase} to {GamePhase.MAIN1}")
            self.gamestate.current_phase = GamePhase.MAIN1
        elif current_phase == GamePhase.MAIN1:
            print(f"Progressing from {current_phase} to {GamePhase.BATTLE}")
            self.gamestate.current_phase = GamePhase.BATTLE
        elif current_phase == GamePhase.BATTLE:
            print(f"Progressing from {current_phase} to {GamePhase.MAIN2}")
            self.gamestate.current_phase = GamePhase.MAIN2
        elif current_phase == GamePhase.MAIN2:
            print(f"Progressing from {current_phase} to {GamePhase.END}")
            self.gamestate.current_phase = GamePhase.END
        elif current_phase == GamePhase.END:
            self.end_turn()

    def end_turn(self) -> None:
        """Ends the current turn and switches to the next player."""
        print(f"Ending turn {self.gamestate.turn_count} for {self.gamestate.current_player.name}")
        if self.gamestate.current_player == self.gamestate.player_1:
            self.gamestate.current_player = self.gamestate.player_2
        else:
            self.gamestate.current_player = self.gamestate.player_1
        self.gamestate.turn_count += 1