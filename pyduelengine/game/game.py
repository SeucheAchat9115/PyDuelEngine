from pyduelengine.game.gamestate import GameState
from pyduelengine.player.player import Player
from pyduelengine.phase.phase_manager import PhaseManager
from pyduelengine.game.chain_manager import ChainManager
from pyduelengine.game.battle_manager import BattleManager
from pyduelengine.game.summon_manager import SummonManager
from pyduelengine.game.action_handler import ActionHandler
from pyduelengine.game.action_generator import ActionGenerator
from pyduelengine.phase.phases import GamePhase

class Game():
    """Main class representing the game."""
    def __init__(
        self,
        player_1_name: str,
        player_1_deck_list: str,
        player_2_name: str,
        player_2_deck_list: str
    ) -> None:
        """Initializes the Game with a new GameState.
        
        Args:
            player_1_name (str): The name of player 1.
            player_1_deck_list (str): The deck list of player 1.
            player_2_name (str): The name of player 2.
            player_2_deck_list (str): The deck list of player 2.
        """

        player_1 = Player(name=player_1_name)
        player_2 = Player(name=player_2_name)

        self.gamestate = GameState(
            player_1=player_1,
            player_2=player_2,
            player_1_deck_list=player_1_deck_list,
            player_2_deck_list=player_2_deck_list
        )

        self.action_generator = ActionGenerator(
            gamestate=self.gamestate,
        )

        self.summon_manager = SummonManager()
        self.battle_manager = BattleManager()
        self.phase_manager = PhaseManager(gamestate=self.gamestate)

        self.chain_manager = ChainManager(
            gamestate=self.gamestate,
            action_generator=self.action_generator,
            phase_manager=self.phase_manager
        )

        self.action_handler = ActionHandler(
            gamestate=self.gamestate,
            chain_manager=self.chain_manager,
            battle_manager=self.battle_manager,
            summon_manager=self.summon_manager,
            phase_manager=self.phase_manager
        )
        

    def start(self) -> None:
        """Starts the game."""

        self.gamestate.current_player = self.gamestate.player_1

        while self._check_win_conditions() is None:
            player = self._get_current_player()

            self.phase_manager.start_turn()

            # Check for Deck Out win after the draw
            if self._check_win_conditions():
                break

            # Execute phases until END phase
            while self.gamestate.current_phase != GamePhase.END:
                if self._check_win_conditions():
                    break
                legal_actions = self.action_generator.get_legal_actions(player)
                chosen_action = player.agent.get_action(self.gamestate, legal_actions)
                self.action_handler.process_action(player, chosen_action)
            
            if self._check_win_conditions():
                break

            self.phase_manager.end_turn()

        winner = self._check_win_conditions()
        print(f"Game Over! The winner is {winner.name}.")

    def _get_current_player(self) -> Player:
        """Helper to get the active Player object."""
        return self.gamestate.current_player

    def _check_win_conditions(self) -> Player | None:
        """Checks if a player has won."""
        p1_state = self.gamestate.get_player_state(self.gamestate.player_1)
        p2_state = self.gamestate.get_player_state(self.gamestate.player_2)

        if p1_state.life_points <= 0:
            return self.gamestate.player_2  # Player 2 wins
        if p2_state.life_points <= 0:
            return self.gamestate.player_1  # Player 1 wins
        
        if len(p1_state.deck) == 0 and p1_state.must_draw:
            return self.gamestate.player_2  # Player 2 wins by Deck Out
        if len(p2_state.deck) == 0 and p2_state.must_draw:
            return self.gamestate.player_1  # Player 1 wins by Deck Out

        # ... add other win conditions (Exodia, etc.)
        return None