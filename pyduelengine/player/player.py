from pyduelengine.player.playerstate import PlayerState
from pyduelengine.game.gamestate import GameState

class Player():
    """
    A class representing a player in the game.
    """
    def __init__(
        self, 
        name: str,
        deck_list: str
    ) -> None:
        """Initializes a Player object.
        
        Args:
            name (str): The name of the player.
            deck_list (str): The deck list of the player.
        """

        self.name = name
        self.playerstate = PlayerState(
            name=name,
            deck_list=deck_list
        )

    def take_action(
        self, 
        game_state: GameState
    ) -> None:
        """Placeholder method for the player to take an action during their turn.
        
        Args:
            game_state: The current state of the game.
        """
        # Placeholder for player action logic
        print(f"{self.name} is taking an action.")
