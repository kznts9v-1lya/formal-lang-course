from typing import Tuple

import cfpq_data
import networkx


def get_description(graph: networkx.MultiDiGraph):
    """Returns dictionary with number of nodes, edges and set of labels in graph"""

    return {
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "labels": cfpq_data.get_labels(graph),
    }


def generate_two_cycles_graph_to_file(
    first_cycle: int, second_cycle: int, edge_labels: Tuple[str, str], file: str
):
    """Writes a graph with two cycles which generates with specified parameters to the file"""

    graph = cfpq_data.labeled_two_cycles_graph(
        first_cycle, second_cycle, edge_labels=edge_labels, verbose=False
    )
    networkx.drawing.nx_pydot.write_dot(graph, file)
