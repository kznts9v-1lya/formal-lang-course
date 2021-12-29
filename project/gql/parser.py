from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, ParserRuleContext
from antlr4.error.Errors import ParseCancellationException
from antlr4.tree.Tree import TerminalNodeImpl
from pydot import Dot, Node, Edge

from project.gql.antlr.gqlLexer import gqlLexer
from project.gql.antlr.gqlParser import gqlParser
from project.gql.antlr.gqlListener import gqlListener

__all__ = ["parse", "accept", "generate_dot"]


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


class DotTreeListener(gqlListener):
    def __init__(self, tree: Dot, rules):
        self.tree = tree
        self.num_nodes = 0
        self.nodes = {}
        self.rules = rules

        super(DotTreeListener, self).__init__()

    def enterEveryRule(self, ctx: ParserRuleContext):
        if ctx not in self.nodes:
            self.num_nodes += 1
            self.nodes[ctx] = self.num_nodes

        if ctx.parentCtx:
            self.tree.add_edge(Edge(self.nodes[ctx.parentCtx], self.nodes[ctx]))

        label = self.rules[ctx.getRuleIndex()]
        self.tree.add_node(Node(self.nodes[ctx], label=label))

    def visitTerminal(self, node: TerminalNodeImpl):
        self.num_nodes += 1
        self.tree.add_edge(Edge(self.nodes[node.parentCtx], self.num_nodes))
        self.tree.add_node(Node(self.num_nodes, label=f"TERM: {node.getText()}"))


def generate_dot(text: str, path: str):
    if not accept(text):
        raise ParseCancellationException("The word doesn't match the ANTLR")

    ast = parse(text).prog()
    tree = Dot("tree", graph_type="digraph")
    ParseTreeWalker().walk(DotTreeListener(tree, gqlParser.ruleNames), ast)

    tree.write(path)
