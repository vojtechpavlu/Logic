"""This module defines the most basic protocol of simplifying transformations
based on the axiomatic system of propositional logic."""

from abc import ABC, abstractmethod
import scripts.src.term as term_module


class AxiomTransformation(ABC):
    """Abstract class of AxiomTransformation defines the most general protocol
    of the simplifier of logical terms.

    The mechanism is based on definition of substitution algorithm ran by
    identification of possibility of application and actual substitution of
    the term by an equivalent one.
    """

    @abstractmethod
    def can_be_applied(self, term: term_module.Term) -> bool:
        """Returns if this axiom can be applied on this term. If it can,
        it returns True.

        Parameters
        ----------
        term: Term
            Term to be checked if this axiom can be applied on it.

        Returns
        -------
        bool
            Result of the check; if it can be applied, it returns True, else
            it returns False.
        """

    @abstractmethod
    def apply(self, term: term_module.Term) -> term_module.Term:
        """Tries to apply the axiom on the given term. If it cannot be applied,
        it returns a deep copy of the given term as a result, otherwise it
        returns it's equivalent form.

        Parameters
        ----------
        term: Term
            Term to be transformed via this axiom to it's equivalent form.

        Returns
        -------
        Term
            Result of the application. When it cannot be applied, it returns
            a deep copy of the given term.
        """


