from pyduelengine.cards.registry import CARD_REGISTRY
from pyduelengine.cards.card import Card

class CardLoader():
    """Base class for all cards in the game."""
    def build_from_id(self, card_id: str) -> 'Card':
        """Factory method to create a Card object from a card ID.
        
        Args:
            card_id (str): The unique identifier for the card.
        Returns:
            Card: An instance of the Card class.
        """
        # Find the card id in the registry and return the appropriate subclass
        card_class = CARD_REGISTRY.get(card_id)

        if card_class is None:
            raise ValueError(f"Card ID {card_id} not found in registry.")
    
        return card_class(card_id)

        