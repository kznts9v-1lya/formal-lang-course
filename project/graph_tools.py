from typing import Tuple, Set

import cfpq_data
import networkx as nx
from networkx import MultiDiGraph

__all__ = [
    "Graph",
    "GraphDescription",
    "get_description",
    "two_cycles_graph",
    "save_to_dot",
]


class GraphDescription:
    """
    Encapsulates description of graph: name, number of nodes, number of edges, set of edge labels.

    Attributes
    ----------
    name: str
        Name of graph
    nodes: int
        Number of graph nodes
    edges: int
        Number of graph edges
    edge_labels: Set[str]
        Graph edge labels set
    """

    def __init__(self, name, nodes: int, edges: int, edge_labels: Set[str]):
        self.name = name
        self.nodes = nodes
        self.edges = edges
        self.edge_labels = edge_labels

    def __str__(self):
        return (
            f"- number of nodes: {str(self.nodes)}\n"
            + f"\t- number of edges: {str(self.edges)}\n"
            + f"\t- edge labels: {str(self.edge_labels)}"
        )


class Graph:
    """
    Encapsulates graph: graph object and it's description.

    Attributes
    ----------
    graph: MultiDiGraph
        Graph object
    description: GraphDescription
        Description of graph object
    """

    def __init__(self, graph: MultiDiGraph):
        self.graph = graph
        self.description = GraphDescription(
            graph.name,
            graph.number_of_nodes(),
            graph.number_of_edges(),
            cfpq_data.get_labels(graph, verbose=False),
        )

    def __str__(self):
        return f"""
            Graph {self.description.name}:
            {str(self.description)}
            """

    def set_name(self, name):
        self.description.name = name


current_graph: Graph


def get_description(name: str) -> GraphDescription:
    """
    Gets a description of real dataset graph encapsulated in GraphDescription.

    Parameters
    ----------
    name: str
        Name of the graph from https://jetbrains-research.github.io/CFPQ_Data/dataset/index.html

    Returns
    -------
    GraphDescription
        Description of graph

    Raises
    ------
    NameError
        If name not in https://jetbrains-research.github.io/CFPQ_Data/dataset/index.html
    """

    graph = cfpq_data.graph_from_dataset(name, verbose=False)

    if graph is None:
        raise NameError("Wrong dataset graph name, please specify it")

    global current_graph
    current_graph = Graph(graph)
    current_graph.set_name(name)

    return current_graph.description


def two_cycles_graph(
    first_cycle: int, second_cycle: int, edge_labels: Tuple[str, str]
) -> Graph:
    """
    Generates two cycles graph specified by parameters.

    Parameters
    ----------
    first_cycle: int
        Number of nodes in the first cycle
    second_cycle: int
        Number of nodes in the second cycle
    edge_labels: Tuple[str, str]
        Labels for edges on the first and second cycles

    Returns
    -------
    Graph
        Class encapsulates graph
    """

    graph = cfpq_data.labeled_two_cycles_graph(
        first_cycle, second_cycle, edge_labels=edge_labels, verbose=False
    )

    global current_graph
    current_graph = Graph(graph)
    current_graph.set_name("tcg")

    return current_graph


def save_to_dot(path: str, graph: MultiDiGraph = None) -> GraphDescription:
    """
    Saves last used graph (or passed graph) to "*.dot" file specified by path.

    Parameters
    ----------
    path: str
        Path to save the graph, extension ".dot" required
    graph: networkx.MultiDiGraph, default = None
        Graph to save

    Returns
    -------
    GraphDescription
        Description of graph
    """

    global current_graph
    if graph is None:
        nx.drawing.nx_pydot.write_dot(current_graph.graph, path)
    else:
        current_graph = Graph(graph)
        nx.drawing.nx_pydot.write_dot(current_graph.graph, path)

    return current_graph.description
