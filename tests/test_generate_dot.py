import sys

import pytest
import os

if sys.platform.startswith("win"):
    pytest.skip("Windows is unsupported", allow_module_level=True)
else:
    from project.gql.parser.parser import generate_dot

from antlr4.error.Errors import ParseCancellationException


def test_tree_dot():
    text = """
    g = LOAD "hello";
    g = SET START OF (SET FINAL OF g TO (SELECT VERTICES FROM g)) TO {1 : 100};
    l1 = "l1" | "l2";
    q1 = ("type" | l1)*;
    q2 = "subclass_of" . q;
    res1 = g & q1;
    res2 = g & q2;
    s = SELECT START VERTICES FROM g;
    vertices1 = FILTER (FUN v => v IN s) (MAP (FUN ((u_g,u_q1),l,(v_g,v_q1))=> u_g) (SELECT EDGES FROM res1));
    vertices2 = FILTER (FUN v=> v IN s) (MAP (FUN ((u_g,u_q2),l,(v_g,v_q1)) => u_g) (SELECT EDGES FROM res2));
    vertices3 = vertices1 & vertices2;
    PRINT vertices3;
    """

    path = os.sep.join(
        [
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "tests",
            "data",
            "dots",
        ]
    )

    expected_path = os.sep.join([path, "expected_tree.dot"])
    actual_path = os.sep.join([path, "actual_tree.dot"])

    generate_dot(text, actual_path)

    with open(actual_path, "r") as actual:
        with open(expected_path, "r") as expected:
            assert actual.read() == expected.read()


def test_incorrect_text():
    text = """g = load "skos";
common_labels = (select lables from g) & (select labels from (load "graph.txt"));
print common_labels;"""

    with pytest.raises(ParseCancellationException):
        generate_dot(text, str(None))
