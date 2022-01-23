from project.gql.interpreter.types.type import Type

from project.gql.interpreter.core.exceptions import NotImplementedException


class Bool(Type):
    def __init__(self, b: bool):
        self.b = b

    def __str__(self):
        return "TRUE" if self.b else "FALSE"

    def __bool__(self) -> bool:
        return self.b

    def __hash__(self):
        return hash(self.b)

    def __eq__(self, other: "Bool") -> bool:
        return self.b == other.b

    def intersect(self, other: "Bool") -> "Bool":
        return Bool(self.b and other.b)

    def union(self, other: "Bool") -> "Bool":
        return Bool(self.b or other.b)

    def concatenate(self, other):
        raise NotImplementedException("Bool does not support '.' operation.")

    def inverse(self) -> "Bool":
        return Bool(not self.b)

    def kleene(self):
        raise NotImplementedException("Bool does not support '*' operation.")
