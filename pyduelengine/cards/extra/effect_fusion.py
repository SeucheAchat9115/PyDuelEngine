from pyduelengine.cards.extra.normal_fusion import NormalFusionMonsterCard

class EffectFusionMonsterCard(NormalFusionMonsterCard):
    """Class representing an Effect Fusion Monster Card in the game."""
    def __init__(self, **kwargs) -> None:
        """Initialize a Effect Fusion Monster Card."""
        super().__init__(**kwargs)