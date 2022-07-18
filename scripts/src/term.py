"""This module contains a definition of logic primitives. That is a
definition of terms, atomic logical variables and operators."""

from abc import ABC, abstractmethod
from scripts.src.environment import Environment
from typing import Iterable, Callable


class Term(ABC):
    """Term is the most general logical primitive. The most significant
    property of this entity is it's ability to be evaluated.

    Realization of this class is abstract, thus it cannot be
    instantiated as is."""

    @property
    @abstractmethod
    def variable_names(self) -> tuple[str]:
        """Returns the tuple of names of variables contained in this term.
        When there is no variable in this term, it returns empty tuple."""

    @property
    @abstractmethod
    def clone(self) -> "Term":
        """Returns a deep copy of this term."""

    @property
    def terms(self) -> "tuple[Term]":
        """This property returns None as a default value, because there are
        no subterms of this term.

        See the Operation class and implementation of this property."""
        return None

    @abstractmethod
    def evaluate(self, env: Environment = None) -> bool:
        """Tries to evaluate the term.

        For resolving the actual logical  value, the definition of an
        environment variable may be needed to be provided. That's the
        reason for the env parameter.

        Parameters
        -----------
        env: Environment
            Declaration of values for specified variables.

        Raises
        ------
        Exception
            When the evaluation cannot be done. Typical reason is that
            there is an atomic variable without specified value.
        """

    def __eq__(self, other: "Term"):
        """Two terms are meant to be equivalent if and only if they are both
        type of Term and has the same string representation."""
        return isinstance(other, Term) and str(self) == str(other)

    def __repr__(self):
        return str(self)


class Atom(Term):
    """Atom is the most basic logic element. It consists of either constant
    value or a variable for logical value itself.

    As any other Term, when the actual value is not provided (by itself or
    using an environment), the evaluation fails.
    """

    def __init__(self, atom_name: str, value: bool = None):
        """Instances of Atom class provides a definition of the most basic
        logic element. It consists of a name of the atom and it's value.
        Because the value may be unknown (the atom may be variable), it's
        optional.

        Parameters
        ----------
        atom_name: str
            Name of the atom; never should be empty. The name can be changed
            at any time during the lifecycle of the instance.

        value: bool
            Value of the atom. When defined, it means the atom is constant.
            If not, the atom is variable. This value can be altered any time
            during the lifecycle of the instance.
        """
        self._atom_name = atom_name
        self._value = value

    @property
    def atom_name(self) -> str:
        """Name of the atom."""
        return self._atom_name

    @property
    def value(self) -> bool:
        """Currently set value to the atom. May be None if the atom is
        currently meant to be variable."""
        return self._value

    @property
    def is_defined(self) -> bool:
        """If the atom is variable (is not defined) returns False. If the
        actual logical value is set (True of False), it returns True."""
        return self._value is not None

    @property
    def variable_names(self) -> tuple[str]:
        """Returns name of this atom."""
        return self.atom_name,

    @atom_name.setter
    def atom_name(self, new_name: str):
        """Sets the current name to the atom. Should never be empty string.
        """
        self._atom_name = new_name

    @value.setter
    def value(self, new_value: bool):
        """Sets the current new value of this atom. This setter allows
        None value."""
        self._value = new_value

    @property
    def clone(self) -> "Term":
        return Atom(self.atom_name, self.value)

    def evaluate(self, env: Environment = None) -> bool:
        """Tries to evaluate the atom.

        If it's defined, returns the current value saved inside. Else, if
        the environment is given and contains the needed declaration, it
        returns this value.

        If the value remains unresolved, it raises exception about the lack
        of certainty of the result.
        """
        if self.is_defined:
            return self.value
        elif env and env.has_declaration(self.atom_name):
            return env.declaration(self.atom_name).value
        else:
            raise Exception(f"Value of atom '{self.atom_name}' is not defined")

    def __str__(self):
        """Returns string representation of this atom term."""
        return self.atom_name


class Constant(Atom):
    """Special type of the atom. It's given value is constantly set and
    should not be changed."""

    def __init__(self, value: bool, constant_name: str = None):
        """Constant type of the atom with given logical value and name.
        The name is optional and if not given, it will be changed to
        'TRUE' or 'FALSE'.

        Parameters
        ----------
        value: bool
            Logical value the constant should have. It is not allowed
            to be changed.

        constant_name: str, optional
            Name of the constant. This name may be generated.
        """
        Atom.__init__(self, constant_name, value)

        # If the value is not set
        if not self.is_defined:
            raise Exception(f"Constant has to be defined")

        # If name is not set as non-empty string
        if not self.atom_name:
            self.atom_name = "TRUE" if value else "FALSE"

    @property
    def value(self) -> bool:
        return super().value

    @value.setter
    def value(self, new_value: bool):
        """Constant should never be changed, thus it just raises exception.
        This property overrides the parent."""
        raise Exception(f"Value of the constant '{self.atom_name}' should "
                        f"never be changed.")

    @property
    def variable_names(self) -> tuple[str]:
        return tuple()

    def __str__(self):
        """Returns string representation of this constant."""
        return self.atom_name


class Operation(Term):
    """This class defines instances of the logical operators.
    These are used to make logical junctions of given terms and
    process it's evaluation.
    """

    def __init__(self, terms: Iterable[Term]):
        """Abstract logical operator build over given terms. These has to
        obey the set cardinality. When there is more or less of the terms,
        it raises exception."""
        self._terms = list(terms)

        # Checks the correctness of the given terms
        self._check_terms(self._terms)

    @property
    @abstractmethod
    def cardinality(self) -> int:
        """The number of parameters this operation works with."""

    @property
    @abstractmethod
    def operator_sign(self) -> str:
        """Returns the operator sign of this operation."""

    @property
    def terms(self) -> tuple[Term]:
        """Tuple of all terms this operation works with."""
        return tuple(self._terms)

    @terms.setter
    def terms(self, terms: Iterable[Term]):
        """Sets the terms. These has to obey the cardinality rule. When
        there is more or less of the terms, it raises exception.
        """
        terms = list(terms)
        self._check_terms(terms)
        self._terms = terms

    @property
    def variable_names(self) -> tuple[str]:
        """Returns all the variable names from the contained terms."""
        names = []
        for term in self.terms:
            for variable_name in term.variable_names:
                if variable_name not in names:
                    names.append(variable_name)
        return tuple(names)

    def can_be_applied(self, terms: Iterable[Term]) -> bool:
        """Returns if the given terms can be set for this operation."""
        try:
            self._check_terms(list(terms))
            return True
        except Exception:
            return False

    def _check_terms(self, terms: list[Term]):
        """Checks if the given terms are usable. If not, it raises
        an exception.
        """
        # Only actual terms stays there
        terms = [term for term in terms if isinstance(term, Term)]

        # If it does not match the cardinality
        if len(terms) != self.cardinality:
            raise Exception(
                f"Number of terms ({len(self._terms)}) is not equal to "
                f"cardinality of the operator ({self.cardinality})")

    def __str__(self):
        return (f"{self.operator_sign}"
                f"{str(self.terms).replace(' ', '').replace(',)', ')')}")


class CustomOperation(Operation):
    """This class provides ability to define and use custom operators
    for any cardinality and with custom way of their evaluation."""

    def __init__(self, cardinality: int, terms: Iterable[Term],
                 operator_sign: str, evaluator: Callable):
        """Initor creating the custom operation.

        Parameters
        ----------
        cardinality: int
            The number of terms the operation can work with. Shouldn't be
            changed in the future.

        terms: Iterable of Term
            The terms the operation has to work with. These can be changed
            in the future.

        operator_sign: str
            Sign used to distinguish this particular operation.

        evaluator: Callable
            The function evaluating the terms resulting in returning a
            logical value. This function has to accept as parameters an
            environment (`scripts.src.environment.Environment`) instance
            and a tuple of terms.
        """
        self._cardinality = cardinality
        if self._cardinality < 0:
            raise Exception(
                f"The cardinality cannot be negative: {self._cardinality}")
        Operation.__init__(self, terms)
        self._evaluator = evaluator
        self._operator_sign = operator_sign

    @property
    def cardinality(self) -> int:
        """Returns the given cardinality, i.e. the number of terms
        the operator can deal with."""
        return self._cardinality

    @property
    def operator_sign(self) -> str:
        """Returns a sign used for this operation."""
        return self._operator_sign

    @property
    def clone(self) -> "Term":
        return CustomOperation(self._cardinality, self.terms,
                               self.operator_sign, self._evaluator)

    def evaluate(self, env: Environment = None) -> bool:
        """Invokes the given function for evaluating the given terms."""
        return self._evaluator(env, self.terms)
