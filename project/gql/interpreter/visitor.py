from project.gql.parser.antlr.gqlVisitor import gqlVisitor
from project.gql.parser.antlr.gqlParser import gqlParser

from project.gql.interpreter.types.type import Type
from project.gql.interpreter.types.automaton import Automaton
from project.gql.interpreter.types.finite_automaton import FiniteAutomaton
from project.gql.interpreter.types.bool import Bool
from project.gql.interpreter.types.set import Set
from project.gql.interpreter.types.context_free_grammar import ContextFreeGrammar

from project.gql.interpreter.memory.memory import Memory

from project.gql.interpreter.core.runtime import load_graph

from project.gql.interpreter.core.exceptions import NotImplementedException, TypingError

from antlr4 import ParserRuleContext
from typing import Union
from collections import namedtuple

import sys

Anfunc = namedtuple("Anfunc", ["parameters", "body"])


class Visitor(gqlVisitor):
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
        unary_operations = {"NOT": "inverse", "KLEENE": "kleene"}
        binary_operations = {
            "AND": "intersect",
            "OR": "union",
            "DOT": "concatenate",
            "IN": "find",
        }

        for un_op in unary_operations:
            if getattr(ctx, un_op)():
                _type = self.visit(ctx.expr(0))

                return getattr(_type, unary_operations[un_op])()

        for bin_op in binary_operations:
            if getattr(ctx, bin_op)():
                left_type = self.visit(ctx.expr(0))
                right_type = self.visit(ctx.expr(1))

                if bin_op == "IN":
                    left_type, right_type = right_type, left_type

                return getattr(left_type, binary_operations[bin_op])(right_type)

        return self.visitChildren(ctx)

    def visitString(self, ctx: gqlParser.StringContext):
        value = ctx.STRING().getText()

        return value

    def visitBoolean(self, ctx: gqlParser.BooleanContext):
        return Bool(ctx.TRUE() is not None)

    def visitVar(self, ctx: gqlParser.VarContext):
        name = ctx.ID().getText()

        return self.memory.find_variable(name)

    def visitVertex(self, ctx: gqlParser.VertexContext):
        return int(ctx.INT().getText())

    def visitVertices_range(self, ctx: gqlParser.Vertices_rangeContext):
        start = int(ctx.INT(0).getText())
        end = int(ctx.INT(1).getText())

        return Set(set(range(start, end + 1)))

    def visitVertices_set(self, ctx: gqlParser.Vertices_setContext):
        if ctx.vertices_range():
            return self.visit(ctx.vertices_range())
        else:
            return Set(set(map(lambda x: int(x.getText()), ctx.INT())))

    def visitLabel(self, ctx: gqlParser.LabelContext):
        return FiniteAutomaton.from_string(self.visit(ctx.string()))

    def visitLabels_set(self, ctx: gqlParser.Labels_setContext):
        labels_set = set()

        for label in ctx.STRING():
            labels_set.add(label.getText())

        return Set(labels_set)

    def visitEdge(self, ctx: gqlParser.EdgeContext):
        vertex_from = self.visit(ctx.vertex(0))
        label = self.visit(ctx.label())
        vertex_to = self.visit(ctx.vertex(1))

        return vertex_from, label, vertex_to

    def visitEdges(self, ctx: gqlParser.EdgesContext):
        return self.visitChildren(ctx)

    def visitCfg(self, ctx: gqlParser.CfgContext) -> ContextFreeGrammar:
        cfg_text = ctx.CFG().getText().strip('"""')

        return ContextFreeGrammar.from_text(cfg_text)

    def visitEdges_set(self, ctx: gqlParser.Edges_setContext):
        edges_set = set()

        for edge in ctx.edge():
            edges_set.add(self.visitEdge(edge))

        return Set(edges_set)

    def visitVariables(self, ctx: gqlParser.VariablesContext):
        anfunc_context = {}

        if ctx.var_edge():
            raise NotImplementedException("Anfunc does not support var_edge now.")
        else:
            for var in ctx.var():
                anfunc_context[var.getText()] = None

        return anfunc_context

    def visitVar_edge(self, ctx: gqlParser.Var_edgeContext):
        pass

    def visitAnfunc(self, ctx: gqlParser.AnfuncContext) -> Anfunc:
        parameters = self.visitVariables(ctx.variables())
        body = ctx.expr()

        return Anfunc(parameters, body)

    def apply_anfunc(self, anfunc: Anfunc, value: Type = None) -> Type:
        self.memory = self.memory.next_scope()

        if len(anfunc.parameters) > 0 and value is not None:
            name = next(iter(anfunc.parameters))
            self.memory.add_variable(name, value)

        result = self.visit(anfunc.body)

        self.memory = self.memory.previous_scope()

        return result

    def iter_func(
        self,
        ctx: Union[gqlParser.MappingContext, gqlParser.FilteringContext],
        func="map",
    ):
        anfunc = self.visit(ctx.anfunc())
        iterable = self.visit(ctx.expr())

        if not isinstance(iterable, Set):
            raise TypingError(
                f"Could not apply {func} on {type(iterable)} object. Set is expected."
            )

        if len(iterable) == 0:
            return iterable

        raise NotImplementedException("TODO")

    def visitMapping(self, ctx: gqlParser.MappingContext):
        self.iter_func(ctx, "map")

    def visitFiltering(self, ctx: gqlParser.FilteringContext):
        self.iter_func(ctx, "filter")

    def visitGraph(self, ctx: gqlParser.GraphContext) -> Automaton:
        return self.visitChildren(ctx)

    def visitLoad_graph(self, ctx: gqlParser.Load_graphContext):
        name = ctx.string().getText().strip('"')

        return load_graph(name)

    def modify_func(
        self,
        ctx: Union[
            gqlParser.Set_startContext,
            gqlParser.Set_finalContext,
            gqlParser.Add_startContext,
            gqlParser.Add_finalContext,
        ],
        func,
    ):
        graph = self.visit(ctx.var(0)) if ctx.var(0) else self.visit(ctx.graph())
        nodes = self.visit(ctx.var(1)) if ctx.var(1) else self.visit(ctx.vertices())

        getattr(graph, func)(nodes)

        return graph

    def visitSet_start(self, ctx: gqlParser.Set_startContext):
        return self.modify_func(ctx, "set_start")

    def visitSet_final(self, ctx: gqlParser.Set_finalContext):
        return self.modify_func(ctx, "set_final")

    def visitAdd_start(self, ctx: gqlParser.Add_startContext):
        return self.modify_func(ctx, "add_start")

    def visitAdd_final(self, ctx: gqlParser.Add_finalContext):
        return self.modify_func(ctx, "add_final")

    def description_func(
        self,
        ctx: Union[
            gqlParser.Select_edgesContext,
            gqlParser.Select_labelsContext,
            gqlParser.Select_verticesContext,
            gqlParser.Select_startContext,
            gqlParser.Select_finalContext,
        ],
        func,
    ):
        graph = self.visit(ctx.var()) if ctx.var() else self.visit(ctx.graph())

        return getattr(graph, func)

    def visitSelect_edges(self, ctx: gqlParser.Select_edgesContext):
        return self.description_func(ctx, "edges")

    def visitSelect_labels(self, ctx: gqlParser.Select_labelsContext):
        return self.description_func(ctx, "labels")

    def visitSelect_start(self, ctx: gqlParser.Select_startContext):
        return self.description_func(ctx, "start")

    def visitSelect_final(self, ctx: gqlParser.Select_finalContext):
        return self.description_func(ctx, "final")

    def visitSelect_vertices(self, ctx: gqlParser.Select_verticesContext):
        return self.description_func(ctx, "vertices")

    def visitSelect_reachable(self, ctx: gqlParser.Select_reachableContext):
        graph = self.visit(ctx.var()) if ctx.var() else self.visit(ctx.graph())

        return graph.get_reachable()
