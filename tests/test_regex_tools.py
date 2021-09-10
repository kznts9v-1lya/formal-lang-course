from pyformlang.finite_automaton import Symbol

from project.regex_tools import get_dfa


def test_dfa():
    dfa = get_dfa("i* l* y* a* | 1901")

    assert dfa.is_deterministic()


def test_get_dfa():
    dfa = get_dfa("i* l* y* a* | 1901")

    expected = [
        [],
        [Symbol("i"), Symbol("l"), Symbol("y"), Symbol("a")],
        [Symbol("1901")],
        [
            Symbol("i"),
            Symbol("i"),
            Symbol("l"),
            Symbol("l"),
            Symbol("y"),
            Symbol("y"),
            Symbol("a"),
            Symbol("a"),
        ],
        [Symbol("y"), Symbol("a"), Symbol("a")],
    ]

    not_expected = [
        [Symbol("i"), Symbol("l"), Symbol("y"), Symbol("a"), Symbol("1901")],
        [Symbol("i"), Symbol("a"), Symbol("1"), Symbol("9"), Symbol("0"), Symbol("1")],
    ]

    assert all(dfa.accepts(word) for word in expected) and all(
        not dfa.accepts(word) for word in not_expected
    )
