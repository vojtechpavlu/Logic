""""""

from abc import ABC, abstractmethod
from scripts.src.environment import Environment
from typing import Iterable


class Term(ABC):
    """"""

    @abstractmethod
    def evaluate(self, env: Environment = None) -> bool:
        """"""


class Atom(Term):
    """"""

    def __init__(self, atom_name: str, value: bool = None):
        """"""
        self._atom_name = atom_name
        self._value = value

    @property
    def atom_name(self) -> str:
        return self._atom_name

    @property
    def value(self) -> bool:
        return self._value

    @property
    def is_defined(self) -> bool:
        return self._value is not None

    @atom_name.setter
    def atom_name(self, new_name: str):
        self._atom_name = new_name

    @value.setter
    def value(self, new_value: bool):
        self._value = new_value

    def evaluate(self, env: Environment = None) -> bool:
        """"""
        if self.is_defined:
            return self.value
        elif env and env.has_declaration(self.atom_name):
            return env.declaration(self.atom_name).value
        else:
            raise Exception(f"Value of atom '{self.atom_name}' is not defined")


class Constant(Atom):
    """"""

    def __init__(self, value: bool, constant_name: str = None):
        """"""
        Atom.__init__(self, constant_name, value)

        if not self.is_defined:
            raise Exception(f"Constant has to be defined")

        if not self.atom_name:
            self.atom_name = "TRUE" if value else "FALSE"


class Operation(Term):
    """"""

    def __init__(self, terms: Iterable[Term]):
        """"""
        self._terms = list(terms)

        # Checks the correctness of the given terms
        self._check_terms(self._terms)

    @property
    @abstractmethod
    def cardinality(self) -> int:
        """"""

    @property
    def terms(self) -> tuple[Term]:
        """"""
        return tuple(self._terms)

    @terms.setter
    def terms(self, terms: Iterable[Term]):
        """"""
        terms = list(terms)
        self._check_terms(terms)
        self._terms = terms

    def can_be_applied(self, terms: Iterable[Term]):
        """"""
        try:
            self._check_terms(list(terms))
            return True
        except Exception:
            return False

    def _check_terms(self, terms: list[Term]):
        """"""
        # Only actual terms stays there
        terms = [term for term in terms if isinstance(term, Term)]

        if len(terms) != self.cardinality:
            raise Exception(
                f"Number of terms ({len(self._terms)}) is not equal to "
                f"cardinality of the operator ({self.cardinality})")




