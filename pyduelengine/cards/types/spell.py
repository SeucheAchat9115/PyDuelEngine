from pyduelengine.cards.types.card import Card

class SpellCard(Card):
    """Represents a Spell Card in the game."""
    def __init__(self, card_id: str, spell_type: str) -> None:
        """Initializes a SpellCard object.

        Args:
            card_id (str): The unique identifier for the card.
            spell_type (str): The type of the spell (e.g., Normal, Continuous, Equip).
        """
        super().__init__(card_id)
        self.spell_type = spell_type