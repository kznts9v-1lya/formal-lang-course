from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.set import Set
from project.gql.interpreter.types.context_free_grammar import ContextFreeGrammar

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
    CastingException,
    TypingError,
)
from pyformlang.regular_expression import MisformedRegexError


class FiniteAutomaton(Automaton):
    """
    Representation of Finite Automaton.

    Attributes
    ----------
    nfa: NondeterministicFiniteAutomaton
        Internal nfa object
    """

    def __init__(self, nfa: NondeterministicFiniteAutomaton):
        self.nfa = nfa

    def __str__(self):
        return str(self.nfa.minimize().to_regex())

    def __eq__(self, other: "FiniteAutomaton") -> bool:
        return self.nfa.is_equivalent_to(other.nfa)

    @classmethod
    def from_graph(cls, graph: MultiDiGraph) -> "FiniteAutomaton":
        """
        Parameters
        ----------
        graph: MultiDiGraph
            Graph to transform into Finite Automaton

        Returns
        -------
        fa: FiniteAutomaton
            Finite Automaton transformed from graph
        """

        return cls(get_nfa_from_graph(graph))

    @classmethod
    def from_string(cls, regex_str: str) -> "FiniteAutomaton":
        """
        Parameters
        ----------
        regex_str: str
            Transform regex string into Finite Automaton

        Returns
        -------
        fa: FiniteAutomaton
            A FiniteAutomaton transformed from regex string

        Raises
        ------
        CastingException
            If the given string violates regular expression rules
        """

        try:
            return FiniteAutomaton(get_min_dfa_from_regex_str(regex_str))
        except MisformedRegexError as exception:
            raise CastingException("str", "Regex") from exception

    @property
    def start(self) -> Set:
        return Set(self.nfa.start_states)

    @property
    def final(self) -> Set:
        return Set(self.nfa.final_states)

    @property
    def labels(self) -> Set:
        return Set(self.nfa.symbols)

    @property
    def edges(self) -> Set:
        edges_set = set()

        edges_dict = self.nfa.to_dict()
        for u in edges_dict.keys():
            for label, v_set in edges_dict.get(u).items():
                for v in v_set:
                    edges_set.add((u, label, v))

        return Set(edges_set)

    @property
    def vertices(self) -> Set:
        return Set(self.nfa.states)

    def _intersect_fa(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        """
        Inner intersection function between two FiniteAutomatons.

        Parameters
        ----------
        other: FiniteAutomaton
            A Finite Automaton to intersect with

        Returns
        -------
        intersection: FiniteAutomaton
            Intersection between two FiniteAutomatons
        """

        left_bm = BooleanAdjacencies(self.nfa)
        right_bm = BooleanAdjacencies(other.nfa)

        intersection = left_bm.intersect(right_bm)

        return FiniteAutomaton(intersection.to_nfa())

    def _intersect_cfg(self, other: "ContextFreeGrammar") -> "ContextFreeGrammar":
        """
        Inner intersection function between two FiniteAutomatons.

        Parameters
        ----------
        other: ContextFreeGrammar
            A ContextFreeGrammar to intersect with

        Returns
        -------
        intersection: ContextFreeGrammar
             Intersection between two ContextFreeGrammar
        """

        intersection = other.intersect(self)

        return intersection

    def intersect(self, other: Automaton) -> Automaton:
        """
        Intersection function between two Automatons.

        Parameters
        ----------
        other: Union[ContextFreeGrammar, FiniteAutomaton]
            ContextFreeGrammar or FiniteAutomaton object

        Returns
        -------
        intersection: Automaton
            ContextFreeGrammar, if other is ContextFreeGrammar
            FiniteAutomaton, if other is FiniteAutomaton

        Raises
        ------
        TypingError
            If other does not represent ContextFreeGrammar or FiniteAutomaton
        """

        if isinstance(other, FiniteAutomaton):
            return self._intersect_fa(other)
        elif isinstance(other, ContextFreeGrammar):
            return self._intersect_cfg(other)

        raise TypingError(f"Expected Automaton, got {str(type(other))}.")

    def union(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        """
        Parameters
        ----------
        other: FiniteAutomaton
            Right FiniteAutomaton

        Returns
        -------
        union: FiniteAutomaton
            Intersection between two FiniteAutomatons
        """
        return FiniteAutomaton(self.nfa.union(other.nfa).to_deterministic())

    def concatenate(self, other: "FiniteAutomaton") -> "FiniteAutomaton":
        """
        Parameters
        ----------
        other: FiniteAutomaton
            Right FiniteAutomaton

        Returns
        -------
        dot: FiniteAutomaton
            Concatenation between two FiniteAutomatons
        """

        left_regex = self.nfa.to_regex()
        right_regex = other.nfa.to_regex()

        return FiniteAutomaton(
            left_regex.concatenate(right_regex).to_epsilon_nfa().to_deterministic()
        )

    def inverse(self) -> "FiniteAutomaton":
        """
        Get complement FiniteAutomaton.

        Returns
        -------
        complement: FiniteAutomaton
            A complement for FiniteAutomaton
        """

        return FiniteAutomaton(self.nfa.get_complement().to_deterministic())

    def kleene(self) -> "FiniteAutomaton":
        """
        Returns
        -------
        kleene: FiniteAutomaton
            A kleene star for FiniteAutomaton
        """

        return FiniteAutomaton(self.nfa.kleene_star().to_deterministic())

    def set_start(self, start_states: Set) -> "FiniteAutomaton":
        nfa = set_nfa_states(self.nfa, start_states=start_states.set)

        return FiniteAutomaton(nfa)

    def set_final(self, final_states: Set) -> "FiniteAutomaton":
        nfa = set_nfa_states(self.nfa, final_states=final_states.set)

        return FiniteAutomaton(nfa)

    def add_start(self, start_states: Set) -> "FiniteAutomaton":
        nfa = add_nfa_states(self.nfa, start_states=start_states.set)

        return FiniteAutomaton(nfa)

    def add_final(self, final_states: Set) -> "FiniteAutomaton":
        nfa = add_nfa_states(self.nfa, final_states=final_states.set)

        return FiniteAutomaton(nfa)

    @staticmethod
    def _get_reachable(nfa: NondeterministicFiniteAutomaton) -> set:
        """
        Internal function to get reachable states of NondeterministicFiniteAutomaton.

        Parameters
        ----------
        nfa: NondeterministicFiniteAutomaton
            A Nondeterministic Finite Automaton

        Returns
        -------
        reachable: set
            Reachable states set
        """

        bm = BooleanAdjacencies(nfa)

        return get_reachable(bm)

    def get_reachable(self) -> Set:
        """
        Returns
        -------
        reachable: Set
            Reachable vertices set
        """

        return Set(FiniteAutomaton._get_reachable(self.nfa))
