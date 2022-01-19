from interpret_token import interpret_token
from project.gql.interpreter.types.bool import Bool
from project.gql.interpreter.exceptions import NotImplementedException

import pytest


@pytest.mark.parametrize(
    "left, operation, right, expected",
    [
        ("TRUE", "&", "TRUE", True),
        ("TRUE", "&", "FALSE", False),
        ("FALSE", "&", "TRUE", False),
        ("FALSE", "&", "FALSE", False),
        ("TRUE", "|", "TRUE", True),
        ("TRUE", "|", "FALSE", True),
        ("FALSE", "|", "TRUE", True),
        ("FALSE", "|", "FALSE", False),
    ],
)
def test_intersect_union(left, operation, right, expected):
    expression = left + operation + right

    assert interpret_token(expression, "expr") == Bool(expected)


@pytest.mark.parametrize(
    "left, expected",
    [
        ("TRUE", False),
        ("FALSE", True),
    ],
)
def test_inversion(left, expected):
    expression = "NOT " + left

    assert interpret_token(expression, "expr") == Bool(expected)


@pytest.mark.parametrize(
    "left, operation, right",
    [
        ("TRUE", ".", "TRUE"),
        ("TRUE", ".", "FALSE"),
        ("TRUE", "*", ""),
        ("FALSE", "*", ""),
    ],
)
def test_kleene_concatenate(left, operation, right):
    expression = left + operation + right

    with pytest.raises(NotImplementedException):
        interpret_token(expression, "expr")
