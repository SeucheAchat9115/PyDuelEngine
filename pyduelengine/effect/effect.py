class Effect():
    def __init__(self):
        pass
    def activate(self, gamestate, player):
        """Activate the effect for the given player in the gamestate."""
        raise NotImplementedError("This method should be overridden by subclasses.")