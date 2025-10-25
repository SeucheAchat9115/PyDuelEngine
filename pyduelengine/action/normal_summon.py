from __future__ import annotations
from typing import TYPE_CHECKING

from pyduelengine.action.action import Action

if TYPE_CHECKING:
    from pyduelengine.cards.monster.normal_monster import NormalMonsterCard
    from pyduelengine.player.player import Player

class NormalSummonAction(Action):
    """An action representing the normal summon of a monster card."""
    def __init__(
        self, 
        owner: Player,
        card: NormalMonsterCard
    ) -> None:
        """Initializes a NormalSummonAction object.

        Args:
            owner (Player): The player performing the action.
            card (NormalMonsterCard): The monster card to be normal summoned.
        """
        super().__init__(owner=owner)
        self.card = card

    def execute(
        self,
        context
    ) -> None:
        """Executes the normal summon action, modifying the game state as necessary.
        
        Args:
            context (Context): The context in which the action is being executed.
        """
        print(f"{self.owner} normal summons {self.card}.")
        context.gamestate.summon_monster(self.owner, self.card, orientation="attack")