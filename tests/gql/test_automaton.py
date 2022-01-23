from tools import interpret

from project.automaton_tools import get_min_dfa_from_regex_str

import pytest


@pytest.mark.parametrize(
    "left, operation, right, expected",
    [
        ('"l1" & "l1"', "&", '"l1" | "l1"', '"l1"'),
        ('"l1" | "l2"', "|", '"l2" | "l3"', '"l1" | "l2" | "l3"'),
    ],
)
def test_intersection(left, operation, right, expected):
    expr = left + ' ' + operation + ' ' + right

    actual = interpret(expr, "expr")
    expected = get_min_dfa_from_regex_str(expected)

    assert actual.nfa.is_equivalent_to(expected)
