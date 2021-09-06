import os
import sys
from pathlib import Path

from networkx import MultiDiGraph

import project.graph_tools as tools

__all__ = []


def exit_repl() -> None:
    """
    Implementation of application exit command.

    Exits the REPL.

    Returns
    -------
    None
    """
    sys.exit(0)


def get_graph_description(name: str) -> None:
    """
    Implementation of get_graph_description application command.

    Prints description of graph by it's real dataset name.

    Parameters
    ----------
    name: str
        Real dataset graph name from https://jetbrains-research.github.io/CFPQ_Data/dataset/index.html.

    Returns
    -------
    None
    """

    description = tools.get_description(name)

    print(
        f"""
        Description of graph "{description.name}":
        {str(description)}
        """
    )


def generate_two_cycles_graph(
    first_cycle: int, second_cycle: int, *edge_labels
) -> None:
    """
    Implementation of generate_two_cycles_graph application command.

    Generates two cycles graph specified by parameters and prints it's description.

    Parameters
    ----------
    first_cycle: int
        Number of nodes in the first cycle
    second_cycle: int
        Number of nodes in the second cycle
    edge_labels: Tuple[Any, ...]
        Edge labels on the cycles

    Returns
    -------
    None
    """

    description = tools.two_cycles_graph(
        first_cycle, second_cycle, (edge_labels[0], edge_labels[1])
    ).description

    print(
        f"""
        Two cycles graph "{description.name}" with
        {str(description)}
        was successfully generated
        """
    )


def save_graph_to_dot(path: str, graph: MultiDiGraph = None) -> None:
    """
    Implementation of save_current_graph_to_dot application command.

    Saves last used graph (or passed graph) to "*.dot" file specified by path and prints it's description.

    Parameters
    ----------
    path: str
        Path to save the graph, extension ".dot" required
    graph: networkx.MultiDiGraph, default = None
        Graph to save

    Returns
    -------
    None

    Raises
    ------
    SyntaxError
        If extension wasn't ".dot"
    """

    _, ext = os.path.splitext(path)

    if not ext == ".dot":
        raise SyntaxError('Wrong extension, ".dot" is required')

    file = Path(path)

    if not file.exists() or not file.is_file():
        open(path, "w+")

    if graph is None:
        description = tools.save_to_dot(path)
    else:
        description = tools.save_to_dot(path, graph)

    print(
        f"""
        Graph "{description.name}" with
        {str(description)}
        was successfully saved in
        {str(file)}
        """
    )
