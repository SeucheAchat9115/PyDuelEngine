from pyduelengine.cards.card import Card

class NormalSpellCard(Card):
    """Represents a Normal Spell Card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a NormalSpellCard object."""
        super().__init__(**kwargs)