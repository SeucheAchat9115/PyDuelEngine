from pyduelengine.cards.registry import CARD_REGISTRY
from pyduelengine.cards.card import Card
from pyduelengine.api.ygopro_api import YGOPROAPIClient

class CardLoader():
    """Base class for all cards in the game."""
    def __init__(self) -> None:
        """Initialize the CardLoader with an API client."""
        self.api_client = YGOPROAPIClient()

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

        card_data = self.api_client.get_card_by_id(card_id)
        if not card_data:
            raise ValueError(f"Card ID {card_id} not found in API.")

        return card_class(**card_data)