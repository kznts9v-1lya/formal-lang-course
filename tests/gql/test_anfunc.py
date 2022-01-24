from tools import interpret
from project.gql.interpreter.types.bool import Bool

import pytest


@pytest.mark.parametrize(
    "initial, anfunc, expected",
    [
        ("{1, 2}", "FUN x => x IN {2}", {Bool(True), Bool(False)}),
        ("{1, 2, 3}", "FUN x => 5", {5}),
        ("{1, 2, 3, 4, 5}", "FUN _ => 0", {0}),
    ],
)
def test_map(initial, anfunc, expected):
    expr = f"MAP ({anfunc}) {initial}"
    actual = interpret(expr, "mapping")

    assert actual.set == expected


@pytest.mark.parametrize(
    "initial, fun, expected_set",
    [
        ("{1, 2, 3, 4, 5}", "FUN x => x IN {2:4}", "{2, 3, 4}"),
        ("{1, 2, 3, 4, 5}", "FUN _ => TRUE", "{1, 2, 3, 4, 5}"),
        ("{1, 2, 3, 4, 5}", "FUN _ => FALSE", "{}"),
    ],
)
def test_filter(initial, fun, expected_set):
    expression = f"FILTER {fun} {initial}"
    actual = interpret(expression, "filtering")
    expected = interpret(expected_set, "vertices")

    assert actual.set == expected.set
