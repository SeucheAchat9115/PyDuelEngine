from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

from pyduelengine.action.pass_priority import PassPriorityAction

if TYPE_CHECKING:
    from pyduelengine.player.player import Player
    from pyduelengine.action.activate_effect import ActivateEffectAction
    from pyduelengine.game.gamestate import GameState
    from pyduelengine.game.action_generator import ActionGenerator
from pyduelengine.effect.effect import Effect

@dataclass
class Context:
    """
    The 'sandbox' API for an effect. This is passed to effect.on_activate().
    It gives the effect a safe way to interact with the game.
    """
    gamestate: GameState
    activating_player: Player
    chain_manager: ChainManager
    chain_link_number: int
    is_negated: bool = False

@dataclass
class ChainLink:
    """
    A single link on the chain. It binds an Effect to its specific Context.
    """
    effect: Effect
    context: Context

class ChainManager():
    """Manages the chain of actions in the game."""
    def __init__(
        self, 
        gamestate: GameState,
        action_generator: ActionGenerator
    ) -> None:
        """Initializes a ChainManager object.
        Args:
            gamestate (GameState): The current game state.
            action_generator (ActionGenerator): The action generator for generating legal actions.
        """
        self.gamestate = gamestate
        self.action_generator = action_generator
        self.chain_stack: list[ChainLink] = []

        # A dictionary to track who has passed priority.
        self._player_passed: dict[Player, bool] = {}

    def is_chain_active(self) -> bool:
        """Is a chain currently being built or resolved?
        
        Returns:
            bool: True if a chain is active, False otherwise.
        """
        return len(self.chain_stack) > 0

    def start_chain(
        self,
        player: Player,
        effect: Effect,
    ) -> None:
        """Starts a new chain with the given effect activated by the player.

        Args:
            player (Player): The player activating the effect.
            effect (Effect): The effect being activated.
        """

        # 1. Clear any old data
        self.chain_stack = []
        self._player_passed = {
            self.gamestate.player1: False,
            self.gamestate.player2: False
        }

        # 2. Add Chain Link 1
        self._add_to_chain(player, effect)

        # 3. Start the "reaction loop" by passing priority to the opponent
        opponent = self.gamestate.get_opponent(player)
        self._build_chain(current_responder=opponent)

    def negate_effect_at(self, link_number: int):
        """
        API for effects (like Ash Blossom) to call via the Context.
        Finds a ChainLink and flags it as 'is_negated'.

        Args:
            link_number (int): The chain link number to negate.
        """

        target_index = link_number - 1
        if 0 <= target_index < len(self.chain_stack):
            target_context = self.chain_stack[target_index].context
            target_context.is_negated = True
            print(f"Marked CL{link_number} as 'is_negated'.")
        else:
            print(f"WARNING: Tried to negate invalid CL{link_number}.")
    
    def _build_chain(
        self,
        current_responder: Player
    ) -> None:
        """
        This is the "reaction" loop. It asks the current_responder
        for an action and handles the response.
        
        This method calls itself recursively, passing priority
        back and forth until both players pass.
        
        Args:
            current_responder (Player): The player whose turn it is to respond.
        """

        # 1. Get all valid *responses* (SS2+) from the generator
        # The generator is smart enough to check spell speeds.
        legal_actions = self.action_generator.get_chain_responses(current_responder)
        
        # 2. Get the agent's choice
        chosen_action = current_responder.agent.get_action(self.gamestate, legal_actions)

        # 3. Handle the chosen action
        if isinstance(chosen_action, PassPriorityAction):
            self._player_passed[current_responder] = True
            opponent = self.gamestate.get_opponent(current_responder)

            # Check if *both* players have passed consecutively
            if self._player_passed[opponent]:
                # Both players passed. The chain is "closed".
                self._resolve_chain()
            else:
                # Only this player passed. Pass priority to the opponent.
                self._build_chain(current_responder=opponent)
        elif isinstance(chosen_action, ActivateEffectAction):
            new_effect = chosen_action.effect_to_activate

            # 1. Add the new effect to the chain
            self._add_to_chain(current_responder, new_effect)
            # 2. An action was taken, so reset the pass flags
            self._player_passed = {p: False for p in self._player_passed}
            # 3. Pass priority back to the *opponent*
            opponent = self.gamestate.get_opponent(current_responder)
            self._build_chain(current_responder=opponent)

    def _add_to_chain(
        self,
        player: Player,
        effect: Effect
    ) -> None:
        """Adds a new link to the chain."""

        new_context = Context(
            game_state=self.gamestate,
            activating_player=player,
            chain_manager=self,
            chain_link_number=len(self.chain_stack) + 1
        )
        new_chain_link = ChainLink(effect=effect, context=new_context)
        self.chain_stack.append(new_chain_link)

    def _resolve_chain(self):
        """
        Resolves the built chain in LIFO (Last-In, First-Out) order.
        Called by _build_chain() when both players pass.
        """
        print("Chain Resolution Started ...")
        
        while self.chain_stack:
            # 1. Get the last link added to the stack
            link_to_resolve = self.chain_stack.pop()
            effect = link_to_resolve.effect
            context = link_to_resolve.context
            
            print(f"Resolving Chain Link {context.chain_link_number}] '{effect.owner.name}'")
            
            # 2. Call the card's actual logic. (context.is_negated flag checked internally.)
            effect.on_activate(context)