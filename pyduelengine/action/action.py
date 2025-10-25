from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyduelengine.player.player import Player
    from pyduelengine.game.chain_manager import Context

class Action():
    """Base class for all actions in the game."""
    def __init__(self, owner: Player) -> None:
        """Initializes an Action object.

        Args:
            owner (Player): The player who owns this action.
        """
        self.owner = owner

    def execute(
        self,
        context: Context
    ) -> None:
        """Executes the action, modifying the game state as necessary.
        
        Args:
            context (Context): The context in which the action is being executed.
        """
        raise NotImplementedError("Execute method must be implemented by subclasses.")