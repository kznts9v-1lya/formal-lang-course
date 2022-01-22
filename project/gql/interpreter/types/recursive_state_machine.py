from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.set import Set

# from project.gql.interpreter.types.finite_automaton import FiniteAutomaton

from pyformlang.cfg import CFG

from project.gql.interpreter.core.exceptions import (
    NotImplementedException,
    CastingException,
)


class RecursiveStateMachine(Automaton):
    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self.reachable = None

    def __str__(self):
        return self.cfg.to_text()

    @classmethod
    def from_text(cls, text: str):
        try:
            cfg = CFG.from_text(text)

            return cls(cfg)
        except ValueError as exception:
            raise CastingException("str", "CFG") from exception

    # def intersect(self, other) -> "RecursiveStateMachine":
    #     if isinstance(other, FiniteAutomaton):
    #         intersection = self.cfg.to_pda().intersection(other.nfa)
    #     else:
    #         raise CastingException("RecursiveStateMachine", str(type(other)))
    #
    #     return RecursiveStateMachine(intersection.to_cfg())

    def union(self, other) -> "RecursiveStateMachine":
        if isinstance(other, RecursiveStateMachine):
            return RecursiveStateMachine(self.cfg.union(other.cfg))

        raise NotImplementedException(
            "Union is implemented only between RecursiveStateMachine types."
        )

    def concatenate(self, other) -> "RecursiveStateMachine":
        if isinstance(other, RecursiveStateMachine):
            return RecursiveStateMachine(self.cfg.concatenate(other.cfg))

        raise NotImplementedException(
            "Concatenate is implemented only between RecursiveStateMachine types."
        )

    def inverse(self):
        raise NotImplementedException(
            "Inverse is not implemented for RecursiveStateMachine type."
        )

    def kleene(self):
        raise NotImplementedException(
            "Kleene is not implemented for RecursiveStateMachine type."
        )

    def set_start(self, start_states):
        pass

    def set_final(self, final_states):
        pass

    def add_start(self, start_states):
        pass

    def add_final(self, final_states):
        pass

    @property
    def start(self):
        return Set(set(self.cfg.start_symbol.to_text()))

    @property
    def final(self):
        raise NotImplementedException("RecursiveStateMachine.final")

    @property
    def labels(self):
        raise NotImplementedException("RecursiveStateMachine.labels")

    @property
    def edges(self):
        raise NotImplementedException("RecursiveStateMachine.edges")

    @property
    def vertices(self):
        return Set(set(self.cfg.variables))

    def get_reachable(self):
        raise NotImplementedException("RecursiveStateMachine.reachable")
