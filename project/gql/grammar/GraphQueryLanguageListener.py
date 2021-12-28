# Generated from ./project/gql/grammar/GraphQueryLanguage.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphQueryLanguageParser import GraphQueryLanguageParser
else:
    from GraphQueryLanguageParser import GraphQueryLanguageParser

# This class defines a complete listener for a parse tree produced by GraphQueryLanguageParser.
class GraphQueryLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by GraphQueryLanguageParser#prog.
    def enterProg(self, ctx:GraphQueryLanguageParser.ProgContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#prog.
    def exitProg(self, ctx:GraphQueryLanguageParser.ProgContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#stmt.
    def enterStmt(self, ctx:GraphQueryLanguageParser.StmtContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#stmt.
    def exitStmt(self, ctx:GraphQueryLanguageParser.StmtContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#expr.
    def enterExpr(self, ctx:GraphQueryLanguageParser.ExprContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#expr.
    def exitExpr(self, ctx:GraphQueryLanguageParser.ExprContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#graph.
    def enterGraph(self, ctx:GraphQueryLanguageParser.GraphContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#graph.
    def exitGraph(self, ctx:GraphQueryLanguageParser.GraphContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#load_graph.
    def enterLoad_graph(self, ctx:GraphQueryLanguageParser.Load_graphContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#load_graph.
    def exitLoad_graph(self, ctx:GraphQueryLanguageParser.Load_graphContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#set_start.
    def enterSet_start(self, ctx:GraphQueryLanguageParser.Set_startContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#set_start.
    def exitSet_start(self, ctx:GraphQueryLanguageParser.Set_startContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#set_final.
    def enterSet_final(self, ctx:GraphQueryLanguageParser.Set_finalContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#set_final.
    def exitSet_final(self, ctx:GraphQueryLanguageParser.Set_finalContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#add_start.
    def enterAdd_start(self, ctx:GraphQueryLanguageParser.Add_startContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#add_start.
    def exitAdd_start(self, ctx:GraphQueryLanguageParser.Add_startContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#add_final.
    def enterAdd_final(self, ctx:GraphQueryLanguageParser.Add_finalContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#add_final.
    def exitAdd_final(self, ctx:GraphQueryLanguageParser.Add_finalContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#vertices.
    def enterVertices(self, ctx:GraphQueryLanguageParser.VerticesContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#vertices.
    def exitVertices(self, ctx:GraphQueryLanguageParser.VerticesContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#vertex.
    def enterVertex(self, ctx:GraphQueryLanguageParser.VertexContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#vertex.
    def exitVertex(self, ctx:GraphQueryLanguageParser.VertexContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#edges.
    def enterEdges(self, ctx:GraphQueryLanguageParser.EdgesContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#edges.
    def exitEdges(self, ctx:GraphQueryLanguageParser.EdgesContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#edge.
    def enterEdge(self, ctx:GraphQueryLanguageParser.EdgeContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#edge.
    def exitEdge(self, ctx:GraphQueryLanguageParser.EdgeContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#labels.
    def enterLabels(self, ctx:GraphQueryLanguageParser.LabelsContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#labels.
    def exitLabels(self, ctx:GraphQueryLanguageParser.LabelsContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#label.
    def enterLabel(self, ctx:GraphQueryLanguageParser.LabelContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#label.
    def exitLabel(self, ctx:GraphQueryLanguageParser.LabelContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#anfunc.
    def enterAnfunc(self, ctx:GraphQueryLanguageParser.AnfuncContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#anfunc.
    def exitAnfunc(self, ctx:GraphQueryLanguageParser.AnfuncContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#mapping.
    def enterMapping(self, ctx:GraphQueryLanguageParser.MappingContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#mapping.
    def exitMapping(self, ctx:GraphQueryLanguageParser.MappingContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#filtering.
    def enterFiltering(self, ctx:GraphQueryLanguageParser.FilteringContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#filtering.
    def exitFiltering(self, ctx:GraphQueryLanguageParser.FilteringContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#select_edges.
    def enterSelect_edges(self, ctx:GraphQueryLanguageParser.Select_edgesContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#select_edges.
    def exitSelect_edges(self, ctx:GraphQueryLanguageParser.Select_edgesContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#select_labels.
    def enterSelect_labels(self, ctx:GraphQueryLanguageParser.Select_labelsContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#select_labels.
    def exitSelect_labels(self, ctx:GraphQueryLanguageParser.Select_labelsContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#select_reachable.
    def enterSelect_reachable(self, ctx:GraphQueryLanguageParser.Select_reachableContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#select_reachable.
    def exitSelect_reachable(self, ctx:GraphQueryLanguageParser.Select_reachableContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#select_final.
    def enterSelect_final(self, ctx:GraphQueryLanguageParser.Select_finalContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#select_final.
    def exitSelect_final(self, ctx:GraphQueryLanguageParser.Select_finalContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#select_start.
    def enterSelect_start(self, ctx:GraphQueryLanguageParser.Select_startContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#select_start.
    def exitSelect_start(self, ctx:GraphQueryLanguageParser.Select_startContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#select_vertices.
    def enterSelect_vertices(self, ctx:GraphQueryLanguageParser.Select_verticesContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#select_vertices.
    def exitSelect_vertices(self, ctx:GraphQueryLanguageParser.Select_verticesContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#vertices_range.
    def enterVertices_range(self, ctx:GraphQueryLanguageParser.Vertices_rangeContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#vertices_range.
    def exitVertices_range(self, ctx:GraphQueryLanguageParser.Vertices_rangeContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#cfg.
    def enterCfg(self, ctx:GraphQueryLanguageParser.CfgContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#cfg.
    def exitCfg(self, ctx:GraphQueryLanguageParser.CfgContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#string.
    def enterString(self, ctx:GraphQueryLanguageParser.StringContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#string.
    def exitString(self, ctx:GraphQueryLanguageParser.StringContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#path.
    def enterPath(self, ctx:GraphQueryLanguageParser.PathContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#path.
    def exitPath(self, ctx:GraphQueryLanguageParser.PathContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#vertices_set.
    def enterVertices_set(self, ctx:GraphQueryLanguageParser.Vertices_setContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#vertices_set.
    def exitVertices_set(self, ctx:GraphQueryLanguageParser.Vertices_setContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#labels_set.
    def enterLabels_set(self, ctx:GraphQueryLanguageParser.Labels_setContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#labels_set.
    def exitLabels_set(self, ctx:GraphQueryLanguageParser.Labels_setContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#edges_set.
    def enterEdges_set(self, ctx:GraphQueryLanguageParser.Edges_setContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#edges_set.
    def exitEdges_set(self, ctx:GraphQueryLanguageParser.Edges_setContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#var.
    def enterVar(self, ctx:GraphQueryLanguageParser.VarContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#var.
    def exitVar(self, ctx:GraphQueryLanguageParser.VarContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#var_edge.
    def enterVar_edge(self, ctx:GraphQueryLanguageParser.Var_edgeContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#var_edge.
    def exitVar_edge(self, ctx:GraphQueryLanguageParser.Var_edgeContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#variables.
    def enterVariables(self, ctx:GraphQueryLanguageParser.VariablesContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#variables.
    def exitVariables(self, ctx:GraphQueryLanguageParser.VariablesContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#val.
    def enterVal(self, ctx:GraphQueryLanguageParser.ValContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#val.
    def exitVal(self, ctx:GraphQueryLanguageParser.ValContext):
        pass


    # Enter a parse tree produced by GraphQueryLanguageParser#boolean.
    def enterBoolean(self, ctx:GraphQueryLanguageParser.BooleanContext):
        pass

    # Exit a parse tree produced by GraphQueryLanguageParser#boolean.
    def exitBoolean(self, ctx:GraphQueryLanguageParser.BooleanContext):
        pass


