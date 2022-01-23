from project.gql.interpreter.types.type import Type
from project.gql.interpreter.types.bool import Bool

from project.gql.interpreter.core.exceptions import NotImplementedException, TypingError


class Set(Type):
    """
    Set object with type consistency.

    Attributes
    ----------
    s: set
        Python set object
    t: type
        Python type object
    """

    def __init__(self, s: set):
        self.t = Set.get_type(s)
        self.s = s

    def __len__(self) -> int:
        return len(self.s)

    def __str__(self):
        return "{" + ", ".join(map(lambda x: str(x), self.set)) + "}"

    @classmethod
    def from_set(cls, s: set) -> "Set":
        """
        Parameters
        ----------
        s: set
            Python set object

        Returns
        -------
        set: Set
            A Set object

        Raises
        ------
        TypingError
            If set type is inconsistent
        """

        if not Set._type_consistency(s):
            raise TypingError("Inconsistent types in a set.")

        return Set(s)

    @staticmethod
    def get_type(s: set) -> type:
        """
        Parameters
        ----------
        s: set
            Python set object

        Returns
        -------
        t: type
            First element type
        """

        if len(s) == 0:
            return type(None)

        iter_seq = iter(s)

        return type(next(iter_seq))

    @staticmethod
    def _type_consistency(s: set) -> bool:
        """
        Parameters
        ----------
        s: set
            Python set object

        Returns
        -------
        is_consistent: bool
            True if elements have the same type
            False otherwise
        """

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
        """
        Check whether value in set or not.

        Parameters
        ----------
        v
            Object for search

        Returns
        -------
        b: Bool
            True if value is in set
            False otherwise
        """

        return Bool(v in self.s)

    def intersect(self, other: "Set") -> "Set":
        """
        Intersection of two Sets.

        Parameters
        ----------
        other: Set
            Another Set object to intersect

        Returns
        -------
        intersection: Set
            Intersection of two Sets

        Raises
        ------
        TypingError
            If given Sets have different types
        """

        if self.set and other.set and self.type != other.type:
            raise TypingError(f"Types mismatched: {self.type} not equals {other.type}.")

        return Set(self.set & other.set)

    def union(self, other: "Set") -> "Set":
        """
        Union of two Sets.

        Parameters
        ----------
        other: Set
            Another Set object to unite

        Returns
        -------
        union: Set
            Union of two Sets

        Raises
        ------
        TypingError
            If given Sets have different types
        """

        if self.set and other.set and self.type != other.type:
            raise TypingError(f"Types mismatched: {self.type} not equals {other.type}.")

        return Set(self.set | other.set)

    def concatenate(self, other):
        raise NotImplementedException("Use union operation for sets.")

    def inverse(self):
        raise NotImplementedException("Set does not support 'NOT' operation.")

    def kleene(self):
        raise NotImplementedException("Set does not support '*' operation.")
