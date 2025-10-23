from pyduelengine.cards.extra.normal_link import NormalLinkMonsterCard

class EffectLinkMonsterCard(NormalLinkMonsterCard):
    """Class representing a Effect Link Monster Card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initialize a Effect Link Monster Card."""
        super().__init__(**kwargs)
