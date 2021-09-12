from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex

__all__ = ["get_dfa"]


def get_dfa(regex: str) -> DeterministicFiniteAutomaton:
    """
    Based on a regular expression given as a string, builds an Deterministic Finite Automaton.

    Parameters
    ----------
    regex: str
        The string representation of a regular expression

    Returns
    -------
    DeterministicFiniteAutomaton
        Deterministic Finite Automaton equivalent to a given regular expression as a string

    Raises
    ------
    MisformedRegexError
        If given as string regular expression has an irregular format
    """

    re = Regex(regex)
    e_nfa = re.to_epsilon_nfa()
    dfa = e_nfa.to_deterministic()

    return dfa
