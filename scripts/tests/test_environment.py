import unittest

import scripts.src.environment as tested


class TestEnvironment(unittest.TestCase):
    """"""

    def setUp(self):
        """Prepares all the testing environments."""
        # Declarations definition
        self.name1 = "added_declaration1"
        self.value1 = True
        self.decl1 = tested.Declaration(self.name1, self.value1)

        self.name2 = "added_declaration2"
        self.value2 = False
        self.decl2 = tested.Declaration(self.name2, self.value2)

        # Environments definition
        self.empty_env = tested.Environment()

        self.env_with_first = tested.Environment()
        self.env_with_first.add_declaration(self.decl1)

        self.env_with_both = tested.Environment()
        self.env_with_both.add_declaration(self.decl1)
        self.env_with_both.add_declaration(self.decl2)

    def test_adding_declaration_size(self):
        """"""
        # Initial size of empty env
        self.assertEqual(0, len(self.empty_env))

        # Adding one declaration
        self.empty_env.add_declaration(self.decl1)

        # Size of env after adding one declaration
        self.assertEqual(1, len(self.empty_env))

        # Adding another one declaration
        self.empty_env.add_declaration(self.decl2)

        # Size of env after adding two declarations
        self.assertEqual(2, len(self.empty_env))

    def test_adding_two_declarations_with_same_name(self):
        """"""
        self.assertEqual(True, self.empty_env.is_empty)

        # This should be OK since the env is empty
        self.empty_env.add_declaration(self.decl1)

        # This should raise an exception
        self.assertRaises(
            Exception, self.empty_env.add_declaration, self.decl1)

    def test_adding_two_declaration_with_different_names(self):
        """"""
        self.assertEqual(True, self.empty_env.is_empty)

        # This should be OK since the env is empty
        self.empty_env.add_declaration(self.decl1)

        # This should be OK too, because it has different name
        self.empty_env.add_declaration(self.decl2)

    def test_getting_declaration_names(self):
        """"""
        self.assertEqual(
            (self.name1,), self.env_with_first.declaration_names)

        self.assertEqual(
            (self.name1, self.name2), self.env_with_both.declaration_names)

    def test_searches_properly_positive(self):
        """"""
        self.empty_env.add_declaration(self.decl1)
        self.assertEqual(
            self.name1,
            self.empty_env.declaration(self.name1).declaration_name)

    def test_searches_properly_negative(self):
        """"""
        self.empty_env.add_declaration(self.decl1)
        self.assertIsNone(self.empty_env.declaration("non-existing-decl"))





