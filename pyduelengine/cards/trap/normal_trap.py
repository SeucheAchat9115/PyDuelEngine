from pyduelengine.cards.card import Card

class NormalTrapCard(Card):
    """Represents a Normal Trap Card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a NormalTrapCard object."""
        super().__init__(**kwargs)