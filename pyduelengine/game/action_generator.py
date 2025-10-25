from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.player.player import Player
    from pyduelengine.action.action import Action
    
from pyduelengine.action.pass_priority import PassPriorityAction
from pyduelengine.action.phase_progress import ProgressPhaseAction

class ActionGenerator:
    """Generates possible actions for players based on the current game state."""
    def __init__(
        self,
        gamestate: GameState,
    ):
        pass
    
    def get_legal_actions(
        self, 
        player: Player
    ) -> list[Action]:
        """Generates a list of legal actions for the given player."""
        legal_actions = []
        # Always add the option to progress to the next phase
        legal_actions.append(ProgressPhaseAction(owner=player))
        return legal_actions

    def get_chain_responses(
        self,
        player: Player
    ) -> list[Action]:
        """Generates a list of legal chain responses for the given player."""
        legal_actions = []
        # Always add the option to pass priority
        legal_actions.append(PassPriorityAction(owner=player))
        return legal_actions

    def process_action(
        self,
        player: Player,
        action: Action
    ) -> None:
        """Processes the given action for the player."""
        pass