""""""

from typing import Iterable


class Declaration:
    """Instances of this class sets a declaration of a logic value for
    variable of specified name."""

    def __init__(self, declaration_name: str, value: bool):
        """Initor creating the instance.

        Parameters
        ----------
        declaration_name: str
            Name of the variable the declaration is for. This should not be
            empty and should be unique in the environment.

        value: bool
            Logic value the variable should be set to.
        """
        self._declaration_name = declaration_name
        self._value = value

    @property
    def declaration_name(self) -> str:
        """Name of the variable this declaration is used for."""
        return self._declaration_name

    @property
    def value(self) -> bool:
        """Logic value the atomic variable should be set to."""
        return self._value


class Environment:
    """Environment is a construction used for setting the set of variables
    with given logic values. This abstraction works as a container of
    declarations (instances of the class Declaration) and provides it's
    general functionalities, like search and summary."""

    def __init__(self):
        self._declarations: list[Declaration] = []

    @property
    def declarations(self) -> tuple[Declaration]:
        """Returns a tuple of the declarations."""
        return tuple(self._declarations)

    @property
    def declaration_names(self) -> tuple[str]:
        """Returns a tuple of names of declared variables."""
        return tuple(map(lambda d: str(d.declaration_name), self.declarations))

    @property
    def is_empty(self) -> bool:
        """Returns if the container of declarations is empty or not."""
        return len(self) == 0

    def declaration(self, declaration_name: str) -> Declaration:
        """Tries to find a specific declaration for the given name.
        When it's not found, returns None.

        Parameters
        ----------
        declaration_name: str
            Name of the variable the search should be performed.
        """
        for declaration in self.declarations:
            if declaration.declaration_name == declaration_name:
                return declaration

    def has_declaration(self, declaration_name: str) -> bool:
        """Returns if there is a declaration for variable of the given name.

        Parameters
        ----------
        declaration_name: str
            Name of the variable the environment should be checked for if the
            declaration is contained. If there is such a declaration, returns
            True, else False.
        """
        return self.declaration(declaration_name) is not None

    def add_declaration(self, declaration: Declaration):
        """Tries to add the given declaration. If there is a declaration of
        the same name, it raises exception.

        Parameters
        ----------
        declaration: Declaration
            Declaration to be added to the environment

        Raises
        ------
        Exception
            When there is one declaration of the same name already
        """
        if not self.has_declaration(declaration.declaration_name):
            self._declarations.append(declaration)
        else:
            raise Exception(f"Declaration '{declaration.declaration_name}' "
                            f"is already registered.")

    def add_values(self, declaration_name: str, value: bool):
        """Tries to add a new declaration by creating new from a name and
        a given value.

        Parameters
        ----------
        declaration_name: str
            Name of the variable the declaration is for

        value: bool
            Logic value the variable's value should be set to

        Raises
        ------
        Exception
            When there is one declaration of this name
        """
        self.add_declaration(Declaration(declaration_name, value))

    def add_all_declarations(self, declarations: Iterable[Declaration]):
        """Tries to add all given declarations.

        Parameters
        ----------
        declarations: Iterable of Declaration
            Iterable set of declarations for variables. These should be unique
            by it's name.

        Raises
        ------
        Exception
            When there is one declaration for a variable of given name
        """
        for declaration in declarations:
            self.add_declaration(declaration)

    def __len__(self) -> int:
        return len(self.declarations)



