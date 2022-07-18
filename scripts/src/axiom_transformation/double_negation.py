"""Double negation is one of the most basic axioms in propositional logic.
The axiom is defined as:

    ¬(¬φ) <=> φ

Sometimes it can be useful to define also the other way, which means:

    φ <=> ¬(¬φ)

These services are provided by instances of both classes in this module.
"""


import scripts.src.term as term_module
from scripts.src.operators import Negation
from .axiom_transformation import AxiomTransformation


class DoubleNegationSimplifier(AxiomTransformation):
    """This simplifier eliminates double negation from the term."""

    def can_be_applied(self, term: term_module.Term) -> bool:
        """"""
        return (isinstance(term, Negation) and
                isinstance(term.terms[0], Negation))

    def apply(self, term: term_module.Term) -> term_module.Term:
        """"""
        if self.can_be_applied(term):
            return term.terms[0].terms[0]
        return term.clone


class GeneralDoubleNegation(AxiomTransformation):
    """This simplifier eliminates double negation from the term."""

    def can_be_applied(self, term: term_module.Term) -> bool:
        """"""
        return True

    def apply(self, term: term_module.Term) -> term_module.Term:
        """"""
        dns = DoubleNegationSimplifier()
        if dns.can_be_applied(term):
            return dns.apply(term)
        else:
            return Negation(Negation(term))




