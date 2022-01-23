from project.gql.interpreter.interpreter import read_program, interpreter
from project.gql.interpreter.core.exceptions import (
    ProgramPathException,
    ProgramExtensionException,
)

from pathlib import Path

import pytest


def test_invalid_file_path():
    with pytest.raises(ProgramPathException):
        read_program(Path("blablabla").absolute())


def test_invalid_file_extension():
    with pytest.raises(ProgramExtensionException):
        read_program(Path("tests/data/gqls/invalid.ggqqll"))


@pytest.mark.parametrize(
    "program",
    [
        "tests/data/gqls/labels_intersection.gql",
        "tests/data/gqls/labels_filter.gql",
        "tests/data/gqls/regex_intersection.gql",
        "tests/data/gqls/regular_path_querying.gql",
    ],
)
def test_correct_script(program):
    assert interpreter([Path(program)]) == 0
