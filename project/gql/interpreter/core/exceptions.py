class RuntimeException(Exception):
    """
    Base interpreter exception.
    """

    def __init__(self, message: str):
        self.message = message


class TypingError(RuntimeException):
    """
    Raises in case of differences between expected and actual type.
    """

    pass


class ProgramPathException(RuntimeException):
    """
    Raises when failed to open the given program.
    """

    def __init__(self, file: str):
        self.message = f"Could not open program from {file}."


class ProgramExtensionException(RuntimeException):
    """
    Raises when given program file does not have '.gql' extension.
    """

    def __init__(self):
        self.message = f"Program file does not have '.gql' extension."


class GraphLoadingException(RuntimeException):
    """
    Raises if there is an error while loading the graph.
    """

    def __init__(self, name: str):
        self.message = (
            f"Could not load graph '{name}'. Check correctness of given name."
        )


class CastingException(RuntimeException):
    """
    Raises if it is impossible to cast two types.
    """

    def __init__(self, left_type: str, right_type: str):
        self.message = f"Casting error between {left_type} and {right_type}."


class VariableNotFoundException(RuntimeException):
    """
    Raises if variable is not found in Memory object.
    """

    def __init__(self, name: str):
        self.message = f"Variable '{name}' is not defined."


class NotImplementedException(RuntimeException):
    """
    Raises when evaluated instruction has not yet implemented.
    """

    def __init__(self, instruction):
        self.message = f"{instruction} is not implemented."
