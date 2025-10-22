class PlayerState:
    """
    Holds all the game-related information and zones for a single player.
    """
    def __init__(self, name: str):
        self.name = name
        self.life_points = 8000

        # --- Card Piles (variable size) ---

        # Player's hand
        self.hand: list[str] = []

        # Main deck (face-down)
        self.deck: list[str] = []

        # Extra deck (face-down)
        self.extra_deck: list[str] = []

        # Graveyard (face-up)
        self.graveyard: list[str] = []

        # Banished pile (face-up, usually)
        self.banished: list[str] = []

        # --- Card Zones (fixed size) ---

        # 5 Main Monster Zones
        # [None, "Card Name", None, None, "Card Name"]
        self.main_monster_zones: list[str | None] = [None] * 5

        # 5 Spell & Trap Zones
        # Can hold Spells, Traps, or be Pendulum Zones (slots 0 and 4)
        self.spell_trap_zones: list[str | None] = [None] * 5

        # 1 Field Spell Zone
        self.field_spell_zone: list[str | None] = [None] * 1

    def __repr__(self) -> str:
        """String representation for the player."""
        return f"<PlayerState: {self.name} | LP: {self.life_points}>"


class GameState:
    """
    Holds the complete gamestate, including both players and shared zones.
    """
    def __init__(self):
        # Initialize both players
        self.player1 = PlayerState(name="Player 1")
        self.player2 = PlayerState(name="Player 2")

        # 2 Extra Monster Zones (shared)
        # The card string can be annotated to show controller, e.g., "Decode Talker (P1)"
        self.extra_monster_zones: list[str | None] = [None] * 2

        # --- Game Metadata ---
        self.turn_number = 1
        self.current_player = self.player1 # Player 1 starts
        self.current_phase = "Draw Phase"

    def display_simple_board(self):
        """
        Prints a simplified text representation of the current board state.
        This prints from Player 2's perspective (top) to Player 1's (bottom).
        """
        print("=" * 60)
        print(f"TURN: {self.turn_number} | PLAYER: {self.current_player.name} | PHASE: {self.current_phase}")
        print("=" * 60)

        # --- Player 2 (Opponent) ---
        print(f"\n--- {self.player2.name}'s Side ---")
        print(f"LP: {self.player2.life_points}")
        print(f"Hand: {len(self.player2.hand)} | Deck: {len(self.player2.deck)} | ED: {len(self.player2.extra_deck)}")
        print(f"Field Spell: {self.player2.field_spell_zone[0]}")
        print(f"S/T Zones:   {self.player2.spell_trap_zones}")
        print(f"Monster Zones: {self.player2.main_monster_zones}")
        print(f"GY: {len(self.player2.graveyard)} | Banish: {len(self.player2.banished)}")

        # --- Shared Zones ---
        print("\n--- Shared Extra Monster Zones ---")
        print(f"EMZ:         {self.extra_monster_zones}")

        # --- Player 1 (Active) ---
        print(f"\n--- {self.player1.name}'s Side ---")
        print(f"LP: {self.player1.life_points}")
        print(f"Monster Zones: {self.player1.main_monster_zones}")
        print(f"S/T Zones:   {self.player1.spell_trap_zones}")
        print(f"Field Spell: {self.player1.field_spell_zone[0]}")
        print(f"GY: {len(self.player1.graveyard)} | Banish: {len(self.player1.banished)}")
        print(f"Hand: {self.player1.hand} ({len(self.player1.hand)} cards)")
        print(f"Deck: {len(self.player1.deck)} | ED: {len(self.player1.extra_deck)}")
        print("=" * 60)


# --- Example Usage ---
if __name__ == "__main__":
    
    # 1. Create a new game
    print("Initializing new game...")
    game = GameState()

    # 2. Set up Player 1's state
    game.player1.hand = ["Dark Magician", "Blue-Eyes White Dragon", "Pot of Greed", "Mirror Force", "Mystical Space Typhoon"]
    game.player1.deck = ["Monster Card 1", "Spell Card 1", "Trap Card 1"] * 12 # 36 cards
    game.player1.extra_deck = ["Dark Paladin", "Blue-Eyes Ultimate Dragon"]
    game.player1.main_monster_zones[1] = "Summoned Skull" # In zone 2
    game.player1.spell_trap_zones[4] = "Magic Cylinder (Set)" # In zone 5
    game.player1.graveyard = ["Kuriboh"]
    game.player1.field_spell_zone[0] = "Yami"

    # 3. Set up Player 2's state
    game.player2.hand = ["Red-Eyes Black Dragon", "Swords of Revealing Light", "Trap Hole"]
    game.player2.deck = ["Monster Card 2", "Spell Card 2", "Trap Card 2"] * 13 # 39 cards
    game.player2.extra_deck = ["Red-Eyes Flare Metal Dragon"]
    game.player2.main_monster_zones[2] = "Beaver Warrior"
    game.player2.banished = ["Pot of Desires"]

    # 4. Set up shared zones
    # (Let's say Player 1 controls a monster in the first EMZ)
    game.extra_monster_zones[0] = "Decode Talker (P1)"

    # 5. Display the board
    game.display_simple_board()

    # 6. Simulate a game action
    print("\nSimulating P1 playing a card...")
    
    # Player 1 activates Pot of Greed from hand
    card_played = game.player1.hand.pop(2) # Remove "Pot of Greed"
    game.player1.graveyard.append(card_played)
    
    # Player 1 draws 2 cards from deck
    game.player1.hand.append(game.player1.deck.pop())
    game.player1.hand.append(game.player1.deck.pop())
    
    game.current_phase = "Main Phase 1"

    # 7. Display the new board state
    game.display_simple_board()
