from __future__ import annotations
from typing import TYPE_CHECKING

from pyduelengine.cards.card import Card

if TYPE_CHECKING:
    from pyduelengine.action.action import Action
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.player.player import Player

class NormalSpellCard(Card):
    """Represents a Normal Spell Card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a NormalSpellCard object."""
        super().__init__(**kwargs)

    def get_possible_actions(
        self,
        gamestate: "GameState",
        player: "Player",
        location: str
    ) -> list["Action"]:
        """Returns a list of possible actions for this Normal Spell Card.

        Args:
            gamestate (GameState): The current game state.
            player (Player): The player considering the actions.
            location (str): The location of the card.
        Returns:
            list[Action]: A list of possible actions for this card.
        """
        possible_actions = []
        
        # Handle effect activations logic
        valid_effect_actions = self.get_effect_actions(
            gamestate=gamestate,
            player=player,
            location=location
        )
        if valid_effect_actions:
            for effect_action in valid_effect_actions:
                possible_actions.append(effect_action)

        return possible_actions
    
    def get_effect_actions(
        self,
        gamestate: GameState,
        player: Player,
        location: str
    ) -> list[Action]:
        """Returns a list of effect actions for this Normal Spell Card.

        Args:
            gamestate (GameState): The current game state.
            player (Player): The player considering the actions.
            location (str): The location of the card.
        Returns:
            list[Action]: A list of effect actions for this card.
        """
        # Placeholder implementation; actual effect logic to be implemented
        return []