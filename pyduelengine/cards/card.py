from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyduelengine.action.action import Action
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.player.player import Player

class Card():
    """Base class for all cards in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a Card object.
        Args:
            card_id (str): The unique identifier for the card.
            name (str): The name of the card.
            desc (str): The description of the card.
            type (str): The type of the card.
        """
        self.card_id = kwargs.get("card_id", None)
        self.name = kwargs.get("name", None)
        self.description = kwargs.get("desc", None)
        self.type = kwargs.get("type", None)
        self.archetype = kwargs.get("archetype", None)

    def __str__(self) -> str:
        return f"{self.name} ({self.card_id})"
    
    def __repr__(self) -> str:
        return f"Card(card_id={self.card_id}, name='{self.name}', type='{self.type}')"
    
    def get_possible_actions(
        self,
        gamestate: GameState,
        player: Player,
        location: str
    ) -> list[Action]:
        """Returns a list of possible actions for this card.

        Args:
            gamestate (GameState): The current game state.
            player (Player): The player considering the actions.
            location (str): The location of the card.

        Returns:
            list[Action]: A list of possible actions for this card.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")