import cfpq_data
import networkx as nx


class GraphDescription:
    """
    Class that stores description of graph:
    - nodes: int,
    - edges: int,
    - edge_labels: set
    """

    def __init__(self, nodes: int, edges: int, edge_labels: set):
        self.nodes = nodes
        self.edges = edges
        self.edge_labels = edge_labels

    def __str__(self):
        return (
            f"- Number of nodes: {str(self.nodes)}\n"
            + f"\t\t- Number of edges: {str(self.edges)}\n"
            + f"\t\t- Edge Labels: {str(self.edge_labels)}"
        )


def get_description(graph: nx.MultiDiGraph):
    """
    Returns GraphDescription with number of nodes, edges and set of edge labels in graph
    """

    return GraphDescription(
        graph.number_of_nodes(),
        graph.number_of_edges(),
        cfpq_data.get_labels(graph, verbose=False),
    )


def generate_two_cycles_graph(
    first_cycle: int, second_cycle: int, edge_labels: tuple[str, str]
):
    """
    Writes a graph with two cycles which generates with specified parameters to the file
    """

    graph = cfpq_data.labeled_two_cycles_graph(
        first_cycle, second_cycle, edge_labels=edge_labels, verbose=False
    )

    return graph
