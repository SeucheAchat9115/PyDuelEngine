from pyduelengine.cards.monster import MonsterCard

class FusionMonsterCard(MonsterCard):
    """Class representing a Fusion Monster Card in the game."""
    def __init__(self, name, level, attribute, fusion_materials) -> None:
        """Initialize a Fusion Monster Card.
        
        Args:
            name (str): The name of the fusion monster card.
            level (int): The level of the fusion monster card.
            attribute (str): The attribute of the fusion monster card.
            fusion_materials (list): A list of materials required for fusion.
        """
        
        super().__init__(name, level, attribute)
        self.fusion_materials = fusion_materials