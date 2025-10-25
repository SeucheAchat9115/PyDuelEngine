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

class PassPriorityAction(Action):
    pass