from pyduelengine.api.ydk_manager import YDKDeckManager
from pyduelengine.cards.types.card import Card
from pyduelengine.cards.card_loader import CardLoader

def load_deck_from_file(deck_list: str, deck_type: str) -> list:
    """
    Loads a deck from a given file path.

    Args:
        deck_list (str): The path to the deck file.
        deck_type (str): The type of the deck ("main", "extra", "side").
    Returns:
        list: A list of card identifiers representing the deck.
    """

    deck_data = YDKDeckManager().load(deck_list)

    if deck_type == "main":
        # Check if length of main deck is valid
        if len(deck_data.get("main", [])) < 40 or len(deck_data.get("main", [])) > 60:
            raise ValueError(f"Main deck must contain between 40 and 60 cards. Found: {len(deck_data.get('main', []))}")
    elif deck_type == "extra":
        # Check if length of extra deck is valid
        if len(deck_data.get("extra", [])) > 15:
            raise ValueError(f"Extra deck cannot contain more than 15 cards. Found: {len(deck_data.get('extra', []))}")
    elif deck_type == "side":
        # Check if length of side deck is valid
        if len(deck_data.get("side", [])) > 15:
            raise ValueError(f"Side deck cannot contain more than 15 cards. Found: {len(deck_data.get('side', []))}")

    deck_data = build_deck_data(deck_data.get(deck_type, []))

    print(f"Loaded {deck_type} deck with {len(deck_data)} cards.")
    return deck_data

def build_deck_data(deck_data: list[str]) -> list[Card]:
    """
    Converts a list of card identifiers into Card objects.

    Args:
        deck_data (list[str]): A list of card identifiers.
    Returns:
        list[Card]: A list of Card objects.
    """
    card_loader = CardLoader()
    return [card_loader.build_from_id(card_id) for card_id in deck_data]