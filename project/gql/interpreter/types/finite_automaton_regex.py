from typing import Union

from project.gql.interpreter.types.type import Type
from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.set import Set

from project.automaton_tools import (
    get_min_dfa_from_regex_str,
    get_nfa_from_graph,
    set_nfa_states,
    add_nfa_states,
)
from project.matrix_tools import BooleanAdjacencies

from networkx import MultiDiGraph
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton

from project.gql.interpreter.exceptions import NotImplementedException, CastingException
from pyformlang.regular_expression import MisformedRegexError


class Regex(Type):
    def __init__(self, regex_str: str):
        self.regex_str = regex_str

    def __str__(self):
        regex_str = self.regex_str

        while regex_str[0] == "(" and regex_str[-1] == ")":
            regex_str = regex_str[1:-1]

        return regex_str

    def __eq__(self, other: Union["Regex", "FiniteAutomaton"]) -> bool:
        left_nfa = Regex.from_str(self.regex_str).nfa

        if isinstance(other, Regex):
            right_nfa = Regex.from_str(other.regex_str).nfa

            return left_nfa.is_equivalent_to(right_nfa)
        elif isinstance(other, FiniteAutomaton):
            return left_nfa.is_equivalent_to(other.nfa)
        else:
            raise CastingException(left_type="Regex", right_type=str(other))

    @classmethod
    def from_str(cls, regex_str: str) -> "FiniteAutomaton":
        try:
            return FiniteAutomaton(get_min_dfa_from_regex_str(regex_str))
        except MisformedRegexError as exception:
            raise CastingException("str", "Regex") from exception

    def intersect(self, other: Union["Regex", "FiniteAutomaton"]) -> "FiniteAutomaton":
        left_nfa = Regex.from_str(self.regex_str)

        if isinstance(other, Regex):
            right_nfa = Regex.from_str(other.regex_str)

            return left_nfa.intersect(right_nfa)
        elif isinstance(other, FiniteAutomaton):
            return left_nfa.intersect(other)
        else:
            raise CastingException(left_type="Regex", right_type=str(other))

    def union(self, other: "Regex") -> "Regex":
        return Regex(f"({self.regex_str}|{other.regex_str})")

    def concatenate(self, other: "Regex") -> "Regex":
        return Regex(f"({self.regex_str}.{other.regex_str})")

    def inverse(self) -> "FiniteAutomaton":
        nfa = Regex.from_str(self.regex_str)

        return nfa.inverse()

    def kleene(self) -> "Regex":
        return Regex(f"({self.regex_str})*")


class FiniteAutomaton(Automaton):
    def __init__(self, nfa: NondeterministicFiniteAutomaton):
        self.nfa = nfa

    def __str__(self):
        return str(self.nfa.to_dict())

    @classmethod
    def from_graph(cls, graph: MultiDiGraph):
        return cls(get_nfa_from_graph(graph))

    @property
    def start(self):
        return Set(self.nfa.start_states)

    @property
    def final(self):
        return Set(self.nfa.final_states)

    @property
    def labels(self):
        return Set(self.nfa.symbols)

    @property
    def edges(self):
        edges_set = set()

        edges_dict = self.nfa.to_dict()
        for u in edges_dict.keys():
            for label, v_set in edges_dict.get(u).items():
                for v in v_set:
                    edges_set.add((u, label, v))

        return Set(edges_set)

    @property
    def vertices(self):
        return Set(self.nfa.states)

    def intersect(self, other: Union["FiniteAutomaton", Regex]) -> "FiniteAutomaton":
        left_bm = BooleanAdjacencies(self.nfa)

        if isinstance(other, FiniteAutomaton):
            right_bm = BooleanAdjacencies(other.nfa)

            return FiniteAutomaton(left_bm.intersect(right_bm).to_nfa())
        elif isinstance(other, Regex):
            right_bm = BooleanAdjacencies(Regex.from_str(other.regex_str).nfa)

            return FiniteAutomaton(left_bm.intersect(right_bm).to_nfa())
        else:
            raise CastingException(left_type="FiniteAutomaton", right_type=str(other))

    def union(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        return FiniteAutomaton(self.nfa.union(other.nfa).to_deterministic())

    def concatenate(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        left_regex = self.nfa.to_regex()
        right_regex = other.nfa.to_regex()

        return FiniteAutomaton(
            left_regex.concatenate(right_regex).to_epsilon_nfa().to_deterministic()
        )

    def inverse(self) -> "FiniteAutomaton":
        inverted_nfa = self.nfa.copy()

        for state in inverted_nfa.states:
            inverted_nfa.add_final_state(state)

        for state in self.nfa.final_states:
            inverted_nfa.remove_final_state(state)

        return FiniteAutomaton(inverted_nfa)

    def kleene(self) -> "FiniteAutomaton":
        return FiniteAutomaton(self.nfa.kleene_star().to_deterministic())

    def set_start(self, start_states: Set):
        self.nfa = set_nfa_states(self.nfa, start_states=start_states.set)

    def set_final(self, final_states: Set):
        self.nfa = set_nfa_states(self.nfa, final_states=final_states.set)

    def add_start(self, start_states: Set):
        self.nfa = add_nfa_states(self.nfa, start_states=start_states.set)

    def add_final(self, final_states: Set):
        self.nfa = add_nfa_states(self.nfa, final_states=final_states.set)

    def get_reachable(self):
        raise NotImplementedException("TODO")
