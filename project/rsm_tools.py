from typing import Iterable

from project.automaton_tools import get_min_dfa_from_regex

from pyformlang.cfg import Variable
from pyformlang.finite_automaton import DeterministicFiniteAutomaton

__all__ = ["RSMBox", "RSM", "minimize_rsm", "get_rsm_from_ecfg"]


class RSMBox:
    """
    A class encapsulates a box with DFA by RSM variable for Recursive State Machine.

    Parameters
    ----------
    variable: Variable
       Variable of RSM
    dfa: DeterministicFiniteAutomaton
        DFA by RSM variable
    """

    def __init__(
        self, variable: Variable = None, dfa: DeterministicFiniteAutomaton = None
    ):
        self._dfa = dfa
        self._variable = variable
        self.minimize()

    @property
    def dfa(self) -> DeterministicFiniteAutomaton:
        return self._dfa

    @property
    def variable(self) -> Variable:
        return self._variable

    def minimize(self) -> None:
        """
        Minimize Deterministic Finite Automaton in the RSMBox.

        Returns
        -------
        None
        """

        self._dfa = self._dfa.minimize()

    def __eq__(self, other: "RSMBox") -> bool:
        return self._variable == other._variable and self._dfa.is_equivalent_to(
            other._dfa
        )


class RSM:
    """
    A class encapsulates a Recursive State Machine.

    Parameters
    ----------
    start_symbol: Variable
        A start symbol for RSM
    boxes: Iterable[RSMBox]
        A collection of RSMBox with DFA by RSM variable
    """

    def __init__(
        self,
        start_symbol: Variable,
        boxes: Iterable[RSMBox],
    ):
        self._start_symbol = start_symbol
        self._boxes = boxes
        self.minimize()

    @property
    def start_symbol(self):
        return self._start_symbol

    @property
    def boxes(self):
        return self._boxes

    @start_symbol.setter
    def start_symbol(self, start_symbol: Variable):
        self._start_symbol = start_symbol

    def minimize(self) -> "RSM":
        """
        Minimize Recursive State Machine means minimize each
        Deterministic Finite Automaton in boxes.

        Returns
        -------
        RSM:
            Minimal RSM
        """

        for box in self._boxes:
            box.minimize()

        return self

    @classmethod
    def from_ecfg(cls, ecfg) -> "RSM":
        """
        Converts an Extended Context Free Grammar to a Recursive State Machine.

        Returns
        -------
        RSM:
            RSM from ECFG
        """

        boxes = [
            RSMBox(production.head, get_min_dfa_from_regex(production.body))
            for production in ecfg.productions
        ]

        return cls(start_symbol=ecfg.start_symbol, boxes=boxes)


def minimize_rsm(rsm: RSM) -> RSM:
    """
    Minimize Recursive State Machine means minimize each
    Deterministic Finite Automaton in boxes.

    Returns
    -------
    RSM:
        Minimal RSM
    """

    return rsm.minimize()


def get_rsm_from_ecfg(ecfg) -> RSM:
    """
    Converts an Extended Context Free Grammar to a Recursive State Machine.

    Returns
    -------
    RSM:
        RSM from ECFG
    """

    return RSM.from_ecfg(ecfg)
