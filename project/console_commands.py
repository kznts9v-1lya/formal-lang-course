import os
import sys
from pathlib import Path

import project.graph_tools as tools

__all__ = []


def exit_repl() -> None:
    sys.exit(0)


def get_graph_description(name: str) -> None:
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


def save_current_graph_to_dot(path: str) -> None:
    _, ext = os.path.splitext(path)

    if not ext == ".dot":
        raise SyntaxError('Wrong extension, ".dot" is required')

    file = Path(path)

    if not file.exists() or not file.is_file():
        open(path, "w+")

    description = tools.save_to_dot(path)

    print(
        f"""
        Graph "{description.name}" with
        {str(description)}
        was successfully saved in
        {str(file)}
        """
    )
