from project.gql.interpreter.types.bool import Bool
from project.gql.interpreter.types.set import Set
from project.gql.interpreter.core.exceptions import NotImplementedException, TypingError
import pytest

from tools import interpret


@pytest.mark.parametrize(
    "left, operation, right, expected",
    [
        ("{1, 2, 3, 4, 5}", "&", "{2, 3, 4}", {2, 3, 4}),
        ("{1, 2, 3, 4, 5}", "&", "{7, 8, 9}", set()),
        ("{7, 8, 9}", "&", "{}", set()),
        ("{}", "&", "{}", set()),
        ("{1, 2, 3}", "|", "{4, 5, 6}", {1, 2, 3, 4, 5, 6}),
        ("{1, 2, 3, 4, 5}", "|", "{4, 5, 6, 7}", {1, 2, 3, 4, 5, 6, 7}),
        ("{}", "|", "{}", set()),
    ],
)
def test_intersect_union(left, operation, right, expected):
    expr = left + operation + right

    actual = interpret(expr, "expr")
    expected = Set(expected)

    assert actual.set == expected.set


@pytest.mark.parametrize(
    "left, operation, right",
    [("{1, 2}", ".", "{1, 2, 3}"), ("{1, 2, 3}", "*", ""), ("", "NOT ", "{1, 2, 3}")],
)
def test_kleene_concatenate_inverse(left, operation, right):
    expr = left + operation + right

    with pytest.raises(NotImplementedException):
        interpret(expr, "expr")


@pytest.mark.parametrize(
    "left, right, expected",
    [("2", "{1 : 10}", True), ("0", "{}", False), ("9", "{10:13}", False)],
)
def test_in(left, right, expected):
    expr = left + " IN " + right

    actual = interpret(expr, "expr")

    assert actual == Bool(expected)


@pytest.mark.parametrize(
    "vertices_range, expected",
    [
        ("{1 : 5}", {1, 2, 3, 4, 5}),
        ("{0:1}", {0, 1}),
        ("{1: 1}", {1}),
    ],
)
def test_vertices_range(vertices_range, expected):
    actual = interpret(vertices_range, "vertices_range")

    assert actual.set == Set(expected).set


def test_types_mismatch():
    left = "{1, 2, 3}"
    right = '{"1", "2", "3"}'

    expr = left + "|" + right

    with pytest.raises(TypingError):
        interpret(expr, "expr")


def test_types_consistency():
    left = {1, "2", 3}

    with pytest.raises(TypingError):
        Set.from_set(left)
