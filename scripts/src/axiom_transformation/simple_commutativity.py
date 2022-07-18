"""In this module are stored rules of commutativity transformation."""


from .axiom_transformation import AxiomTransformation
from scripts.src.operators import *
import scripts.src.term as term_module


class ConjunctionCommutativity(AxiomTransformation):
    """Commutativity of conjunction is one of the most basic axioms of
    propositional logic.

    Basically it says the terms of the relation can be switched, resulting
    always the same. Formally, it can be stated that:

        -------------------
        | φ ∧ ψ <=> ψ ∧ φ |
        |_________________|

    This axiom can be applied on conjunction only.
    """

    def can_be_applied(self, term: term_module.Term) -> bool:
        """Returns if the given term is type of conjunction, because this
        axiom transformation can be applied on conjunction terms only.
        """
        return isinstance(term, Conjunction)

    def apply(self, term: term_module.Term) -> term_module.Term:
        """If the term can be transformed using this axiom, it returns a
        brand new instance of conjunction with reversed deep copies of the
        terms of the original conjunction. Else, it returns the original
        term intact.
        """
        if self.can_be_applied(term):

            # Return a brand new conjunction with reversed copies of terms
            return Conjunction(
                reversed(list(map(lambda t: t.clone, term.terms))))

        # Returns the intact original term
        return term



