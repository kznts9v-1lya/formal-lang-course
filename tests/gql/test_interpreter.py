import pytest
from project.gql.interpreter.interpreter import GQLInterpreter


@pytest.mark.parametrize(
    "input_, expect_output",
    [
        (
            "PRINT 12\n",
            [">>>12"],
        ),
        (
            "PRINT FILTER (FUN (df) -> df IN {1, 2, 34,})({1, 2, 3, 4,})\n",
            [">>>{'1', '2'}", ">>>{'2', '1'}"],
        ),
        ("PRINT ('last')**\n", [">>>(last)*"]),
        ("PRINT 'type' || 'last'\n", [">>>(type|last)"]),
        ("PRINT 'last' && 'type'\n", [">>>Empty"]),
        ("PRINT 'last' && 'last'\n", [">>>($.last)"]),
        (
            "PRINT MAP (FUN (df) -> 44 * df)({1, 2,})\n",
            [">>>{'88', '44'}", ">>>{'44', '88'}"],
        ),
    ],
)
def test_atomic_functions(input_, expect_output):
    test_interp = GQLInterpreter()
    test_interp.run_query(input_)
    answer = test_interp.visitor.output_logger

    result = False
    for out in expect_output:
        result = answer == out
        if result:
            break

    assert result


@pytest.mark.parametrize(
    "input_, expect_output",
    [
        (
            """Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n
PRINT SELECT LABELS OF (Ig1)\n""",
            [">>>{b, a}", ">>>{a, b}"],
        ),
        (
            """Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n
Ig2 = SET START OF (Ig1) TO SELECT STARTS OF ( Ig1 )\n
st = SELECT FINALS OF (Ig1)\n
PRINT FILTER (FUN (df) -> df IN {'0', '3;2', '4',})(st)\n""",
            [">>>{'0', '4'}", ">>>{'4', '0'}"],
        ),
        (
            """PRINT 'a' && ('b' || 'a')**\n""",
            [">>>($.a)"],
        ),
        (
            """Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n
PRINT Ig1 && 'a b b'\n""",
            [">>>($.((a.b).b))", ">>>($.(a.(b.b)))"],
        ),
        (
            """Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n
Ig2 = SET START OF (Ig1) TO SELECT STARTS OF ( Ig1 )\n
st = SELECT FINALS OF (Ig1)\n
query = ('b')** || 'a' || 'a b'\n
inter = Ig1 && query\n
PRINT inter && 'a b'\n""",
            [">>>($.(a.b))"],
        ),
        (
            """Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n
Ig2 = SET START OF (Ig1) TO SELECT STARTS OF ( Ig1 )\n
PRINT Ig2 && 'a b'\n""",
            [">>>($.(a.b))"],
        ),
        (
            """Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n
ff = SELECT REACHABLE OF (Ig1)\n
PRINT FILTER (FUN (df) -> df[1] IN {0,})(FILTER (FUN (df) -> df[0] IN {1, 2,})(ff))\n""",
            [">>>{(1, 0), (2, 0)}", ">>>{(2, 0), (1, 0)}", ">>>set()"],
        ),
        (
            """Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n
PRINT FILTER (FUN (df) -> df IN {'0',})(SELECT FINALS OF (Ig1))\n""",
            [">>>{'0'}"],
        ),
    ],
)
def test_multiple_functions(input_, expect_output):
    for i in range(4):
        test_interp = GQLInterpreter()
        test_interp.run_query(input_)
        answer = test_interp.visitor.output_logger

        result = False
        for out in expect_output:
            result = answer == out
            if result:
                break
        if result:
            break

    assert result


@pytest.mark.parametrize(
    "input_, expect_output",
    [
        (
            """PRINT SELECT LABELS OF (Ig1)\n""",
            [
                "----Exception----",
                "No value with name: Ig1",
                "-----------------",
                "memory call",
                "var expr pure",
                "expr var",
                "expr get_labels",
                "print statement: [PRINTSELECT LABELS OF (Ig1)]",
                "-----------------",
            ],
        ),
        (
            "Ig1 = LOAD GRAPH 'aaa.dot'\n",
            [
                "----Exception----",
                "Can not load graph: aaa.dot",
                "-----------------",
                "expr load",
                "bind statement: [Ig1]",
                "-----------------",
            ],
        ),
        (
            """st = SELECT FINALS OF (Ig1)\n
Ig1 = LOAD GRAPH 'tests/data/graphs/two_cycles2.dot'\n""",
            [
                "----Exception----",
                "No value with name: Ig1",
                "-----------------",
                "memory call",
                "var expr pure",
                "expr var",
                "expr get_final",
                "bind statement: [st]",
                "-----------------",
            ],
        ),
    ],
)
def test_errors(input_, expect_output):
    test_interp = GQLInterpreter()
    test_interp.run_query(input_)
    answer = test_interp.out_log_list

    assert answer == expect_output


@pytest.mark.parametrize(
    "input_, expect_output",
    [
        (
            "PRINT SELECT STARTS OF (LOAD GRAPH 'tests/data/graphs/two_cycles2.dot')\n",
            [">>>{0;1;2;3;4;5}", ">>>{0;1;2;3;4;5;\\n}"],
        ),
    ],
)
def test_multi_single_command(input_, expect_output):
    test_interp = GQLInterpreter()
    test_interp.run_query(input_)
    answer = test_interp.visitor.output_logger

    result = False
    for out in expect_output:
        result = answer == out
        if result:
            break
    assert result
