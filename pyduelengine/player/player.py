from typing import TYPE_CHECKING

from pyduelengine.player.playerstate import PlayerState
from pyduelengine.action.action_handler import ActionHandler

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState

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
        self.action_handler = ActionHandler()

    def get_action(
        self, 
        game_state: "GameState"
    ) -> None:
        """Placeholder method for the player to take an action during their turn.
        
        Args:
            game_state: The current state of the game.
        """
        # Placeholder for player action logic
        print(f"{self.name} is taking an action.")

        possible_actions = self.action_handler.get_possible_actions(self, game_state)
        
        if len(possible_actions) == 0:
            print(f"{self.name} has no possible actions to take.")
            return

        # For now, just pick the first action
        action = possible_actions[0]  
        print(f"{self.name} performs action: {action}")

    def has_actions(
        self,
        game_state: "GameState"
    ) -> bool:
        """Checks if the player has any possible actions to take.

        Args:
            game_state: The current state of the game.

        Returns:
            bool: True if the player has actions, False otherwise.
        """
        possible_actions = self.action_handler.get_possible_actions(self, game_state)
        return True if len(possible_actions) > 0 else False