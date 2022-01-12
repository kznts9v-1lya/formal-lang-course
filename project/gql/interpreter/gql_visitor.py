from project.gql.parser.antlr.gqlVisitor import gqlVisitor, gqlParser

from project.gql.interpreter.types.type import Type
from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.regex import Regex
from project.gql.interpreter.types.bool import Bool
from project.gql.interpreter.types.set import Set

from project.gql.interpreter.memory.memory import Memory

from project.gql.interpreter.core.runtime import load_graph

from project.gql.interpreter.exceptions import NotImplementedException, TypingError

from antlr4 import ParserRuleContext
from typing import Union
from collections import namedtuple

import sys

Lambda = namedtuple("Lambda", ["parameters", "body"])


class GQLVisitor(gqlVisitor):
    def __init__(self):
        self.memory = Memory()

    def visitProg(self, ctx: ParserRuleContext):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx: gqlParser.StmtContext):
        if ctx.PRINT():
            value = self.visit(ctx.expr())

            sys.stdout.write(str(value) + "\n")
        else:
            name = ctx.var().getText()
            value = self.visit(ctx.expr())

            self.memory.add_variable(name, value)

    def visitExpr(self, ctx: gqlParser.ExprContext) -> Type:
        binary_operations = {"AND": "intersect", "OR": "union", "DOT": "concatenate", "IN": "find_variable"}
        unary_operations = {"NOT": "inverse", "KLEENE": "kleene"}

        for bin_op in binary_operations:
            if getattr(ctx, bin_op)():
                left_type = self.visit(ctx.expr(0))
                right_type = self.visit(ctx.expr(1))

                if bin_op == "IN":
                    left_type, right_type = right_type, left_type

                return getattr(left_type, binary_operations[bin_op])(right_type)

        for un_op in unary_operations:
            if getattr(ctx, un_op)():
                _type = self.visit(ctx.expr(0))

                return getattr(_type, unary_operations[un_op])()

        return self.visitChildren(ctx)



