from __future__ import annotations
from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from pyduelengine.player.player import Player
    from pyduelengine.action.action import Action
    from pyduelengine.game.gamestate import GameState

class RandomAgent():
    """An agent that makes random valid moves."""

    def __init__(
        self, 
        player: Player
    ):
        self.player = player

    def get_action(
        self, 
        gamestate: GameState,
        valid_actions: list[Action]
    ) -> Action:
        """Chooses a random action from the list of valid actions.

        Args:
            gamestate (GameState): The current state of the game.
            valid_actions (list[Action]): A list of valid actions.
        Returns:
            Action: A randomly selected action.
        """
        if not valid_actions:
            raise ValueError("No valid actions available for the agent to choose from.")

        return random.choice(valid_actions)