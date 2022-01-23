from project.gql.interpreter.core.exceptions import RuntimeException
from project.gql.parser.parser import parse
from project.gql.interpreter.visitor import Visitor

__all__ = ["interpreter"]


def interpreter(prog: str):
    """
    Interpreter function.

    Parameters
    ----------
    prog: str
        Program text

    Returns
    -------
    error_code: int
        0 - success
        1 - failed
    """

    parser = parse(prog)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise RuntimeException("Invalid syntax.")

    visitor = Visitor()
    visitor.visit(tree)

    return 0
