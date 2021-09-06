import os
from random import randint

import cfpq_data

from project import graph_tools, console_commands


def test_graph_info():
    graph = cfpq_data.labeled_barabasi_albert_graph(
        randint(25, 49), randint(1, 24), verbose=False
    )
    desc = graph_tools.get_description(graph)

    assert desc.nodes == graph.number_of_nodes()
    assert desc.edges == graph.number_of_edges()
    assert desc.edge_labels == cfpq_data.get_labels(graph)


def test_generate_two_cycles_graph():
    path = "data/two_cycles_graph.dot"

    if os.path.exists(path):
        os.remove(path)

    console_commands.generate_and_save_two_cycles_graph(
        path, randint(25, 49), randint(1, 24), "one", "two"
    )

    assert os.path.exists(path)
