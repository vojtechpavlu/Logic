""""""

from abc import ABC, abstractmethod
import scripts.src.term as term_module


class AxiomTransformation(ABC):
    """"""

    @abstractmethod
    def can_be_applied(self, term: term_module.Term) -> bool:
        """"""

    @abstractmethod
    def apply(self, term: term_module.Term) -> term_module.Term:
        """"""


