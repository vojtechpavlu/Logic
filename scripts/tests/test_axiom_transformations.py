import unittest

from scripts.src.term import *
from scripts.src.operators import *
from scripts.src.axiom_transformation import DoubleNegation


class TestDoubleNegation(unittest.TestCase):

    def setUp(self):
        self.true_const = Constant(True)
        self.false_const = Constant(False)
        self.dn = DoubleNegation()

    def d_negator(self, term: Term):
        """Shorthand for double-sealing"""
        return Negation(Negation(term))

    def test_applicability(self):
        self.assertEqual(True, self.dn.can_be_applied(self.true_const))
        self.assertEqual(True, self.dn.can_be_applied(self.false_const))

        self.assertEqual(
            True, self.dn.can_be_applied(self.d_negator(self.true_const)))
        self.assertEqual(
            True, self.dn.can_be_applied(self.d_negator(self.false_const)))

    def test_check_elimination(self):
        """The result of application of DN axiom transformation on
        double negated term should result in a term itself."""
        self.assertEqual(
            Constant, type(self.dn.apply(self.d_negator(self.true_const))))
        self.assertEqual(
            Constant, type(self.dn.apply(self.d_negator(self.false_const))))

    def test_check_double_elimination(self):
        """Double negating double negated axiom should result in the internal
        term itself."""
        self.assertEqual(
            Constant, type(self.dn.apply(self.dn.apply(self.true_const))))
        self.assertEqual(
            Constant, type(self.dn.apply(self.dn.apply(self.false_const))))

    def test_sealing_in_negation(self):
        # actually, it should be double negation
        self.assertEqual(Negation, type(self.dn.apply(self.true_const)))
        self.assertEqual(Negation, type(self.dn.apply(self.false_const)))
