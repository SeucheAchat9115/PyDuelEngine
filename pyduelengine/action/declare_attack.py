from pyduelengine.action.action import Action

class DeclareAttackAction(Action):
    def __init__(self, attacker_card_id: int, defender_card_id: int) -> None:
        """Initializes a DeclareAttackAction object.

        Args:
            attacker_card_id (int): The ID of the attacking card.
            defender_card_id (int): The ID of the defending card.
        """
        self.attacker_card_id = attacker_card_id
        self.defender_card_id = defender_card_id