from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.set import Set

from project.rsm_tools import get_rsm_from_ecfg
from project.matrix_tools import BooleanAdjacencies
from project.grammar_tools import ECFG

from pyformlang.cfg import CFG

from project.gql.interpreter.core.exceptions import (
    NotImplementedException,
    CastingException,
    TypingError,
)


class ContextFreeGrammar(Automaton):
    """
    Representation of Context Free Grammar.

    Attributes
    ----------
    cfg: CFG
        Internal CFG object
    """

    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def __str__(self) -> str:
        return self.cfg.to_text()

    @classmethod
    def from_text(cls, text: str) -> "ContextFreeGrammar":
        """
        Parameters
        ----------
        text: str
            String given in terms of CFG
            E.g. 'S -> a S
                  S -> epsilon'

        Returns
        -------
        cfg: ContextFreeGrammar
            Object transformed from text

        Raises
        ------
        CastingException
            If text violates CFG format
        """

        try:
            cfg = CFG.from_text(text)

            return cls(cfg)
        except ValueError as exception:
            raise CastingException("str", "CFG") from exception

    def intersect(self, other: "Automaton") -> "ContextFreeGrammar":
        """
        Parameters
        ----------
        other: FiniteAutomaton
            Finite automaton represents a regular expression

        Returns
        -------
        intersection: ContextFreeGrammar
            Intersection of ContextFreeGrammar and FiniteAutomaton

        Raises
        ------
        GQLTypeError
            If 'other' type is not GQLFA
        """

        if not isinstance(other, Automaton):
            raise TypingError(f"Expected FiniteAutomaton, got {str(type(other))}.")

        if isinstance(other, ContextFreeGrammar):
            raise TypingError(
                f"ContextFreeGrammar does not support intersection with another ContextFreeGrammar."
            )

        intersection = self.cfg.intersection(other.nfa)

        return ContextFreeGrammar(intersection)

    def union(self, other: "ContextFreeGrammar") -> "ContextFreeGrammar":
        """
        Parameters
        ----------
        other: ContextFreeGrammar
            A ContextFreeGrammar object

        Returns
        -------
        union: ContextFreeGrammar
            Union of ContextFreeGrammar with another ContextFreeGrammar
        """

        if isinstance(other, ContextFreeGrammar):
            return ContextFreeGrammar(self.cfg.union(other.cfg))

        raise NotImplementedException(
            "Union is implemented only between ContextFreeGrammar types."
        )

    def concatenate(self, other: "ContextFreeGrammar") -> "ContextFreeGrammar":
        """
        Parameters
        ----------
        other: ContextFreeGrammar
            A ContextFreeGrammar object

        Returns
        -------
        concatenation: ContextFreeGrammar
            Concatenation of ContextFreeGrammar with another ContextFreeGrammar
        """

        if isinstance(other, ContextFreeGrammar):
            return ContextFreeGrammar(self.cfg.concatenate(other.cfg))

        raise NotImplementedException(
            "ContextFreeGrammar support concatenation only with another ContextFreeGrammar."
        )

    def inverse(self):
        raise NotImplementedException(
            "ContextFreeGrammar does not support 'NOT' operation."
        )

    def kleene(self):
        raise NotImplementedException(
            "ContextFreeGrammar does not support '*' operation."
        )

    def set_start(self, start_states):
        raise NotImplementedException(
            "ContextFreeGrammar does not support set start operation."
        )

    def set_final(self, final_states):
        raise NotImplementedException(
            "ContextFreeGrammar does not support set final operation."
        )

    def add_start(self, start_states):
        raise NotImplementedException(
            "ContextFreeGrammar does not support add start operation."
        )

    def add_final(self, final_states):
        raise NotImplementedException(
            "ContextFreeGrammar does not support add final operation."
        )

    @property
    def start(self) -> Set:
        return Set(self.cfg.start_symbol.value)

    @property
    def final(self) -> Set:
        return Set(set(self.cfg.get_reachable_symbols()))

    @property
    def labels(self) -> Set:
        return Set(set(self.cfg.terminals))

    @property
    def edges(self):
        raise NotImplementedException(
            "ContextFreeGrammar does not support edges operation."
        )

    @property
    def vertices(self) -> Set:
        return Set(set(self.cfg.variables))

    def get_reachable(self) -> Set:
        """
        Get reachable vertices from the start symbol.

        Returns
        -------
        reachable: Set
            A Set of reachable vertices
        """

        ecfg = ECFG.from_cfg(self.cfg)
        rsm = get_rsm_from_ecfg(ecfg)

        rsm_bm = BooleanAdjacencies.from_rsm(rsm)
        tc = rsm_bm.get_transitive_closure()

        reachable = set()

        for i, j in zip(*tc.nonzero()):
            reachable.add((i, rsm_bm.states_box_variables.get(i, j), j))

        return Set(reachable)
