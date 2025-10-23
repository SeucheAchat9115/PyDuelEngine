from pyduelengine.game.gamestate import GameState
from pyduelengine.player.player import Player
from pyduelengine.game.phases import GamePhase

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
        player_1 = Player(name=player_1_name, deck_list=player_1_deck_list)
        player_2 = Player(name=player_2_name, deck_list=player_2_deck_list)

        # Initialize GameState to track the state of the game
        self.state = GameState(
            player_1=player_1,
            player_2=player_2
        )

    def start(self) -> None:
        """Starts the game."""

        print("Game started!")
        print(f"Current Phase: {self.state.current_phase.name}")
        print(f"Current Player: {self.state.current_player.name}")
        print(f"Current Turn: {self.state.current_turn}")

        while not self.check_win_condition():
            self.execute_phase()
            self.advance_phase()

    def check_win_condition(self) -> bool:
        """Checks if a win condition has been met.
        
        Returns:
            bool: True if the game has been won, False otherwise.
        """
        # Placeholder for win condition logic
        return False
    
    def execute_phase(self) -> None:
        """Executes the logic for the current phase."""
        print(f"Executing {self.state.current_phase.name} phase for {self.state.current_player.name}.")
        
        # Turn player and non-turn player actions
        while self.one_players_has_actions():
            self.state.current_player.take_action(self.state)
            self.state.non_current_player.take_action(self.state)

    def one_players_has_actions(self) -> bool:
        """Placeholder function to determine if either player has actions left.
        
        Returns:
            bool: True if either player has actions left, False otherwise.
        """
        # Placeholder logic; in a real implementation, this would check actual game state
        return False

    def advance_phase(self) -> None:
        """Advances to the next phase or turn."""
        if self.state.current_phase == GamePhase.END:
            self.state.current_turn += 1
            self.state.current_phase = GamePhase.DRAW
            self.state.current_player = (
                self.state.player_1 
                if self.state.current_player == self.state.player_2 
                else self.state.player_2
            )
        else:
            self.state.current_phase = GamePhase(self.state.current_phase.value + 1)
