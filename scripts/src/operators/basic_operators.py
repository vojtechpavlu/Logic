from scripts.src.term import Operation, Environment


class Negation(Operation):
    """"""

    @property
    def cardinality(self) -> int:
        return 1

    def evaluate(self, env: Environment = None) -> bool:
        """"""
        return not self.terms[0].evaluate(env)


class Conjunction(Operation):
    """"""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        return self.terms[0].evaluate(env) and self.terms[1].evaluate(env)


class Disjunction(Operation):
    """"""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        return self.terms[0].evaluate(env) or self.terms[1].evaluate(env)


class Implication(Operation):
    """"""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        if self.terms[0].evaluate(env):
            return self.terms[1].evaluate(env)
        return True


class Equivalence(Operation):
    """"""

    @property
    def cardinality(self) -> int:
        return 2

    def evaluate(self, env: Environment = None) -> bool:
        return self.terms[0].evaluate(env) == self.terms[1].evaluate(env)





