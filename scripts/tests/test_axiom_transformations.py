import unittest

from scripts.src.term import *
from scripts.src.operators import *
from scripts.src.axiom_transformation import DoubleNegation


class TestAxiomTransformations(unittest.TestCase):

    def setUp(self):
        self.true_const = Constant(True)
        self.false_const = Constant(False)

    def test_double_negation(self):

        # DN transformation
        dn = DoubleNegation()

        # Shorthand of syntax using nested function
        def d_negator(term: Term):
            return Negation(Negation(term))

        # Check applicability
        self.assertEqual(True, dn.can_be_applied(self.true_const))
        self.assertEqual(True, dn.can_be_applied(self.false_const))
        self.assertEqual(True, dn.can_be_applied(d_negator(self.true_const)))
        self.assertEqual(True, dn.can_be_applied(d_negator(self.false_const)))

        # Check of the elimination
        self.assertEqual(Constant, type(dn.apply(d_negator(self.true_const))))
        self.assertEqual(Constant, type(dn.apply(d_negator(self.false_const))))

        # Check of double negating
        self.assertEqual(Negation, type(dn.apply(self.true_const)))
        self.assertEqual(Negation, type(dn.apply(self.false_const)))

        # Check double double negating
        self.assertEqual(Constant, type(dn.apply(dn.apply(self.true_const))))
        self.assertEqual(Constant, type(dn.apply(dn.apply(self.false_const))))
