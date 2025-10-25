from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.game.chain_manager import ChainManager
    from pyduelengine.game.action_generator import ActionGenerator
    from pyduelengine.player.player import Player
from pyduelengine.action.normal_summon import NormalSummonAction


from pyduelengine.action.action import Action

class SummonManager():
    """Class responsible for managing summons in the game."""
    def __init__(
        self,
        game_state: GameState, 
        chain_manager: ChainManager, 
        action_generator: ActionGenerator
    ) -> None:
        """Initializes the SummonManager.
        
        Args:
            game_state (GameState): The current game state.
            chain_manager (ChainManager): The chain manager for handling chains.
            action_generator (ActionGenerator): The action generator for generating actions.
        """
        self.game_state = game_state
        self.chain_manager = chain_manager
        self.action_generator = action_generator

    def handle_summon(self, player: Player, action: Action):
        """
        The single public-facing method called by the ActionHandler.
        It dispatches the action to the correct internal processor.
        """
        print(f"[SummonHandler] Received action: {action.__class__.__name__}")
        
        # This is the "sub-dispatcher" logic
        if isinstance(action, NormalSummonAction):
            self._process_normal_summon(player, action)
            
        # elif isinstance(action, SetMonsterAction):
        #     self._process_set_monster(player, action)
            
        # elif isinstance(action, SpecialSummonAction):
        #     self._process_special_summon(player, action)
            
        else:
            raise ValueError("Unknown summon action type.")
        
    def _process_normal_summon(self, player: Player, action: NormalSummonAction):
        """Processes a normal summon action.
        
        Args:
            player (Player): The player performing the summon.
            action (NormalSummonAction): The normal summon action to process.
        """
        print(f"Normal summoning for player: {player.name}")
        
        card = action.card
        player_state = self.game_state.get_player_state(player)

        # 1. Legality & Cost Check
        if player_state.has_normal_summoned_this_turn:
            raise Exception("Player has already performed a normal summon this turn.")
        
        required_tributes = 0
        if card.level >= 7: required_tributes = 2
        elif card.level >= 5: required_tributes = 1

        if len(action.tributes) != required_tributes:
            raise Exception(f"Incorrect number of tributes provided. Required: {required_tributes}, Given: {len(action.tributes)}")
        
        # 2. Move the Card
        player_state.hand.remove_card(card)
        player_state.field.add_monster(card, action.position)
        card.position = action.position
        # 3. Update Game State 
        player_state.has_normal_summoned_this_turn = True
        # 4. Open the Summon Response Window
        self._trigger_summon_response_window(player, card)
