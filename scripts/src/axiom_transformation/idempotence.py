"""In this module are stored rules of idempotence transformation axioms.

Idempotence in general means if the result of an operation remains the same,
no matter how many times the operation is performed. In propositional logic
it's defined as (for example) one of the properties of conjunction and
disjunction:

        φ ∧ φ <=> φ
        φ ∨ φ <=> φ
"""


from .axiom_transformation import AxiomTransformation
from scripts.src.operators import *
import scripts.src.term as term_module


class ConjunctionIdempotence(AxiomTransformation):
    """Conjunction idempotence provides transformation of the logical term
    reducing redundancy. This particular axiom is focusing on conjunction
    terms.
    """

    def can_be_applied(self, term: term_module.Term) -> bool:
        """To apply the idempotence axiom for conjunction (cumulatively):

            1) The given term has to be a conjunction
            2) The given conjunction's terms has to be equal

        This method returns result of these preconditions fulfillment.
        """
        if isinstance(term, Conjunction):
            return term.terms[0] == term.terms[1]
        return False

    def apply(self, term: term_module.Term) -> term_module.Term:
        """If this axiom can be applied on the term, it returns the result
        of the application, i.e. the subterm of the conjunction. Else the
        term remain unchanged.
        """
        if self.can_be_applied(term):
            return term.terms[0].clone
        return term


class DisjunctionIdempotence(AxiomTransformation):
    """Disjunction idempotence provides transformation of the logical term
    reducing redundancy. This particular axiom is focusing on disjunction
    terms.
    """

    def can_be_applied(self, term: term_module.Term) -> bool:
        """To apply the idempotence axiom for disjunction (cumulatively):

            1) The given term has to be a disjunction
            2) The given conjunction's terms has to be equal

        This method returns result of these preconditions fulfillment.
        """
        if isinstance(term, Disjunction):
            return term.terms[0] == term.terms[1]
        return False

    def apply(self, term: term_module.Term) -> term_module.Term:
        """If this axiom can be applied on the term, it returns the result
        of the application, i.e. the subterm of the conjunction. Else the
        term remain unchanged.
        """
        if self.can_be_applied(term):
            return term.terms[0].clone
        return term

