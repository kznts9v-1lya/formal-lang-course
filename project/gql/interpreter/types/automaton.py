from abc import ABC, abstractmethod

from project.gql.interpreter.types.type import Type


class Automaton(Type, ABC):
    """
    Base class for Automatons.
    """

    @abstractmethod
    def set_start_states(self, start_states):
        pass

    @abstractmethod
    def set_final_states(self, final_states):
        pass

    @abstractmethod
    def add_start_states(self, start_states):
        pass

    @abstractmethod
    def add_final_states(self, final_states):
        pass

    @abstractmethod
    def get_reachable_states(self):
        pass

    @property
    @abstractmethod
    def start_states(self):
        pass

    @property
    @abstractmethod
    def final_states(self):
        pass

    @property
    @abstractmethod
    def symbols(self):
        pass

    @property
    @abstractmethod
    def transitions(self):
        pass

    @property
    @abstractmethod
    def states(self):
        pass
