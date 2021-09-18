from typing import Set

import networkx as nx
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    EpsilonNFA,
    NondeterministicFiniteAutomaton,
)
from pyformlang.regular_expression import Regex

__all__ = ["get_min_dfa", "get_nfa"]


def get_min_dfa(regex: str) -> DeterministicFiniteAutomaton:
    """
    Based on a regular expression given as a string, builds an Deterministic Finite Automaton.

    Parameters
    ----------
    regex: str
        The string representation of a regular expression

    Returns
    -------
    DeterministicFiniteAutomaton
        Deterministic Finite Automaton equivalent to a given regular expression as a string

    Raises
    ------
    MisformedRegexError
        If given as string regular expression has an irregular format
    """

    re = Regex(regex)
    e_nfa = re.to_epsilon_nfa()
    min_dfa = e_nfa.minimize()

    return min_dfa


def get_nfa(
    graph: nx.MultiDiGraph, start_nodes: Set[int] = None, final_nodes: Set[int] = None
) -> NondeterministicFiniteAutomaton:
    """
    Generates an Epsilon Nondeterministic Finite Automaton for a specified graph and start or end nodes.

    If start_nodes and final_nodes are not specified, all nodes are considered start and end.

    Parameters
    ----------
    graph: nx.MultiDiGraph
        Graph to generating an Epsilon Nondeterministic Finite Automaton from it
    start_nodes: Set[int], default = None
        Set of start nodes to configure Epsilon Nondeterministic Finite Automaton
    final_nodes: Set[int], default = None
        Set of final nodes to configure Epsilon Nondeterministic Finite Automaton

    Returns
    -------
    EpsilonNFA
        Epsilon Nondeterministic Finite Automaton equivalent to a specified graph

    Raises
    ------
    ValueError
        If number of non-existent in the specified graph node is used
    """

    nfa = NondeterministicFiniteAutomaton()

    for node_from, node_to in graph.edges():
        edge_label = graph.get_edge_data(node_from, node_to)[0]["label"]
        nfa.add_transition(node_from, edge_label, node_to)

    if not start_nodes and not final_nodes:
        for state in nfa.states:
            nfa.add_start_state(state)
            nfa.add_final_state(state)

    if start_nodes:
        for start_node in start_nodes:
            if start_node not in range(graph.number_of_nodes()):
                raise ValueError(
                    f"Node {start_node} does not exists in specified graph"
                )

        # Does not spoil the original states
        for node in start_nodes:
            state = list(nfa.states)[node]
            nfa.add_start_state(state)

    if final_nodes:
        for final_node in final_nodes:
            if final_node not in range(graph.number_of_nodes()):
                raise ValueError(
                    f"Node {final_node} does not exists in specified graph"
                )

        # Does not spoil the original states
        for node in final_nodes:
            state = list(nfa.states)[node]
            nfa.add_final_state(state)

    return nfa
