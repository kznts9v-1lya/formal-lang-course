import sys

from antlr4 import InputStream, CommonTokenStream

from project.gql.parser.antlr.gqlLexer import gqlLexer
from project.gql.parser.antlr.gqlParser import gqlParser

if __name__ == '__main__':
    input_stream = InputStream(''.join(sys.stdin.readlines()))

    lexer = gqlLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gqlParser(token_stream)

    tree = parser.prog()


