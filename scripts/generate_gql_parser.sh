#!/bin/sh

cd project/gql/parser/grammar
antlr4 -Dlanguage=Python3 -visitor ./gql.g4 -o ../antlr
