from typing import TYPE_CHECKING
import random

from pyduelengine.constants import LOCATIONS

if TYPE_CHECKING:
    from pyduelengine.player.player import Player
    from pyduelengine.action.action import Action
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.game.chain_manager import ChainManager

class RandomAgent():
    """An agent that makes random valid moves."""

    def __init__(self, player: "Player"):
        self.player = player

    def choose_action(self, valid_actions: list["Action"]) -> "Action":
        """Chooses a random action from the list of valid actions.

        Args:
            valid_actions (list[Action]): A list of valid actions.
        """
        return random.choice(valid_actions)