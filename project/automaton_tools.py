from typing import Set

import networkx as nx
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
    State,
)
from pyformlang.regular_expression import Regex

__all__ = [
    "get_min_dfa_from_regex_str",
    "get_min_dfa_from_regex",
    "get_nfa_from_graph",
    "check_regex_equality",
    "set_nfa_states",
    "add_nfa_states",
]


def get_min_dfa_from_regex_str(regex_str: str) -> DeterministicFiniteAutomaton:
    """
    Based on a regular expression given as a Regex string, builds a Deterministic Finite Automaton.

    Parameters
    ----------
    regex_str: str
        The Regex string representation of a regular expression

    Returns
    -------
    DeterministicFiniteAutomaton
        Deterministic Finite Automaton equivalent to a given regular expression as a Regex string
    """

    return get_min_dfa_from_regex(Regex(regex_str))


def get_min_dfa_from_regex(regex: Regex) -> DeterministicFiniteAutomaton:
    """
    Based on a regular expression given as Regex, builds a Deterministic Finite Automaton.

    Parameters
    ----------
    regex: Regex
        The Regex representation of a regular expression

    Returns
    -------
    DeterministicFiniteAutomaton
        Deterministic Finite Automaton equivalent to a given regular expression as a Regex
    """

    e_nfa = regex.to_epsilon_nfa()
    min_dfa = e_nfa.minimize()

    return min_dfa


def get_nfa_from_graph(
    graph: nx.MultiDiGraph,
    start_node_nums: Set[int] = None,
    final_node_nums: Set[int] = None,
) -> NondeterministicFiniteAutomaton:
    """
    Generates an Nondeterministic Finite Automaton for a specified graph and start or final nodes.

    If start_nodes or final_nodes are not specified, all nodes are considered start or final respectively.

    Parameters
    ----------
    graph: nx.MultiDiGraph
        Graph to generating an Nondeterministic Finite Automaton from it
    start_node_nums: Set[int], default = None
        Set of start node numbers to configure Nondeterministic Finite Automaton,
        which must exist in the graph
    final_node_nums: Set[int], default = None
        Set of final node numbers to configure Nondeterministic Finite Automaton,
        which must exist in the graph

    Returns
    -------
    NondeterministicFiniteAutomaton
        Nondeterministic Finite Automaton equivalent to a specified graph

    Raises
    ------
    ValueError
        If non-existent in the specified graph node number is used
    """

    nums_nodes = dict()

    if graph.number_of_nodes() != 0:
        nums_nodes = {num: node for num, node in enumerate(graph.nodes)}

    start_nums_nodes = dict()
    final_nums_nodes = dict()

    if not start_node_nums:
        for num, node in nums_nodes.items():
            start_nums_nodes[num] = node
    else:
        if not start_node_nums.issubset(set(nums_nodes.keys())):
            raise ValueError(
                f"Non-existent start node numbers in the graph: "
                f"{start_node_nums.difference(set(nums_nodes.keys()))}"
            )

        for num in start_node_nums:
            start_nums_nodes[num] = nums_nodes[num]

    if not final_node_nums:
        for num, node in nums_nodes.items():
            final_nums_nodes[num] = node
    else:
        if not final_node_nums.issubset(set(nums_nodes.keys())):
            raise ValueError(
                f"Non-existent final node numbers in the graph: "
                f"{final_node_nums.difference(set(nums_nodes.keys()))}"
            )

        for num in final_node_nums:
            final_nums_nodes[num] = nums_nodes[num]

    nfa = NondeterministicFiniteAutomaton()

    for node in nums_nodes.values():
        nfa.states.add(State(node))

    for node_from, node_to in graph.edges():
        edge_label = graph.get_edge_data(node_from, node_to)[0]["label"]
        nfa.add_transition(node_from, edge_label, node_to)

    for num in start_nums_nodes.keys():
        start_state = list(nfa.states)[num]
        nfa.add_start_state(start_state)

    for num in final_nums_nodes.keys():
        final_state = list(nfa.states)[num]
        nfa.add_final_state(final_state)

    return nfa


def set_nfa_states(
    nfa: NondeterministicFiniteAutomaton,
    start_states: Set[State] = None,
    final_states: Set[State] = None,
) -> NondeterministicFiniteAutomaton:
    new_nfa = nfa.copy()

    new_nfa._start_state = set()
    new_nfa._final_states = set()

    if start_states:
        for state in start_states:
            new_nfa.add_start_state(state)

    if final_states:
        for state in final_states:
            new_nfa.add_final_state(state)

    return new_nfa


def add_nfa_states(
    nfa: NondeterministicFiniteAutomaton,
    start_states: Set[State] = None,
    final_states: Set[State] = None,
) -> NondeterministicFiniteAutomaton:
    new_nfa = nfa.copy()

    if start_states:
        for state in start_states:
            new_nfa.add_start_state(state)

    if final_states:
        for state in final_states:
            new_nfa.add_final_state(state)

    return new_nfa


def check_regex_equality(regex1: Regex, regex2: Regex) -> bool:
    """
    Check whether Regex1 is equivalent to Regex2.
    It means their languages are equal.

    Parameters
    ----------
    regex1: Regex
        First regex
    regex2: Regex
        Second regex

    Returns
    -------
    bool:
        True if regex1 is equivalent to regex2
        False otherwise
    """

    return get_min_dfa_from_regex(regex1).is_equivalent_to(
        get_min_dfa_from_regex(regex2)
    )
