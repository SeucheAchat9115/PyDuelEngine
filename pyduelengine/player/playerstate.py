from pyduelengine.deck.deck import load_deck_from_file

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