from project.gql.interpreter.types.automaton import Automaton
from project.automaton_tools import get_nfa_from_graph, set_nfa_states, add_nfa_states
from project.matrix_tools import BooleanAdjacencies

from networkx import MultiDiGraph
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton

from project.gql.interpreter.exceptions import NotImplementedException


class FiniteAutomaton(Automaton):
    def __init__(self, nfa: NondeterministicFiniteAutomaton):
        self.nfa = nfa

    def __str__(self):
        return str(self.nfa.to_dict())

    @classmethod
    def from_graph(cls, graph: MultiDiGraph):
        return cls(get_nfa_from_graph(graph))

    def intersect(self, other: "FiniteAutomaton"):
        left_nfa = BooleanAdjacencies(self.nfa)
        right_nfa = BooleanAdjacencies(other.nfa)

        intersection_nfa = left_nfa.intersect(right_nfa).to_nfa()

        return FiniteAutomaton(intersection_nfa)

    def union(self, other: "FiniteAutomaton"):
        return FiniteAutomaton(self.nfa.union(other.nfa).to_deterministic())

    def concatenate(self, other: "FiniteAutomaton"):
        left_regex = self.nfa.to_regex()
        right_regex = other.nfa.to_regex()

        return FiniteAutomaton(left_regex.concatenate(right_regex).to_epsilon_nfa().to_deterministic())

    def inverse(self):
        inverted_nfa = self.nfa.copy()

        for state in inverted_nfa.states:
            inverted_nfa.add_final_state(state)

        for state in self.nfa.final_states:
            inverted_nfa.remove_final_state(state)

        return FiniteAutomaton(inverted_nfa)

    def kleene(self):
        return FiniteAutomaton(self.nfa.kleene_star().to_deterministic())

    def set_start_states(self, start_states):
        self.nfa = set_nfa_states(self.nfa, start_states=start_states)

    def set_final_states(self, final_states):
        self.nfa = set_nfa_states(self.nfa, final_states=final_states)

    def add_start_states(self, start_states):
        self.nfa = add_nfa_states(self.nfa, start_states=start_states)

    def add_final_states(self, final_states):
        self.nfa = add_nfa_states(self.nfa, final_states=final_states)

    def get_reachable_states(self):
        raise NotImplementedException("TODO")

    @property
    def start_states(self):
        return self.nfa.start_states

    @property
    def final_states(self):
        return self.nfa.final_states

    @property
    def symbols(self):
        return self.nfa.symbols

    @property
    def transitions(self):
        return self.nfa.to_dict()

    @property
    def states(self):
        return self.nfa.states
