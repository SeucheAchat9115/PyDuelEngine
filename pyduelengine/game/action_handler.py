from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.game.chain_manager import ChainManager
    from pyduelengine.game.battle_manager import BattleManager
    from pyduelengine.game.summon_manager import SummonManager
    from pyduelengine.phase.phase_manager import PhaseManager
    from pyduelengine.player.player import Player

from pyduelengine.action.action import Action

class ActionHandler:
    def __init__(
        self,
        gamestate: GameState,
        chain_manager: ChainManager,
        battle_manager: BattleManager,
        summon_manager: SummonManager,
        phase_manager: PhaseManager
    ) -> None:
        """Initializes an ActionHandler object.

        Args:
            gamestate (GameState): The current game state.
            chain_manager (ChainManager): The chain manager for handling chains.
            battle_manager (BattleManager): The battle manager for handling battles.
            summon_manager (SummonManager): The summon manager for handling summons.
            phase_manager (PhaseManager): The phase manager for handling phases.
        """

        self.gamestate = gamestate
        self.chain_manager = chain_manager
        self.battle_manager = battle_manager
        self.summon_manager = summon_manager
        self.phase_manager = phase_manager

    def process_action(
        self,
        player: Player,
        action: Action
    ) -> None:
        """Processes the given action for the player."""
        self.chain_manager.start_chain(player, action)