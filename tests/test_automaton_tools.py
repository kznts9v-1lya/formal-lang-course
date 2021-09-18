from typing import Iterable

import pytest
from pyformlang.finite_automaton import (
    Symbol,
    State,
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
)
from pyformlang.regular_expression import MisformedRegexError

from project import get_two_cycles, Graph
from project.automaton_tools import *


def test_wrong_regex() -> None:
    with pytest.raises(MisformedRegexError):
        get_min_dfa("*|wrong_regex|*")


def test_dfa() -> None:
    min_dfa = get_min_dfa("i* l* y* a* | 1901")

    assert min_dfa.is_deterministic()


def test_min_dfa() -> None:
    actual_dfa = get_min_dfa("i* l* y* a* | 1901")
    expected_min_dfa = actual_dfa.minimize()

    assert actual_dfa.is_equivalent_to(expected_min_dfa) and len(
        actual_dfa.states
    ) == len(expected_min_dfa.states)


@pytest.mark.parametrize(
    "actual_regex, expected_word, not_expected_word",
    [
        ("", [], [Symbol("*")]),
        (
            "i* l* y* a* | 1901",
            [Symbol("i"), Symbol("l"), Symbol("y"), Symbol("a")],
            [Symbol("i"), Symbol("l"), Symbol("y"), Symbol("a"), Symbol("1901")],
        ),
        (
            "(a | b)* 00* | 11*",
            [Symbol("a"), Symbol("a"), Symbol("00"), Symbol("00"), Symbol("00")],
            [Symbol("a"), Symbol("b"), Symbol("11")],
        ),
    ],
)
def test_min_dfa_accepts(
    actual_regex: str,
    expected_word: Iterable[Symbol],
    not_expected_word: Iterable[Symbol],
) -> None:
    actual_min_dfa = get_min_dfa(actual_regex)

    if actual_regex == "":
        assert actual_min_dfa.is_empty()
    else:
        assert actual_min_dfa.accepts(expected_word) and not actual_min_dfa.accepts(
            not_expected_word
        )


def test_get_min_dfa() -> None:
    expected_min_dfa = DeterministicFiniteAutomaton()

    state_0 = State(0)
    state_1 = State(1)
    state_2 = State(2)
    state_3 = State(3)

    symbol_i = Symbol("i")
    symbol_l = Symbol("l")
    symbol_y = Symbol("y")
    symbol_a = Symbol("a")

    expected_min_dfa.add_start_state(state_0)

    expected_min_dfa.add_final_state(state_0)
    expected_min_dfa.add_final_state(state_1)
    expected_min_dfa.add_final_state(state_2)
    expected_min_dfa.add_final_state(state_3)

    expected_min_dfa.add_transition(state_0, symbol_i, state_0)
    expected_min_dfa.add_transition(state_0, symbol_l, state_1)
    expected_min_dfa.add_transition(state_0, symbol_y, state_2)
    expected_min_dfa.add_transition(state_0, symbol_a, state_3)

    expected_min_dfa.add_transition(state_1, symbol_l, state_1)
    expected_min_dfa.add_transition(state_1, symbol_y, state_2)
    expected_min_dfa.add_transition(state_1, symbol_a, state_3)

    expected_min_dfa.add_transition(state_2, symbol_y, state_2)
    expected_min_dfa.add_transition(state_2, symbol_a, state_3)

    expected_min_dfa.add_transition(state_3, symbol_a, state_3)

    actual_min_dfa = get_min_dfa("i* l* y* a*")

    assert actual_min_dfa.is_equivalent_to(expected_min_dfa) and len(
        actual_min_dfa.states
    ) == len(expected_min_dfa.states)


@pytest.fixture
def two_cycles_graph() -> Graph:
    return get_two_cycles(2, 2)


@pytest.fixture
def expected_nfa() -> NondeterministicFiniteAutomaton:
    nfa = NondeterministicFiniteAutomaton()
    nfa.add_transitions(
        [(0, "a", 1), (1, "a", 2), (2, "a", 0), (0, "b", 3), (3, "b", 4), (4, "b", 0)]
    )

    return nfa


def test_wrong_states(two_cycles_graph) -> None:
    with pytest.raises(ValueError):
        get_nfa(two_cycles_graph.graph, {0, 4, 199}, {-9, 3, 19})


def test_nfa(two_cycles_graph) -> None:
    nfa = get_nfa(two_cycles_graph.graph)

    assert not nfa.is_deterministic()


@pytest.mark.parametrize(
    "expected_word, not_expected_word",
    [
        ("", "epsilon"),
        ("aaa", "bb"),
        ("bbb", " "),
        ("bbbbbb", "aaabb"),
        ("aaabbbaaa", "b"),
    ],
)
def test_nfa_accepts(two_cycles_graph, expected_word, not_expected_word) -> None:
    actual_nfa = get_nfa(two_cycles_graph.graph, {0}, {0})

    assert actual_nfa.accepts(expected_word) and not actual_nfa.accepts(
        not_expected_word
    )


@pytest.mark.parametrize(
    "start_states, final_states",
    [({0}, {3}), ({0}, {1, 4}), ({2, 3}, {0}), ({0, 1, 2}, {0, 3, 4}), (None, None)],
)
def test_get_nfa(two_cycles_graph, expected_nfa, start_states, final_states) -> None:
    if not start_states:
        start_states = {0, 1, 2, 3, 4}

    for state in start_states:
        expected_nfa.add_start_state(State(state))

    if not final_states:
        final_states = {0, 1, 2, 3, 4}

    for state in final_states:
        expected_nfa.add_final_state(State(state))

    actual_nfa = get_nfa(two_cycles_graph.graph, start_states, final_states)

    assert actual_nfa.is_equivalent_to(expected_nfa)
