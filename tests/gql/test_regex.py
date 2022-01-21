from project.gql.interpreter.types.finite_automaton_regex import Regex, FiniteAutomaton
from project.gql.interpreter.exceptions import NotImplementedException

from pyformlang.finite_automaton import NondeterministicFiniteAutomaton, State

import pytest

from tools import interpret


@pytest.mark.parametrize(
    "regex",
    [
        '"19"*',
        '"a"*',
        '"tg"*',
        '""*',
    ],
)
def test_kleene(regex):
    actual = interpret(regex, "expr")

    assert actual == Regex(regex)


@pytest.mark.parametrize(
    "regex",
    [
        '"a" . "b"',
        '"a" . "1a"',
        '"abc" . "a"',
        '"a" . ""',
    ],
)
def test_concatenate(regex):
    actual = interpret(regex, "expr")

    assert actual == Regex(regex)


@pytest.mark.parametrize(
    "regex",
    [
        '"a" | "1"',
        '"a" | "1" | "bc"',
        # '"a" | ("b" | "c")',
        '"a" | "" | ""',
    ],
)
def test_union(regex):
    actual = interpret(regex, "expr")

    assert actual == Regex(regex)


# @pytest.mark.parametrize(
#     "regex",
#     [
#         # 'NOT "a" | "b"',
#     ],
# )
# def test_inverse(regex):
#     actual = interpret(regex, "expr")
#
#     assert actual == Regex.from_str(regex).inverse()


# @pytest.mark.parametrize(
#     "regex, expected",
#     [
#         ('"a" & "b"',
#             NondeterministicFiniteAutomaton({State("0⋂0"), State("1⋂1")}, start_state={State("0⋂0")},
#                                             final_states={State("1⋂1")})),
#     ],
# )
# def test_intersect(regex, expected):
#     actual = interpret(regex, "expr")
#
#     assert actual == FiniteAutomaton(expected)

# @pytest.mark.parametrize(
#     "regex",
#     [
#         '"a" | "1"*',
#         '"a"* . "1"',
#         '"a" | "1"* . "bc"',
#         '"a23"* . "1"* . "bc" | "we"',
#         '"a23"* | "1"* . "bc" & "a"',
#     ],
# )
# def test_regex_combination_operations(regex):
#     actual_regex = interpreter_with_value(regex, "expr")
#     expected_regex = Regex(regex)
#     assert actual_regex == expected_regex
