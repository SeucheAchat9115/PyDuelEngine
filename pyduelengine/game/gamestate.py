from typing import TYPE_CHECKING
from pyduelengine.phase.phases import GamePhase
from pyduelengine.player.playerstate import PlayerState
from pyduelengine.constants import LOCATIONS

if TYPE_CHECKING:
    from pyduelengine.cards.card import Card

class GameState:
    """
    Holds the complete gamestate, including both players and shared zones.
    """
    def __init__(
        self,
        player_1_name: str,
        player_1_deck_list: str,
        player_2_name: str,
        player_2_deck_list: str
    ) -> None:
        """Initializes the GameState with two players.

        Args:
            player_1_name (str): The name of player 1.
            player_1_deck_list (str): The deck list of player 1.
            player_2_name (str): The name of player 2.
            player_2_deck_list (str): The deck list of player 2.
        """

        self.player_1_state = PlayerState(
            name=player_1_name,
            deck_list=player_1_deck_list
        )
        self.player_2_state = PlayerState(
            name=player_2_name,
            deck_list=player_2_deck_list
        )

        # Initialize the game phase and current player
        self.current_phase = GamePhase.DRAW
        self.current_player = self.player_1_state.name
        self.non_current_player = self.player_2_state.name
        self.current_turn = 1

    def switch_current_player(self) -> None:
        """Switches the current player to the other player."""
        if self.current_player == self.player_1_state.name:
            self.current_player = self.player_2_state.name
            self.non_current_player = self.player_1_state.name
        else:
            self.current_player = self.player_1_state.name
            self.non_current_player = self.player_2_state.name

    def __str__(self) -> str:
        return (
            f"GameState(Current Phase: {self.current_phase}, "
            f"Current Player: {self.current_player}, "
            f"Turn: {self.current_turn}, "
            f"Player 1 State: {self.player_1_state}, "
            f"Player 2 State: {self.player_2_state}, "
            f")"
        )

    def get_cards_by_location(self, player_name: str, location: str) -> list["Card"]:
        """Return the cards in a given location for the specified player.

        Args:
            player_name (str): The name of the player whose cards to retrieve.
            location (str): The location to query (e.g. "hand" or "graveyard").
        Returns:
            list: A list of cards in the requested location.
        """
        if location not in LOCATIONS:
            raise ValueError(f"Invalid location: {location}")

        if player_name == self.player_1_state.name:
            player_state = self.player_1_state
        elif player_name == self.player_2_state.name:
            player_state = self.player_2_state
        else:
            raise ValueError(f"Player with name {player_name} not found in game state.")

        return getattr(player_state, location)
