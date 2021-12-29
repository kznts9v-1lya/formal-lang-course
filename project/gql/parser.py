from antlr4 import InputStream, CommonTokenStream

from project.gql.antlr.gqlLexer import gqlLexer
from project.gql.antlr.gqlParser import gqlParser

__all__ = ["parse", "accept"]


def parse(text: str) -> gqlParser:
    input_stream = InputStream(text)
    lexer = gqlLexer(input_stream)
    lexer.removeErrorListeners()
    token_stream = CommonTokenStream(lexer)
    parser = gqlParser(token_stream)

    return parser


def accept(text: str) -> bool:
    parser = parse(text)
    parser.removeErrorListeners()
    _ = parser.prog()

    return parser.getNumberOfSyntaxErrors() == 0
