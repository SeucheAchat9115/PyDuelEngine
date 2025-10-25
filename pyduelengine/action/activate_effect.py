from typing import TYPE_CHECKING
from pyduelengine.action.action import Action

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.player.player import Player
    from pyduelengine.cards.card import Card

class ActivateEffectAction(Action):
    def __init__(self, card: Card, effect_id: int):
        self.card = card
        self.effect_id = effect_id

    def execute(self, gamestate: GameState, player: Player) -> None:
        """Activates the effect for the given player."""
        self.card.activate_effect(gamestate, player, self.effect_id)