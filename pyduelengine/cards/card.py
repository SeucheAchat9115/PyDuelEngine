class Card():
    """Base class for all cards in the game."""
    def __init__(self, card_id: str) -> None:
        """Initializes a Card object.
        Args:
            card_id (str): The unique identifier for the card.
        """
        self.card_id = card_id