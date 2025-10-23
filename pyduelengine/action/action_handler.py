from typing import TYPE_CHECKING
from pyduelengine.constants import LOCATIONS

if TYPE_CHECKING:
    from pyduelengine.player.player import Player
    from pyduelengine.game.gamestate import GameState

class ActionHandler:
    def __init__(self) -> None:
        """Initializes an ActionHandler object.
        """
        pass

    def get_possible_actions(
        self, 
        player: "Player",
        game_state: "GameState"
    ) -> list[str]:
        """Returns a list of possible actions for the player based on the game state.
        
        Args:
            player (Player): The player for whom to get possible actions.
            game_state (GameState): The current state of the game.

        Returns:
            list[str]: A list of possible actions.
        """
        possible_actions = []

        for location in LOCATIONS:
            if location in ["deck", "extra_deck"]:
                # Effects here cannot be activated directly by the player
                continue  

            cards_in_location = game_state.get_cards_by_location(player.name, location)
            for card in cards_in_location:
                actions = card.get_possible_actions(player, game_state)
                possible_actions.extend(actions)
        return possible_actions