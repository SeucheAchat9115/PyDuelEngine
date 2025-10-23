class Card():
    """Base class for all cards in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a Card object.
        Args:
            card_id (str): The unique identifier for the card.
            name (str): The name of the card.
            desc (str): The description of the card.
            type (str): The type of the card.
        """
        self.card_id = kwargs.get("card_id", None)
        self.name = kwargs.get("name", None)
        self.description = kwargs.get("desc", None)
        self.type = kwargs.get("type", None)
        self.archetype = kwargs.get("archetype", None)

    def __str__(self) -> str:
        return f"{self.name} ({self.card_id})"
    
    def __repr__(self) -> str:
        return f"Card(card_id={self.card_id}, name='{self.name}', type='{self.type}')"