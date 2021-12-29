import sys

import pytest

if sys.platform.startswith("win"):
    pytest.skip("Skipping tests", allow_module_level=True)
else:
    from project.gql.parser import parse


@pytest.mark.parametrize(
    "text, expected",
    [
        ("_a", True),
        ("graph1", True),
        ("213", False),
        ("аыфв", False),
    ],
)
def test_parse_variable(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.var()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("FUN x, y, z => x", True),
        ("FUN v=>v IN s", True),
        ("FUN ((u_g, u_q2), l, (v_g, v_q1)) => u_g", True),
        ("FUN {x, y, z} => 1", False),
        ("FUN 1,2,3 => 1", False),
    ],
)
def test_anonymous_func(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.anfunc()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("MAP (FUN x => x) g", True),
        ("MAP (FUN ((u_g,u_q1),l,(v_g,v_q1)) => u_g) (SELECT EDGES FROM res1)", True),
        (" MAP (FUN 1 => 1) 1", False),
        ("MAP p p", False),
    ],
)
def test_map(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.mapping()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("FILTER (FUN x => x) g", True),
        (
                "FILTER (FUN ((u_g,u_q1),l,(v_g,v_q1)) => u_g) (SELECT EDGES FROM res1)",
                True,
        ),
        (" FILTER (FUN 1 => 1) 1", False),
        ("FILTER p p", False),
    ],
)
def test_filter(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.filtering()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("TRUE", True),
        ("FALSE", True),
        ("True", False),
        ("False", False),
        ("{1 : 100}", True),
        ("(1:100)", False),
        ("{1, 2, 3}", True),
        ("{1, 2, 3)", False),
        (
                '''"""
    S -> A S B S
    A -> a
    B -> b
    """
    ''',
                True,
        ),
        ('(1, "l", 2)', True),
        ('("l", "k", "m")', False),
        ("{(1, 2), (3, 4), (5, 6)}", True),
        ("{(1, 2), ('l', 4), (5, 6)}", False),
        ('"label"', True),
        ("label", False),
        ('{"l1", "l2"}', True),
        ('{"l1", l2}', False),
        ("0", True),
        ("_0", False),
        ("SET START OF g TO {1 : 100}", True),
        ("SET START OF g TO {1..100}", False),
        ("SET FINAL OF g TO {1:100}", True),
        ("ADD START OF g TO {1, 2, 3}", True),
        ("ADD FINAL OF g TO labels1", True),
        ("SELECT VERTICES FROM g", True),
        ("SELECT START VERTICES FROM g", True),
        ("SELECT REACHABLE VERTICES FROM g", True),
        ("SELECT FROM g", False),
        ("SELECT LABELS FROM g", True),
        ("SELECT EDGES FROM g", True),
        ("SELECT EDGES FROM 1", False),
        ("SELECT START FROM 1", False),
    ],
)
def test_val(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.val()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("g1 & g2", True),
        ("g1", True),
        ("{2:100} & {1}", True),
        ("", False),
        ("(SELECT EDGES FROM g) & {(1, 2)}", True),
        ("(SELECT FROM g) & {(1, 2)}", False),
        ("l1 . l2 . l3 | l4", True),
        ("l1 . l2 . l3 & l4", True),
        ('"label1" . "label2" | "label3"', True),
        ("FILTER (FUN (x, y)=> x IN s) g", True),
    ],
)
def test_expr(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.expr()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("PRINT g2", True),
        ("print g2", False),
        ("PRINT {1:100}", True),
        ("PRINT", False),
        ('g1 = LOAD "wine"', True),
        ("g1 = LOAD graph", False),
        ("g1 = {1 : 100}", True),
    ],
)
def test_stmt(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.stmt()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (
                """
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
    """,
                True,
        ),
        ('g = LOAD "hello"', False),
    ],
)
def test_prog(text, expected):
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.prog()
    actual = parser.getNumberOfSyntaxErrors() == 0

    assert actual == expected
