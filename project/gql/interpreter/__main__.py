import sys

from project.gql.interpreter.interpreter import interpreter


def main():
    prog = "".join(sys.stdin.readlines())

    return interpreter(prog)


if __name__ == "__main__":
    main()
