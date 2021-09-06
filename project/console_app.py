import console_commands as commands

command_names = ("exit", "graph_description", "two_cycles_graph")

command_names_commands = {
    command_names[0]: commands.exit_repl,
    command_names[1]: commands.get_graph_description,
    command_names[2]: commands.generate_and_save_two_cycles_graph,
}

description = f"""
Available commands:
- {command_names[0]}
- {command_names[1]} [graph_file: str]
- {command_names[2]} [path_to_save: str] [first_cycle: int] [second_cycle: int] [first_label: str] [second_label: str]
"""


def analyse_input(inputs):
    command_name = inputs[0]

    if command_name not in command_names:
        raise SyntaxError("Such command is not supported")

    if command_name == command_names[0] and not len(inputs) == 1:
        raise SyntaxError("Wrong arguments count, it must be empty")

    if command_name == command_names[1] and not len(inputs) == 2:
        raise SyntaxError("Wrong arguments count, it must be one")

    if command_name == command_names[2]:
        if not len(inputs) == 6:
            raise SyntaxError("Wrong arguments count, it must be six")

        if not inputs[2].isnumeric() or not inputs[3].isnumeric():
            raise TypeError(
                "Wrong type of count of nodes in cycles, it must be a number"
            )

        for i in (inputs[4], inputs[5]):
            if not i.isalpha():
                raise TypeError(
                    "Wrong type of edge labels, it must be a chars (strings)"
                )


def repl():
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
        except FileNotFoundError as err:
            print(err)
            continue
