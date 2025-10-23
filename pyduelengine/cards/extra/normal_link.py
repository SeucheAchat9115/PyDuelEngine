from pyduelengine.cards.monster.normal_monster import NormalMonsterCard

class NormalLinkMonsterCard(NormalMonsterCard):
    """Class representing a Normal Link Monster Card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initialize a Normal Link Monster Card."""
        super().__init__(**kwargs)
