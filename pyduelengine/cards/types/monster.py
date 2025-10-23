from pyduelengine.cards.types.card import Card

class MonsterCard(Card):
    """A class representing a monster card in the game."""
    def __init__(self, card_id: str, attack: int, defense: int, level: int) -> None:
        """Initializes a MonsterCard object.

        Args:
            card_id (str): The unique identifier for the card.
            attack (int): The attack points of the monster.
            defense (int): The defense points of the monster.
            level (int): The level of the monster.
        """
        super().__init__(card_id)
        self.attack = attack
        self.defense = defense
        self.level = level