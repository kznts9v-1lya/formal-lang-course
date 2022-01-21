import sys
from antlr4 import *
from project.gql.parser.antlr.gqlLexer import gqlLexer
from project.gql.parser.antlr.gqlParser import gqlParser
from project.gql.parser.antlr.gqlListener import gqlListener

from pydot import Dot, Node, Edge
from antlr4.tree.Tree import TerminalNodeImpl

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, ParserRuleContext


def main(argv):
    input_ = FileStream(argv[1])
    lexer = gqlLexer(input_)

    # lexer = grammarGQLLexer(InputStream(argv[1]))
    stream = CommonTokenStream(lexer)
    parser = gqlParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))


def parse_to_string(line):
    lexer = gqlLexer(InputStream(line))
    stream = CommonTokenStream(lexer)
    parser = gqlParser(stream)
    tree = parser.prog()
    return tree.toStringTree(recog=parser)


def is_in_grammar(line):
    lexer = gqlLexer(InputStream(line))
    stream = CommonTokenStream(lexer)
    parser = gqlParser(stream)
    parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        return False
    else:
        return True


def write_to_dot(line: str, path: str):
    if not is_in_grammar(line):
        print("Can not parse input line!")
        return False
    lexer = gqlLexer(InputStream(line))
    stream = CommonTokenStream(lexer)
    parser = gqlParser(stream)
    ast = parser.prog()
    tree = Dot("tree", graph_type="digraph")
    ParseTreeWalker().walk(DotTreeListener(tree, gqlParser.ruleNames), ast)
    tree.write(path)
    return True


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


if __name__ == "__main__":
    main(sys.argv)
