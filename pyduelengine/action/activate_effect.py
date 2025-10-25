from __future__ import annotations
from typing import TYPE_CHECKING
from pyduelengine.action.action import Action

if TYPE_CHECKING:
    from pyduelengine.cards.card import Card
    from pyduelengine.game.chain_manager import Context

class ActivateEffectAction(Action):
    def __init__(self, card: Card, effect_id: int):
        """Initializes an ActivateEffectAction.
        
        Args:
            card (Card): The card whose effect is being activated.
            effect_id (int): The ID of the effect to activate.
        """
        super().__init__()
        self.card = card
        self.effect_id = effect_id

    def execute(self, context: Context) -> None:
        """Activates the effect for the given player.
        
        Args:
            context (Context): The context in which the action is being executed.
        """
        self.card.activate_effect(
            context.gamestate, 
            context.activating_player, 
            self.effect_id
        )