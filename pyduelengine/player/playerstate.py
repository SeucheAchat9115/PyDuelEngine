class PlayerState:
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
        self.hand: list[str] = []
        self.deck: list[str] = []
        self.extra_deck: list[str] = []
        self.graveyard: list[str] = []
        self.banished: list[str] = []

        self.main_monster_zones: list[str | None] = [None] * 5
        self.extra_monster_zones: list[str | None] = [None] * 2
        self.spell_trap_zones: list[str | None] = [None] * 5
        self.field_spell_zone: list[str | None] = [None] * 1