import sys

from project.gql.interpreter.interpreter import interpreter
from project.gql.interpreter.core.exceptions import RuntimeException


def main(*argv):
    try:
        interpreter(*argv)
    except RuntimeException as exception:
        sys.stdout.write(f"Exception: {exception.message}\n")

        exit(1)

    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
