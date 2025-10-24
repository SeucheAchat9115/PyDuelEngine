from typing import TYPE_CHECKING
from pyduelengine.agent.random_agent import RandomAgent

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.game.chain_manager import ChainManager
    from pyduelengine.action.action import Action

class Player():
    """
    A class representing a player in the game.
    """
    def __init__(
        self, 
        name: str,
    ) -> None:
        """Initializes a Player object.
        
        Args:
            name (str): The name of the player.
        """

        self.name = name
        self.agent = RandomAgent(self)

    def get_valid_actions(
        self, 
        game_state: "GameState",
        chain_manager: "ChainManager"
    ) -> list["Action"]:
        """Returns a list of valid actions for the player based on the game state and chain manager.

        Args:
            game_state (GameState): The current state of the game.
            chain_manager (ChainManager): The manager responsible for handling action chains.

        Returns:
            list[Action]: A list of valid actions for the player.
        """
        valid_actions = self.agent.get_valid_actions(game_state, chain_manager)
        return valid_actions