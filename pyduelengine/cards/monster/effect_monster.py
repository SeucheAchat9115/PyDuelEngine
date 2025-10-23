from pyduelengine.cards.monster.normal_monster import NormalMonsterCard

class EffectMonsterCard(NormalMonsterCard):
    """A class representing an effect monster card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initializes a EffectMonsterCard object."""
        super().__init__(**kwargs)