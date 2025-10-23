from pyduelengine.cards.monster.normal_monster import NormalMonsterCard

class NormalFusionMonsterCard(NormalMonsterCard):
    """Class representing a Fusion Monster Card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initialize a Fusion Monster Card."""
        super().__init__(**kwargs)