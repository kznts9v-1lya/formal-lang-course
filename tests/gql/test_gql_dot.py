import os

from project.gql.parser.parser import write_to_dot

path = os.sep.join(
    [
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "dots",
    ]
)
actual_path = os.sep.join([path, "actual.dot"])
expected_path = os.sep.join([path, "expected.dot"])


def test_write_to_dot():
    line = """Ig1 = LOAD GRAPH 'wine'
Ig1 = LOAD GRAPH FROM 'home/wine.dot'
Iquery1 = ('type' || Il1)**\n"""
    status = write_to_dot(line, actual_path)
    obtained = open(actual_path, "r")

    expected = open(expected_path, "r")
    assert (expected.read() == obtained.read()) and status


def test_incorrect_text():
    line = """Ig1 Ig2 = LOAD GRAPH 'wine'
Ig1 = LOAD GRAPH FROM 'home/wine.dot'
Iquery1 = ('type' || Il1)**\n"""
    status = write_to_dot(line, actual_path)

    assert not status
