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

from typing import Type


class _GeneralIdempotence(AxiomTransformation):
    """General Idempotence mechanism used for both conjunction and
    disjunction.
    """

    def __init__(self, for_operation: Type):
        """Initor of the instance creating the idempotence transformation.

        Parameters
        ----------
        for_operation: Type
            Type the idempotence should be provided for. Only available should
            be `Conjunction` and `Disjunction`.
        """
        AxiomTransformation.__init__(self)
        self._for_operation = for_operation

    @property
    def for_operation(self) -> Type:
        return self._for_operation

    def can_be_applied(self, term: term_module.Term) -> bool:
        """To apply the idempotence axiom for (cumulatively):

            1) The given term has to be of a specified type
            2) The given operation's subterms has to be equal

        This method returns result of these preconditions fulfillment.
        """
        if isinstance(term, self.for_operation):
            return term.terms[0] == term.terms[1]
        return False

    def apply(self, term: term_module.Term) -> term_module.Term:
        """If this axiom can be applied on the term, it returns the result
        of the application, i.e. the subterm of the operation. Else the
        term remain unchanged.
        """
        if self.can_be_applied(term):
            return term.terms[0].clone
        return term


class ConjunctionIdempotence(_GeneralIdempotence):
    """Conjunction idempotence provides transformation of the logical term
    reducing redundancy. This particular axiom is focusing on conjunction
    terms.
    """

    def __init__(self):
        _GeneralIdempotence.__init__(self, Conjunction)


class DisjunctionIdempotence(_GeneralIdempotence):
    """Disjunction idempotence provides transformation of the logical term
    reducing redundancy. This particular axiom is focusing on disjunction
    terms.
    """

    def __init__(self):
        _GeneralIdempotence.__init__(self, Disjunction)




