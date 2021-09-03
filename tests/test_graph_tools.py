from random import randint

import cfpq_data

from project import graph_tools


def test_graph_info():
    graph = cfpq_data.labeled_barabasi_albert_graph(
        randint(25, 49), randint(1, 24), verbose=False
    )
    desc = graph_tools.get_description(graph)

    assert desc["nodes"] == graph.number_of_nodes()
    assert desc["edges"] == graph.number_of_edges()
    assert desc["labels"] == cfpq_data.get_labels(graph)


def test_generate_two_cycles_graph_to_file():
    file = "data/two_cycles_graph.dot"

    graph_tools.generate_two_cycles_graph_to_file(
        randint(25, 49), randint(1, 24), ("a", "b"), file
    )
