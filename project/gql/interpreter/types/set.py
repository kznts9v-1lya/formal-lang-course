from project.gql.interpreter.types.type import Type
from project.gql.interpreter.types.bool import Bool

from project.gql.interpreter.exceptions import NotImplementedException, TypingError


class Set(Type):
    def __init__(self, s: set):
        self.t = Set.get_type(s)
        self.s = s

    def __len__(self) -> int:
        return len(self.s)

    def __str__(self):
        return "{" + ", ".join(map(lambda x: str(x), self.set)) + "}"

    @classmethod
    def from_set(cls, s: set) -> "Set":
        if not Set.type_consistency(s):
            raise TypingError("Inconsistent types in set.")

        return Set(s)

    @staticmethod
    def get_type(s: set) -> type:
        if len(s) == 0:
            return type(None)

        iter_seq = iter(s)

        return type(next(iter_seq))

    @staticmethod
    def type_consistency(s: set) -> bool:
        if len(s) == 0:
            return True

        iter_seq = iter(s)
        t = type(next(iter_seq))

        return all(map(lambda x: isinstance(x, t), iter_seq))

    @property
    def type(self) -> type:
        return self.t

    @property
    def set(self) -> set:
        return self.s

    def find(self, v) -> Bool:
        return Bool(v in self.s)

    def intersect(self, other: "Set") -> "Set":
        if self.set and other.set and self.type != other.type:
            raise TypingError(f"Types mismatched: {self.type} not equals {other.type}.")

        return Set(self.set & other.set)

    def union(self, other: "Set") -> "Set":
        if self.set and other.set and self.type != other.type:
            raise TypingError(f"Types mismatched: {self.type} not equals {other.type}.")

        return Set(self.set | other.set)

    def concatenate(self, other):
        raise NotImplementedException("Use union operation for sets.")

    def inverse(self):
        raise NotImplementedException("Set does not support 'NOT' operation.")

    def kleene(self):
        raise NotImplementedException("Set does not support '*' operation.")
