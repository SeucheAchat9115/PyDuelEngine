from pyduelengine.cards.card import Card

class NormalMonsterCard(Card):
    """A class representing a monster card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a NormalMonsterCard object.

        Args:
            card_id (str): The unique identifier for the card.
            attack (int): The attack points of the monster.
            defense (int): The defense points of the monster.
            level (int): The level of the monster.
        """
        super().__init__(**kwargs)
        self.attack = kwargs.get("attack", None)
        self.defense = kwargs.get("defense", None)
        self.level = kwargs.get("level", None)
        self.race = kwargs.get("race", None)

    def can_be_normal_summoned(self) -> bool:
        """Determines if the monster can be normal summoned.

        Returns:
            bool: True if the monster can be normal summoned, False otherwise.
        """
        return self.level <= 4
    
    def can_be_special_summoned(self) -> bool:
        """Determines if the monster can be special summoned.

        Returns:
            bool: True if the monster can be special summoned, False otherwise.
        """
        return False # Placeholder implementation