from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.set import Set

from project.rsm_tools import get_rsm_from_ecfg
from project.matrix_tools import BooleanAdjacencies
from project.grammar_tools import ECFG

from pyformlang.cfg import CFG

from project.gql.interpreter.core.exceptions import (
    NotImplementedException,
    CastingException,
)


class ContextFreeGrammar(Automaton):
    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def __str__(self) -> str:
        return self.cfg.to_text()

    @classmethod
    def from_text(cls, text: str) -> "ContextFreeGrammar":
        try:
            cfg = CFG.from_text(text)

            return cls(cfg)
        except ValueError as exception:
            raise CastingException("str", "CFG") from exception

    def intersect(self, other) -> "ContextFreeGrammar":
        if not isinstance(other, Automaton):
            raise CastingException("ContextFreeGrammar", str(type(other)))

        if isinstance(other, ContextFreeGrammar):
            raise CastingException("ContextFreeGrammar", str(type(other)))

        intersection = self.cfg.intersection(other.nfa)

        return ContextFreeGrammar(intersection)

    def union(self, other) -> "ContextFreeGrammar":
        if isinstance(other, ContextFreeGrammar):
            return ContextFreeGrammar(self.cfg.union(other.cfg))

        raise NotImplementedException(
            "Union is implemented only between ContextFreeGrammar types."
        )

    def concatenate(self, other) -> "ContextFreeGrammar":
        if isinstance(other, ContextFreeGrammar):
            return ContextFreeGrammar(self.cfg.concatenate(other.cfg))

        raise NotImplementedException(
            "Concatenate is implemented only between ContextFreeGrammar types."
        )

    def inverse(self):
        raise NotImplementedException(
            "Inverse is not implemented for ContextFreeGrammar type."
        )

    def kleene(self):
        raise NotImplementedException(
            "Kleene is not implemented for ContextFreeGrammar type."
        )

    def set_start(self, start_states):
        raise NotImplementedException(
            "Set start is not implemented for ContextFreeGrammar type."
        )

    def set_final(self, final_states):
        NotImplementedException(
            "Set final is not implemented for ContextFreeGrammar type."
        )

    def add_start(self, start_states):
        NotImplementedException(
            "Add start is not implemented for ContextFreeGrammar type."
        )

    def add_final(self, final_states):
        NotImplementedException(
            "Add final is not implemented for ContextFreeGrammar type."
        )

    @property
    def start(self):
        return Set(self.cfg.start_symbol.value)

    @property
    def final(self):
        raise NotImplementedException(
            "Final is not implemented for ContextFreeGrammar type."
        )

    @property
    def labels(self):
        raise NotImplementedException(
            "Labels is not implemented for ContextFreeGrammar type."
        )

    @property
    def edges(self):
        raise NotImplementedException(
            "Edges is not implemented for ContextFreeGrammar type."
        )

    @property
    def vertices(self) -> Set:
        return Set(set(self.cfg.variables))

    def get_reachable(self) -> Set:
        ecfg = ECFG.from_cfg(self.cfg)
        rsm = get_rsm_from_ecfg(ecfg)

        rsm_bm = BooleanAdjacencies.from_rsm(rsm)
        tc = rsm_bm.get_transitive_closure()

        reachable = set()

        for i, j in zip(*tc.nonzero()):
            reachable.add((i, rsm_bm.states_box_variables.get(i, j), j))

        return Set(reachable)
