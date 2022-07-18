import unittest

from scripts.src.axiom_transformation.simple_commutativity import \
    EquivalenceCommutativity
from scripts.src.term import *
from scripts.src.operators import *
from scripts.src.axiom_transformation import (
    DoubleNegation, ConjunctionCommutativity, DisjunctionCommutativity)


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


class TestConjunctionCommutativity(unittest.TestCase):

    def setUp(self):
        # Definition of variables
        self.phi = Atom("PHI")
        self.psi = Atom("PSI")

        # Can be applied method (careful; method reference only!)
        self.ca = ConjunctionCommutativity().can_be_applied

        # Application method (careful; method reference only!)
        self.a = ConjunctionCommutativity().apply

    def test_applicability(self):
        # Should be applicable on conjunction
        self.assertEqual(True, self.ca(Conjunction([self.phi, self.psi])))

        # Should not be applicable on disjunction
        self.assertEqual(False, self.ca(Disjunction([self.phi, self.psi])))

    def test_application(self):
        # Switches the terms of the operation
        self.assertEqual(Conjunction([self.psi, self.phi]),
                         self.a(Conjunction([self.phi, self.psi])))

        # Stays intact
        self.assertEqual(Disjunction([self.phi, self.psi]),
                         self.a(Disjunction([self.phi, self.psi])))


class TestDisjunctionCommutativity(unittest.TestCase):

    def setUp(self):
        # Definition of variables
        self.phi = Atom("PHI")
        self.psi = Atom("PSI")

        # Can be applied method (careful; method reference only!)
        self.ca = DisjunctionCommutativity().can_be_applied

        # Application method (careful; method reference only!)
        self.a = DisjunctionCommutativity().apply

    def test_applicability(self):
        # Should be applicable on disjunction
        self.assertEqual(True, self.ca(Disjunction([self.phi, self.psi])))

        # Should not be applicable on conjunction
        self.assertEqual(False, self.ca(Conjunction([self.phi, self.psi])))

    def test_application(self):
        # Switches the terms of the operation
        self.assertEqual(Disjunction([self.psi, self.phi]),
                         self.a(Disjunction([self.phi, self.psi])))

        # Stays intact
        self.assertEqual(Conjunction([self.phi, self.psi]),
                         self.a(Conjunction([self.phi, self.psi])))


class TestEquivalenceCommutativity(unittest.TestCase):

    def setUp(self):
        # Definition of variables
        self.phi = Atom("PHI")
        self.psi = Atom("PSI")

        # Can be applied method (careful; method reference only!)
        self.ca = EquivalenceCommutativity().can_be_applied

        # Application method (careful; method reference only!)
        self.a = EquivalenceCommutativity().apply

    def test_applicability(self):
        # Should be applicable on disjunction
        self.assertEqual(True, self.ca(Equivalence([self.phi, self.psi])))

        # Should not be applicable on conjunction
        self.assertEqual(False, self.ca(Conjunction([self.phi, self.psi])))

    def test_application(self):
        # Switches the terms of the operation
        self.assertEqual(Equivalence([self.psi, self.phi]),
                         self.a(Equivalence([self.phi, self.psi])))

        # Stays intact
        self.assertEqual(Conjunction([self.phi, self.psi]),
                         self.a(Conjunction([self.phi, self.psi])))





