import sys

from project.gql.interpreter.interpreter import interpreter
from project.gql.interpreter.core.exceptions import RuntimeException


def main():
    prog = "".join(sys.stdin.readlines())

    try:
        interpreter(prog)
        sys.stdout.write("\nSuccessfully done\nExit code: 0\n")
        return 0
    except RuntimeException as exception:
        sys.stdout.write(exception.message)
        sys.stdout.write("\nFailed\nExit code: 1\n")
        return 1


if __name__ == "__main__":
    main()
