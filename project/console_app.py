from typing import List

import project.console_commands as commands

__all__ = ["repl"]

command_names = (
    "exit",
    "get_graph_description",
    "generate_two_cycles_graph",
    "save_current_graph_to_dot",
)

command_names_commands = {
    command_names[0]: commands.exit_repl,
    command_names[1]: commands.get_graph_description,
    command_names[2]: commands.generate_two_cycles_graph,
    command_names[3]: commands.save_current_graph_to_dot,
}

description = f"""
Available commands:
- {command_names[0]}
- {command_names[1]} [name: str]
- {command_names[2]} [first_cycle: int] [second_cycle: int] [first_label: str] [second_label: str]
- {command_names[3]} [path: str]: save the last used graph
"""


def analyse_input(inputs: List[str]) -> None:
    command_name = inputs[0]

    if command_name not in command_names:
        raise SyntaxError(
            f"Command {command_name} is not supported: use commands from the list"
        )

    if command_name == command_names[0] and not len(inputs) == 1:
        raise SyntaxError("Wrong arguments count, it must be empty")

    if (
        command_name == command_names[1] or command_name == command_names[3]
    ) and not len(inputs) == 2:
        raise SyntaxError("Wrong arguments count, it must be one")

    if command_name == command_names[2]:
        if not len(inputs) == 5:
            raise SyntaxError("Wrong arguments count, it must be five")

        if not inputs[1].isnumeric() or not inputs[2].isnumeric():
            raise TypeError(
                "Wrong type of count of nodes in cycles, it must be a number"
            )

        for i in (inputs[3], inputs[4]):
            if not i.isalpha():
                raise TypeError(
                    "Wrong type of edge labels, it must be a chars (strings)"
                )


def repl() -> None:
    print(description)

    while True:
        inputs = input(">>> ").split(" ")

        try:
            analyse_input(inputs)
        except SyntaxError as se:
            print(se)
            continue
        except TypeError as te:
            print(te)
            continue

        command_name = inputs[0]
        arguments = inputs[1:]

        try:
            command_names_commands[command_name](*arguments)
        except SyntaxError as err:
            print(err)
            continue
        except NameError as err:
            print(err)
            continue
