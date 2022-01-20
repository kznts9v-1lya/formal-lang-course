from project.graph_tools import get_from_dataset
from project.gql.interpreter.exceptions import GraphLoadingException
from project.gql.interpreter.types.finite_automaton_regex import FiniteAutomaton


def load_graph(name: str) -> FiniteAutomaton:
    try:
        graph = get_from_dataset(name)
    except NameError as exception:
        raise GraphLoadingException(name) from exception

    return FiniteAutomaton.from_graph(graph.graph)
