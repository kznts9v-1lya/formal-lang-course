from pyformlang.regular_expression import MisformedRegexError

from project.gql.interpreter.types.type import Type
from project.gql.interpreter.types.finite_automaton import FiniteAutomaton
from project.gql.interpreter.exceptions import CastingException

from project.automaton_tools import get_min_dfa_from_regex_str


class Regex(Type):
    def __init__(self, regex_str: str):
        self.regex_str = regex_str

    def __str__(self):
        return self.regex_str.lstrip("(").rstrip(")")

    @classmethod
    def from_str(cls, regex_str: str):
        try:
            return FiniteAutomaton(get_min_dfa_from_regex_str(regex_str))
        except MisformedRegexError as exception:
            raise CastingException("str", "Regex") from exception

    def intersect(self, other):
        left_nfa = Regex.from_str(self.regex_str)

        if isinstance(other, Regex):
            right_nfa = Regex.from_str(other.regex_str)

            return left_nfa.intersect(right_nfa)
        elif isinstance(other, FiniteAutomaton):
            return left_nfa.intersect(other)
        else:
            raise CastingException(left_type="Regex", right_type=str(other))

    def union(self, other):
        return Regex(f"({self.regex_str}|{other.regex_str})")

    def concatenate(self, other):
        return Regex(f"({self.regex_str}.{other.regex_str})")

    def inverse(self):
        nfa = Regex.from_str(self.regex_str)

        return nfa.inverse()

    def kleene(self):
        return Regex(f"({self.regex_str})*")
