from project.gql.parser.parser import parse
from project.gql.interpreter.antlr.visitor import Visitor
from project.gql.interpreter.types.type import Type


def interpret(text: str, token: str) -> Type:
    parser = parse(text)
    parser.removeErrorListeners()

    tree = getattr(parser, token)()

    visitor = Visitor()
    value = visitor.visit(tree)

    return value
