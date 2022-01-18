from project.gql.interpreter.exceptions import RuntimeException
from project.gql.parser.parser import parse
from project.gql.interpreter.visitor import Visitor

__all__ = ["interpreter"]


def interpreter(prog: str):
    parser = parse(prog)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise RuntimeException("Invalid syntax.")

    visitor = Visitor()
    visitor.visit(tree)

    return 0
