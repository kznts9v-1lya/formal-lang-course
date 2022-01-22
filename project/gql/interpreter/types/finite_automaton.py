from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.set import Set
from project.gql.interpreter.types.recursive_state_machine import RecursiveStateMachine

from project.matrix_tools import BooleanAdjacencies
from project.path_querying_tools import get_reachable
from project.automaton_tools import (
    get_min_dfa_from_regex_str,
    get_nfa_from_graph,
    set_nfa_states,
    add_nfa_states,
)

from networkx import MultiDiGraph
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton

from project.gql.interpreter.core.exceptions import (
    NotImplementedException,
    CastingException,
)
from pyformlang.regular_expression import MisformedRegexError


class FiniteAutomaton(Automaton):
    def __init__(self, nfa: NondeterministicFiniteAutomaton, reachable: set = None):
        self.nfa = nfa
        self.reachable = reachable or self._get_reachable(nfa)

    def __str__(self):
        return str(self.nfa.minimize().to_regex())

    def __eq__(self, other: "FiniteAutomaton") -> bool:
        return self.nfa.is_equivalent_to(other.nfa)

    @classmethod
    def from_graph(cls, graph: MultiDiGraph) -> "FiniteAutomaton":
        return cls(get_nfa_from_graph(graph))

    @classmethod
    def from_string(cls, regex_str: str) -> "FiniteAutomaton":
        try:
            return FiniteAutomaton(get_min_dfa_from_regex_str(regex_str))
        except MisformedRegexError as exception:
            raise CastingException("str", "Regex") from exception

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

    def _intersect_fa(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        left_bm = BooleanAdjacencies(self.nfa)
        right_bm = BooleanAdjacencies(other.nfa)

        intersection = left_bm.intersect(right_bm)

        return FiniteAutomaton(intersection.to_nfa(), get_reachable(intersection))

    def _intersect_rsm(self, other: "RecursiveStateMachine") -> "RecursiveStateMachine":
        left_bm = BooleanAdjacencies(self.nfa)
        right_bm = BooleanAdjacencies(other.rsm)

        intersection = left_bm.intersect(right_bm)

    def intersect(self, other):
        if isinstance(other, FiniteAutomaton):
            return self._intersect_fa(other)
        elif isinstance(other, RecursiveStateMachine):
            return self._intersect_rsm(other)
        else:
            raise CastingException("FiniteAutomaton", str(type(other)))

    def union(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        return FiniteAutomaton(self.nfa.union(other.nfa).to_deterministic())

    def concatenate(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        left_regex = self.nfa.to_regex()
        right_regex = other.nfa.to_regex()

        return FiniteAutomaton(
            left_regex.concatenate(right_regex).to_epsilon_nfa().to_deterministic()
        )

    def inverse(self) -> "FiniteAutomaton":
        return FiniteAutomaton(self.nfa.get_complement().to_deterministic())

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

    @staticmethod
    def _get_reachable(nfa: NondeterministicFiniteAutomaton) -> set:
        bm = BooleanAdjacencies(nfa)

        return get_reachable(bm)

    def get_reachable(self):
        return Set(self.reachable)
