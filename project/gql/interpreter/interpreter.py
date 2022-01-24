from project.gql.parser.parser import parse
from project.gql.interpreter.antlr.visitor import Visitor
from project.gql.interpreter.core.exceptions import (
    RuntimeException,
    ProgramPathException,
    ProgramExtensionException,
)

from pathlib import Path
import sys

__all__ = ["interpreter", "read_program"]


def interpreter(*argv):
    """
    GQL interpreter function.

    Parameters
    ----------
    argv:
        0 params - no filename given, interpret program in console mode
        1 params - filename given, interpret program from the file with '.gql' extension
        2+ params - ignored

    Returns
    -------
    code: int
        Interpreter exit code

    Raises
    ------
    RuntimeException
        Interpreter exception
    """

    if len(argv[0]) == 0:
        sys.stdout.write("No file given, console mode is ON\n=====================\n")
        prog = "".join(sys.stdin.readlines())
    else:
        prog = read_program(Path(argv[0][0]))

    return _interpreter(prog)


def read_program(filename: Path) -> str:
    """
    Read program with '.gql' extension.

    Parameters
    ----------
    filename: str
        Name of the file with program as '*.gql'

    Returns
    -------
    program: str
        Program text
    """

    try:
        prog = filename.open()
    except FileNotFoundError as exception:
        raise ProgramPathException(filename.name) from exception

    if not filename.name.endswith(".gql"):
        raise ProgramExtensionException()

    return "".join(prog.readlines())


def _interpreter(prog: str):
    """
    Interpreter function.

    Parameters
    ----------
    prog: str
        Program text

    Returns
    -------
    error_code: int
        0 - success
        1 - failed
    """

    parser = parse(prog)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise RuntimeException("Invalid syntax.")

    visitor = Visitor()
    visitor.visit(tree)

    return 0
