from pyduelengine.cards.card import Card

class TrapCard(Card):
    """Represents a Trap Card in the game."""
    def __init__(self, card_id: str, trap_type: str) -> None:
        """Initializes a TrapCard object.

        Args:
            card_id (str): The unique identifier for the card.
            trap_type (str): The type of the trap (e.g., Normal, Continuous, Counter).
        """
        super().__init__(card_id)
        self.trap_type = trap_type