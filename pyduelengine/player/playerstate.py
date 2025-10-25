from pyduelengine.deck.deck import load_deck_from_file
import random

class PlayerState():
    """
    A class representing a player's state in the game.
    """
    def __init__(
        self, 
        name: str,
        deck_list: str
    ) -> None:
        """Initializes a Player object.
        
        Args:
            name (str): The name of the player.
            deck_list (str): Path to the player's deck file.
        """
        
        self.name = name
        self.life_points = 8000

        self.deck_list = deck_list
        self.deck: list[str] = load_deck_from_file(deck_list, "main")
        self.extra_deck: list[str] = load_deck_from_file(deck_list, "extra")
        self.side_deck: list[str] = load_deck_from_file(deck_list, "side")

        self.hand: list[str] = []
        self.graveyard: list[str] = []
        self.banished: list[str] = []

        self.main_monster_zones: list[str | None] = [None, None, None, None, None]
        self.spell_trap_zones: list[str | None] = [None, None, None, None, None]
        self.extra_monster_zones: list[str | None] = [None, None]
        self.field_spell_zone: list[str | None] = None

        self.must_draw: bool = False

        self.init_player_state()

    def init_player_state(self) -> None:
        """Initializes the player's state at the start of the game.
        Draws an initial hand of 5 cards from the deck.
        """
        # Shuffle the deck
        random.shuffle(self.deck)

        # Draw initial hand of 5 cards
        for _ in range(5):
            if self.deck:
                drawn_card = self.deck.pop(0)
                self.hand.append(drawn_card)

        self.must_draw = False # No draw required at game start

    def __str__(self) -> str:
        return (
            f"PlayerState(Name: {self.name}, "
            f"Life Points: {self.life_points}, "
            f"Deck Size: {len(self.deck)}, "
            f"Hand: {self.hand}, "
            f"Graveyard: {self.graveyard}, "
            f"Banished: {self.banished}, "
            f"Main Monster Zones: {self.main_monster_zones}, "
            f"Spell/Trap Zones: {self.spell_trap_zones}, "
            f"Extra Monster Zones: {self.extra_monster_zones}, "
            f"Field Spell Zone: {self.field_spell_zone})"
        )