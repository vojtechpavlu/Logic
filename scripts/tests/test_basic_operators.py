import unittest

from scripts.src.operators import *
from scripts.src.term import Constant


class TestOperators(unittest.TestCase):

    def setUp(self):
        # Definition of the constants used in tests
        self.t = Constant(True)
        self.f = Constant(False)

    def test_negation(self):
        self.assertEqual(True,  Negation([self.f]).evaluate())
        self.assertEqual(False, Negation([self.t]).evaluate())

    def test_conjunction(self):
        self.assertEqual(False, Conjunction([self.f, self.f]).evaluate())
        self.assertEqual(False, Conjunction([self.f, self.t]).evaluate())
        self.assertEqual(False, Conjunction([self.t, self.f]).evaluate())
        self.assertEqual(True,  Conjunction([self.t, self.t]).evaluate())

    def test_disjunction(self):
        self.assertEqual(False, Disjunction([self.f, self.f]).evaluate())
        self.assertEqual(True,  Disjunction([self.f, self.t]).evaluate())
        self.assertEqual(True,  Disjunction([self.t, self.f]).evaluate())
        self.assertEqual(True,  Disjunction([self.t, self.t]).evaluate())

    def test_implication(self):
        self.assertEqual(True,  Implication([self.f, self.f]).evaluate())
        self.assertEqual(True,  Implication([self.f, self.t]).evaluate())
        self.assertEqual(False, Implication([self.t, self.f]).evaluate())
        self.assertEqual(True,  Implication([self.t, self.t]).evaluate())

    def test_equivalence(self):
        self.assertEqual(True,  Equivalence([self.f, self.f]).evaluate())
        self.assertEqual(False, Equivalence([self.f, self.t]).evaluate())
        self.assertEqual(False, Equivalence([self.t, self.f]).evaluate())
        self.assertEqual(True,  Equivalence([self.t, self.t]).evaluate())




