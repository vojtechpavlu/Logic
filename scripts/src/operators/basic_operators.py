"""This module contains a definition of the most general operators of the
logic. These includes negation, conjunction, disjunction, implication and
equivalence.
"""


from scripts.src.term import Operation, Environment


class Negation(Operation):
    """Negation is one of the most general operators. This provides changing
    the value of it's only internal term on the other one. This means there
    is it's cardinality equal to one."""

    @property
    def cardinality(self) -> int:
        return 1

    def evaluate(self, env: Environment = None) -> bool:
        """Returns the value of the evaluated term turned on the other one.

        Parameters
        ----------
        env: Environment
            Environment containing declaration of values set to the variables

        Raises
        ------
        Exception
            When the internal term cannot be evaluated due to the lack of
            certainty when evaluating.
        """
        return not self.terms[0].evaluate(env)


class Conjunction(Operation):
    """Conjunction (AND) is operator, which returns the lowest of the values.
    In the case of propositional logic, it's true iff both of the values are
    true."""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        """Returns the value calculated of both of the terms. It returns True
        iff both the terms are evaluated as True.

        Parameters
        ----------
        env: Environment
            Environment containing declaration of values set to the variables

        Raises
        ------
        Exception
            When the internal term cannot be evaluated due to the lack of
            certainty when evaluating.
        """
        return self.terms[0].evaluate(env) and self.terms[1].evaluate(env)


class Disjunction(Operation):
    """Disjunction is a logic operator returning the highest value of both
    of the terms inside. In propositional logic it returns true when at least
    one of the terms are evaluated as true."""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        """Returns the value calculated of both of the terms. It returns True
        if at least one of the terms is evaluated as true.

        Parameters
        ----------
        env: Environment
            Environment containing declaration of values set to the variables

        Raises
        ------
        Exception
            When the internal term cannot be evaluated due to the lack of
            certainty when evaluating.
        """
        return self.terms[0].evaluate(env) or self.terms[1].evaluate(env)


class Implication(Operation):
    """Implication is an operator evaluated as a comparison of the both
    premise and consequence; when premise is not greater than consequence.
    In propositional logic it means when the premise is true, the consequence
    has to be true to be the implication true. If the premise is not true,
    the result is always true."""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        """Returns the value calculated of both of the terms. It returns True
        by the schema in this table:

        +----------------+
        | φ | ψ | φ => ψ |
        +----------------+
        | 0 | 0 |   1    |
        | 0 | 1 |   1    |
        | 1 | 0 |   0    |
        | 1 | 1 |   1    |
        +----------------+

        Parameters
        ----------
        env: Environment
            Environment containing declaration of values set to the variables

        Raises
        ------
        Exception
            When the internal term cannot be evaluated due to the lack of
            certainty when evaluating.
        """
        if self.terms[0].evaluate(env):
            return self.terms[1].evaluate(env)
        return True


class Equivalence(Operation):
    """One of the most general logical junctions, evaluating the equality
    of the logical values of both the terms."""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        return self.terms[0].evaluate(env) == self.terms[1].evaluate(env)





