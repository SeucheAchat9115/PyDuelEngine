from pyduelengine.action.action import Action

class ProgressPhaseAction(Action):
    """Action to progress to the next phase of the game."""
    def execute(
        self,
        gamestate,
        player,
        chain_manager,
        battle_manager,
        summon_manager,
        phase_manager
    ) -> None:
        """Executes the action to progress to the next phase.
        
        Args:
            gamestate (GameState): The current game state.
            player (Player): The player performing the action.
            chain_manager (ChainManager): The chain manager for handling chains.
            battle_manager (BattleManager): The battle manager for handling battles.
            summon_manager (SummonManager): The summon manager for handling summons.
            phase_manager (PhaseManager): The phase manager for handling phases.
        """
        phase_manager.progress_phase()