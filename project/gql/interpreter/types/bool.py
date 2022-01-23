from project.gql.interpreter.types.type import Type

from project.gql.interpreter.core.exceptions import NotImplementedException


class Bool(Type):
    """
    Boolean class.

    Attributes
    ----------
    b: bool
        Internal boolean value
    """

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
        """
        '&'.

        Parameters
        ----------
        other: Bool
            Right boolean object
        Returns
        -------
        intersection: Bool
            Logical 'AND'
        """

        return Bool(self.b and other.b)

    def union(self, other: "Bool") -> "Bool":
        """
        '|'.

        Parameters
        ----------
        other: Bool
            Right boolean object
        Returns
        -------
        intersection: Bool
            Logical 'OR'
        """

        return Bool(self.b or other.b)

    def concatenate(self, other):
        raise NotImplementedException("Bool does not support '.' operation.")

    def inverse(self) -> "Bool":
        """
        'NOT'.

        Returns
        -------
        complement: Bool
            Logical 'NOT'
        """

        return Bool(not self.b)

    def kleene(self):
        raise NotImplementedException("Bool does not support '*' operation.")
