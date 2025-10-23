from .monster import MonsterCard

class LinkMonsterCard(MonsterCard):
    """Class representing a Link Monster Card in the game."""
    def __init__(self, name, level, attribute, link_materials) -> None:
        """Initialize a Link Monster Card.

        Args:
            name (str): The name of the link monster card.
            level (int): The level of the link monster card.
            attribute (str): The attribute of the link monster card.
            link_materials (list): A list of materials required for link summoning.
        """
        super().__init__(name, level, attribute)
        self.link_materials = link_materials
