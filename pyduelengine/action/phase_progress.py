from pyduelengine.action.action import Action
from pyduelengine.game.chain_manager import Context

class ProgressPhaseAction(Action):
    """Action to progress to the next phase of the game."""
    def execute(
        self,
        context: Context
    ) -> None:
        """Executes the action to progress to the next phase.
        
        Args:
            context (Context): The context in which the action is being executed.
        """
        context.phase_manager.progress_phase()