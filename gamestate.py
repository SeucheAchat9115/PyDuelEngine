class PlayerState:
    """
    Holds all the game-related information and zones for a single player.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.life_points = 8000
        self.hand: list[str] = []
        self.deck: list[str] = []
        self.extra_deck: list[str] = []
        self.graveyard: list[str] = []
        self.banished: list[str] = []

        self.main_monster_zones: list[str | None] = [None] * 5
        self.extra_monster_zones: list[str | None] = [None] * 2
        self.spell_trap_zones: list[str | None] = [None] * 5
        self.field_spell_zone: list[str | None] = [None] * 1

class GameState:
    """
    Holds the complete gamestate, including both players and shared zones.
    """
    def __init__(self):
        self.player1 = PlayerState(name="Player 1")
        self.player2 = PlayerState(name="Player 2")

        self.turn_number = 1
        self.current_player = self.player1
        self.current_phase = "Draw"