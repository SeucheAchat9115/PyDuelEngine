from pyduelengine.game.gamestate import GameState
from pyduelengine.player.player import Player
from pyduelengine.phase.phase_manager import PhaseManager
from pyduelengine.chain.chain_manager import ChainManager

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

        # Initialize Players who can take actions
        self.player_1 = Player(name=player_1_name)
        self.player_2 = Player(name=player_2_name)
        self.current_player = self.player_1
        self.non_current_player = self.player_2

        # Initialize GameState to track the state of the game
        self.gamestate = GameState(
            player_1_name=player_1_name,
            player_1_deck_list=player_1_deck_list,
            player_2_name=player_2_name,
            player_2_deck_list=player_2_deck_list
        )

        # Initialize PhaseManager to handle phase transitions
        self.phase_manager = PhaseManager(game_state=self.gamestate)
        # Initialize ChainManager to handle chain resolutions
        self.chain_manager = ChainManager()

    def start(self) -> None:
        """Starts the game."""

        print("Game started!")
        print(f"Current Phase: {self.gamestate.current_phase.name}")
        print(f"Current Player: {self.gamestate.current_player}")
        print(f"Current Turn: {self.gamestate.current_turn}")

        while not self.check_win_condition():
            self.execute_phase()
            self.phase_manager.advance_phase()

    def check_win_condition(self) -> bool:
        """Checks if a win condition has been met.
        
        Returns:
            bool: True if the game has been won, False otherwise.
        """
        # Placeholder for win condition logic
        return False
    
    def execute_phase(self) -> None:
        """Executes the logic for the current phase."""
        print(f"Executing {self.gamestate.current_phase.name} phase for {self.gamestate.current_player}.")
        
        # Turn player and non-turn player actions
        while self.one_players_has_actions():
            self.current_player.apply_actions(self.gamestate)
            self.non_current_player.apply_actions(self.gamestate)

    def one_players_has_actions(self) -> bool:
        """Placeholder function to determine if either player has actions left.
        
        Returns:
            bool: True if either player has actions left, False otherwise.
        """

        current_player_has_actions = self.current_player.has_actions(self.gamestate)
        non_current_player_has_actions = self.non_current_player.has_actions(self.gamestate)
        return current_player_has_actions or non_current_player_has_actions
