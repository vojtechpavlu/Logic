"""Double negation is one of the most basic axioms in propositional logic.
The axiom is defined as:

    ¬(¬φ) <=> φ

Sometimes it can be useful to define also the other way, which means:

    φ <=> ¬(¬φ)

These services are provided by instances of the class defined in this module.
"""


import scripts.src.term as term_module
from scripts.src.operators import Negation
from .axiom_transformation import AxiomTransformation


class DoubleNegation(AxiomTransformation):
    """This AxiomTransformation provides service of sealing the given
    term in to a double negation. On top of that, if the term currently
    is double-negated term, the double negation is eliminated."""

    def can_be_applied(self, term: term_module.Term) -> bool:
        """Returns always True, because this transformation can be applied
        on any non-empty term.

        The only time it does not return True is when the given term is None.
        """
        return term is not None

    def apply(self, term: term_module.Term) -> term_module.Term:
        """Tries to apply the axiom on the given term and transform it. It
        either removes double negation or it returns the element sealed in
        it."""
        if self.__is_double_negated(term):
            return term.terms[0].terms[0]
        else:
            return Negation(Negation(term))

    @staticmethod
    def __is_double_negated(t: term_module.Term) -> bool:
        """Private function providing a service of resolving the double
        negation in the given term."""
        return isinstance(t, Negation) and isinstance(t.terms[0], Negation)


