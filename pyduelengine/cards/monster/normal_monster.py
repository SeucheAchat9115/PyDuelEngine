from __future__ import annotations
from typing import TYPE_CHECKING

from pyduelengine.cards.card import Card
from pyduelengine.action.normal_summon import NormalSummonAction

if TYPE_CHECKING:
    from pyduelengine.action.action import Action

class NormalMonsterCard(Card):
    """A class representing a monster card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a NormalMonsterCard object.

        Args:
            card_id (str): The unique identifier for the card.
            attack (int): The attack points of the monster.
            defense (int): The defense points of the monster.
            level (int): The level of the monster.
        """
        super().__init__(**kwargs)
        self.attack = kwargs.get("attack", None)
        self.defense = kwargs.get("defense", None)
        self.level = kwargs.get("level", None)
        self.race = kwargs.get("race", None)

    def get_possible_actions(
        self,
        gamestate,
        player,
        location
    ) -> list[Action]:
        """Generates a list of possible actions for this NormalMonsterCard.

        Args:
            gamestate (GameState): The current game state.
            player (Player): The player who owns the card.
            location (str): The location of the card (e.g., hand, field).
        """
        possible_actions = []

        if location == "hand":
            if self.level <= 4:
                if self.can_be_normal_summoned():
                    possible_actions.append(NormalSummonAction(owner=player, card=self))
            elif self.level <= 6:
                # Placeholder for tribute summon logic
                pass
            elif self.level >= 7:
                # Placeholder for tribute summon logic
                pass
        elif location == "monster_zones":
            # Placeholder for actions when the monster is on the field
            # e.g. battle, change position, etc.
            pass
        else:
            # Other locations do not have actions for Normal Monsters
            pass

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

    def can_be_normal_summoned(self) -> bool:
        """Determines if the monster can be normal summoned.

        Returns:
            bool: True if the monster can be normal summoned, False otherwise.
        """
        # Placeholder logic for normal summon conditions
        return True
    
    def get_effect_actions(
        self,
        gamestate,
        player,
        location
    ) -> list[Action]:
        """Generates a list of effect actions for this NormalMonsterCard.

        Args:
            gamestate (GameState): The current game state.
            player (Player): The player who owns the card.
            location (str): The location of the card (e.g., hand, field).
        """
        # Normal Monsters do not have effects
        return []