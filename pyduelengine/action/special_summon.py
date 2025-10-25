from pyduelengine.action.action import Action

class SpecialSummonAction(Action):
    """An action representing the special summon of a monster card."""
    def __init__(self, **kwargs) -> None:
        """Initializes a SpecialSummonAction object.

        Args:
            owner (Player): The player performing the action.
            card (NormalMonsterCard): The monster card to be special summoned.
        """
        super().__init__(**kwargs)
        self.card = kwargs.get("card", None)
        self.owner = kwargs.get("owner", None)