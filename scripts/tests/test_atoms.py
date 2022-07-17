import unittest

import scripts.src.term as tested


class TestAtoms(unittest.TestCase):
    """"""

    def test_atom_successful_creation_name(self):
        """Tests that the created atom holds a correct name."""
        atom = tested.Atom("random_atom")
        self.assertEqual("random_atom", atom.atom_name)

    def test_atom_successful_creation_value_positive(self):
        """Tests that the created atom holds a positive value."""
        atom = tested.Atom("positive", True)
        self.assertEqual(True, atom.value)

    def test_atom_successful_creation_value_negative(self):
        """Tests that the created atom holds a negative value."""
        atom = tested.Atom("negative", False)
        self.assertEqual(False, atom.value)

    def test_atom_successful_creation_value_undefined(self):
        """Tests that the created atom does not fill in a value."""
        atom = tested.Atom("undefined")
        self.assertIsNone(atom.value)

    def test_atom_evaluation_defined_value(self):
        """Tests that the atom with defined value is able to be evaluated."""
        atom = tested.Atom("defined_value", True)
        self.assertEqual(True, atom.evaluate())

    def test_atom_evaluation_environment(self):
        """Tests that the atom is able to pick it's value from the environment.
        """
        from scripts.src.environment import Environment

        name = "declared"                   # Name of the atom

        environment = Environment()         # Environment creation
        environment.add_values(name, True)  # Adding specified value

        atom = tested.Atom(name)            # Atom without defined value
        self.assertEqual(True, atom.evaluate(environment))

    def test_atom_evaluation_without_definition_without_env(self):
        """Tests that atom raises exception when evaluated without definition
        of a value."""

        atom = tested.Atom("undefined")

        # Should raise an exception when evaluated without value definition
        self.assertRaises(Exception, atom.evaluate)







