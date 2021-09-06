import os
import sys
from pathlib import Path

import networkx as nx
import pydot

import project.graph_tools as tools


def exit_repl():
    sys.exit(0)


def get_graph_description(path: str):
    file = Path(path)

    if not file.exists() or not file.is_file():
        raise FileNotFoundError("No such file or not a file")

    _, ext = os.path.splitext(path)

    if not ext == ".dot":
        raise SyntaxError('Wrong extension, ".dot" is required')

    graph_pydot = pydot.graph_from_dot_file(file)[0]
    graph = nx.drawing.nx_pydot.from_pydot(graph_pydot)
    description = tools.get_description(graph)

    print(
        f"""
        Description of graph {str(file)}:
        {str(description)}
        """
    )


def generate_and_save_two_cycles_graph(
    path: str, first_cycle: int, second_cycle: int, *edge_labels
):
    file = Path(path)

    if not file.exists() or not file.is_file():
        open(path, "w+")

    graph = tools.generate_two_cycles_graph(
        first_cycle, second_cycle, (edge_labels[0], edge_labels[1])
    )
    nx.drawing.nx_pydot.write_dot(graph, file)

    print(
        f"""
        Two cycles graph with
        - {str(first_cycle)} nodes in first cycle
        - {str(second_cycle)} nodes in second cycle
        - {str(edge_labels)} labels on edges
        was successfully generated and saved in
        {str(file)}
        """
    )
