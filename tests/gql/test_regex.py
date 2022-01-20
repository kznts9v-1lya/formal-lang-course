import sys

from project.gql.interpreter.types.finite_automaton_regex import Regex
from project.gql.interpreter.exceptions import NotImplementedException
import pytest

if sys.platform.startswith("win"):
    pytest.skip("Windows is unsupported", allow_module_level=True)
else:
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
#         '"1" & "2"',
#     ],
# )
# def test_intersect(regex):
#     actual = interpret(regex, "expr")
#
#
#     assert actual == expected


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
